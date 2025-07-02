# Data Modeling Overview

To understand data modeling in Zenlytic, there are a few key concepts to grasp. If you've used data models like LookML before, these will be intuitive, and you'll be able to go straight to the implementation of your model. To better understand how to define context for Zoë, the AI analyst, check out the [tips & tricks doc](../2_tips_and_tricks/getting-started.md).

Note: You can also use our automatic LookML -> ZenML converter [here](https://lookml-zenml.netlify.app/).

## Key concepts

* [Models](model.md)
  * Models are references to a database connection. They serve as the data model's reference to the warehouses itself. They give your data model the ability to reference multiple data warehouses, and set some high level properties like the week start day or the timezone.
* [Views](view.md)
  * Views directly represent a underlying database table. They contain both the [dimensions (columns)](dimension.md) and [measures (aggregates)](measure.md) inside of the table they reference. In addition, they contain [identifiers](view.md#identifiers) which define the possible join to or from the table.
* [Dimensions](dimension.md)
  * A dimension represents a column in the database table it's view references. You can also have groups of dimensions (like timeframes) which reference the same column with different transformations applied.
* [Measures (metrics)](measure.md)
  * A measure (or metric) represents the aggregation of a dimension or dimensions inside the table its view references. Any valid aggregation in a SQL statement with a `group by` will work as a measure (e.g. `sum(sales)`).

## Examples

The best way to learn to to see examples. We have an example using our metrics yaml syntax.

* [Metrics Layer yaml example](https://github.com/Zenlytic/demo-data-model)

## Naming conventions

Naming is a crucial part of any data model and one of the most difficult aspects of maintaining a data model that can be understood by end users. Here are some Zenlytic naming conventions, both technically required and recommended.

### Technically Required

* The `name` field. Name fields must only contain letters, numbers, or the `_` character. They must be unique throughout your collection they are in, and despite how you may choose to enter them, they will always be lower-cased when referenced in Zenlytic. This syntax is required when naming objects in Zenlytic

### Recommendations

Naming can be challenging. This is especially true in a domain as complex as your company's data model. These are a few recommendations from our experience on how to make it easier.

* Plurals vs singulars: When you name views, be consistent with your choice of plural or singular words. For example, if you name the table with sales orders in it `orders` don't name the table with order lines `order_line`, you should name it `order_lines`. It doesn't matter if you choose to go with singular or plural name, just be consistent.
* Prefixes and suffixes: Often you'll have metrics that total or sum up a column, e.g. sales or revenue. Again, consistency is key. If you have a metric named `total_gross_revenue` don't also have one `sum_net_revenue` or just `net_revenue`, you should name that metric `total_net_revenue`. End users will be confused by inconsistency in prefixes or suffixes. Again, it is less important _which_ prefixes you use (if any). Consistency is the most important aspect.
* Multiple versions: You will almost certainly have some data issue in your warehouse that duplicates some table or view. Use your data model to hide those tables from your end users. They don't care that they're getting data from the `company_ga_3` table, and you shouldn't make them care. Eliminate duplicate names by designing joins that combine previously separate data into one view.
