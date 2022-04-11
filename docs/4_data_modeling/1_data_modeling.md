---
sidebar_position: 2
---

# Data modeling


To understand data modeling in Zenlytic there are a few key concepts to grasp. If you've used data models like LookML before, these will be intuitive and you'll be able to go straight to the implementation of your model.

### Key concepts

* [Models](2_model.md)
    * Models are collections of explores that reference a database connection. They serve as the data model's reference to the warehouses itself. They give your data model the ability to reference multiple data warehouses.

* [Explores](4_explore.md)
    * Explores are collections of views (that is, database tables) that can be joined together. [Joins](5_join.md) are specified in the explore between the [views (tables)](6_view.md) that are included in the explore. They give users of Zenlytic the ability to dynamically join various tables together without worrying about doing the join in the wrong way.

* [Views](6_view.md)
    * Views directly represent a underlying database table. They contain both the [dimensions (columns)](91_dimension.md) and [measures (aggregates)](93_measure.md) inside of the table they reference.

* [Dimensions](91_dimension.md)
    * A dimension represents a column in the database table it's view references. You can also have groups of dimensions (like timeframes) which reference the same column with different transformations applied.

* [Measures (metrics)](93_measure.md)
    * A measure (or metric) represents the aggregation of a dimension or dimensions inside the table its view references. Any valid aggregation in a SQL statement with a `group by` will work as a measure (e.g. `sum(sales)`).


### Naming conventions

Naming is a crucial part of any data model and one of the most difficult aspects of maintaining a data model that can be understood by end users. Here are some Zenlytic naming conventions, both technically required and recommended

* The `name` field. Name fields must only contain letters, numbers, or the `_` character. They must be unique throughout your collection they are in, and despite how you may choose to enter them, they will always be lower-cased when referenced in Zenlytic. This syntax is required when naming objects in Zenlytic

##### Recommendations

Naming is very, very hard. This is especially true in a domain as complex as your company's data model. These are a few recommendations from our experience on how to make it easier.

* Plurals vs singulars: When you name views, be consistent with your choice of plural or singular words. For example, if you name the table with sales orders in it `orders` don't name the table with order lines `order_line`, you should name it `order_lines`. It doesn't matter if you choose to go with singular or plural name, just be consistent.

* Prefixes and suffixes: Often you'll have metrics that total or sum up a column, e.g. sales or revenue. Again, consistency is key. If you have a metric named `total_gross_revenue` don't also have one `sum_net_revenue` or just `net_revenue`, you should name that metric `total_net_revenue`. End users will be confused by inconsistency in prefixes or suffixes. Again, it is less important *which* prefixes you use (if any). Consistency is the most important aspect.

* Multiple versions: You will almost certainly have some data issue in your warehouse that duplicates some table or view. Use your data model to hide those tables from your end users. They don't care that they're getting data from the `company_ga_3` table, and you shouldn't make them care. Eliminate duplicate names by designing joins that combine previously separate data into one view.