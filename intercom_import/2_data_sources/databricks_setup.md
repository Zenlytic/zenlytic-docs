# Databricks setup

> This article will help you connect your Databricks instance to Zenlytic

This document will help you connect your Databricks data warehouse to Zenlytic to access modern, LLM-powered business intelligence.

Connection Name

First, you'll name your connection. This name is how Zenlytic's [model](/data_modeling/model) connects the credentials you'll enter in the next step to your data warehouse. You can name the credential whatever you want, but we usually recommend naming it something like `my_company_name` to keep things simple.

Server Hostname

The Server Hostname in Databricks is how we know which Databricks SQL Warehouse to connect to. To get this value, go to the Connection Details tab of the SQL warehouse you want to connect.

![Databricks Setup 1](/assets/databricks-setup-1.png)

The value under the first header, "Server Hostname" is the value you should use.

Http Path

To get this value, go to the Connection Details tab of the SQL warehouse you want to connect and use the value under the "Http Path" heading.

![Databricks Setup 1](/assets/databricks-setup-1.png)

Personal Access Token

This is the access token associated with the user you want to use for connecting to Zenlytic. To find or create this token, go to User Settings -> Developer -> Access Tokens

![Databricks Setup 2](/assets/databricks-setup-2.png)
Then, click Generate New Token, set the Lifetime (days) to empty (this indicates the token does not expire), give the token a name like "Zenlytic" and click Generate

![Databricks Setup 3 - png)
Then, click Generate New Token, set the Lifetime (days) to empty (this indicates the token does not expire), give the token a name like "Zenlytic" and click Generate](/images/databricks-setup-3.png)

The value shown in the next step is the value you will use.

IP Whitelisting

If you use IP whitelisting in your data warehouse, whitelist the following IP addresses:

```
184.73.175.163 
18.209.132.30
```
