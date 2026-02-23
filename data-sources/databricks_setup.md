# Databricks Setup

To connect Zenlytic to Databricks, you'll need to configure the connection using a personal access token. Here's how to do it:

## Step 1: Create a Personal Access Token

1. Log into your Databricks workspace
2. Go to User Settings (click your username in the top right)
3. Click on "Developer" tab
4. Click "Generate New Token"
5. Give it a name (e.g., "Zenlytic Integration")
6. Set an expiration date
7. Click "Generate"
8. Copy the token (you won't be able to see it again)

![Databricks Setup 1](../.gitbook/assets/databricks-setup-1.png)

## Step 2: Get Your Workspace URL

1. In your Databricks workspace, look at the URL in your browser
2. It should look like: `https://your-workspace.cloud.databricks.com`
3. Copy this URL

![Databricks Setup 1](../.gitbook/assets/databricks-setup-1.png)

## Step 3: Add the Connection in Zenlytic

1. In Zenlytic, go to Settings > Data Sources
2. Click "Add Data Source"
3. Select "Databricks" from the list
4. Enter the connection details:
   * **Workspace URL**: Your Databricks workspace URL
   * **Personal Access Token**: The token you generated
   * **HTTP Path**: Usually `/sql/1.0/warehouses/<warehouse-id>`

![Databricks Setup 2](../.gitbook/assets/databricks-setup-2.png)

## Step 4: Configure HTTP Path

To find your HTTP path:

1. Go to SQL Warehouses in Databricks
2. Click on your warehouse
3. Look for the "Connection Details" section
4. Copy the HTTP Path

![Databricks Setup 3](../.gitbook/assets/databricks-setup-3.png)

## IP Whitelisting

If you use IP whitelisting in your data warehouse, whitelist the following IP addresses:

```
184.73.175.163 
18.209.132.30
```

## Step 5: Test Your Connection

1. Click "Test Connection" to verify it works
2. If successful, click "Save"
3. You should now be able to see your Databricks tables in Zenlytic
