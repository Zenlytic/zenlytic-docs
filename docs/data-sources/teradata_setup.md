---
description: >-
  Connect Teradata to Zenlytic and verify access to your database.
---

# Teradata Setup

To connect Zenlytic to Teradata, gather the connection details from your database administrator.

## Gather connection information

* **Host**: Your Teradata hostname or IP address
* **Database**: The database to connect to
* **Username and password**: Credentials for a user with access to the data you want to query
* **Port (optional)**: Leave blank to use the default, 1025
* **Schema (optional)**: Leave blank to use the user's default schema

## Add the data source

1. In Zenlytic, go to **Settings > Data Sources**.
2. Select **Add Data Source**, then **Teradata**.
3. Enter the connection details.
4. Test the connection. A successful test confirms that Zenlytic can reach and authenticate to Teradata.
5. Save the data source.

## Troubleshooting

If the test fails, check the host and port, confirm the credentials and database name, and verify that the user can access the tables you intend to use. If your network restricts incoming connections, allow the addresses for your Zenlytic deployment listed in [IP Whitelisting](../authentication-and-security/ip_whitelisting.md), then test again.
