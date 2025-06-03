# Motherduck Setup

> For a ducking great setup experience

This document will help you connect your DuckDB data warehouse (on Motherduck) to Zenlytic to access modern, LLM-powered business intelligence.

Connection Name

First, you'll name your connection. This name is how Zenlytic's [model](/data_modeling/model) connects the credentials you'll enter in the next step to your data warehouse. You can name the credential whatever you want, but we usually recommend naming it something like `my_company_name` to keep things simple.

Service Token

You'll go to settings in your Motherduck interface, and copy the service token using the copy button on this page.

![Motherduck Setup 1](/assets/motherduck-setup-1.png)

Then, you'll put the service token in the Zenyltic interface.

Database

You must specify the database you want Zenlytic to connect to using DuckDB. For example, when you set up a new account with Motherduck, you'll have a database called `sample_data`, to connect that database to Zenlytic, you'd enter `sample_data` in the database field. 

### IP Whitelisting

If you use IP whitelisting in your data warehouse, whitelist the following IP addresses:

```
184.73.175.163 
18.209.132.30
```
