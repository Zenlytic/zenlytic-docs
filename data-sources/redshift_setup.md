# Redshift Setup

To connect Zenlytic to Amazon Redshift, you'll need to configure the connection with your database credentials. Here's how to do it:

## Step 1: Gather Connection Information

You'll need the following information from your Redshift cluster:

* **Host**: Your Redshift cluster endpoint
* **Port**: Usually 5439 (default Redshift port)
* **Database**: The database name
* **Username**: A database user with appropriate permissions
* **Password**: The password for the user

## Step 2: Create a Database User (if needed)

If you don't have a dedicated user for Zenlytic, create one:

```sql
CREATE USER zenlytic_user WITH PASSWORD 'your_secure_password';
GRANT USAGE ON DATABASE your_database TO zenlytic_user;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO zenlytic_user;
```

## Step 3: Add the Connection in Zenlytic

1. In Zenlytic, go to Settings > Data Sources
2. Click "Add Data Source"
3. Select "Redshift" from the list
4. Enter the connection details:
   * **Host**: Your Redshift cluster endpoint
   * **Port**: 5439 (or your custom port)
   * **Database**: Your database name
   * **Username**: Your database username
   * **Password**: Your database password

![Redshift Setup 1](../.gitbook/assets/redshift-setup-1.png)

## Step 4: Configure Security Group

Make sure your Redshift security group allows connections from Zenlytic's IP addresses:

* **184.73.175.163**
* **18.209.132.30**

## Step 5: Test Your Connection

1. Click "Test Connection" to verify it works
2. If successful, click "Save"
3. You should now be able to see your Redshift tables in Zenlytic

![Redshift Setup 2](../.gitbook/assets/redshift-setup-2.png)

## Troubleshooting

If you encounter connection issues:

1. Verify the host endpoint is correct
2. Check that the security group allows connections from Zenlytic's IPs
3. Ensure the user has the necessary permissions
4. Verify the database name and credentials are correct
