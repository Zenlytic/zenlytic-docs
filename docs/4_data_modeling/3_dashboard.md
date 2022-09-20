---
sidebar_position: 3
---

# Dashboards

Dashboards are collections of dashboard elements. Dashboard elements are plots or tables created with a combination of measures and dimensions that can be joined together.

Dashboards are specified in yaml files, like all files in Zenlytic.

---

### Dashboard Properties

`type`: (Required) The type of the file. For these dashboard files is should always be `dashboard`.

`name`: (Required) The name of the dashboard. This name is used to uniquely determine the dashboard and presented in the url, so it must be unique across dashboards in your project. If you reference this dashboard elsewhere this is the name you will use. Like all names, it follows [Zenlytic naming conventions](1_data_modeling.md#naming-conventions)

`label`: The label of the dashboard is what shows up to the end users of your data model. If not specified it defaults to the name of the dashboard.

`description`: This is the description of the dashboard. This is helpful to let business users know what plots and tables to expect.

`filters`: This is a list of filters which follow the [field filter](94_field_filter.md) syntax.
```
  - field: orders.new_vs_repeat
    value: New
```
`elements`: This is a list of dashboard elements, which are covered below.



# Dashboard Elements

Dashboard elements determine what to display for each element in the dashboard.

### Dashboard Element Properties

`model`: (Required) The name of the model you want to base this dashboard element from.

`metrics`: (Required) This is a list of metric names to display in the dashboard element. For example, `orders.total_revenue` would reference the `total_revenue` measure in the `orders` view.

`slice_by`: This is a list of slices (dimensions or dimension_groups) to apply to the plot or table. For example, `orders.new_vs_repeat` references the `new_vs_repeat` dimension in the `orders` view, and `orders.order_month` references the dimension_group `order` using the `month` timeframe.

`filters`: This is a list of filters that follow the standard [field filter](94_field_filter.md) syntax. For example, the following filter ensures that the `product_name` dimension in the `order_lines` view is not equal to "Handbag"
```
  - field: order_lines.product_name
    value: -Handbag
```

`cohort_by`: This is a dimension group of type `duration` that you would like to cohort the plot by.

`time_period`: This is the time period for Zenlytic to apply to all metrics and slices in the query. The default value is `any_time`, which does not apply a time period filter. The options are:
  `1_days`
  `7_days`
  `last_week`
  `30_days`
  `last_month`
  `90_days`
  `last_quarter`
  `180_days`
  `last_year`
  `wtd` (week to date)
  `mtd` (month to date)
  `qtd` (quarter to date)
  `ytd` (year to date)
  `any_time` (or leaving the field blank)
For more advanced, fine-grained controls over the time filters, use the [field filters](94_field_filter.md) under the `filters` property.

`sort`: This is a list of sorts to apply. A sort is defined with a `field` (any field accessible in the data model) and `value` (either asc or desc, defaults to asc if empty) property like this:
```
sort:
- field: orders.campaign
  value: desc
```
## Examples

Here is an example of a dashboard file for a retention dashboard with two elements (the second of which is a cohort plot). The time period applied to both plots means that the data will all be within the last 30 days.

```
type: dashboard
name: retention_dashboard
label: Retention Dashboard
description: Retention data broken out by various factors

elements:
  - model: demo
    metrics: [orders.repeat_order_rate, orders.average_order_value]
    slice_by: [orders.product]
    time_period: 30_days

  - model: demo
    metrics: [orders.repeat_order_rate]
    slice_by: [orders.product]
    cohort_by: orders.weeks_duration_firstorder_thisorder
    time_period: 30_days
```

Here is an example of a dashboard file with a filter at the dashboard level, and an additional filter applied to the second plot. The dashboard level filter will apply to both plots when the dashboard is run and/or when the filter is changed. The second of the two plots will have an additional filter applied which filters out the `CabinSummerVideo_TikTok` campaign from the results. This dashboard also includes a sort to make sure the campaigns are organized from highest in terms of total revenue to lowest.


```
type: dashboard
name: sales_dashboard
label: Sales Dashboard (with campaigns)
description: Sales data broken out by campaign and repurchasing behavior
filters:
  - field: orders.acquisition_channel
    value: -Organic

elements:
  - model: demo
    metric: orders.total_revenue
    slice_by: [orders.new_vs_repeat, orders.product]
    time_period: last_month

  - model: demo
    metrics:
      - orders.total_revenue
      - orders.average_order_value
      - orders.number_of_orders
    slice_by: [orders.campaign]
    time_period: last_month
    filters:
     - field: campaign
       value: -CabinSummerVideo_TikTok
    sort:
    - field: orders.total_revenue
      value: desc
```

