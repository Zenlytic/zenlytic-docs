---
sidebar_position: 1
---

# Exploring the Data model

There are several options in python for exploring a data model. Here are some examples of their usage:


### Views

When listing views, the default is to return a list of `View` objects. More information is available in the [view section](../../5_data_modeling/5_view.md) of the docs

```
from metrics_layer import MetricsLayerConnection

# Connect to the repo we're at the root of right now
conn = MetricsLayerConnection('./')

# Lists of *all* the views in your data model
views = conn.list_views()

# You can also get a single view based on it's name.
view = conn.get_view("order_lines")
```


### Metrics

When listing metrics, the default is to return a list of `Field` objects. Listing metrics will return all measures associated with your data model.

```
from metrics_layer import MetricsLayerConnection

# Connect to the repo we're at the root of right now
conn = MetricsLayerConnection('./')

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

When listing dimensions, like listing metrics, the default is to return a list of `Field` objects. Listing dimensions will return all dimensions and dimension_groups associated with your data model.

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