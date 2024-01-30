---
sidebar_position: 2
---

# Integrations

The metrics layer (obviously) integrates with [Zenlytic's own data model](../../4_data_modeling/1_data_modeling.md) as a data model, and dbt's semantic layer with [Metricflow](https://docs.getdbt.com/docs/build/sl-getting-started).

The metrics layer no longer supports dbt Metrics (changed in `0.11.X` and above). Use `0.10.X` and below if you need dbt metrics support.

It integrates with BigQuery, Redshift, Postgres, Databricks SQL Warehouse, Druid, DuckDB (MotherDuck), SQL Server, and Snowflake for data warehouses.

