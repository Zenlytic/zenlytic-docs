---
sidebar_position: 1
---

# Setting up

This is a high level overview of how to get started creating your Zenlytic data model. 


To start you'll create a GitHub repo if you don't already have one (if you're using dbt and you'd like to integrate it with Zenlytic, you can use that existing repo).

To connect to your data warehouse in the Zenlytic UI follow [these steps](3_database_connection.md#zenlytic-connection), and to connect for local development follow the [steps here](3_database_connection.md#local-connection). 

To initialize your project you'll use the [metrics layer cli](4_cli.md#initialize) and run `ml init` in the root of the repo you want to use. 

To seed your model from your existing data warehouse tables follow the [instructions on seeding](4_cli.md#seeding). 

That's the setup process! For further information on the data model and how to develop the metrics your company needs check out the documentation on [Zenlytic's data model](../4_data_modeling/1_data_modeling.md).

The steps above with links to more information:

1. [Create a GitHub repo](2_git.md)
2. [Connect to your database](3_database_connection.md)
3. [Initialize your project](4_cli.md)
4. [Seed your project with your data warehouse tables](4_cli.md#seeding)
5. [Integrate with dbt](6_dbt_files.md) (Optional)
