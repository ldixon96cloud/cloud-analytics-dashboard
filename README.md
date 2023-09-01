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

15. **Run Metabase**
   - Run Metabase using the downloaded Jar File

   ```bash
   java -jar metabase.jar
   ```

16. **Access Metabase**
   - Access Metabase by visiting http://yourlinodeIPaddress:300



