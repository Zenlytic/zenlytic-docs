# Views

Views reference exactly one table in the database. In Zenlytic, they are organized into [topics](topic.md) for usage that define how they join together.

Views, like all files in Zenlytic, are YAML text files.

## Properties

`type`: (Required) The type of the file. For these view files is should always be `view`.

`name`: (Required) The name of the view. If you reference this view elsewhere this is the name you will use. Like all names, it follows [Zenlytic naming conventions](data_modeling.md#naming-conventions)

`model_name`: (Required) The name of the [model](model.md) (e.g. database connection) the view references.

`label`: The label of the view is what shows up to the end users of your data model. If not specified it defaults to the name of the view.

`description`: The description of the view. This can help business users understand what the view represents and how it is created. This is also sent to Zoë (Zenlytic's AI Analyst) to give her context on how to use different views in your data model. Use this to provide Zoë view or table-level context.

`sql_table_name`: This is the table name in the database that the view references. For example, `prod.customers` would be a valid `sql_table_name`.

`derived_table`: This is a property that you can use to define transformed tables using a SQL statement. This SQL statement is run and is considered to be the "base" of the view. Note, we generally prefer using [dbt](https://getdbt.com) over derived tables for better testing and maintainability. This property has a nested property `sql` inside of the `derived_table` property that you use to define the SQL statement.

{% code overflow="wrap" %}
```yaml
...
name: my_view
derived_table: 
  sql: "select *, row_number() over (partition by customer_id order by order_date) as order_number from myschema.mytable"
...
```
{% endcode %}

Note: The filters in `always_filter` _will not_ be applied if you are using this property to define the data for the view to sit on top of.

You can also reference any [referenceable attributes](referenceable_attributes.md) and drop them into the derived SQL statement. For example, in this case we are dynamically applying a filter to the SQL query based on the user's user attribute for 'owned\_region'

```yaml
...
name: my_view
derived_table: 
  sql: >
    select 
      * 
    from myschema.mytable
    where '{{ user_attributes['owned_region'] }}' = mytable.region
...
```

`default_date`: This is the default date [dimension group](dimension_group.md) without a time frame chosen for it. For example, if your dimension group is named `order` you would use the value `order` here, not `order_month` or `order_week` like you would reference elsewhere.

`sets`: This is a list of [sets](set.md) that are defined in this view. Example syntax of the definition is below.

```yaml
  - name: set_name
    fields: [field_or_set, field_or_set]
```

`always_filter`: This is an optional list of filters which use the usual [field filter selection syntax](field_filter.md) and will _always_ be applied to the query. These filters are applied to the entire query, not just a metric or dimension, and if it is not possible to reference or join in the field needed for the filter it will result in an error.

Note: This set of filters _will not_ be applied if you are using a derived table mentioned above instead of `sql_table_name`.

### Example below:

Here are two filters that will be applied to _all_ queries that reference this view. One field `context_os` is present in the view, and does not need to specify its view name. The other field `is_churned` is _not_ present in this view and must specify its view name. It will be joined in dynamically whenever this view is referenced to apply the filter.

```yaml
always_filter:
- field: customers.is_churned
  value: FALSE
- field: context_os
  value: -NULL
```

`access_filters`: This is an optional list of [access filters](access_grants.md#access-filters) to apply to the view when it is queried.

Access filters can be used to apply row-level security against views. The following example shows how to make a specified column only visible to workspace members with a user attribute value:

```yaml
access_filters:
  - field: orders.product
    user_attribute: 'products'
```

`required_access_grants`: This is a list of [access grant](access_grants.md#access-grants) names that are required to access this view. The grant names are always an `OR` condition. For example, if you listed `human_resources` and `executive` under this parameter, users who qualified for `human_resources`, `executive` or both would all be able to access data in this view. Note, these access grants will _always_ be applied for this view in any join sequence.


`identifiers`: This is a list of [fields](field.md) with additional information defining what kind of key (primary, foreign) they are to the table the view references. 

Identifiers can be used to create a join_as view, which will allow a table to join into a topic more than once on different keys. More information is in the [joins](./join.md) section.

`fields`: This is a list of [fields](../5_data_modeling/9_field.md). Each field must have all required parameters included.

## Joins 

Joins are defined in [topics](./topic.md). 