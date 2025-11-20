# Sql Server Setup

To connect Zenlytic to SQL Server, you'll need to configure the connection with your database credentials. Here's how to do it:

## Step 1: Gather Connection Information

You'll need the following information from your SQL Server instance:

* **Host**: Your SQL Server hostname or IP address
* **Port**: Usually 1433 (default SQL Server port)
* **Database**: The database name
* **Username**: A database user with appropriate permissions
* **Password**: The password for the user

## Step 2: Create a Database User (if needed)

If you don't have a dedicated user for Zenlytic, create one:

```sql
CREATE LOGIN zenlytic_user WITH PASSWORD = 'your_secure_password';
USE your_database;
CREATE USER zenlytic_user FOR LOGIN zenlytic_user;
GRANT CONNECT TO zenlytic_user;
GRANT SELECT ON SCHEMA::dbo TO zenlytic_user;
```

## Step 3: Add the Connection in Zenlytic

1. In Zenlytic, go to Settings > Data Sources
2. Click "Add Data Source"
3. Select "SQL Server" from the list
4. Enter the connection details:
   * **Host**: Your SQL Server hostname
   * **Port**: 1433 (or your custom port)
   * **Database**: Your database name
   * **Username**: Your database username
   * **Password**: Your database password

![Sql Server Setup 1](../.gitbook/assets/sql-server-setup-1.png)

## Step 4: Configure Firewall/Security

Make sure your SQL Server allows connections from Zenlytic's IP addresses:

* **184.73.175.163**
* **18.209.132.30**

## Step 5: Test Your Connection

1. Click "Test Connection" to verify it works
2. If successful, click "Save"
3. You should now be able to see your SQL Server tables in Zenlytic

## Troubleshooting

If you encounter connection issues:

1. Verify the host and port are correct
2. Check that the firewall allows connections from Zenlytic's IPs
3. Ensure the user has the necessary permissions
4. Verify the database name and credentials are correct
5. Check that SQL Server is configured to accept remote connections
6. Ensure SQL Server Browser service is running (if using named instances)
