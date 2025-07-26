# Joins

**Topics are the primary way joins are organized and managed in Zenlytic.** [Topics](topic.md) define collections of views that can be joined together and specify how those joins work. This approach provides clearer organization, better governance, and more intuitive data relationships.

Topics allow you to:
- Explicitly specify which views belong together, and how they should join
- Provide business context about how data relates
- Apply consistent access controls across related data

## Topics

Topics organize your views into logical groupings and handle the join relationships between them. When you create a topic, you specify:

1. A **base view** that anchors the topic
2. **Additional views** that join to the base view or to each other
3. **Join logic** to define the sql to use when joining the views together

Here's how joins work within topics:

```yaml
type: topic
label: Customer Analytics
base_view: customers
model_name: my_model

views:
  # Simple join using default logic
  orders:
    join:
      join_type: left_outer
      relationship: one_to_many
      sql_on: ${customers.customer_id} = ${orders.customer_id}
  
  # One-to-many join with multiple columns
  order_line_items:
    join:
      join_type: left_outer
      relationship: one_to_many
      sql_on: ${orders.order_id} = ${order_line_items.order_id} AND ${customers.customer_id} = ${order_line_items.customer_id}
  
  # Custom join with specific logic
  customer_segments:
    join:
      join_type: left_outer
      relationship: many_to_one
      sql_on: ${customers.customer_id} = ${customer_segments.customer_id}
      
  # Override default access filters for this join
  # This means the access filters will only be applied once at 
  # the topic-level, instead of individually at the view level 
  customer_support_tickets:
    override_access_filters: true
    join:
      join_type: inner
      relationship: one_to_many
      sql_on: ${customers.customer_id} = ${customer_support_tickets.customer_id}
```

Zoë uses topics to understand what data can be joined together and how those relationships work, making her responses more accurate and contextually appropriate.

## Join As: How to join a table in more than once to a topic

Sometimes you need to join the same table into a topic multiple times with different meanings. For example, you might have an `orders` table that needs to reference `customers` as both "billing customer" and "shipping customer". This is where `join_as` comes in.

The `join_as` feature allows you to create multiple aliases for the same view within a topic, each with its own join logic and field prefixes.


First, define the identifiers in the view you want to join twice into your topic with `join_as` specifications:

{% code overflow="wrap" %}
```yaml
version: 1
type: view
name: cx_users
model_name: my_model
sql_table_name: PROD.CX_USERS

identifiers:
- name: requestor_user_id
  type: primary                   # Identifiers MUST be set to primary for the join_as to work in the topic.
  sql: ${user_id}
  join_as: requestor_users        # This value must be unique like view names
  join_as_label: Requestor        # This value is optional and will look like the view label

- name: assignee_user_id
  type: primary                   # Identifiers MUST be set to primary for the join_as to work in the topic.
  sql: ${user_id}
  join_as: assigned_users
  join_as_label: Assigned To      # This will be the label of the view when joined
  join_as_field_prefix: Assignee  # This will be the prefix for the fields when joined
...
```
{% endcode %}

Then, in your topic, you can join in the view like so:

{% code overflow="wrap" %}
```yaml
type: topic
label: Zendesk Tickets
base_view: tickets
model_name: my_model

views:
  # Join using requestor_users join_as alias
  requestor_users:
    join:
      join_type: left_outer
      relationship: many_to_one
      sql_on: ${tickets.requestor_user_id} = ${requestor_users.user_id}
  
  # Join using assigned_users join_as alias
  assigned_users:
    join:
      join_type: left_outer
      relationship: many_to_one
      sql_on: ${tickets.assignee_user_id} = ${assigned_users.user_id}
      
  # Custom join with specific logic
  user_segments:
    join:
      join_type: left_outer
      relationship: many_to_one
      sql_on: ${tickets.user_id} = ${user_segments.id}
```
{% endcode %}

This will let you join in the same underlying `cx_users` table twice using different aliases and join keys.

## Best Practices

1. **Group related views logically**

Create topics that make business sense. Don't join views only because it's possible to join them. Zoë can run queries on separate topics and merge the results afterwards, so it's not necessary all data you'd want to ask about is in the same topic.

2. **Provide descriptive topic labels and descriptions** 

Help users (and Zoë) understand the data relationships, and which topic to use for answering which questions by defining descriptions on the topic.
