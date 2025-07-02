# dbt MetricFlow Integration

To integrate Zenlytic's data model with your dbt models, define the dimensions and measures (metrics) in semantic models section of dbt. Follow this page to get started with [Metricflow (dbt Semantic Layer)](https://docs.getdbt.com/docs/get-started-dbt).

## Setup

If you want to see an end to end example, you can follow [this example](https://github.com/Zenlytic/demo-data-model/tree/metricflow) on top of a demo data model.

To start, you will need to connect your github repo that has your dbt semantic layer project.

Next, you'll need to add a `zenlytic_project.yml` file in the root of the repo. This file is what Zenlytic uses to find files in your repo. You'll want it to look like:

{% hint style="info" %}
Configuration File

```
# The name doesn't matter functionally.
name: demo_zenlytic_project

# To connect with metricflow, you'll need to add this line. 
# This tells Zenlytic to look for Metricflow files.
mode: metricflow

# This is the connection name for the warehouse creds you entered in the Zenlytic UI profile: `demo`

# If your metricflow files are not located in a subfolder to the `dbt_project.yml` file, you will need to specify this location.
metricflow-path: 'metricflow/'

# Zenlytic has a concept of "Topics" that Metricflow doesn't have. 
# We can make them automatically (default behavior) when this arg is
# `true`, and we will not make them, if it is false use_default_topics: `true`

# These are paths to file resources.

topic-paths:
- topics
view-paths:
- views
dashboard-paths:
- dashboards
model-paths:
- models
```
{% endhint %}

Once you have that `zenlytic_project.yml` file ready to go, Zenlytic will be able to see your files.

## Reading Metricflow Semantics

Zenlytic will handle all mappings for Metricflow native objects automatically. Here are a few ways you might want to extend Metricflow in Zenlytic.

### Models

The default model will act as nothing but a connection to the data warehouse (the `profile` property does that in the above file example). If you want to use more advanced options in the [model](model.md), like [access controls](access_grants.md) or changing the `week_start_day`, then you can create one (and only one) model file, and put that file in whatever directory you have in the `model-paths` options in the `zenlytic_project.yml` file.

### Topics

[Topics](topic.md) are collections of tables (views) that can be joined together. You can choose to leave the `use_default_topics: true` and let Zenlytic automatically infer the topics based on your Metricflow join graph, or you can set it to `use_default_topics: false` and define the topics yourself for more granular control.

### Extra properties

For all objects, which are: Semantic Models (which map to [views](view.md) in Zenlytic), dimensions (which map to [dimensions](dimension.md) or [dimension groups](dimension_group.md) in Zenlytic), measures and Metrics (which both map to [measures](measure.md) in Zenlytic), you can pass through extra Zenlytic-specific properties using the dbt `meta` tag.

In every dbt `meta` tag, Zenlytic will look for a `zenlytic` property, which should include the properties you want to pass through, and will apply all of those properties to the object in Zenlytic.

For example, if you wanted to add an access control for the `email` dimension in Metricflow using your `pii_access` access grant, you would define it like so:

```yaml
- name: first_name
  type: categorical
  meta:
    zenlytic:
        required_access_grants: [pii_access]
```

The `required_access_grants: [pii_access]` property will get passed through to Zenlytic.

Likewise, in Semantic Models (what Zenlytic calls [views](view.md)), you may want to be explicit about the schema the model is pointing to, beyond the default in the database credentials setting. You could do that like:

```yaml
semantic_models:
  - name: products        
    label: Product        
    model: ref('products')
    meta:
      zenlytic:
        sql_table_name: demo_prod.products
```

This will pass through the `sql_table_name: demo_prod.products` property tp the Zenlytic view, which will override the value inherited automatically from the `model: ref('products')` property.

## Limitations

Here let's talk through some limitations of Zenlytic's integration with Metricflow.

Zenlytic does _not_ support the following concepts in Metricflow:

1. The `percentile` aggregation on a measure
2. The usage of [natural keys](https://docs.getdbt.com/docs/build/entities) in joins (using an array of fields to join instead of 1 field or custom SQL)
3. [Cumulative metrics](https://docs.getdbt.com/docs/build/cumulative)
4. [Conversion metrics](https://docs.getdbt.com/docs/build/conversion)
5. `offset_window` property in derived metrics
6. `Metric` and `Entity` parameterized [filter types](https://docs.getdbt.com/docs/build/ref-metrics-in-filters)

Have other questions? Reach out to our support in-application for more help.
