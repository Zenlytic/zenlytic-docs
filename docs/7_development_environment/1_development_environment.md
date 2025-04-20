---
sidebar_position: 1
---

# Setting up

This is a high-level overview of how to start creating your Zenlytic data model in your local development environment. 

To start, you'll create a GitHub repo if you don't already have one (if you're using dbt and would like to integrate it with Zenlytic, you can use that existing repo).

To connect to your data warehouse in the Zenlytic UI follow [these steps](3_database_connection.md#zenlytic-connection), and to connect for local development follow the [steps here](3_database_connection.md#local-connection). 

We no longer support dbt Metrics, and only support dbt Metricflow.

If you're integrating with dbt Metricflow, you'll follow it's syntax and just set the `mode: metricflow` in your `zenlytic_project.yml` file.

If you're not integrating with dbt Metricflow, initialize your project you'll use the [metrics layer cli](4_cli.md#initialize) and run `ml init` in the root of the repo you want to use. 

To seed your model from your existing data warehouse tables follow the [instructions on seeding](4_cli.md#seeding) (note: this does not work for dbt Metricflow). 

That's the setup process! For further information on the data model and how to develop the metrics your company needs check out the documentation on [Zenlytic's data model](../5_data_modeling/1_data_modeling.md).

The steps above with links to more information:

1. [Create a GitHub repo](2_git.md)
2. [Connect to your database](3_database_connection.md)
3. [Initialize your project](4_cli.md)
4. [Seed your project with your data warehouse tables](4_cli.md#seeding)
5. [Integration with dbt Metricflow](../5_data_modeling/12_dbt_metricflow.md) (Optional)
