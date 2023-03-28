---
sidebar_position: 1
---

# Project

The project object is the class you use to interact with your project as a whole. It has many convenience methods that allow you to look around the project.

Once you create a connection, you can access the project like this:

```
from metrics_layer import MetricsLayerConnection

# Connect to the repo we're at the root of right now
conn = MetricsLayerConnection('./')

project = conn.project
```

Using the project object, you can look around your entire data model.


### Models
```
# Models
all_models_in_project = project.models()

a_single_model = project.get_model(model_name="revenue")
```

### Dashboards
```
# Dashboards
all_dashboards_in_project = project.dashboards()

a_single_dashboard = project.get_dashboard("sales_dashboard")
```

### Views
```
# Views
all_views_in_project = project.views()

a_single_view = project.get_view(view_name="orders")
```


### Fields
```
# Fields
all_fields_in_project = project.fields()


all_fields_in_view = project.fields(view_name="orders")

# Only specify field name
a_single_field = project.get_field("total_revenue")

# Specify view and field name
a_single_field = project.get_field("orders.total_revenue")

# OR pass them as arguments
a_single_field = project.get_field("total_revenue", view_name="orders")
```


To learn more about any of the types returned here, look at the documentation for [models](../../4_data_modeling/2_model.md), [dashboards](../../4_data_modeling/3_dashboard.md), [views](../../4_data_modeling/5_view.md), or [fields](../../4_data_modeling/9_field.md).
