# MySQL setup

> How to set up your MySQL data warehouse

This document will help you connect your MySQL database to Zenlytic to access modern, LLM-powered business intelligence.

Connection Name

First, you'll name your connection. This name is how Zenlytic's [model](/data_modeling/model) connects the credentials you'll enter in the next step to your data warehouse. You can name the credential whatever you want, but we usually recommend naming it something like `my_company_name` to keep things simple.

Host

The host for MySQL is the "Endpoint" value in your AWS console (if you're using AWS). If you're not using AWS, you must get the host value and enter it.

![Mysql Setup 1](/assets/mysql-setup-1.png)

In this example using MySQL hosted on RDS, the host (privacy obscured) is `mysql-behind-ssh-tunnel.blahblahblah.us-east-1.rds.amazonaws.com`

Username

This is the username for your MySQL user. You'll create a user in SQL and use that username/password combination to let Zenlytic connect to your database.

In this example, we'll assume your username is `mysql_user`

Password

This is the password associated with the user you entered above.

Database

The database is where you have the data you're interested in MySQL. You can use a tool like [MySQL Workbench](https://www.mysql.com/products/workbench/) to run queries on your database. In this example, we'll assume your database is named `analytics`

Port

The default port is `3306`, so leave this field empty unless you've changed the value for the port.

Advanced Settings (SSH Tunnel)

There are also advanced settings that allow you to configure the connection to flow through a bastion host via SSH.

IP Whitelisting

If you use IP whitelisting in your data warehouse, whitelist the following IP addresses:

```
184.73.175.163 
18.209.132.30
```
