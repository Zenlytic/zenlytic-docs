# Topics

Topics are collections of tables (views) that can be joined together using foreign keys. They are specified in their own yaml files. Each topic uses its model's `connection` that it is defined in to get data.

Topics exist to let you specify sections of your data that join together. They let you specify an explicit base view, and how joins work to connect other views to that base view.

You do not need to specify a join to add a view to a topic if there is already a join from the view you're adding to the base view of the topic. If you want to override that existing join, you can do so on the topic, and that will change the logic of how the view you're adding is joined into the topic.

Topics are how Zoë understands what views join together and how she finds data that is related to each other.

## Properties

`type`: (Required) The type of the file. For these topic files is should always be `topic`.

`base_view`: (Required) The base view of the topic. This is the name of the [view](view.md) you want to create the topic from.

`model_name`: (Required) The name of the [model](model.md) (e.g. database connection) the view references.

`label`: (Required) The label of the topic is what shows up to the end users of your data model. If not specified it defaults to the name of the topic.

`description`: This is the description of the topic. This is helpful to let business users know what data is referenced here.

`zoe_description`: The description of the topic shown to Zoë. If not set, Zoë uses `description` instead. If set, this replaces `description` for Zoë only. End users will still see `description` in the UI. Use this to provide context to Zoë on how to use the topic correctly.

`hidden`: A `true` indicates that this topic should be hidden in the user interface. If a topic is hidden it can still be referenced in the data model, despite not appearing to end users in the UI or to Zoë. The default is false which shows the topic in the UI.

`required_access_grants`: This is a list of [access grant](access_grants.md) names that are required to access this topic. The grant names are always an `OR` condition. For example, if you listed `human_resources` and `executive` under this parameter, users who qualified for `human_resources`, `executive` or both would all be able to access data in this topic.

`always_filter`: This is an optional list of filters which use the usual [field filter selection syntax](field_filter.md) and will _always_ be applied to the query. These filters are applied to the entire query, not just a metric or dimension, and if it is not possible to reference or join in the field needed for the filter it will result in an error.

### **Example below:**

Here are two filters that will be applied to _all_ queries that reference this topic. All fields need to specify the `view_name.field_name` they reference. Fields will be joined in dynamically whenever this topic is referenced to apply the filters.

```yaml
always_filter:
- field: customers.is_churned
  value: FALSE
- field: sessions.context_os
  value: -NULL
```

`access_filters`: This is an optional list of [access filters](access_grants.md#access-filters) to apply to the topic when it is queried.

`views`: References to views that are included in this topic. Each entry specifies either a view with default join logic or with custom join specifications. Views are joined to the base view or to previously defined views in the list.

Each view can have the following properties:

* `override_access_filters`: When set to `true`, access filters for this view will be ignored within this topic.
* `from`: The view to pull from to perform the join. This property is used when you want to join a view in twice to a topic on different conditions. By default, it is the same as the name of the view, and is optional. &#x20;
* `join`: Optional configuration to specify custom join logic:
  * `join_type`: The type of join (e.g., `left_outer`, `inner`, `full_outer`).
  * `relationship`: The cardinality relationship (e.g., `many_to_one`, `one_to_one`, `one_to_many`, `many_to_many`).
  * `sql_on`: The SQL expression that defines the join condition, using the `${view_name.field_name}` syntax.

If a view is specified with empty braces `{}` or without a `join` property, default join logic will be used based on foreign key relationships defined in the views.

`extra`: The extra property is like dbt `meta` property, and you can put whatever additional properties you want in here. For example, under this property you could add a property like this `maintainer: "jane doe"`

## Examples

The simplest example of a topic is how it's defined in a model when it's referencing only one view, in this case the `orders` view. This would be in a yaml file (e.g. `simple_topic.yml`).

```yaml
type: topic
base_view: orders
label: Orders
model_name: test_model
```

Topics can be extended by defining joins related to the topic. Here's a full example with many of the available properties.

{% code overflow="wrap" %}
```yaml
type: topic
label: Order lines unfiltered
base_view: order_lines
model_name: test_model
description: Vanilla order lines topic description
zoe_description: Secret info that is only shown to zoe
hidden: false

access_filters:
  - field: orders.warehouse_location
    user_attribute: warehouse_location
  - field: order_lines.order_id
    user_attribute: allowed_order_ids

views:
  orders:
    override_access_filters: true

  customers: {}

  discounts:
    join:
      join_type: left_outer
      relationship: many_to_many
      sql_on: ${order_lines.order_id} = ${discounts.order_id} and ${discounts.order_date} is not null

  discount_detail:
    join:
      join_type: left_outer
      relationship: one_to_one
      sql_on: ${discounts.discount_id} = ${discount_detail.discount_id} and ${orders.order_id} = ${discount_detail.discount_order_id}


```
{% endcode %}

#### Joining with from

You can use the `from` syntax to join the same view into a topic multiple times. This is an example of what that syntax looks like

```yaml
type: topic
label: From Syntax Topic Example
base_view: order_lines
model_name: test_model

views:
  # Join customers once via customer_id
  customers:
    from: customers  # In this case the from statement is redundent, and optional 
    label: Customer Info
    field_prefix: 'Customer'
    include_metrics: false
    join:
      join_type: left_outer
      relationship: many_to_one
      sql_on: ${order_lines.customer_id} = ${customers.customer_id}

  # Join customers again with different alias
  customer_accounts:
    from: customers
    label: Account Holder
    field_prefix: 'Account'
    join:
      join_type: left_outer
      relationship: many_to_one
      sql_on: ${order_lines.account_id} = ${customer_accounts.account_id}

```
