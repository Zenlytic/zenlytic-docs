---
sidebar_position: 2
---

# Integrations

The metrics layer (obviously) integrates with [Zenlytic's own data model](../../5_data_modeling/1_data_modeling.md) as the Cognitive layer, and dbt's semantic layer with [Metricflow](https://docs.getdbt.com/docs/build/sl-getting-started). The metrics layer supports versions 1.8 - 1.10 of dbt's semantic layer (Metricflow). More details on the integration can be found [here](../../5_data_modeling/12_dbt_metricflow.md).

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
