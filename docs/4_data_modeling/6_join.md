---
sidebar_position: 6
---

# Joins

Joins are how views are connected to each other. The are defined by `identifiers` on the views. `identifiers` can be defined as primary keys, foreign keys, or explicit point to point joins.

Joins, are stored in View files in Zenlytic, which are YAML text files.

---

### Properties

These properties are the ones you can define for an `identifier` in a view.

`name`: (Required) The name of the identifier. This is the value used to match identifiers across views. Like all names, it follows [Zenlytic naming conventions](1_data_modeling.md#naming-conventions).

`type`: (Required) The type of the join. This can be one of `primary` (for a unique, primary key), 'foreign` (for a foreign key), or `join` (a custom point-to-point join).

`sql`: The sql definition of the join. This is only used for `primary` and `foreign` join types, and is just a reference to the key (e.g. `${user_id}`). 

`reference`: Only used for type `join`. This is the other view referenced in the join. For example, if you define the identifier in the `orders` view and you want to join in customer information, you would specify `customers` as the `reference`.

`relationship`: Only used for type `join`. One of `one_to_one`, `many_to_one`, `one_to_many`, `many_to_many`. It specifies the join type from the view the join is defined in to the referenced view. The default is `many_to_one`.

`sql_on`: This is only for (type `join`) joins and can be any arbitrary SQL with references to either the view the join is defined in or to referenced view.

`allowed_fanouts`: This is used for `primary` and `foreign` join types, and it is a list of referenced views you would like to allow fanout joins for. By default, Zenlytic will not allow fanout joins, but you can explicitly allow them for certain views using this property. Zenlytic uses [symmetric aggregates](./96_symmetric_aggregates.md) to calculate metrics correctly even in the event of a fanout join

### Identifier Join Example

This is a basic view with a few dimensions and measures, that explicitly references the `prod.order_lines` table. This view defines it's primary key (`order_line_id`), a foreign key (named customer_id but that references the `customer_email` field), and a custom join to the `discounts` view based on a `sql_on` criteria.

Since `order_line_id` is defined as a primary key, this view will be available to join in any table that references `order_line_id` as a foreign key.

Since `customer_id` is defined as a foreign key, all views that define `customer_id` as a primary key will be available to join in to this view.

Since `discount_join` is defined as a custom join, exactly one (`many_to_one`) join relationship will exist between `order_lines` and `discounts` with this criteria.

```
version: 1
type: view
name: order_lines
model_name: demo_model

sql_table_name: prod.order_lines
default_date: order
row_label: Order Line

identifiers:
- name: order_line_id
  type: primary
  sql: ${order_line_id}
- name: customer_id
  type: foreign
  sql: ${customer_email}
- name: discount_join 
  type: join
  reference: discounts
  sql_on: ${discounts.order_id}=${order_lines.order_id} and ${discounts.product_id}=${order_lines.product_id}

fields:
.
.
. 

```

### Merged Results & Mappings


In addition to joins on specific keys (e.g. `customers.customer_id=orders.customer_id`), Zenlytic also has the ability to merge results. Merging results is where a join happens *after* the aggregation in the query. Merged results are closely related to Zenlytic's concept of "mappings." Mappings equate fields that mean the same thing but are in different un-joinable tables. For example, you might have a `channel` field on the orders table and a `marketing_channel` field on the marketing_spend table, and they represent the same thing and have the same values. You can set up a mapping that connects those two fields in Zenlytic and leaves only one option for the end users to select. Zenlytic will dynamically figure out which field it should use or if it needs to use both.

Additionally, Zenlytic automatically performs this mapping for time fields associated with metric. For example, in the subscription table you might have `number_of_subscriptions` trended over time by `created_at` and `number_of_cancellations` trended by `cancelled_at` You can select the mapped date, `number_of_cancellations`, and `number_of_subscriptions`, and when running the query, Zenlytic will query `number_of_cancellations` by `cancelled_at` and `number_of_subscriptions` by `created_at` and then merge the results of those two queries together for the final result. This ensures your metrics are always calculated correctly over time.

You can also define metrics that use merged results. For example, to define cost_per_acquisition or CPA you'll need to divide `marketing_spend` by `number_of_new_customers`. Those metrics don't live in the same table, to calculate them you'll have to calculate `marketing_spend` in one table and `number_of_new_customers` in another, then merge the results. Let's look at a full example of that here: 

This is the `demo_model` model. It contains a connection to the warehouse and a mapping between the `orders.channel` dimension and the `marketing_spend.marketing_channel` column.

```
version: 1
type: model
name: demo_model
connection: my_connection
timezone: America/New_York

# Note: The data, week, month, quarter, year mappings are reserved by default, and based on dates connected to metrics
mappings:
  channel: 
    fields: [marketing_spend.marketing_channel, orders.channel]
    group_label: "Acquisition" # This controls the header under which the mapped field shows up in the UI
    description: "The channel the customer came to our site from"

```

This is the `marketing_spend` view, it has several dimensions and metrics and a merged result metric, `cost_per_acquisition` which references a metric in the `orders` view.

```
version: 1
type: view
name: marketing_spend
model_name: demo_model

sql_table_name: prod.marketing_spend
default_date: spend_at

fields:
...

- name: marketing_channel
  field_type: dimension
  type: string
  sql: ${TABLE}.marketing_channel
  
...

- name: total_marketing_spend
  field_type: dimension
  type: sum
  sql: ${TABLE}.spend
  value_format_name: usd

- name: cost_per_acquisition
  field_type: measure
  type: number
  sql: ${total_marketing_spend} / nullif(${orders.number_of_new_customers}, 0)
  value_format_name: usd
  description: The cost per acquisition = marketing spend / newly acquired customers
  is_merged_result: yes # This tells Zenlytic explicitly to only ever calculate this metric as a merged result
  
  
```

With this setup, we could query `cost_per_acquisition` by `channel` by `week` and Zenlytic will calculate `total_marketing_spend` by `marketing_channel` and `spend_at_week` then merge that result with the result of `number_of_new_customers` by `channel` and `order_week` merging them together by `week` and `channel`. This let's you simply define a few mappings and dramatically increase the transformations available to end users on a self-serve basis.
