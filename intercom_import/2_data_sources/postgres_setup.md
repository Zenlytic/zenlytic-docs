# Postgres setup

> Connect your Postgres database to Zenlytic

This document will help you connect your Postgres database to Zenlytic to access modern, LLM-powered business intelligence.

Connection Name

First, you'll name your connection. This name is how Zenlytic's [model](/data_modeling/model) connects the credentials you'll enter in the next step to your data warehouse. You can name the credential whatever you want, but we usually recommend naming it something like `my_company_name` to keep things simple.

Host

The host for Postgres is the "Endpoint" value in your AWS console (if you're using AWS). If you're not using AWS, you must get the host value and enter it.

![Postgres Setup 1](/assets/postgres-setup-1.png)
In this example using Postgres hosted on RDS, the host (privacy obscured) is `zenlytic-demo-data-db.blahblahblah.us-east-1.rds.amazonaws.com`

Username

This is the username for your Postgres user. You'll create a user in SQL and use that username/password combination to let Zenlytic connect to your database.

In this example, we'll assume your username is `postgres_user`

Password

This is the password associated with the user you entered above.

Database

The database is where you have the data you're interested in Postgres. You can use a tool like [PgAdmin](https://www.pgadmin.org/) or [psql](https://www.postgresql.org/docs/current/app-psql.html) to view databases in your Postgres instance. In this example, we'll assume your database is named `analytics`

Port

The default port is `5432`, so leave this field empty unless you've changed the value for the port.

Schema (optional)

This is the schema you want to use as a default. This field is optional and is usually left blank.

Advanced Settings (SSH Tunnel)

There are also advanced settings that allow you to configure the connection to flow through a bastion host via SSH.

### IP Whitelisting

If you use IP whitelisting in your data warehouse, whitelist the following IP addresses:

```
184.73.175.163 
18.209.132.30
```
