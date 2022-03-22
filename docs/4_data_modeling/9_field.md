---
sidebar_position: 1
---

# Fields

Fields reference either columns in the database (dimensions and dimension groups) or aggregates computed in a `group by` statement (measures or metrics). There are three types of fields `dimension`, `dimension_group` and `measure` (we also refer to measures as metrics, and use the terms interchangeably). For all fields their `field_type` (one of the three just listed) is a required property.

- [Dimensions](91_dimension.md) are references to columns in your database table. They can either reference each other or raw columns in the database.

- [Dimension Groups](92_dimension_group.md) are a special type of dimension used for timeframes (referencing the same date column but having slices for it daily, weekly, monthly, etc), and for intervals (referencing the difference between two date columns and slicing it days between, weeks between, months between, etc).

- [Measures (or metrics)](93_measure.md) are reference dimensions or raw columns in the database and specify an aggregate on those columns. They can also reference other measures and perform operations referencing each other post-aggregation. E.g. if you have a measure `total_gross_revenue` and a measure `total_discounts` you can define a new measure like this to calculate total net revenue.
```
name: total_net_revenue
field_type: measure
type: number
sql: ${total_gross_revenue} - ${total_discounts}
```

There will be more examples of each type of field in their respective documentation pages.

Fields are defined in view files.
