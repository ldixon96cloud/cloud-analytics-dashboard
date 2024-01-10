import mysql.connector
import numpy as np
import pandas as pd
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange
from google.analytics.data_v1beta.types import Dimension
from google.analytics.data_v1beta.types import Metric
from google.analytics.data_v1beta.types import RunReportRequest
from google.analytics.data_v1beta.types import OrderBy
import os

# MySQL connection setup
mysql_host = "YOUR MYSQL HOST HERE"
mysql_user = "YOUR MYSQL USER HERE"
mysql_password = "YOUR MYSQL PASSWORD HERE"
mysql_database = "YOUR MYSQL DATABASE HERE"

mydb = mysql.connector.connect(
    host=mysql_host,
    user=mysql_user,
    passwd=mysql_password,
    database=mysql_database
)

# Google Analytics configuration
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'your/path/to/creds.json'
property_id = 'your_google_analytics_property_id'
client = BetaAnalyticsDataClient()

# Format Report - run_report method
def format_report(request):
    response = client.run_report(request)
    
    # Row index
    row_index_names = [header.name for header in response.dimension_headers]
    row_header = []
    for i in range(len(row_index_names)):
        row_header.append([row.dimension_values[i].value for row in response.rows])

    row_index_named = pd.MultiIndex.from_arrays(np.array(row_header), names=np.array(row_index_names))
    
    # Row flat data
    metric_names = [header.name for header in response.metric_headers]
    data_values = []
    for i in range(len(metric_names)):
        data_values.append([row.metric_values[i].value for row in response.rows])

    output = pd.DataFrame(data=np.transpose(np.array(data_values, dtype='f')),
                          index=row_index_named, columns=metric_names)
    return output

# Create the report request
request = RunReportRequest(
    property='properties/'+property_id,
    dimensions=[Dimension(name="date")],
    metrics=[Metric(name="screenPageViews"), 
             Metric(name="addToCarts"),
             Metric(name="ecommercePurchases"),
             Metric(name="grossPurchaseRevenue")],
    order_bys=[OrderBy(dimension={'dimension_name': 'date'})],
    date_ranges=[DateRange(start_date="2023-01-01", end_date="today")],
)

# Call the format_report function with the request and get the output
report_output = format_report(request)

# Convert report_output to a pandas DataFrame
dataframe = pd.DataFrame(report_output)

# Create a new table 'funnel_metrics' in the MySQL database
cursor = mydb.cursor()
create_table_query = """
CREATE TABLE IF NOT EXISTS funnel_metrics (
    date DATE PRIMARY KEY,
    screenPageViews FLOAT,
    addToCarts FLOAT,
    ecommercePurchases FLOAT,
    grossPurchaseRevenue FLOAT
)
"""
cursor.execute(create_table_query)

# Insert data into the 'funnel_metrics' table
for index, row in dataframe.iterrows():
    insert_query = """
    INSERT INTO funnel_metrics (date, screenPageViews, addToCarts, ecommercePurchases, grossPurchaseRevenue)
    VALUES (%s, %s, %s, %s, %s)
    """
    data = (
        index[0],
        float(row['screenPageViews']),
        float(row['addToCarts']),
        float(row['ecommercePurchases']),
        float(row['grossPurchaseRevenue'])
    )
    cursor.execute(insert_query, data)


# Commit changes and close cursor
mydb.commit()
cursor.close()

# Close MySQL connection
mydb.close()

print("Data imported into 'funnel_metrics' table successfully.")

