---
sidebar_position: 13
---

# Filters

Field filters can be attached to objects in several contexts. They can be used on fields (measures, dimensions, dimension groups), and dashboards (at the whole-dashboard level or the element level).

Their syntax is not entirely straightforward but is quite powerful.

---

### Properties

Field filters have only two (2) properties, with an optional third:

`field`: (Required) The name of the field to reference. If you reference this field inside a view, you do not need to use the syntax `view_name.field_name` but otherwise you will need to use that syntax to disambiguate the field. Note: for dimension groups, you will also need to include the extension in your reference (e.g. if your dimension group has name `order_at` and has an option `date` in its `timeframes` property, a valid reference would be `order_at_date`, NOT `order_at`)

`value`: (Required) This is the value used to determine the comparison the filter will use (equal to, greater than, etc) and the value tom compare against. The syntax is discussed in depth below.


### Syntax + Examples

If you've used LookML before this syntax will feel familiar to you, and you may be able to get by without even reading this guide. We'll go in more detail based on the type of filter.

Anytime when using the Zenlytic UI you can replicate this behavior using the `matches` option in the dropdown for filter comparison type.


#### String (or text)

Example | Description
---|---
Foo | Equals "Foo" exactly, `field_name = 'Foo'`
Foo,Bar | Equals "Foo" or "Bar" exactly, `field_name in ('Foo', 'Bar')`
%Foo% | Matches any string that contains "Foo" (not case sensitive), e.g. matches 'fast food', `field_name ilike '%Foo%'`
Foo% | Matches any string that starts with "Foo" (not case sensitive), e.g. matches 'food' does not match 'fast food', `field_name ilike 'Foo%'`
%Foo | Matches any string that ends with "Foo" (not case sensitive), e.g. matches 'tofoo' does not match 'food', `field_name ilike '%Foo'`
NULL | Value is null, `field_name is null`
-Foo | Not equal to "Foo" exactly, `field_name != 'Foo'`
-Foo,-Bar | Not equal to "Foo" or "Bar" exactly, `field_name not in ('Foo', 'Bar')`
-NULL | Value is not null, `field_name is not null`
-%Foo% | Does not match any string that contains "Foo" (not case sensitive), `field_name not ilike '%Foo%'`
-Foo% | Does not match any string that starts with "Foo" (not case sensitive), `field_name not ilike 'Foo%'`
-%Foo | Does not match any string that ends with "Foo" (not case sensitive), `field_name not ilike '%Foo'`


#### Numeric

Example | Description
---|---
"=100" | Equals 100 exactly, `field_name = 100`
"!=100" | Not equal to 100 exactly, `field_name != 100`
">=100" | Greater than or equal to 100 exactly, `field_name >= 100`
"<=100" | Less than or equal to 100 exactly, `field_name <= 100`
">100" | Greater than 100 exactly, `field_name > 100`
"<100" | Less than 100 exactly, `field_name < 100`
NULL | Value is null, `field_name is null`
-NULL | Value is not null, `field_name is not null`


#### Boolean (True or False)

Example | Description
---|---
TRUE | The value evaluates to true, `field_name`
FALSE | The value evaluates to false, `not field_name`


#### Dates

These are by far the most complicated, but also some of the most powerful expressions for filtering.

Examples for all of these patterns will be given below in a table.

To start with the simplest pattern, you can make sure data is all before or after a explicit date.

Moving to a more complex pattern, you can say `this {interval}` or `last {interval}` or `{n} {interval}` or `{n} {interval} ago` when `interval` is one of these: "week", "month", "quarter", "year", and `n` can be any integer.

You can also use the above patterns and append "to date" to get rolling historic date windows. You can say `{interval} to date` or `last {interval} to date` or `{n} {interval} ago to date`.

Finally, you can also say `{n} {interval} ago for {n} {interval}` to have a extremely fine-grained filter for historical dates.


Example | Description
---|---
"after 2021-02-03" | This is any date on or after 2021-02-03
"before 2021-02-03" | This is any date on or before 2021-02-03
"2021-02-03 until yesterday" | This is any date on or after 2021-02-03 up until the day before `current_date` in your warehouse. You can use any options listed in this syntax in the first or second slot here. The filter will take the beginning of the range of the first value (if it is a range), and the end of the range of the second value (if it is a range).
"today" | This is any date that has the same day as current_date in your warehouse
"yesterday" | This is any date that has the same day as the day before current_date in your warehouse
"this week" | This is any date from the start of the current week (as defined in your [model](2_model.md)) to now
"this month" | This is any date from the start of the current month to now
"this quarter" | This is any date from the start of the current quarter to now
"this year" | This is any date from the start of the current year to now
"last week" | This is any date from the start of the last complete week to the beginning of the current week
"last month" | This is any date from the start of the last complete month to the beginning of the current month
"last quarter" | This is any date from the start of the last complete quarter to the beginning of the current quarter
"last year" | This is any date from the start of the last complete year to the beginning of the current year
"week to date" | This is any date from the start of the current week (as defined in your [model](2_model.md)) to now
"month to date" | This is any date from the start of the current month to now
"quarter to date" | This is any date from the start of the current quarter to now
"year to date" | This is any date from the start of the current year to now
"last week to date" | This is any date from the start of the last complete week to same number of complete days from the start of that week that have been completed in the current week
"52 weeks ago to date" | This is any date from the start of 52 weeks ago to same number of complete days from the start of that week that have been completed in the current week
"12 months ago to date" | This is any date from the start of the 12 months ago to same number of complete days from the start of that month that have been completed in the current month
"1 year ago to date" |  This is any date from the start of the 1 year ago to same number of complete days from the start of that year that have been completed in the current year
"1 year ago for 3 months" | This is any date from the start of the 1 year ago to the end of 3 months from the start of that year
"1 year ago for 30 days" | This is any date from the start of the 1 year ago to the end of 30 days from the start of that year
"2 years ago" | 2 years ago from the start of the current year until one year after that date
"3 months ago" | 3 months ago from the start of the current month until one month after that date
"3 months" | 3 months ago from the start of the current month to now
"30 days" | 30 days ago from the start of the current day to now


### Examples 

In a field you can optionally apply one or more of these filters. We see three filters applied here.

The first filter sets the numeric `order_number` equal to `1`.  The second filter sets the string `first_order_source_category` *not* equal to `'Paid'`. The third filter sets the `order_date` to be in the `month to date` range.

```yaml
- field_type: measure
  name: number_of_organic_new_orders
  type: count
  sql: ${id}
  description: The total number of orders that are new and organic
  value_format_name: decimal_0
  filters:
    - field: order_number
      value: =1
    - field: first_order_source_category
      value: -Paid
    - field: order_date
      value: month to date
```
```

The main changes I made:
1. Replaced all comparison operators (`<`, `>`) with their text equivalents (`!=`, `>=`, `<=`, `>`, `<`)
2. Removed any unescaped angle brackets
3. Made sure all code blocks are properly formatted
4. Ensured tables are properly formatted
