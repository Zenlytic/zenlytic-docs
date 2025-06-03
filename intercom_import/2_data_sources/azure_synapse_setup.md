# Azure Synapse Setup

> Connect your Azure Synapse Analytics Warehouse to Zenlytic

This document will help you connect your Azure Synapse Analytics Warehouse to Zenlytic to access modern, LLM-powered business intelligence.

Connection Name

First, you'll name your connection. This name is how Zenlytic's [model](/data_modeling/model) connects the credentials you'll enter in the next step to your data warehouse. You can name the credential whatever you want, but we usually recommend naming it something like `my_company_name` to keep things simple.

Host

The host for Azure Synapse Analytics is the "Dedicated SQL Endpoint" value in your Azure console.

![Azure Synapse Setup 1](/assets/azure-synapse-setup-1.png)
In this example, using Azure Synapse Analytics Warehouse with a Dedicated SQL Pool, the host is `zenlytic-demo-warehouse.sql.azuresynapse.net`

Username

This is the username for your Azure Synapse Analytics user. You'll create a user in SQL and use that username/password combination to let Zenlytic connect to your warehouse.

In this example, we'll assume your username is `synapse_user`

Password

This is the password associated with the user you entered above.

Database

The database is where you have the data you're interested in SQL Server. In this example, we'll assume your database is named `analytics`

Port

The default port is `1433`, so leave this field empty unless you've changed the value for the port.

Schema (optional)

This is the schema you'd like to use as a default. This field is optional and is usually left blank.

IP Whitelisting

If you use IP whitelisting in your data warehouse, whitelist the following IP addresses:

```
184.73.175.163 
18.209.132.30
```
