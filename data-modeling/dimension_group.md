---
layout:
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# Dimension Groups

Dimension Groups are a particular type of dimension used for timeframes (referencing the same date column but having slices for it daily, weekly, monthly, etc), and for intervals (referencing the difference between two date columns and slicing it days between, weeks between, months between, etc).

## Properties

`name`: (Required) The name of the dimension group. If you reference this dimension group in the `default_date` property you will use this name. If you reference this dimension group elsewhere, in sets, other dimensions, etc you will use syntax as follows: `name_timeframe`. Like all names, it follows [Zenlytic naming conventions](data_modeling.md#naming-conventions)

`field_type`: (Required) The field type of the field. For dimension groups this is always `dimension_group`.

`type`: (Required) The type of the field. For dimension groups this is one of `time` or `duration`.

`label`: The label of the dimension group is what shows up to the end users of your data model. If not specified it defaults to the name of the dimension group.

`description`: The description of the dimension group. This is shown in the UI and can help end users understand what the field represents. When this is set and the `zoe_description` property is not set, this will be shown to Zoë. Use this to provide context to Zoë on how to use the field correctly.

`zoe_description`: The description of the dimension group shown to Zoë. If not set, Zoë uses `description` instead. If set, this replaces `description` for Zoë only. End users will still see `description` in the UI. Use this to provide context to Zoë on how to use the field correctly.

`group_label`: The label of the view the field is put into in the left hand sidebar menu. If not specified it defaults to the name of the view the field is present in.

`hidden`: A `true` indicates that this field should be hidden in the user interface. If a field is hidden it can still be referenced in the data model, despite not appearing to end users as a selectable field. The default is false which shows the field in the UI.

`sql`: (Required, only for `type` = time) This is the SQL expression that generates the field value. It can be as simple as `${TABLE}.my_field_name` which just references a column in the database table, or something more advanced that references previously defined fields, like `case when ${channel} ilike '%owned' then 'Yes' else 'No' end`.

You can also reference any [referenceable attributes](referenceable_attributes.md) and drop them into the `sql` statement here. For example, you can use the query attribute for which dimension group is selected to take advantage of specialized database extensions, like Timescale DB.

```yaml
- name: rainfall_at
  field_type: dimension_group
  type: time
  timeframes:
    - raw
    - date
    - week
    - month
  sql: >
    case 
      when '{{ query_attributes['dimension_group'] }}' = 'raw' then ${TABLE}.rain_date 
      when '{{ query_attributes['dimension_group'] }}' = 'date' then time_bucket('1 day', ${TABLE}.rain_date) 
      when '{{ query_attributes['dimension_group'] }}' = 'week' then time_bucket('1 week', ${TABLE}.rain_date) 
      when '{{ query_attributes['dimension_group'] }}' = 'month' then time_bucket('1 month', ${TABLE}.rain_date) 
      else null
    end
```

`required_access_grants`: This is a list of [access grant](access_grants.md) names that are required to access this field. The grant names are always an `OR` condition. For example, if you listed `human_resources` and `executive` under this parameter, users who qualified for `human_resources`, `executive` or both would be able to access this field. Note, if the user has access to the field but does NOT have access to the view the field is defined in, the user will not be able to see the field.

`synonyms`: This is a list of strings phrases or words that you want to act as synonyms for natural language search. For example, if your measure is named `total_revenue` you might have synonyms of `['total sales', 'income']`. This works like a keyword search under the hood, to make fields with synonyms related to the question asked show up in context for Zoë.

`timeframes`: (Required, only for `type` = time) This property is only for dimension groups of type `time`. It's a list of values which you want to make available to the end user. The options are [listed below](dimension_group.md#timeframes).

`intervals`: (Required, only for `type` = duration) This property is only for dimension groups of type `duration`. It's a list of values which you want to make available to the end user. The options are [listed below](dimension_group.md#intervals).

`convert_tz`: A yes (or true) indicates that you want the timezone to be converted, a no (or false) indicates you do not want to convert the timezone from the native timezone to the timezone you specified in your model.

`datatype`: This indicates the database type of the date column referenced by the dimension group. The options are `timestamp`, `datetime` and `date`. The default is `timestamp`.

`sql_start`: (Required, only for `type` = duration) This is the SQL expression that generates the field value for the start of the duration.

`sql_end`: (Required, only for `type` = duration) This is the SQL expression that generates the field value for the end of the duration.

`extra`: The extra property is like dbt `meta` property, and you can put whatever additional properties you want in here. For example, under this property you could add a property like this `maintainer: "jane doe"`

## Timeframes

{% hint style="info" %}
Fiscal date reporting

All `fiscal_` timeframes are based on the model's `fiscal_month_offset` property. This let's you set up your fiscal year/quarter/month reporting right in Zenlytic! Find out more information [here](model.md).
{% endhint %}

The available timeframe options are:

* `raw`: Shows the raw value and can be used in references, but is not used in the Zenlytic UI.
* `time`: Shows the raw timestamp.
* `second`: Shows the value truncated to the second.
* `minute`: Shows the value truncated to the minute.
* `hour`: Shows the value truncated to the hour.
* `date`: Shows the value truncated to the day.
* `week`: Shows the value truncated to the week.
* `month`: Shows the value truncated to the month.
* `quarter`: Shows the value truncated to the quarter.
* `year`: Shows the value truncated to the year.
* `fiscal_month`: Shows the value truncated to the fiscal month.
* `fiscal_quarter`: Shows the value truncated to the fiscal quarter.
* `fiscal_year`: Shows the value truncated to the fiscal year.
* `week_index`: Shows the week of the year as an integer (alias of `week_of_year` below).
* `week_of_year`: Shows the week of the year as an integer.
* `week_of_month`: Shows the week of the month as an integer.
* `month_of_year`: Shows the month of the year as a 3 character string ('Jan', 'Feb', 'Mar', etc).
* `month_of_year_full_name`: Shows the month of the year as a string ('January', 'February', 'March', etc).
* `month_of_year_index`: Shows the month of the year as an integer.
* `fiscal_month_index`: Shows the fiscal month of the year as an integer. The first fiscal month is the first month of the fiscal year.
* `fiscal_month_of_year_index`: Shows the fiscal month of the year as an integer (alias of the `fiscal_month_index`).
* `month_name`: Shows the month of the year as a 3 character string (alias of `month_of_year`).
* `month_index`: Shows the month of the year as an integer (alias of `month_of_year_index`).
* `quarter_of_year`: Shows the quarter of the year as an integer.
* `fiscal_quarter_of_year`: Shows the fiscal quarter of the year as an integer.
* `hour_of_day`: Shows the hour of the day as an integer.
* `day_of_week`: Shows the day of the week as a 3 character string ('Mon', 'Tue', 'Wed', etc).
* `day_of_month`: Shows the day of the month as an integer.
* `day_of_year`: Shows the day of the year as an integer.

## Intervals

The available interval options are:

* `second`: The number of seconds between the `sql_start` and the `sql_end`.
* `minute`: The number of minutes between the `sql_start` and the `sql_end`.
* `hour`: The number of hours between the `sql_start` and the `sql_end`.
* `day`: The number of days between the `sql_start` and the `sql_end`.
* `week`: The number of weeks between the `sql_start` and the `sql_end`.
* `month`: The number of months between the `sql_start` and the `sql_end`.
* `quarter`: The number of quarters between the `sql_start` and the `sql_end`.
* `year`: The number of years between the `sql_start` and the `sql_end`.

## Examples

This example shows several fields, the first of which is the table's primary key and the second of which is a dimension group for a date and the third of which is a duration dimension group. In the Zenlytic interface, you'll reference the dates defines in the second field like `order_date`, `order_month`, etc. You'll reference the third field like `days_between_first_order_and_this_order`, `months_between_first_order_and_this_order`, etc.

```yaml
version: 1
type: view
name: order_lines

sql_table_name: prod.order_lines
default_date: order

fields:
- name: order_line_id
  field_type: dimension
  type: string
  sql: ${TABLE}.order_line_id
  primary_key: yes
  hidden: yes

- name: order
  sql: ${TABLE}.order_at
  field_type: dimension_group
  type: time
  timeframes:
  - raw
  - date
  - week
  - month
  - quarter
  - year
  datatype: timestamp

- name: between_first_order_and_this_order
  field_type: dimension_group
  type: duration
  sql_start: ${TABLE}.first_order_date
  sql_end: ${order_raw}
  intervals: [day, week, month, quarter]
```
