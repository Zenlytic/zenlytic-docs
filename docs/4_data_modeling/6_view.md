---
sidebar_position: 6
---

# Views

Views reference exactly one table in the database. They can be joined together using `identifiers`, but always reference the same table in the database.

Views, like all files in Zenlytic, are yaml text files.

---

### Properties

`type`: (Required) The type of the file. For these view files is should always be `view`.

`name`: (Required) The name of the view. If you reference this view elsewhere this is the name you will use. Like all names, it follows [Zenlytic naming conventions](1_data_modeling.md#naming-conventions)

`model_name`: (Required) The name of the [model](./2_model.md) (e.g. database connection) the view references.

`label`: The label of the view is what shows up to the end users of your data model. If not specified it defaults to the name of the view.

`sql_table_name`: This is the table name in the database that the view references. For example, `prod.customers` would be a valid `sql_table_name`. You can also reference a dbt `ref` if you define your metrics layer in the same repo as your dbt. For example, `{{ ref('customers') }}`. Zenlytic will check for the validity of the `ref` when you run validation on your data model.

`derived_table`: This is a nested property that you can use to define transformed tables using a SQL statement. This SQL statement is run and is considered to be the "base" of the view. Note, we prefer using [dbt](https://getdbt.com) over derived tables for better testing and maintainability.
```
sql: "select *, row_number() over (partition by customer_id order by order_date) as order_number from myschema.mytable"

```

`default_date`: This is the default date [dimension group](92_dimension_group.md) without a time frame chosen for it. For example, if your dimension group is named `order` you would use the value `order` here, not `order_month` or `order_week` like you would reference elsewhere.

`row_label`: This is the text label of what a row in this table logically represents (e.g. a table of customers, would have a logical row label of "Customer").

`sets`: This is a list of [sets](7_set.md) that are defined in this view. Example syntax of the definition is below.
```
  - name: set_name
    fields: [field_or_set, field_or_set]
```

`required_access_grants`: This is a list of [access grant](8_access_grants.md) names that are required to access this view. The grant names are always an `OR` condition. For example, if you listed `human_resources` and `executive` under this parameter, users who qualified for `human_resources`, `executive` or both would all be able to access data in this view. Note, these access grants will *always* be applied for this view in any join sequence.

identifiers: This is a list of [fields](9_field.md) with additional information defining what kind of key (primary, foreign) they are to the table the view references. An example 
```
- name: order_key
  type: primary
  sql: ${order_id}
```
Identifiers will be used to form the join graph for your database. By default, Zenlytic will not allow fan-out or chasm joins, but if you specify views in the `allow_fanouts` parameter those will be joined and calculated accurately using [symmetric aggregates](./96_symmetric_aggregates.md).

fields: This is a list of [fields](9_field.md). Each field must have all required parameters included.


### Examples

This is a basic view with just 2 dimensions and 1 measure, that explicitly references the `prod.order_lines` table. This view also defines it's primary key as an identifier and a foreign key as an identifier.

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

fields:
- name: order_line_id
  field_type: dimension
  type: string
  sql: ${TABLE}.order_line_id
  primary_key: yes
  hidden: yes

- name: customer_email
  field_type: dimension
  type: string
  sql: ${TABLE}.email

- name: price
  field_type: dimension
  type: number
  sql: ${TABLE}.item_price

- name: avg_price
  field_type: measure
  type: average
  # This references the "price" dimension above to calculate the average
  sql: ${price} 
```