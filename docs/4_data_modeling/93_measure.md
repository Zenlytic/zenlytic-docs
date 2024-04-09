---
sidebar_position: 12
---

# Measures (or metrics)

Measures (or metrics) are aggregations performed inside of a SQL `group by` statement. A simple one is `sum(sales)`, which you could specify in your data model with `type: sum` and `sql: ${TABLE}.sales`. They can get highly complex and are as flexible as your data warehouse's SQL syntax.

---

### Properties

`name`: (Required) The name of the measure (or metric). If you reference this measure (or metric) elsewhere in your data model you will use this value. Like all names, it follows [Zenlytic naming conventions](1_data_modeling.md#naming-conventions)

`field_type`: (Required) The field type of the field. For measures (or metrics) this is always `measure`.

`type`: (Required) The type of the field. For measures this is one of `sum`, `average`, `count`, `count_distinct`, `sum_distinct`, `average_distinct`, `median` (if supported in your database), `max`, `min`, `cumulative`, or `number`. Note, both `sum_distinct` and `average_distinct` require you to pass a value to the `sql_distinct_key` property. `cumulative` requires you to pass the `measure` property.

`label`: The label of the measure (or metric) is what shows up to the end users of your data model. If not specified it defaults to the name of the measure (or metric).

`description`: The description of the measure (or metric). This is shown in the UI and can help end users understand what the field represents. When this is set and the `zoe_description` property is not set, this will be shown to Zoë. Use this to provide context to Zoë on how to use the field correctly.

`zoe_description`: The description of the measure (or metric) shown to Zoë. If not set, Zoë uses `description` instead. If set, this replaces `description` for Zoë only. End users will still see `description` in the UI. Use this to provide context to Zoë on how to use the field correctly.

`group_label`: The label of the view the field is put into in the left hand sidebar menu. If not specified it defaults to the name of the view the field is present in.

`hidden`: A `true` indicates that this field should be hidden in the user interface. If a field is hidden it can still be referenced in the data model, despite not appearing to end users as a selectable field. The default is false which shows the field in the UI.

`sql`: (Required) This is the SQL expression that generates the field value. It can be as simple as `${TABLE}.my_field_name` which just references a column in the database table, or something more advanced that references previously defined fields, like `case when ${channel} ilike '%owned' then 1 else 0 end`.

`value_format_name`: This is the format to use when displaying the field. Check out [field formatting](95_formatting.md) to see available options. The default is `decimal_1`, which formats `12543.5524` to `12,543.6`.

`synonyms`: This is a list of strings phrases or words that you want to act as synonyms for natural language search. For example, if your measure is named `total_revenue` you might have synonyms of `['total sales', 'income']`. This works like a keyword search under the hood, to make fields with synonyms related to the question asked show up in context for Zoë.

`required_access_grants`: This is a list of [access grant](8_access_grants.md) names that are required to access this field. The grant names are always an `OR` condition. For example, if you listed `human_resources` and `executive` under this parameter, users who qualified for `human_resources`, `executive` or both would be able to access this field. Note, if the user has access to the field but does NOT have access to the view the field is defined in, the user will not be able to see the field.

`sql_distinct_key`: This tells Zenlytic that the measure you are calculating here is duplicated, and what field or expression it is unique on. For example, if you have a sales amount that is tied to an order but present in a order lines table, you could set this value to `order_id` and the type to `sum_distinct` to correctly sum up the sales amount without double counting. See [symmetric aggregates](96_symmetric_aggregates.md) for more information.

`measure`: This is only used when the metric has the type `cumulative`. A cumulative metric will sum up that metric over all time, and the measure property specifies which metric to aggregate over all time. For example, you could have a metric of type `sum` called `total_revenue` and create a cumulative metric referencing that named `cumulative_revenue` which calculates the `total_revenue` metric cumulatively. 

`filters`: This is a list of [field filters](94_field_filter.md), which have two properties, `field` and `value`. For example, the below field filter equates to the SQL where clause `where channel != 'Paid'`. Note, you *cannot* apply filters to measures of type `number`. You must apply your filters to the input measures, to achieve that result.
```
- field: channel
  value: "-Paid"
```

`canon_date`: This is the date to use when trending this metric over time or applying a time period. It defaults to the `default_date` of the view the metric is in, but you can override it here. When you override it, just use the `name` of the date field (e.g. use `order_at` instead of `order_at_date` which also contains a dimension group).

`non_additive_dimension`: This property defines a dimension over which the metric cannot be aggregated (usually a time dimension). An example of this type of metric would be MRR (Monthly Recurring Revenue) where each customer in your database has their MRR as of a single day in the database. To get the right answer, you can't just sum up MRR over all days, you have to take MRR for each customer on the most recent day that customer had an MRR value and then sum *that*. 

For example, let's look at a daily MRR table that includes one row per date of the account, the account's id, the account's plan type, and the plan's MRR in the following columns:

| record_date   | account_id | plan_type | mrr_value |
|------------|------------|-----------|------------|
| 2022-01-01 | 123        | Basic     | $20        |
| 2022-01-02 | 123        | Basic     | $50        |
| 2022-01-03 | 125        | Basic     | $20        |
| 2022-01-04 | 126        | Enterprise| $100       |

The Non Additive Dimension has three properties in it. 
* `name`: This references the fully qualified name of the field you're referencing (e.g. `record_date_raw`). 
* `window_choice`: This is either `max` or `min` and indicated whether you want to choose the start of period value (min) or the end of period value (max). 
* `window_aware_of_query_dimensions`: (Optional) This is either `true` or `false`. When `true`, it will include all group by dimensions in the metric's calculation. For example, when calculating inventory you might want the value to be `true` so that when grouping by product you get the most recent date for each product. In another example, you might want the value to be `false` if you are calculating account balances because you don't want the most recent date of an account type to influence the balance of a account holder's balance. The default is `true`.
* `window_groupings` (Optional) This is an array of fully qualified field references, which tells Zenlytic which groups to consider specially when finding the start or end of the period
  * Example: If you have MRR, like our example here, you will want to use `account_id` as the window grouping because if you have `account_id` X who's most recently recorded day is 2023-01-02 and `account_id` Y who's most recently recorded day is 2023-01-04, you want to use the `mrr_value` from 2023-01-02 for `account_id` X and 2023-01-04 for `account_id` Y. Window groupings allow you to specify the `account_id` as a window grouping to achieve that end.

__Example 1 (MRR):__
```
- name: account_id
  field_type: dimension
  type: string
  sql: ${TABLE}.id

- name: record
  field_type: dimension_group
  type: time
  sql: ${TABLE}.record_at
  timeframes: [raw, date, week, month, year]

- name: mrr
  field_type: measure
  type: sum
  sql: ${TABLE}.mrr_value
  non_additive_dimension:
    name: record_raw      # This is referencing the raw timestamp of the above dimension group
    window_choice: max
    window_groupings: [account_id]
```

__Example 2 (Inventory):__
```
- name: snapshot
  field_type: dimension_group
  type: time
  sql: ${TABLE}.snapshot_at
  timeframes: [raw, date, week, month, year]

- name: beginning_of_period_inventory_levels
  field_type: measure
  type: sum
  sql: ${TABLE}.inventory_value
  non_additive_dimension:
    name: snapshot_date      # This is referencing the timestamp truncated to the date of the above dimension group
    window_choice: min
    window_aware_of_query_dimensions: true     # The default is true 
```

`extra`: The extra property is like dbt `meta` property, and you can put whatever additional properties you want in here. For example, under this property you could add a property like this `maintainer: "jane doe"`

## Examples


The first measure takes the average of price for every order lines row. The second measure, sums up the price value, but it performs the sum uniquely based on each unique order_id instead of every row in the table, which ensures there is no double counting.
```
version: 1
type: view
name: order_lines

sql_table_name: prod.order_lines
default_date: order
row_label: Order Line

fields:
- name: order_line_id
  field_type: dimension
  type: string
  sql: ${TABLE}.order_line_id
  primary_key: yes
  hidden: yes

- name: order_id
  field_type: dimension
  type: string
  sql: ${TABLE}.order_id
  hidden: yes

- name: price
  field_type: dimension
  type: number
  sql: ${TABLE}.item_price
  label: "Item price"
  description: "The price we currently have on the item in Shopify"

- name: avg_price
  field_type: measure
  type: average
  # This references the "price" dimension above to calculate the average
  sql: ${price} 

- name: total_price_order_level
  field_type: measure
  type: sum_distinct
  sql_distinct_key: ${order_id}
  sql: ${price} 

- name: number_of_orders
  field_type: measure
  type: count_distinct
  sql: ${order_id}

- name: cumulative_orders
  field_type: measure
  type: cumulative
  measure: number_of_orders
  description: "The unique cumulative number of orders"
  value_format_name: decimal_0

```
