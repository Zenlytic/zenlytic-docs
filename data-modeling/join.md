# Joins

Joins are how views are connected to each other. The are defined by `identifiers` on the views. `identifiers` can be defined as primary keys, foreign keys, or explicit point to point joins.

Joins, are stored in View files in Zenlytic, which are YAML text files.

## Properties

These properties are the ones you can define for an `identifier` in a view.

`name`: (Required) The name of the identifier. This is the value used to match identifiers across views. Like all names, it follows [Zenlytic naming conventions](data_modeling.md#naming-conventions).

`type`: (Required) The type of the join. This can be one of `primary` (for a unique, primary key), `foreign` (for a foreign key), or `join` (a custom point-to-point join).

`sql`: The sql definition of the join. This is only used for `primary` and `foreign` join types, and is just a reference to the key (e.g. `${user_id}`).

`reference`: Only used for type `join`. This is the other view referenced in the join. For example, if you define the identifier in the `orders` view and you want to join in customer information in the `customers` view, you would specify `customers` as the `reference`.

`relationship`: Only used for type `join`. One of `one_to_one`, `many_to_one`, `one_to_many`, `many_to_many`. It specifies the join type from the view the join is defined in to the referenced view. The default is `many_to_one`.

`join_type`: Only used for type `join`. One of `left_outer`, `inner`, `full_outer`, `cross`. It specifies the SQL join type from the view the join is defined in to the referenced view. The default is `left_outer`.

`sql_on`: This is only for (type `join`) joins and can be any arbitrary SQL with references to either the view the join is defined in or to referenced view.

`allowed_fanouts`: This is used for `primary` and `foreign` join types, and it is a list of referenced views you would like to allow fanout joins for. By default, Zenlytic will not allow fanout joins, but you can explicitly allow them for certain views using this property. Zenlytic uses [symmetric aggregates](symmetric_aggregates.md) to calculate metrics correctly even in the event of a fanout join.

`identifiers`: This is only valid for a composite key (see [example below](join.md#composite-keys)). It contains a list of dictionaries with a `name` property that references identifiers defined above it. The composite key enables you to specify "bridge" tables to facilitate many-to-many relationships in your data model.

`join_as`: This is a name that identifies how you want to alias the view you are joining in as if it was another view. For example, if you have a tickets view with a requestor\_id and a assignee\_id and a cx\_users view, you could have two 'join\_as' statements from the cx\_users view to join in those users once as "Requestors" and another time as "Assignees." Note: this property must follow [Zenlytic naming conventions](data_modeling.md#naming-conventions), and it _must be unique in your project_, just like view names.

`join_as_label`: This is the label that will show up in the sidebar menu like a view label if you specify a `join_as` value. If you leave it blank, it will default to a prettified version of the `join_as` property.

`join_as_field_prefix`: This is a prefix that goes in front of all fields aliased under the `join_as` property. For example, if you have a cx\_users table with an email field, you might want the prefix "Requestor" before each field to make it clear which email field belongs to the requestor and which belongs to the assignee. If you leave it blank, it will default to the `join_as_label` value.

`include_metrics`: This boolean defines if the metrics from the `join_as` join should be included in the fields joined in and shown in the UI. If you leave it blank, it will default to `false` and no metrics from your join\_as statement will be shown.

## Identifier Join Example

This is a basic view with a few dimensions and measures, that explicitly references the `prod.order_lines` table. This view defines its primary key (`order_line_id`), a foreign key (named `customer_id` but that references the `customer_email` field), and a custom join to the `discounts` view based on a `sql_on` criteria. _Note: identifiers are connected to each other based on the `name` property only. The `sql` property is just used to reference the name of the appropriate field in the view. E.g. you might have a `customer_id` in one view as a foreign key and a `id` in another as a primary key. You could name the identifier `customer` on both views and in one reference `sql: ${customer_id}` and in the other reference `sql: ${id}` and Zenlytic would join them correctly since they have a matching `name` property._

Since `order_line_id` is defined as a primary key, this view will be available to join in any table that references `order_line_id` as a foreign key.

Since `customer_id` is defined as a foreign key, all views that define `customer_id` as a primary key will be available to join in to this view.

Since `discount_join` is defined as a custom join, exactly one (`many_to_one`) join relationship will exist between `order_lines` and `discounts` with this criteria.

```yaml
version: 1
type: view
name: order_lines
model_name: demo_model

sql_table_name: prod.order_lines
default_date: order

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
  relationship: many_to_one
  join_type: left_outer
  sql_on: ${discounts.order_id}=${order_lines.order_id} and ${discounts.product_id}=${order_lines.product_id}

fields:
.
.
. 

```

## Composite Keys

In many situations you will have many to many relationships in your data. For example, let's think about a SaaS application that has tables `users` and `workspaces`. A user can be a part of one or more workspaces, which means we'll need a "bridge" table called `user_workspaces` that shows which users have access to which workspaces. If we set up joins (identifiers) in the `user_workspaces` view as follows the join will happen as we expect.

{% hint style="info" %}
Composite keys vs. Custom joins

Composite keys just handle choosing the correct bridge table, they do not construct a join like `a.user_id=b.user_id and a.workspace_id=b.workspace_id`. For that behavior, use a custom join mentioned above.
{% endhint %}

```yaml
version: 1
type: view
name: user_workspaces
model_name: my_model
sql_table_name: PROD.USER_WORKSPACES

identifiers:
- name: user_id
  type: foreign
  sql: ${user_id}
- name: workspace_id
  type: foreign
  sql: ${workspace_id}

...
```

But, if we also have another table that lists both `user_id` and `workspace_id` as foreign keys, Zenlytic will have no way of knowing which table to use to join users and workspaces by default.

Composite keys give you the ability to specify the right bridge table to use in these type of situations. We'll specify a composite key below, which will tell Zenlytic to prioritize this join between users and workspaces if there aren't other tables involved which require a change to the join pattern.

```yaml
version: 1
type: view
name: user_workspaces
model_name: my_model
sql_table_name: PROD.USER_WORKSPACES

identifiers:
- name: user_id
  type: foreign
  sql: ${user_id}
- name: workspace_id
  type: foreign
  sql: ${workspace_id}
  # This one is the composite key. It references the existing foreign keys specified 
  # in the table, and tells Zenlytic that this table is unique on a key that 
  # would concatenate ${workspace_id} and ${user_id}
- name: user_workspace
  type: primary
  identifiers:
    - name: workspace_id
    - name: user_id
...
```

Now that we've defined the composite key, we can be sure Zenlytic will handle our many to many join between `users` and `workspaces` correctly.

## Join As

In many situations you will have a table like `tickets` that joins to another table `cx_users` on two keys, which have different meanings when joined on, like `requestor_id` and `assignee_id`.

`join_as` gives you the ability to join in your `cx_users` table twice to the `tickets` table, once as a Requestor and once as an Assignee.

In the tickets table, we will set up two identifiers. One for requestors and one for assignees.

```yaml
version: 1
type: view
name: tickets
model_name: my_model
sql_table_name: PROD.TICKETS

identifiers:
- name: requestor_user_id
  type: foreign
  sql: ${requestor_id}
- name: assignee_user_id
  type: foreign
  sql: ${assignee_id}

...
```

Now, in the `cx_users` table, we can specify the `join_as` statements, and the labels we want to show up in the UI.

```yaml
version: 1
type: view
name: cx_users
model_name: my_model
sql_table_name: PROD.CX_USERS

identifiers:
- name: requestor_user_id
  type: primary
  sql: ${user_id}
  join_as: requestor_users        # This value must be unique like view names
  join_as_label: Requestor        # This value is optional and will look like the view label

- name: assignee_user_id
  type: primary
  sql: ${user_id}
  join_as: assigned_users
  join_as_label: Assigned To      # This will be the label of the view when joined
  join_as_field_prefix: Assignee  # This will be the prefix for the fields when joined
...
```

Now that we've defined our `join_as` statement, Zenlytic will show options in the sidebar menu for both "Requestor" and "Assigned To" fields from the `cx_users` view.

## Merged Results & Mappings

Zenlytic also has the ability to merge results. Merging results is where a join happens _after_ the aggregation in the query.

Merged results are closely related to Zenlytic's concept of "mappings." Mappings equate fields that mean the same thing but are in different, un-joinable tables. For example, you might have a `channel` field on the orders table and a `marketing_channel` field on the `marketing_spend` table, and they represent the same thing and have the same values. You can set up a mapping that connects those two fields in Zenlytic and leaves only one option for the end users to select. Zenlytic will dynamically figure out which field it should use or if it needs to use both.

Additionally, Zenlytic automatically performs this mapping for time fields associated with metric. For example, in the subscription table you might have `number_of_subscriptions` trended over time by `created_at` and `number_of_cancellations` trended by `cancelled_at`. You can select the mapped date, `number_of_cancellations`, and `number_of_subscriptions`, and when running the query, Zenlytic will query `number_of_cancellations` by `cancelled_at` and `number_of_subscriptions` by `created_at` and then merge the results of those two queries together for the final result. This ensures your metrics are always calculated correctly over time.

You can also define metrics that use merged results. For example, to define `cost_per_acquisition` or CPA you'll need to divide `marketing_spend` by `number_of_new_customers`. Those metrics don't live in the same table, to calculate them you'll have to calculate `marketing_spend` in one table and `number_of_new_customers` in another, then merge the results. Let's look at a full example of that here:

This is the `demo_model` model. It contains a connection to the warehouse and a mapping between the `orders.channel` dimension and the `marketing_spend.marketing_channel` column.

Mappings are not meant to map separate fields to the one field in separate mapping arguments. For example, if you want to map field X and field Y to field Z, you must do so with a `fields` argument like `fields: [view_1.X, view_2.Y, view_3.Z]`, NOT in two separate mappings, one mapping X -> Z and the other mapping Y -> Z.

{% hint style="info" %}
Mappings with null values

Most databases have logic that results in `null=null` being `false` which, means if you map two columns, both with null values, the two nulls won't map to each other. You can solve this using your database's `ifnull` function to replace those `null` values with a string of your choosing.
{% endhint %}

```yaml
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

```yaml
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

With this setup, we could query `cost_per_acquisition` by `channel` by `week` and Zenlytic will calculate `total_marketing_spend` by `marketing_channel` and `spend_at_week` then merge that result with the result of `number_of_new_customers` by `channel` and `order_week` merging them together by `week` and `channel`.

This let's you define a few mappings and dramatically increase the transformations available to end users on a self-serve basis.
