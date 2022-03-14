---
sidebar_position: 1
---

# Views

Views reference exactly one table in the database. They can be used in multiple [explores](../_2_data_modeling_explore.md), but always reference the same table in the database.

Views, like all files in Zenlytic, are yaml text files.

---

### Properties

`type`: (Required) The type of the file. For these view files is should always be `view`.

`name`: (Required) The name of the view. If you reference this view elsewhere this is the name you will use. Like all names, it follows [Zenlytic naming conventions](../_2_data_modeling.md#naming-conventions)

`label`: The label of the view is what shows up to the end users of your data model. If not specified it defaults to the name of the view.

`sql_table_name`: This is the table name in the database that the view references. For example, `prod.customers` would be a valid `sql_table_name`. You can also reference a dbt `ref` if you define your metrics layer in the same repo as your dbt. For example, `{{ ref('customers') }}`. Zenlytic will check for the validity of the `ref` when you run validation on your data model.

`derived_table`: This is a nested property that you can use to define transformed tables using a SQL statement. This SQL statement is run and is considered to be the "base" of the view. Note, we prefer using [dbt](https://getdbt.com) over derived tables for better testing and maintainability.
```
sql: "select *, row_number() over (partition by customer_id order by order_date) as order_number from myschema.mytable"

```

`default_date`: This is the default date [dimension group](../_2_data_modeling_field_dimension_group.md) without a time frame chosen for it. For example, if your dimension group is named `order` you would use the value `order` here, not `order_month` or `order_week` like you would reference elsewhere.

`row_label`: This is the text label of what a row in this table logically represents (e.g. a table of customers, would have a logical row label of "Customer").

`sets`: This is a list of [sets](../_2_data_modeling_set.md) that are defined in this view. Example syntax of the definition is below.
```
  - name: set_name
    fields: [field_or_set, field_or_set]
```

`required_access_grants`: This is a list of [access grant](../_2_data_modeling_access_grants.md) names that are required to access this view. The grant names are always an `OR` condition. For example, if you listed `human_resources` and `executive` under this parameter, users who qualified for `human_resources`, `executive` or both would all be able to access data in this view. Note, these access grants will *always* be applied for this view in every explore it is present in.

fields: This is a list of [fields](../_2_data_modeling_field.md). Each field must have all required parameters included.
