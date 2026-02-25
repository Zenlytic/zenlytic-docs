# Model

Models are references to a database connection. They serve as the data model's reference to the warehouses itself. That connection to the database is referenced by the model's `connection` property, which references the `name` property of the credentials specified in the Zenlytic interface.

Models, like all files in Zenlytic, are YAML text files.

## Properties

Models only have a few core properties:

`type`: (Required) The type of the file. For these model files is should always be `model`.

`name`: (Required) The name of the model. If you reference this model elsewhere this is the name you will use. Like all names, it follows [Zenlytic naming conventions](data_modeling.md#naming-conventions)

`label`: The label of the model is what shows up to the end users of your data model. If not specified it defaults to the name of the model.

`connection`: (Required) This is the name of the database connection that is being referenced in Zenlytic. You will specify this name when you enter the database credentials in Zenlytic, and it follows [Zenlytic's conventions for names](data_modeling.md#naming-conventions)

`fiscal_month_offset`: This controls the offset applied by Zenlytic to calculate "Fiscal" time frames. For example, if you set it to `1` then the `fiscal_quarter` will be set to start in `February` instead of `January`, which is the default. This takes any positive or negative integer. Default is `0`.

`week_start_day`: This controls which day of the week Zenlytic assumes your definition of "Week" starts on. The default value is `monday` (which is standard across ISO dates).

`timezone`: This controls which timezone Zenlytic uses when querying dates and times from your database. Zenlytic will automatically change the timezone from the database timezone to the timezone you set here. The default is to make no change to the timezone found in the database.

`default_convert_tz`: This field sets the default value for `convert_tz` in each [dimension group](dimension_group.md) in this model. This defaults to `true` so if you set a timezone, it will be applied, unless you either set this value to `false` or set `convert_tz: false` on the field itself.

`access_grants`: This field is a list of [access grants](access_grants.md). You can use access grants to control what data users of Zenlytic are allowed to see and access.

`mappings`: Mappings equate fields that mean the same thing but are in different, un-joinable tables. For example, you might have a `channel` field on the orders table and a `marketing_channel` field on the `marketing_spend` table, and they represent the same thing and have the same values. You can set up a mapping that connects those two fields in Zenlytic and leaves only one option for the end users to select. Zenlytic will dynamically figure out which field it should use or if it needs to use both. Find out more about mappings [in the join docs](join.md#merged-results--mappings) or in the example below.

`relationships`: Relationships define joins that can happen between any two tables throughout views that are accessible in the model. These are always visible to the agent and help it make better decisions about complex joints.

## Examples

### Basic Example

Here is an example of a model that also sets a timezone for all queries to the database.

```yaml
version: 1
type: model
name: my_model
connection: my_connection
timezone: America/New_York
```

### Relationships

The relationships property defines join paths between views. Zoë uses these relationships (alongside identifiers and topics, for backwards compatibility) to understand how tables connect and to generate correct SQL joins.

Relationships are the preferred location for structured join definitions. For joins that are not obvious from matching column names, define them here so Zoë has explicit join context.

#### Relationship Properties

Each entry in the relationships list supports the following properties:

| Property     | Type   | Required | Description                                                                                                              |
| ------------ | ------ | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| from\_table  | string | Yes      | The name of the source view.                                                                                             |
| join\_table  | string | Yes      | The name of the view to join to.                                                                                         |
| join\_type   | string | No       | The type of SQL join. Options: left\_outer, inner, full\_outer. Default: left\_outer                                     |
| relationship | string | No       | The cardinality of the join. Options: many\_to\_one, one\_to\_many, one\_to\_one, many\_to\_many. Default: many\_to\_one |
| sql\_on      | string | Yes      | The join condition using ${view\_name.field\_name} syntax. Supports multiple conditions with AND.                        |

#### Relationship Example

This example defines basic relationships without complex concepts.

```yaml
version: 1
type: model
name: my_model
connection: my_connection


relationships:
  - from_table: orders
    join_table: customers
    join_type: left_outer
    relationship: many_to_one
    sql_on: ${orders.customer_id} = ${customers.customer_id}


  - from_table: order_lines
    join_table: orders
    join_type: left_outer
    relationship: many_to_one
    sql_on: ${order_lines.order_id} = ${orders.order_id}


  - from_table: order_lines
    join_table: products
    join_type: left_outer
    relationship: many_to_one
    sql_on: ${order_lines.product_id} = ${products.product_id}

```

#### Multi-Column Joins

For joins that require matching on more than one column, use AND in the sql\_on condition:

```yaml
relationships:
  - from_table: inventory
    join_table: warehouse_costs
    join_type: left_outer
    relationship: many_to_one
    sql_on: ${inventory.warehouse_id} = ${warehouse_costs.warehouse_id}
            AND ${inventory.product_id} = ${warehouse_costs.product_id}
```

#### When to Use Relationships

* Non-obvious joins where column names don't match across views, or where the join requires multiple columns or type casting.
* Joins you want Zoë to know about so she can generate correct SQL when users ask questions spanning multiple tables.
* You do not need to add relationships for obvious joins where column names match naturally between views (e.g., both views have a customer\_id column with matching identifiers). Over-documenting obvious concepts can decrease Zoë's performance.

#### Relationship Types

| Type           | Description                                                                                                          |
| -------------- | -------------------------------------------------------------------------------------------------------------------- |
| many\_to\_one  | Multiple records in from\_table map to one record in join\_table. The most common type (e.g., order lines → orders). |
| one\_to\_many  | One record in from\_table maps to multiple records in join\_table.                                                   |
| one\_to\_one   | Each record in from\_table maps to exactly one record in join\_table.                                                |
| many\_to\_many | Multiple records on both sides. Use with caution — can cause fan-out if not handled carefully in queries.            |

#### Join Types

| Type        | Description                                                                                                                |
| ----------- | -------------------------------------------------------------------------------------------------------------------------- |
| left\_outer | Include all records from from\_table, with matched records from join\_table. Unmatched rows in join\_table appear as NULL. |
| inner       | Only include records that match in both tables.                                                                            |
| full\_outer | Include all records from both tables, with NULLs where there is no match.                                                  |

### Access Grants

This is an example of an access grant defined in a model. In this case, this access grant could be reused in a view or in fields to limit viewing to only users who have the their `department` user attribute equal to "Marketing". This model also sets the `week_start_day` property which tells which day to start weeks on (the default is monday).

The mapping example here maps the `marketing_spend.marketing_channel` to the `orders.channel` field so Zenlytic (and Zoë) know they are the same concept.

{% code overflow="wrap" %}
```yaml
version: 1
type: model
name: demo
week_start_day: sunday

# This defines the access grant
access_grants:
  - name: restrict_dept
    user_attribute: department
    allowed_values: ["Marketing"]

mappings:
  channel: 
    fields: [marketing_spend.marketing_channel, orders.channel]
    group_label: "Acquisition" # This controls the header under which the mapped field shows up in the UI
    description: "The channel the customer came to our site from"
```
{% endcode %}
