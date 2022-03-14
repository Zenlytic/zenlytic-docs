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

`description`: "description string"
`primary_key`: no
`hidden`: no
`sql`: "SQL expression to generate the field value ;;"
`value_format_name`: format_name
`drill_fields`: [field_or_set, field_or_set]
`tags`: ["string1", "string2"]
`required_access_grants`: [access_grant_name, access_grant_name]
`timeframes`: [timeframe, timeframe]
`convert_tz`: no
`datatype`: timestamp
`intervals`: [interval, interval]
`sql_start`: "SQL expression for start time of duration ;;"
`sql_end`: "SQL expression for end time of duration ;;"
`sql_distinct_key`: "SQL expression to define repeated entities ;;"
`filters`:
      - field: dimension_name
        value: "looker filter expression"

`extra`: The extra property is like dbt `meta` property, and you can put whatever additional properties you want in here. For example, under this property you could add a property like this `maintainer: "jane doe"`

`tiers`: [N, N]
