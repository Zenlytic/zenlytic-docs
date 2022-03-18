---
sidebar_position: 1
---

# Dimension Groups

Dimension Groups are a special type of dimension used for timeframes (referencing the same date column but having slices for it daily, weekly, monthly, etc), and for intervals (referencing the difference between two date columns and slicing it days between, weeks between, months between, etc).

---

### Properties

`name`: (Required) The name of the dimension group. If you reference this dimension group in the `default_date` property you will use this name. If you reference this dimension group elsewhere, in sets, other dimensions, etc you will use syntax as follows: `name_timeframe`. Like all names, it follows [Zenlytic naming conventions](../_2_data_modeling.md#naming-conventions)

`field_type`: (Required) The field type of the field. For dimension groups this is always `dimension_group`.

`type`: (Required) The type of the field. For dimension groups this is one of `time` or `duration`.

`label`: The label of the dimension group is what shows up to the end users of your data model. If not specified it defaults to the name of the dimension group.

`description`: The description of the dimension group. This can help business users understand what the field represents.

`hidden`: A yes (or true) indicates that this field should be hidden in the user interface. If a field is hidden it can still be referenced in the data model, despite not appearing to end users as a selectable field. The default is "no" which shows the field in the UI.

`sql`: (Required, only for `type` = time) This is the SQL expression that generates the field value. It can be as simple as `${TABLE}.my_field_name` which just references a column in the database table, or something more advanced that references previously defined fields, like `case when ${channel} ilike '%owned' then 'Yes' else 'No' end`.

`required_access_grants`: This is a list of [access grant](../_2_data_modeling_access_grants.md) names that are required to access this field. The grant names are always an `OR` condition. For example, if you listed `human_resources` and `executive` under this parameter, users who qualified for `human_resources`, `executive` or both would be able to access this field. Note, if the user has access to the field but does NOT have access to the view the field is defined in, the user will not be able to see the field.

`timeframes`: (Required, only for `type` = time) This property is only for dimension groups of type `time`. It's a list of values which you want to make available to the end user. The options are [listed below](_2_data_modeling_field_dimension_group.md#timeframes).

`intervals`: (Required, only for `type` = duration) This property is only for dimension groups of type `duration`. It's a list of values which you want to make available to the end user. The options are [listed below](_2_data_modeling_field_dimension_group.md#intervals).

`convert_tz`: A yes (or true) indicates that you want the timezone to be converted, a no (or false) indicates you do not want to convert the timezone from the native timezone to the timezone you specified in your model.

`datatype`: This indicates the database type of the date column referenced by the dimension group. The options are `timestamp`, `datetime` and `date`. The default is `timestamp`.

`sql_start`: (Required, only for `type` = duration) This is the SQL expression that generates the field value for the start of the duration.

`sql_end`: (Required, only for `type` = duration) This is the SQL expression that generates the field value for the end of the duration.

`extra`: The extra property is like dbt `meta` property, and you can put whatever additional properties you want in here. For example, under this property you could add a property like this `maintainer: "jane doe"`
