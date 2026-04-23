{% hint style="danger" %}
**DRAFT — pending engineering review.** The schema/behavior described below was drafted from the data-model-management skill and has not yet been verified with engineering. Do not publish until confirmed.
{% endhint %}

# Relationships

Relationships are the recommended way to define joins between tables in Zenlytic. They are defined as a list on the [model](model.md) file and are always visible to Zoë when generating SQL, so you don't need to group views into a topic for joins to work.

Relationships replace both [topics](topic.md) and the `identifiers` block for the purpose of defining joins. Topics and identifiers continue to be supported for backward compatibility — see [Migrating from Memories and Topics](../migrations/migrating-from-memories-and-topics.md) for guidance on moving existing configuration.

## When to define a relationship

* **Non-obvious joins** — joins where column names don't match across views, where type casting is required, or where multiple columns need to line up. Zoë can't infer these from column names alone, so define them explicitly.
* **Joins with non-default cardinality or join type** — anything other than a `many_to_one` `left_outer` join that you want handled correctly for fan-out and filter semantics.
* **Repeated joins** (self-joins, or the same table joined in under different aliases) — use `join_as` on the relationship to handle these in one place.

**Obvious joins don't need to be stored.** If a `customer_id` foreign key obviously maps to a `customer_id` primary key, Zoë will figure it out. Focus your relationship definitions on joins where the connection isn't clear from column names alone. Over-documenting obvious joins can decrease Zoë's performance.

## Schema

Relationships are a list on the model file:

```yaml
version: 1
type: model
name: my_model
connection: my_connection

relationships:
  - from_table: orders
    join_table: customers
    relationship: many_to_one
    join_type: left_outer
    sql_on: ${orders.customer_id} = ${customers.customer_id}
```

Each entry supports the following properties:

| Property                | Required | Description                                                                                                                                                |
| ----------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `from_table`            | Yes      | The name of the source view.                                                                                                                               |
| `join_table`            | Yes      | The name of the view to join to.                                                                                                                           |
| `sql_on`                | Yes      | The join condition using `${view_name.field_name}` syntax. Combine multiple conditions with `AND`.                                                         |
| `relationship`          | No       | The cardinality of the join: `many_to_one` (default), `one_to_one`, `one_to_many`, `many_to_many`.                                                         |
| `join_type`             | No       | The SQL join type: `left_outer` (default), `inner`, `full_outer`, `cross`.                                                                                 |
| `join_as`               | No       | An alias for the joined view. Required when joining the same table in more than once (e.g., `requestor_users` and `assigned_users` both pointing at `cx_users`). |
| `join_as_label`         | No       | Display label to use for the aliased view in the UI and in Zoë's responses.                                                                                |
| `join_as_field_prefix`  | No       | Prefix to apply to field names from the aliased view so they don't collide with the original view's fields.                                                |
| `include_metrics`       | No       | Whether to include measures from the `join_table` when this join is used. Boolean. Defaults to `true`.                                                     |

## Cardinality matters

The `relationship` property tells Zoë how many rows on each side of the join it should expect.

| Type           | Description                                                                                                          |
| -------------- | -------------------------------------------------------------------------------------------------------------------- |
| `many_to_one`  | Multiple rows in `from_table` map to one row in `join_table`. The most common case (e.g., `order_lines` → `orders`). Default. |
| `one_to_one`   | Each row in `from_table` maps to exactly one row in `join_table`.                                                    |
| `one_to_many`  | One row in `from_table` maps to many rows in `join_table`. Can cause fan-out — use with care.                        |
| `many_to_many` | Multiple rows on both sides. Easiest to produce fan-out; handle aggregation carefully.                               |

{% hint style="warning" %}
**Fan-out warning.** `one_to_many` and `many_to_many` joins can cause rows to multiply and produce incorrect aggregate results. For these joins, aggregate in separate CTEs first or use Zenlytic's symmetric aggregate support via a `primary_key` on the view.
{% endhint %}

Cardinality is easier to get right when table and column names are human-readable. You can reason about a one-to-many join from `orders` to `line_items`, but you cannot reason about one from `tbl_a` to `tbl_b`. When table names are cryptic, add generous view descriptions to compensate.

## Worked example

A typical e-commerce model with orders, order lines, customers, and discounts:

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
    join_table: products
    relationship: many_to_one
    join_type: left_outer
    sql_on: ${order_lines.product_id} = ${products.product_id}

  - from_table: order_lines
    join_table: discounts
    relationship: many_to_many
    join_type: left_outer
    sql_on: ${order_lines.order_id} = ${discounts.order_id} and ${discounts.order_date} is not null
```
{% endcode %}

This replaces a corresponding topic definition and is visible to Zoë globally — you don't have to wrap it in a topic to use it.

## Multi-column joins

For joins that need more than one condition, combine them in `sql_on` with `AND`:

```yaml
relationships:
  - from_table: inventory
    join_table: warehouse_costs
    relationship: many_to_one
    join_type: left_outer
    sql_on: ${inventory.warehouse_id} = ${warehouse_costs.warehouse_id}
            AND ${inventory.product_id} = ${warehouse_costs.product_id}
```

## Joining the same table in twice (`join_as`)

If you need to join the same table into your model under multiple aliases — e.g., a `users` table serving as both "requestor" and "assignee" on a tickets table — use `join_as`:

{% code overflow="wrap" %}
```yaml
relationships:
  - from_table: tickets
    join_table: cx_users
    join_as: requestor_users
    join_as_label: Requestor
    relationship: many_to_one
    join_type: left_outer
    sql_on: ${tickets.requestor_user_id} = ${requestor_users.user_id}

  - from_table: tickets
    join_table: cx_users
    join_as: assigned_users
    join_as_label: Assigned To
    join_as_field_prefix: Assignee
    relationship: many_to_one
    join_type: left_outer
    sql_on: ${tickets.assignee_user_id} = ${assigned_users.user_id}
```
{% endcode %}

This lets users (and Zoë) reason about "requestor" and "assignee" as distinct views while still pointing at the same underlying `cx_users` table.

## Natural-language context about joins

Relationships define the structure of joins, but Zoë often needs plain-language context about which join paths are valid, which are pitfalls, and which should happen conditionally. For that:

* Use the [view](view.md) `description` or `zoe_description` to explain join paths that are specific to that table.
* Use the system prompt (Settings → Prompt) for universal join-routing rules that apply across all questions.

Common things to call out in prose:

* Which join paths are valid for common questions, and which are invalid.
* Fan-out pitfalls on specific one-to-many relationships.
* Granularity mismatches (see below).
* Conditional joins or joins that are only used to apply certain filters.

## Time-granularity mismatches

Tables at different time granularities — for example, daily vs. hourly — cannot be joined directly and produce correct results. The joined tables must first be aggregated to a common level (e.g., monthly) in separate CTEs, then combined in the final result.

If two tables in your model are at different granularities and users commonly ask questions that span them, add guidance to the system prompt or to the relevant view's `zoe_description` explaining the granularity mismatch and the recommended pattern. Relationships alone don't solve this — Zoë needs the prose context to construct the CTE-first query.

## Fiscal calendars

Industries that use non-standard calendars (e.g., retail 4-5-4) often need fiscal-period logic that goes beyond anything relationships can express. Complex fiscal calendar logic is a good candidate for a [Skill](../zenlytic-ui/skills.md) rather than trying to encode it in relationships or descriptions.
