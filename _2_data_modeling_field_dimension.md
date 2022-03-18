---
sidebar_position: 1
---

# Dimensions

Dimensions are references to a column in the database, or combinations of those references to columns. They let you define columns along with labels and descriptions so business users can make sense of the data. You can also use dimensions as building blocks for measures, so if something changes in your database table, you only have to update it in one spot.

---

### Properties

`name`: (Required) The name of the dimension. If you reference this dimension elsewhere in your data model you will use this value. Like all names, it follows [Zenlytic naming conventions](../_2_data_modeling.md#naming-conventions)

`field_type`: (Required) The field type of the field. For dimensions this is always `dimension`.

`type`: The type of the field. For dimensions this is one of `string`, `yesno`, `tier` or `number`. The default is `string`.

`label`: The label of the dimension is what shows up to the end users of your data model. If not specified it defaults to the name of the dimension.

`description`: The description of the dimension. This can help business users understand what the field represents.

`primary_key`: A yes (or true) indicates that this field is the primary key of the table. The default is (or course) "no".

`hidden`: A yes (or true) indicates that this field should be hidden in the user interface. If a field is hidden it can still be referenced in the data model, despite not appearing to end users as a selectable field. The default is "no" which shows the field in the UI.

`sql`: (Required) This is the SQL expression that generates the field value. It can be as simple as `${TABLE}.my_field_name` which just references a column in the database table, or something more advanced that references previously defined fields, like `case when ${channel} ilike '%owned' then 'Yes' else 'No' end`.

`value_format_name`: This is the format to use when displaying the field. Check out [field formatting](../_2_data_modeling_field_formatting.md) to see available options. The default is `decimal_1`, which formats `12543.5524` to `12,543.6`.

`tags`: This is a list of strings that tag a field with special meaning. For instance, the `customer` tag indicates that this field is the unique identifier for a customer and Zenlytic will use that to know throughout your queries what you mean when you say "Customer".

`searchable`: A yes (or true) means that you want Zenlytic to index the categories of this dimension for use in natural language search. For example, if you indexed the column `state` you'd be able to search for states just by typing "New York" without having to mention the state field.

`synonyms`: This is a list of strings phrases or words that you want to act as synonyms for natural language search. For example, if your measure is named `total_revenue` you might have synonyms of `['total sales', 'income']`.

`required_access_grants`: This is a list of [access grant](../_2_data_modeling_access_grants.md) names that are required to access this field. The grant names are always an `OR` condition. For example, if you listed `human_resources` and `executive` under this parameter, users who qualified for `human_resources`, `executive` or both would be able to access this field. Note, if the user has access to the field but does NOT have access to the view the field is defined in, the user will not be able to see the field.

`filters`: This is a list of [field filters](../_2_data_modeling_field_filter), which have two properties, `field` and `value`. For example, the below field filter equates to the SQL where clause `where channel != 'Paid'`.
```
- field: channel
  value: "-Paid"
```

`tiers`: For dimensions of type `tier`, specify the breakpoints for the various tiers. For example you might have a dimension `age` which you want to break into tiers, using `[0, 20, 30, 40, 50]` would partition the `age` dimension into groups depending in which range the age fell into between the buckets `[0,20)`, `[20,30)`, `[30,40)`, `[40,50)`, `50+`.

`extra`: The extra property is like dbt `meta` property, and you can put whatever additional properties you want in here. For example, under this property you could add a property like this `maintainer: "jane doe"`
