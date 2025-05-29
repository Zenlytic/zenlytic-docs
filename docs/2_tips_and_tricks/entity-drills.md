---
sidebar_position: 6
title: "Entity Drills"
description: "How to define and use entity drills in Zenlytic"
---

# Use drills to define your entities

You can use drills/entities in Zenlytic to let Zoë know about important entities in your data. Entities can be any group of fields that you want, and they can describe anything from `products` to `users` to `transactions` to `sales_reps`. Let's look at an example of defining one of those entities for `sales_reps`:

```bash
version: 1
type: view
name: sales_reps
model_name: my_company
sql_table_name: PROD.SALES_REPS
default_date: joined_at

fields:
...
- name: sales_rep_id
  field_type: dimension
  type: string
  sql: ${TABLE}.id
  tags: ['Sales Rep']
  drill_fields: [first_name, last_name, email, status]

- name: first_name
  field_type: dimension
  type: string
  sql: ${TABLE}.first_name

- name: last_name
  field_type: dimension
  type: string
  sql: ${TABLE}.last_name

- name: email
  field_type: dimension
  type: string
  sql: ${TABLE}.email

- name: status
  field_type: dimension
  type: string
  sql: ${TABLE}.status

- name: joined_at
  field_type: dimension_group
  type: time
  timeframes:
  - raw
  - date
  - week
  - month
  - quarter
  - year
  sql: ${TABLE}.JOINED_AT
```

This will let Zoë know that you have an entity called a "Sales rep" and that entity should typically include the fields `first_name`, `last_name`, `email`, and `status` when that entity is referenced.

This will also give you a drop down option on all Zenlytic plots for "Drill into sales reps" when it's possible to join these fields into your data.