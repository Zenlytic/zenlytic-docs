---
description: >-
  Move from legacy memories and topics to skills and relationships without
  breaking existing behavior.
---

# Migrating from Memories and Topics

Zenlytic is consolidating two legacy configuration surfaces onto newer, more capable replacements:

* **Memories** are being replaced by **Skills**. Memories you have today will migrate automatically in a future release — you don't need to do anything. For new context, prefer Skills.
* **Topics** (and the related `identifiers` block on views) are being replaced by **Relationships** defined on the model file. Existing topics continue to work, but we no longer recommend adding new context to them.

Both legacy surfaces remain supported, so nothing breaks while you migrate. This page shows side-by-side examples of what the new surfaces look like and when to move existing context over.

## Memories → Skills

Memories let you save a canned question-and-answer pattern that Zoë retrieves when a similar question is asked. Skills cover the same use cases plus broader ones — complex analysis patterns, fiscal calendars, brand style guides — and you decide when they load rather than relying on semantic match.

### Before (Memory)

Created through **Add to memory** in chat or **Settings → Memory → New Text memory**:

> **User question**: "What was our revenue last quarter?"
>
> **Zoë response**: "Use the `total_net_revenue` measure from the `orders` view, grouped by `order_quarter`, filtered to the most recent complete quarter."

### After (Skill)

Created in the **Context Manager**:

* **Name**: Revenue Reporting
* **Description**: How to answer revenue and sales questions across the business.
*   **Instructions**:

    > When a user asks about revenue, use `total_net_revenue` from `orders`. For quarterly reporting, group by `order_quarter` and default to the most recent complete quarter unless the user specifies otherwise. Gross revenue is `total_gross_revenue`; only use it when the user explicitly asks for gross.

Skills are broader than memories by design. A single skill can cover an entire topic area, an industry-specific calendar, or a multi-step workflow, with no hard character limit. See [Skills](../zenlytic-ui/skills.md).

### When to move a memory today

You do not need to move existing memories — they will be migrated automatically. But if you are actively adding new context, create a skill instead:

* Short Q\&A patterns → one skill per topic area
* Brand, formatting, and tone rules → the built-in Brand Style Guide skill
* Complex recurring analysis → a dedicated skill with detailed instructions

## Topics → Relationships

Topics let you group views and define how they join. Relationships move join definitions onto the model file, which makes them always visible to Zoë without requiring users to select a topic, and avoids the implicit-join fan-out gotcha that topics have.

### Before (Topic)

A topic that joins `customers`, `orders`, and `discounts`:

{% code overflow="wrap" %}
```yaml
type: topic
label: Order lines
base_view: order_lines
model_name: my_model

views:
  orders:
    join:
      join_type: left_outer
      relationship: many_to_one
      sql_on: ${order_lines.order_id} = ${orders.order_id}

  customers:
    join:
      join_type: left_outer
      relationship: many_to_one
      sql_on: ${orders.customer_id} = ${customers.customer_id}

  discounts:
    join:
      join_type: left_outer
      relationship: many_to_many
      sql_on: ${order_lines.order_id} = ${discounts.order_id} and ${discounts.order_date} is not null
```
{% endcode %}

### After (Relationships on the model file)

The same joins, defined once on the model file and available globally:

{% code overflow="wrap" %}
```yaml
version: 1
type: model
name: my_model
connection: my_connection

relationships:
  - from_table: order_lines
    join_table: orders
    relationship: many_to_one
    join_type: left_outer
    sql_on: ${order_lines.order_id} = ${orders.order_id}

  - from_table: orders
    join_table: customers
    relationship: many_to_one
    join_type: left_outer
    sql_on: ${orders.customer_id} = ${customers.customer_id}

  - from_table: order_lines
    join_table: discounts
    relationship: many_to_many
    join_type: left_outer
    sql_on: ${order_lines.order_id} = ${discounts.order_id} and ${discounts.order_date} is not null
```
{% endcode %}

See [Relationships](../data-modeling/relationships.md) for the full schema and more examples.

### `join_as` (multiple joins to the same table)

If your existing model uses `identifiers` with `join_as` to join a view in twice (e.g., `requestor_users` and `assigned_users` against the same `cx_users` table), the same pattern is supported directly on relationships using `join_as`, `join_as_label`, and `join_as_field_prefix`. No per-view identifier block is required.

### Do I have to migrate?

No. Existing topics and identifiers continue to be read by Zoë and will keep working. You only need to move if:

* You want the join to be globally visible to Zoë without requiring a topic selection.
* You're hitting the topic implicit-join fan-out gotcha and want explicit cardinality handled once on the model.
* You're starting a new model from scratch — in that case, skip topics entirely.

### Obvious joins don't need to be migrated — or defined at all

If the join is obvious from column names (e.g., `orders.customer_id` → `customers.customer_id`), Zoë figures it out without an explicit relationship. You only need to define relationships for non-obvious joins, multi-column joins, or joins that need a specific `join_type` or `relationship` other than the default.

## Summary table

| Legacy surface        | Replacement                                                     | Status                                                   |
| --------------------- | --------------------------------------------------------------- | -------------------------------------------------------- |
| Memories              | [Skills](../zenlytic-ui/skills.md)                              | Auto-migrates in a future release. Usable now.           |
| Topics                | [Relationships](../data-modeling/relationships.md) on the model | Supported indefinitely. Not recommended for new context. |
| `identifiers` on view | `join_as` on relationships                                      | Supported indefinitely. Not recommended for new context. |
