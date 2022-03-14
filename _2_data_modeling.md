---
sidebar_position: 2
---

# Data modeling


To understand data modeling in Zenlytic there are a few key concepts to grasp. If you've used data models like LookML before, these will be intuitive and you'll be able to go straight to the implementation of your model.

### Key concepts

* Models
    * Models are collections of explores that reference a database connection. They serve as the data model's reference to the warehouses itself. They give your data model the ability to reference multiple data warehouses.

* Explores
    * Explores are collections of views (that is, database tables) that can be joined together. Joins are specified in the explore between the views (tables) that are included in the explore. They give users of Zenlytic the ability to dynamically join various tables together without worrying about doing the join in the wrong way.

* Views
    * Views directly represent a underlying database table. They contain both the dimensions (columns) and measures (aggregates) inside of the table they reference.

* Dimensions
    * A dimension represents a column in the database table it's view references. You can also have groups of dimensions (like timeframes) which reference the same column with different transformations applied.

* Measures (metrics)
    * A measure (or metric) represents the aggregation of a dimension or dimensions inside the table its view references. Any valid aggregation in a SQL statement with a `group by` will work as a measure (e.g. `sum(sales)`).


### Naming conventions

Naming is a crucial part of any data model and one of the most difficult aspects of maintaining a data model that can be understood by end users. Here are some Zenlytic naming conventions, both technically required and recommended

* The `name` field. Name fields must only contain letters, numbers, or the `_` character. They must be unique throughout your collection they are in, and despite how you may choose to enter them, they will always be lower-cased when referenced in Zenlytic.

