---
layout:
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# Druid Setup

> Connect your Apache Druid data warehouse with Zenlytic

This document will help you connect your Apache Druid data warehouse to Zenlytic to access modern, LLM-powered business intelligence.

## Connection Name

First, you'll name your connection. This name is how Zenlytic's [model](../5_data_modeling/model/) connects the credentials you'll enter in the next step to your data warehouse. You can name the credential whatever you want, but we usually recommend naming it something like `my_company_name` to keep things simple.

## Host

The host in Druid is how we know where you're hosting your data warehouse. This can be an IP address or a URL if you're hosting Druid on cloud resources you own.

In this example, you'd enter `44.33.25.5` for your account.

## Port

This is the port to use to connect to your Druid data warehouse. The default value is `8082`.

In this example, the port is `8082`

## Username

This is the username of your user in Druid.

In this example, the username is `pblankley`

## Password

This is the password associated with the user you logged in with. Enter the value in the input.

## Advanced Settings

### Path (optional)

This is the path in your Druid instance to submit SQL API statements to. The default is `/druid/v2/sql/`, and you rarely have to change this value.

In this example, we'll use the default `/druid/v2/sql/` path.

### Scheme (optional)

This is the method of connecting to your Druid data warehouse. The default is `http` and you rarely have to change this.

In this example, we'll use the default `http` scheme.

### IP Whitelisting

If you use IP whitelisting in your data warehouse, whitelist the following IP addresses:

```
184.73.175.163 
18.209.132.30
```
