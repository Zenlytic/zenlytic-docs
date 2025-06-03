# Redshift setup

> Connect your Redshift data warehouse to Zenlytic

This document will help you connect your Redshift data warehouse to Zenlytic to access modern, LLM-powered business intelligence.

Connection Name

First, you'll name your connection. This name is how Zenlytic's [model](/data_modeling/model) connects the credentials you'll enter in the next step to your data warehouse. You can name the credential whatever you want, but we usually recommend naming it something like `my_company_name` to keep things simple.

Host
====

The host for Redshift is the "Endpoint" value in your AWS console. 

![Redshift Setup 1](/assets/redshift-setup-1.png)

In this example using Redshift Serverless, the host (privacy obscured) is `default.123456789.us-east-1.redshift-serverless.amazonaws.com:5439/dev`

Username

This is the username for Redshift. You'll create this user using SQL. In this example, let's assume your username is `redshift_user`

Password

This is the password associated with the user you entered above.

Database

This is the default database to connect to when connecting to Redshift. You can find this value under Namespace Configuration.

![Redshift Setup 2](/assets/redshift-setup-2.png)

In this example, the database is `dev`

Port

The default port is `5439`, so leave this field empty unless you've changed the value for the port.

Schema (optional)

This is the schema you want to use as a default. This field is optional and is usually left blank.

### IP Whitelisting

If you use IP whitelisting in your data warehouse, whitelist the following IP addresses:

```
184.73.175.163 
18.209.132.30
```
