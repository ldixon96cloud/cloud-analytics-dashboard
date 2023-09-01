import numpy as np
import pandas as pd

from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange
from google.analytics.data_v1beta.types import Dimension
from google.analytics.data_v1beta.types import Metric
from google.analytics.data_v1beta.types import RunReportRequest
from google.analytics.data_v1beta.types import OrderBy
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'your/path/to/credentials.json'



# Google Analytics configuration
property_id = 'your-google-analytics-property-id'

client = BetaAnalyticsDataClient()

## Format Report - run_report method
def format_report(request):
    response = client.run_report(request)
    
    # Row index
    row_index_names = [header.name for header in response.dimension_headers]
    row_header = []
    for i in range(len(row_index_names)):
        row_header.append([row.dimension_values[i].value for row in response.rows])

    row_index_named = pd.MultiIndex.from_arrays(np.array(row_header), names = np.array(row_index_names))
    # Row flat data
    metric_names = [header.name for header in response.metric_headers]
    data_values = []
    for i in range(len(metric_names)):
        data_values.append([row.metric_values[i].value for row in response.rows])

    output = pd.DataFrame(data = np.transpose(np.array(data_values, dtype = 'f')), 
                          index = row_index_named, columns = metric_names)
    return output



request = RunReportRequest(
        property='properties/'+property_id,
        dimensions=[Dimension(name="date"),
                    Dimension(name="sessionMedium")],
        metrics=[Metric(name="totalUsers")],
        order_bys = [OrderBy(dimension = {'dimension_name': 'date'}),
                    OrderBy(dimension = {'dimension_name': 'sessionMedium'})],
        date_ranges=[DateRange(start_date="2023-08-01", end_date="2023-09-01")],
    )

request

# Call the format_report function with the request and print the output
report_output = format_report(request)
print(report_output)
