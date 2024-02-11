---
sidebar_position: 1
---

# Getting Started

We're going to walk through setting up Zenlytic from scratch using your local development environment. You should have received a login to your workspace to begin the setup process.


## Defining your data model.

Documentation on defining your data model can be found [here](./4_data_modeling/1_data_modeling.md). You'll first need to create a GitHub repo, if one has not been defined already, then in that repo define the [models](./4_data_modeling/2_model.md) and [views](./4_data_modeling/5_view.md) you want. 


:::tip Zenlytic UI

To avoid messing around with your local python, you can use the [Zenlytic UI](https://app.zenlytic.com/data-model-editor) for all tasks listed below. The UI has error tracking built in, so you'll know if something isn't right.

:::


Once you create your repo, you can install the most recent version of the metrics layer with the database option of your choice.
```
pip install metrics-layer[snowflake]
``` 

This will install the metrics-layer package with the connector for Snowflake. It will also give you access to the `ml` command line interface, which you'll use throughout the setup process.

Then you'll run the init command to create your project structure. This will create folders and the `zenlytic_project.yml` file. 
```
ml init
```

Then you'll need to define your local connection credentials. You'll do this in exactly the same way as [you would for dbt](https://docs.getdbt.com/dbt-cli/configure-your-profile). Make sure that `profile` in your `zenlytic_project.yml` file is set to the same name as the dbt profile you just created.


Now you can use the seeding capability to make setup of the data model much easier. To seed all view files for a database schema run
```
ml seed --schema <YOUR_SCHEMA_NAME>
``` 
To seed a specific table run 
```
ml seed --schema <YOUR_SCHEMA_NAME> --table <YOUR_TABLE_NAME>
```

To ensure your data model is correct you can run validation in the root of your repo and it will give you any warnings or errors associated with your project.
```
ml validate
```

There are a some example repos to help you as well! Here's one for our [standard yaml](https://github.com/Zenlytic/demo-data-model) syntax.
