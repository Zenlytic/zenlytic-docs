---
sidebar_position: 10
---

# Dimensions

Dimensions are references to a column in the database or combinations of those references to columns. They let you define columns along with labels and descriptions so business users can make sense of the data. You can also use dimensions as building blocks for measures, so if something changes in your database table, you only have to update it in one spot.

---

### Properties

`name`: (Required) The name of the dimension. If you reference this dimension elsewhere in your data model you will use this value. Like all names, it follows [Zenlytic naming conventions](1_data_modeling.md#naming-conventions)

`field_type`: (Required) The field type of the field. For dimensions this is always `dimension`.

`type`: The type of the field. For dimensions this is one of `string`, `yesno`, `tier` or `number`. The default is `string`.

`label`: The label of the dimension is what shows up to the end users of your data model. If not specified it defaults to the name of the dimension.

`description`: The description of the dimension. This is shown in the UI and can help end users understand what the field represents. When this is set and the `zoe_description` property is not set, this will be shown to Zoë. Use this to provide context to Zoë on how to use the field correctly.

`zoe_description`: The description of the dimension as shown to Zoë. If not set, Zoë uses `description` instead. If set, this replaces `description` for Zoë only. End users will still see `description` in the UI. Use this to provide context to Zoë on how to use the field correctly.

`group_label`: The label of the view the field is put into in the left hand sidebar menu. If not specified it defaults to the name of the view the field is present in.

`primary_key`: A yes (or true) indicates that this field is the primary key of the table. The default is (or course) "no".

`hidden`: A yes (or true) indicates that this field should be hidden in the user interface. If a field is hidden it can still be referenced in the data model, despite not appearing to end users as a selectable field. The default is "no" which shows the field in the UI.

`sql`: (Required) This is the SQL expression that generates the field value. It can be as simple as `${TABLE}.my_field_name` which just references a column in the database table, or something more advanced that references previously defined fields, like `case when ${channel} ilike '%owned' then 'Yes' else 'No' end`.

`value_format_name`: This is the format to use when displaying the field. Check out [field formatting](95_formatting.md) to see available options. The default is `decimal_1`, which formats `12543.5524` to `12,543.6`.

`tags`: This is a list of strings that tag a field with special meaning. For instance, the `customer` tag indicates that this field is the unique identifier for a customer and Zenlytic will use that to know throughout your queries what you mean when you say "Customer".

`drill_fields`: This is a list of field names (dimensions or measures) to include in the drill query for the name of the tag (see below).

`searchable`: A yes (or true) means that you want Zenlytic to index the categories of this dimension for use in natural language search. For example, if you indexed the column `state` you'd be able to search for states just by typing "New York" without having to mention the state field.

`synonyms`: This is a list of strings phrases or words that you want to act as synonyms for natural language search. For example, if your measure is named `total_revenue` you might have synonyms of `['total sales', 'income']`. This works like a keyword search under the hood, to make fields with synonyms related to the question asked show up in context for Zoë.

`required_access_grants`: This is a list of [access grant](8_access_grants.md) names that are required to access this field. The grant names are always an `OR` condition. For example, if you listed `human_resources` and `executive` under this parameter, users who qualified for `human_resources`, `executive` or both would be able to access this field. Note, if the user has access to the field but does NOT have access to the view the field is defined in, the user will not be able to see the field.

`filters`: This is a list of [field filters](94_field_filter.md), which have two properties, `field` and `value`. For example, the below field filter equates to the SQL where clause `where channel != 'Paid'`.
```
- field: channel
  value: "-Paid"
```

`tiers`: For dimensions of type `tier`, specify the breakpoints for the various tiers. For example you might have a dimension `age` which you want to break into tiers, using `[0, 20, 30, 40, 50]` would partition the `age` dimension into groups depending in which range the age fell into between the buckets `[0,20)`, `[20,30)`, `[30,40)`, `[40,50)`, `50+`.

`link`: You can specify a link on a dimension with the option to impute the value of the cell clicked on in the link as a follow up question in Zenlytic. For example, with the link `https://myshopify.com/myfakestore/orders/{{value}}` on the order_id dimension, when a user asks a follow up question by clicking on the order id, they'll have an option to drill into the above link where the order id they clicked on replaces `{{value}}` in the url (i.e. `https://myshopify.com/myfakestore/orders/112335499`).

`extra`: The extra property is like dbt `meta` property, and you can put whatever additional properties you want in here. For example, under this property you could add a property like this `maintainer: "jane doe"`


### Examples


This example shows several fields, the first of which is the table's primary key, the second of which is the order id with a special tag to denote to Zenlytic that it is an "order", and the third of which is a numeric column, with a label and description.

The dimension `order_id` is tagged as an 'order' which means it will show up in the Zenlytic UI with an option to "Drill into orders."  If that option is selected, zenlytic will create a query filtered for the group selected and add that column, `order_id` and all fields (if any) defined in the `drill_fields` property. Since `order_id` also has the `link` specified, you will also see a follow up question to go to the link with the order id imputed in the link.

This is a view on top of the `order_lines` table which defines the `total_revenue` metric, and a drill defined on the `order_id`. This will result in a "Drill into orders" option in the Zenlytic UI. The link on the order will result in an option to "Go to external link" in the Zenlytic UI.
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
  type: number
  sql: ${TABLE}.order_id
  hidden: yes
  tags: ['orders']
  drill_fields: [marketing_channel, total_revenue]
  link: https://myshopify.com/myfakestore/orders/{{value}}

- name: price
  field_type: dimension
  type: number
  sql: ${TABLE}.item_price
  label: "Item price"
  description: "The price we currently have on the item in Shopify"

- name: marketing_channel
  field_type: dimension
  type: string
  sql: ${TABLE}.marketing_channel

- name: total_revenue
  field_type: measure
  type: sum
  sql: ${TABLE}.revenue

```
