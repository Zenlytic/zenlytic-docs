---
sidebar_position: 1
---

# Measures (or metrics)

Measures (or metrics) are aggregations performed inside of a SQL `group by` statement. A simple one is `sum(sales)`, which you could specify in your data model with `type: sum` and `sql: ${TABLE}.sales`. They can get extremely complex, and are basically as flexible as your data warehouse's SQL syntax.

---

### Properties

`name`: (Required) The name of the measure (or metric). If you reference this measure (or metric) elsewhere in your data model you will use this value. Like all names, it follows [Zenlytic naming conventions](1_data_modeling.md#naming-conventions)

`field_type`: (Required) The field type of the field. For measures (or metrics) this is always `measure`.

`type`: (Required) The type of the field. For measures this is one of `sum`, `average`, `count`, `count_distinct`, `sum_distinct`, `average_distinct` or `number`. Note, both `sum_distinct` and `average_distinct` require you to pass a value to the `sql_distinct_key` property.

`label`: The label of the measure (or metric) is what shows up to the end users of your data model. If not specified it defaults to the name of the measure (or metric).

`description`: The description of the measure (or metric). This can help business users understand what the field represents.

`hidden`: A yes (or true) indicates that this field should be hidden in the user interface. If a field is hidden it can still be referenced in the data model, despite not appearing to end users as a selectable field. The default is "no" which shows the field in the UI.

`sql`: (Required) This is the SQL expression that generates the field value. It can be as simple as `${TABLE}.my_field_name` which just references a column in the database table, or something more advanced that references previously defined fields, like `case when ${channel} ilike '%owned' then 1 else 0 end`. Note, for the `count` type you can leave this property blank and it will default to counting the primary key of the view it's defined in.

`value_format_name`: This is the format to use when displaying the field. Check out [field formatting](95_formatting.md) to see available options. The default is `decimal_1`, which formats `12543.5524` to `12,543.6`.

`tags`: This is a list of strings that tag a field with special meaning. For instance, the `customer` tag indicates that this field is the unique identifier for a customer and Zenlytic will use that to know throughout your queries what you mean when you say "Customer".

`synonyms`: This is a list of strings phrases or words that you want to act as synonyms for natural language search. For example, if your measure is named `total_revenue` you might have synonyms of `['total sales', 'income']`.

`required_access_grants`: This is a list of [access grant](8_access_grants.md) names that are required to access this field. The grant names are always an `OR` condition. For example, if you listed `human_resources` and `executive` under this parameter, users who qualified for `human_resources`, `executive` or both would be able to access this field. Note, if the user has access to the field but does NOT have access to the view the field is defined in, the user will not be able to see the field.

`sql_distinct_key`: This tells Zenlytic that the measure you are calculating here is duplicated, and what field or expression it is unique on. For example, if you have a sales amount that is tied to an order but present in a order lines table, you could set this value to `order_id` and the type to `sum_distinct` to correctly sum up the sales amount without double counting. See [symmetric aggregates](96_symmetric_aggregates.md) for more information.

`filters`: This is a list of [field filters](94_field_filter.md), which have two properties, `field` and `value`. For example, the below field filter equates to the SQL where clause `where channel != 'Paid'`. Note, you *cannot* apply filters to measures of type `number`. You must apply your filters to the input measures, to achieve that result.
```
- field: channel
  value: "-Paid"
```

`extra`: The extra property is like dbt `meta` property, and you can put whatever additional properties you want in here. For example, under this property you could add a property like this `maintainer: "jane doe"`

