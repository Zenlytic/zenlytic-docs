---
sidebar_position: 2
---

# Models

Models are collections of explores that contain exactly one connection to a database. That connection to the database is referenced by the model's `connection` property and it references the `name` property of the credentials specified in the Zenlytic interface.

Models, like all files in Zenlytic, are yaml text files.

---

### Properties

Models only have a few core properties:

`type`: (Required) The type of the file. For these model files is should always be `model`.

`name`: (Required) The name of the model. If you reference this model elsewhere this is the name you will use. Like all names, it follows [Zenlytic naming conventions](1_data_modeling.md#naming-conventions)


`label`: The label of the model is what shows up to the end users of your data model. If not specified it defaults to the name of the model.


`connection`: (Required) This is the name of the database connection that is being referenced in Zenlytic. You will specify this name when you enter the database credentials in Zenlytic, and it follows [Zenlytic's conventions for names](1_data_modeling.md#naming-conventions)

`week_start_day`: This controls which day of the week Zenlytic assumes your definition of "Week" starts on. The default value is `monday` (which is standard across ISO dates).

`access_grants`: This field is a list of [access grants](8_access_grants.md). You can use access grants to control what data users of Zenlytic are allowed to see and access.

explores: This is a list of [explores](4_explore.md). Each explore must have all required parameters included.

### Examples 

Here is an example of a model with a single explore and a single join in that explore, which also specifies the `fields_for_analysis` to limit the default search space for deeper questions.

```
version: 1
type: model
name: my_model
connection: my_connection
explores:
- name: order_lines

  fields_for_analysis: 
    - product_title
    - product_type
    - sku
    - new_vs_repeat
    - source
    - medium
    - acquisition_channel

  joins:
    - name: customers
      relationship: many_to_one
      type: left_outer
      sql_on: ${order_lines.customer_id}=${customers.customer_id}
```

This is an example of an access filter and an access grant applied to a model. In this case, the orders explore is limited to only be viewed by users who have the their `department` user attribute equal to "Marketing". Furthermore, because of the additional `access_filter` property, all queries run in this explore will have a dynamic SQL `where` clause added to them that sets the user_attribute `owned_product` equal to the field `product` in the view `orders`.  

```
version: 1
type: model
name: demo

# This defines the access grant
access_grants:
  - name: restrict_dept
    user_attribute: department
    allowed_values: ["Marketing"]

explores:
  - name: orders
    required_access_grants: [restrict_dept]

    access_filters:
      - field: orders.product
        user_attribute: 'owned_product'
```

