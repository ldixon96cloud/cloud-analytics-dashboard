# lamp-dashboard
Leveraging Linode as the chosen cloud provider, this project seamlessly integrates server deployment, data analysis, and data visualization to provide valuable insights for marketing campaigns.

# CloudDashboard-LAMP Project

Welcome to the CloudDashboard-LAMP project repository! This project showcases the creation of a web-based dashboard application powered by a LAMP stack, hosted on Linode. Below are the steps to set up your development environment.

## Linode Instance and LAMP Stack Setup

1. **Linode Instance Provisioning:**
   - Log in to your Linode account and create a new Linode instance.
   - Note down the IP address of your Linode instance for future reference.

2. **SSH Access:**
   - Open your terminal and connect to your Linode instance using SSH:
     ```bash
     ssh username@your_linode_ip
     ```

3. **Update and Upgrade:**
   - Update package repositories and upgrade installed packages:
     ```bash
     sudo apt update
     sudo apt upgrade
     ```

4. **Apache2 Installation:**
   - Install the Apache web server:
     ```bash
     sudo apt install apache2
     ```

5. **MySQL Server Installation:**
   - Install the MySQL server package and follow the prompts for secure installation:
     ```bash
     sudo apt install mysql-server
     mysql_secure_installation
     ```

6. **PHP and Modules Installation:**
   - Install PHP and required modules:
     ```bash
     sudo apt install php libapache2-mod-php php-mysql
     ```

7. **Verify LAMP Stack:**
   - To verify the LAMP stack installation, create a `phpinfo.php` file:
     ```bash
     sudo nano /var/www/html/phpinfo.php
     ```
     Add the following lines to the file:
     ```php
     <?php
     phpinfo();
     ?>
     ```
     Save and exit. Access this page in your web browser by visiting `http://your_linode_ip/phpinfo.php`.

8. **Cleanup:**
   - Remove the `phpinfo.php` file:
     ```bash
     sudo rm /var/www/html/phpinfo.php
     ```

9. **Install java:**
   - Metabase requires Java to run. Install OpenJDK.
     ```bash
     sudo apt install openjdk-11-jdk
     ```

10. **Download Metabase**
    - Go to the Metabase website and download the latest version of Metabase
    ```bash
    wget https://downloads.metabase.com/v0.41.3/metabase.jar
    ```

11. **Configure MySQL Bind Settings**
   - You'll need to configure this setting in order to remotely connect to the MySQL server.
   - The MySQL configuration file, typically named my.cnf, is located in the /etc/mysql/ directory. You'll need superuser privileges to edit it.
 
   ```bash
   sudo nano /etc/mysql/my.cnf
   ```

12. **Locate the 'bind-address' option**
   - In the my.cnf file, look for the bind-address option. By default, it's often set to 127.0.0.1, which means MySQL only listens on the localhost. You need to change this to your server's public IP address to allow external connections.
   
   ```bash
   bind-address = your_server_public_ip
   ```
13. **Save and exit**
   - Save the changes you made to the my.cnf file and exit the text editor.

14. **Restart MySQL**
   - To apply the changes, restart the MySQL service.

   ```bash
   sudo service mysql restart
   ```

15. **Enable the Google Analytics 4 Data API**
   - Go to the Google Cloud Console.
   - Select your project or create a new one if necessary.
   - In the left sidebar, navigate to "APIs & Services" > "Library."
   - Search for "Google Analytics 4 Data API" and click on it.
   - Click the "Enable" button to enable the API for your project.

16. **Create a Service Account**
   - In the Google Cloud Console, navigate to "APIs & Services" > "Credentials."
   - Click the "Create credentials" dropdown and select "Service account key."
   - Fill out the necessary information for your service account:
   - Service account name: Provide a name for your service account.
   - Role: Select the appropriate role based on your project's requirements. For Google Analytics access, consider using the "Editor" role.
   - Key type: Choose "JSON" as the key type.
   - Click the "Continue" button.
   - In the next step, you will be prompted to set up the service account's permissions. If you're using this service account for Google Analytics, add the appropriate permissions for your Google Analytics 4 property.
   - Click "Continue" and review the permissions.
   - Click "Create" to create the service account and generate a JSON key file.

17. **Save the JSON credentials File**
   - After creating the service account, a JSON key file will be downloaded to your computer. Keep this file secure, as it contains sensitive information.
   - Rename the JSON key file to something meaningful for your project, e.g., project-name-ga4-credentials.json.
   - Place the JSON key file in a secure location within your project's directory, preferably outside of the public directory to ensure its security.

18. **Add a new user in Google Analytics 4 Admin Panel**
   - Log in to your Google Analytics 4 account.
   - In the left sidebar, click on "Admin."
   - Under the "Account" section, click on the account to which you want to grant access.
   - Click on "User Management."
   - Click the "+ Add users" button.
   - In the "Email addresses" field, enter the email address associated with the service account you created earlier.
   - Assign the appropriate permissions to the service account user. Typically, you would assign permissions like "Read & Analyze" or "Edit."
   - Click "Add" to add the service account as a user with the specified permissions. 

15. **Run Metabase**
   - Run Metabase using the downloaded Jar File

   ```bash
   java -jar metabase.jar
   ```

16. **Access Metabase**
   - Access Metabase by visiting http://yourlinodeIPaddress:300



