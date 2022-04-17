---
sidebar_position: 15
---

# Symmetric Aggregates

Symmetric aggregates allow Zenlytic to calculate your metrics accurately even when there's a situation where the joins make that very difficult by duplicating the values to aggregate.

We could go in-depth into how we do this, but we're obviously not the first to do this and Looker has already written the best piece of content about this [here](https://help.looker.com/hc/en-us/articles/360023722974-A-Simple-Explanation-of-Symmetric-Aggregates-or-Why-On-Earth-Does-My-SQL-Look-Like-That-), which we strongly recommend checking out.


### Examples 

You can use `distinct` aggregates to tell Zenlytic how to distinctly calculate your metric. For example, this measure is a sum, but uniquely for each `order_id`.

```
- name: total_price_order_level
  field_type: measure
  type: sum_distinct
  sql_distinct_key: ${order_id}
  sql: ${price} 
```
