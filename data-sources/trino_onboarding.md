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

# Trino Onboarding

> How to set up a Trino data warehouse in Zenlytic

This document will help you connect your Trino data warehouse to Zenlytic to access modern, LLM-powered business intelligence.

## Connection Name

First, you'll name your connection. This name is how Zenlytic's [model](../5_data_modeling/model/) connects the credentials you'll enter in the next step to your data warehouse. You can name the credential whatever you want, but we usually recommend naming it something like `my_company_name` to keep things simple.

## Host

The host in Trino is how we know where you're hosting your data warehouse. This can be an IP address or a URL if you're hosting Trino on cloud resources you own.

In this example, you'd enter `44.33.25.5` for your account.

## Port

This is the port to use to connect to your Trino data warehouse. The default value is `8080`.

In this example, the port is `8080`

## Username

This is the username of your user in Trino.

In this example, the username is `pblankley`

## Password

This is the password associated with the user you logged in with. Enter the value in the input.

## Catalog

This is the catalog you want to set as the default. A catalog in Trino references a data source (e.g. a Postgres database). All catalogs can be referenced in subsequent queries, but a default is required.

In this example, the catalog is `postgresql`

## Advanced Settings

### Scheme (optional)

This is the method of connecting to your Trino data warehouse. The default is `http`, but it can be changed to `https`.

In this example, we'll use the default `http` scheme.

### IP Whitelisting

If you use IP whitelisting in your data warehouse, whitelist the following IP addresses:

```
184.73.175.163 
18.209.132.30
```
