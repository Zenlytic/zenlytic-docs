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

# Integrations Overview

The metrics layer (obviously) integrates with [Zenlytic's own data model](../data-modeling/data_modeling.md) as the Cognitive layer, and dbt's semantic layer with [Metricflow](https://docs.getdbt.com/docs/build/sl-getting-started). The metrics layer supports versions 1.8 - 1.10 of dbt's semantic layer (Metricflow). More details on the integration can be found [here](../data-modeling/dbt_metricflow.md).

The metrics layer no longer supports dbt Metrics (changed in `0.11.X` and above). Use `0.10.X` and below if you need dbt metrics support.

Zenlytic integrates with the following data warehouses:

* Snowflake
* BigQuery
* Redshift
* Postgres
* MySQL
* Databricks SQL Warehouse
* Druid
* DuckDB (MotherDuck)
* Trino
* SQL Server
* Azure Synapse Analytics
