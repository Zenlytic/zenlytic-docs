---
sidebar_position: 1
---

# Exploring the Data model

There are several options in python for exploring a data model. Here are some examples of their usage:


### Views

When listing views, the default is to return a list of `View` [objects](../6_project/4_view.md). More information is available in the [view section](../../4_data_modeling/6_view.md) of the docs

```
from metrics_layer import MetricsLayerConnection

conn = MetricsLayerConnection()

# Lists of *all* the views in your data model
views = conn.list_views()

# You can also get a single view based on it's name.
view = conn.get_view("order_lines")
```


### Metrics

When listing metrics, the default is to return a list of `Field` [objects](../6_project/5_field.md). Listing metrics will return all measures associated with your LookML project.

```
from metrics_layer import MetricsLayerConnection

conn = MetricsLayerConnection()

# Lists of *all* the metrics in your data model
metrics = conn.list_metrics()

# List of metrics in this view
metrics_in_orders_customers_view = conn.list_metrics(view_name="customers")

# You can also get a single metric based on it's name.
# The below three calls return the same thing

# Metric name
metric = conn.get_metric("total_revenue")

# View and metric name
metric = conn.get_metric("orders.total_revenue")
```


### Dimensions

When listing dimensions, like listing metrics, the default is to return a list of `Field` [objects/](../6_project/5_field.md). Listing dimensions will return all dimensions and dimension_groups associated with your LookML project.

```
# Lists of *all* the dimensions in your data model
dimensions = conn.list_dimensions()


# List of dimensions in this view
dimensions_in_orders_customers_view = conn.list_dimensions(view_name="customers")

# You can also get a single dimension based on it's name.
# The below three calls return the same thing

# Dimension name
dimension = conn.get_dimension("total_revenue")

# View and dimension name
dimension = conn.get_dimension("orders.total_revenue")

```