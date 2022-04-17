---
sidebar_position: 5
---

# Joins

Joins are specified in explores, and they serve to define the mechanics of the join between the base view in the explore and the new view that is joined in as defined.

Joins are quite flexible. They can handle complex join conditions using the `sql_on` parameter. They can also handle more difficult join relationships like "one to many", while still calculating your metrics correctly using [symmetric aggregates](96_symmetric_aggregates.md).

---

### Properties

`name`: (Required) The name of the join. This can be the name of the [view](6_view.md) you want to join into the explore, or any name you choose. Note, if this name does not reference a view, you must specify the `from` parameter. If you reference this join elsewhere this is the name you will use. Like all names, it follows [Zenlytic naming conventions](1_data_modeling.md#naming-conventions).

`from`: This is the [view](6_view.md) name to reference for joining into the explore. This parameter is optional, but it must be specified if the name of the join does not reference a view.

`type`: This is the type of the join. The options are `left_outer`, `inner`, or `full_outer`. You should determine the type of join by how you would join this view into the base view of the explore. The default is `left_outer`.

`relationship`: This is the relationship of the join. The options are `many_to_one`, `one_to_one`, `one_to_many`, or `many_to_many`. You should determine the relationship of the join based on the logical result of the join between this view and the base view of the explore. The default is `many_to_one`.


`sql_on`: This is the SQL clause to join this view into the explore. You do not have to reference a field in the base explore here. You can reference another field that is joined into the explore to make the join. The metrics layer will automatically figure out which joins it needs to make to make the query possible.

For example, if `order_lines` is the base view and you want to join `orders` into it, you could write a `sql_on` like this `${order_lines.order_id}=${orders.id}`. Say you then wanted to join a `customers` view into this explore, but you have no `customer_id` field in the `order_lines` view, that's in the `orders` view. You could write a `sql_on` like this `${orders.customer_id}=${customers.id}`.


`foreign_key`: This is a single dimension name that is the same in both this view and the base view of the explore. For example, if the base view had a field `customer_id` and this table has a primary key `customer_id` you could use `customer_id` as the value for this property. Note that if both this property and `sql_on` are present your data model will throw an error.

`required_access_grants`: This is a list of [access grant](8_access_grants.md) names that are required to access the fields joined into this explore from this join. The grant names are always an `OR` condition. For example, if you listed `human_resources` and `executive` under this parameter, users who qualified for `human_resources`, `executive` or both would all be able to access data from this join.

### Examples 

Joins are specified like this in explores 

```
version: 1
type: model
name: my_model
connection: my_connection
explores:
- name: order_lines

  joins:
    - name: customers
      relationship: many_to_one
      type: left_outer
      sql_on: ${order_lines.customer_id}=${customers.customer_id}
```

You can have multiple joins in any explore, and the joins do not have to reference the original table at the base of the explore.

```
version: 1
type: model
name: my_model
connection: my_connection
explores:
- name: order_lines

  joins:
    - name: customers
      relationship: many_to_one
      type: left_outer
      sql_on: ${order_lines.customer_id}=${customers.customer_id}

    - name: customer_acquisition
      relationship: many_to_one
      type: left_outer
      sql_on: ${customers.first_channel_id}=${customer_acquisition.channel_id}

```