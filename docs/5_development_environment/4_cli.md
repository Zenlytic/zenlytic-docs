---
sidebar_position: 4
---

# Command Line Interface

There are a few cli methods Zenlytic's metrics layer provides using its cli `ml`.

The first is the `debug` command. Once you finish [git setup](2_git.md) and [connection setup](3_database_connection.md), simply run the following command from the terminal.

```
$ ml debug
```

### Initialize

To initialize your project run this command.

```
$ ml init
```

This will create folders for models and views in addition to creating a file called `zenlytic_project.yml` that will tell Zenlytic which dbt profile to look for, and where to find the data model itself.

An example of that file will look like this

```
name: my_project_name # This can be anything you want
mode: dbt (only necessary when using dbt metrics)
profile: my_dbt_profile # This references the name in your dbt profiles.yml file

model-paths: ['models'] # This is the folder where your models are (optional with dbt metrics)
view-paths: ['views'] # This is the folder where your views are (unnecessary with dbt metrics)
dashboard-paths: ['dashboards'] # This is the folder where your dashboards are

```


### Seeding 

One of the most helpful if you're just starting out is the `seed` method. If you haven't started writing your data model or if you've recently added a new database, it's a pain to go in and manually set up the views and columns. `seed` allows you to specify a database and optionally a schema, and it will programmatically read the tables in that database or schema and generate the views and fields to give you a nice starting place.

Here are some examples (the `$` indicates these examples are taking place in the terminal):

If you want to generate initial views from only tables in the `prod_zendesk` schema inside the `analytics` database

```
$ ml seed --database analytics --schema prod_zendesk
```


If you want to generate initial views from all tables inside the `analytics` database

```
$ ml seed --database analytics 
```

If you want to generate initial views from the `zendesk_metrics` table 

```
$ ml seed --database analytics --schema prod_zendesk --table zendesk_metrics
```


### Validation 

Another helpful feature is the `validate` feature. It allows you to statically check if you have any broken references or invalid types in your project before deploying it anywhere or using it top query live data. It is run with the following command.

```
$ ml validate
```

Two additional helper commands are the `list` and `show` commands. The `list` command lists the names of objects from the type you pass, and the `show` command shows printable attributes of the object with the name you pass. Here are some examples.

This lists the names of all the models in your project

```
$ ml list
```

This command lists all the metrics (fields of type `measure`) in the view `transactions`

```
$ ml list --view transactions metrics
```

This command shows the attributes of the field `total_revenue`

```
$ ml show --type field total_revenue
```

This command shows the attributes of the view `transaction_lines`

```
$ ml show --type view transaction_lines
```

Have any other ideas for good cli tools to help with development? Open a [GitHub issue](https://github.com/Zenlytic/metrics_layer/issues) and let us know!