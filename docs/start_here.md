---
sidebar_position: 2
---

# Start here

We're going to walk through setting up Zenlytic from scratch. You should have received a login to your workspace to begin the setup process.


## Connecting your git repo

First, if it's not already created, set up a Github repo for your data model. Once you create your repo, go to the [Zenlytic UI](https://app.zenlytic.com/data-model-editor), and go to Workspace Settings. 


![workspace-settings](assets/workspace-settings.png)

Once there, follow the docs for [connecting your Github repo using a deploy key](https://intercom.help/zenlytic/en/articles/6960775-connecting-to-github-with-a-deploy-key).


## Connecting to your data warehouse

Once you've filled in GitHub credentials, you can click "+ Add Connection" under "Database Connections" in the settings menu. You'll first need to select your warehouse type from the drop down, and name your connection. 

The naming of the connection is how Zenlytic links database credentials with your data model. The name of the connection here must be the same as the `connection` property in the [model](./5_data_modeling/2_model.md) or the same as the dbt `profile` if integrating with dbt Metricflow without a model file. 

For example, to connect with this [example repo](https://github.com/Zenlytic/demo-data-model) we'd use the connection name `demo` because that's the value of `connection` in the [model file](https://github.com/Zenlytic/demo-data-model/blob/master/models/pure_organics_model.yml).  


Finally, finish filling out your data warehouse's connection information and click save

![finish-connection](assets/finish-connection.png)



## Defining your data model

Documentation on defining your data model can be found [here](./5_data_modeling/1_data_modeling.md). In the repo you connected earlier, you'll define the [models](./5_data_modeling/2_model.md) and [views](./5_data_modeling/5_view.md) you want. Here's an example repo for an direct-to-consumer cosmetics brand in our [standard yaml](https://github.com/Zenlytic/demo-data-model) syntax.


To start defining metrics, go to the [Data Model Editor](https://app.zenlytic.com/data-model-editor) in the Zenlytic UI.


To add a new table click "Create view from table" and select tables to bring into your data model. You can bring tables in using AI to define your metrics (which takes 1-3 min), or you can uncheck that box to just get the explicit table metadata.


![create-view-from-table](assets/create-view-from-table.png)


Once, the table is imported, you'll see a yaml file with dimensions defined. Make sure you select your desired `default_date` for the [view](./5_data_modeling/5_view.md) if you're defining metrics, define the [identifiers](./5_data_modeling/6_join.md) for joins, and define the aggregates ([metrics / measures](./5_data_modeling/93_measure.md)) you want to use.


To make your changes live for other users on the production branch, click "Deploy to Production" in the upper right of the data model editor page. That will publish your changes and make sure Zoë (the chatbot) has the latest information on your production metrics.


## FAQ

**Not seeing metrics in the Zenlytic interface?**
* If you have the `hidden` property set to `true`, you won't see those metrics or dimensions anywhere in the UI. Make sure you remove the hidden property or set it to `false` if you want those metrics to show up in the UI. 

```
# This metric won't show up in the UI because hidden is set to true
- name: number_of_orders
  field_type: measure
  type: count_distinct
  sql: ${order_id}
  description: "The unique number of orders placed"
  value_format_name: decimal_0
  hidden: yes
```

**Want to use a local development environment?**
* If you'd prefer to use a local development environment you can follow [our docs for setup](./6_connecting_with_python/getting_started_local.md). 


## Where do I go from here?

If you want to learn more about how to use the user interface and the different capabilities it has, check out the [documentation on the user interface](./3_zenlytic_ui/1_using_zenlytic.md)!

If you want to learn about data modeling and how to define your metrics check out the [documentation on the data model](./5_data_modeling/1_data_modeling.md)

If you'd like to learn about how to get everything set up for defining those metric definitions look at the [documentation on your metric development environment](./5_development_environment/1_development_environment.md)

As always, feel free to reach out to your Zenlytic contact if you have questions that aren't answered in the documentation!
