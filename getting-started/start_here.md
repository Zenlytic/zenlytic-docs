# Start Here

We're going to walk through setting up Zenlytic from scratch. You should have received a login to your workspace to begin the setup process.

There are two external connections Zenlytic needs to make to function.

1. Your data warehouse.
2. Git for your data model.

## Connecting to your data warehouse

You can click "+ Add Connection" under "Database Connections" in the settings menu. You'll first need to select your warehouse type from the drop down, and name your connection.

The naming of the connection is how Zenlytic links database credentials with your data model. The name of the connection here must be the same as the `connection` property in the [model](../data-modeling/model.md) or the same as the dbt `profile` if integrating with dbt Metricflow without a model file

For example, to connect with this [example repo](https://github.com/Zenlytic/demo-data-model) we'd use the connection name `demo` because that's the value of `connection` in the [model file](https://github.com/Zenlytic/demo-data-model/blob/master/models/pure_organics_model.yml)

Finally, finish filling out your data warehouse's connection information and click save

![Finish Connection](../.gitbook/assets/finish-connection.png)

## Git

Git should be already connected. You should continue using Zenlytic's default "Managed Repo", which involves no setup. If you want to switch from that to a separate repo, you can contact support.
