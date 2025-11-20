# Motherduck Setup

To connect Zenlytic to MotherDuck, you'll need to configure the connection using a service token. Here's how to do it:

## Step 1: Create a Service Token

1. Log into your MotherDuck account
2. Go to Settings > Service Tokens
3. Click "Create Service Token"
4. Give it a name (e.g., "Zenlytic Integration")
5. Set appropriate permissions (read access to your databases)
6. Click "Create"
7. Copy the token (you won't be able to see it again)

## Step 2: Add the Connection in Zenlytic

1. In Zenlytic, go to Settings > Data Sources
2. Click "Add Data Source"
3. Select "MotherDuck" from the list
4. Enter the connection details:
   * **Service Token**: The token you generated
   * **Database**: Your database name (optional, can be specified later)

![Motherduck Setup 1](../.gitbook/assets/motherduck-setup-1.png)

## Step 3: Test Your Connection

1. Click "Test Connection" to verify it works
2. If successful, click "Save"
3. You should now be able to see your MotherDuck tables in Zenlytic

## Troubleshooting

If you encounter connection issues:

1. Verify the service token is correct
2. Check that the token has the necessary permissions
3. Ensure the database name is correct (if specified)
4. Verify your MotherDuck account is active
