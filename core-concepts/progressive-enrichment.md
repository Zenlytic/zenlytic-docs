# Progressive Enrichment: What to Configure First

You do not need to build out a full semantic layer before asking Zoë questions. The fastest way to get value from Zenlytic is to import raw tables, start asking questions, observe where Zoë makes mistakes, and add targeted context to fix those specific errors.

Use this list as a priority order when you're adding context, not as a checklist to complete before starting. Each rung up this ladder has higher cost and narrower impact — start at the top and only add the next layer when you hit a problem it would solve.

## 1. Start with raw table imports

Import tables into the [Data Model Editor](../zenlytic-ui/data_model_editor.md) and start asking questions. If your tables have sensible names and obvious primary/foreign keys, Zoë can often answer without any additional configuration.

**Don't build everything before testing.** Ask real questions, see what breaks, and let that drive what you add next.

## 2. Set `default_date` on every view with time-series data

This is the single most impactful structural change you can make. Without `default_date`, temporal questions like "revenue this quarter" don't have a date field to scope against. Set it once per view and you'll correctly scope most time-series queries going forward.

See [Views](../data-modeling/view.md).

## 3. Add `synonyms` to your most important fields

Synonyms are the single highest-impact change for field-level discoverability. They get a **+20 boost in search ranking**, which makes it dramatically more likely Zoë finds the right field.

Add the terms users actually say — not just the technical column names. "Income", "sales", "top-line" might all be synonyms for `total_revenue`.

See [Descriptions and Synonyms](../tips-and-tricks/descriptions-and-synonyms.md).

## 4. Write view `description` on your key tables

Explain what the table represents, which join paths are valid, and any data caveats. `description` is shown to both users and Zoë, so it doubles as end-user documentation.

Use `zoe_description` when you need to say something to Zoë only — typically things like "join to `customers` through `orders`, never directly" or "this table only has data since 2023-01-01."

Both are capped at 10,000 characters per view. See [Views](../data-modeling/view.md) and [Context Surfaces](context-surfaces.md).

## 5. Add universal business rules to the system prompt

Default time ranges, terminology definitions, data freshness, join-routing preferences — anything that applies to **every** question, not just questions about a specific table.

The system prompt is always visible to Zoë, so putting something here guarantees she'll consider it. The tradeoff is that everything here costs attention on every question, so keep it focused on truly universal rules.

See [Context Surfaces](context-surfaces.md).

## 6. Define `relationships` for non-obvious joins

Obvious foreign-key/primary-key joins (`orders.customer_id` → `customers.customer_id`) don't need to be stored — Zoë figures those out. Focus [Relationships](../data-modeling/relationships.md) on:

* Joins where column names don't match across views
* Multi-column joins
* Joins that need a specific cardinality or join type
* Self-joins and repeated joins (via `join_as`)

Over-documenting obvious joins can decrease performance. Less is more.

## 7. Set `searchable: true` on status, type, and category columns

When the **values** in a column determine how users filter or group — statuses like "active/churned", types like "B2B/B2C", categories — set `searchable: true` so Zoë can see the values during field search.

**Do not** set `searchable` on high-cardinality columns. The default limit is 10,000 categories per dimension; IDs and timestamps blow past that and produce no useful context.

See [Dimensions](../data-modeling/dimension.md).

## 8. Write `zoe_description` on measures with non-obvious logic

For measures that exclude certain rows, use a non-obvious formula, or are easy to confuse with a similar measure, write a `zoe_description` that explains:

* What the measure calculates
* Any exclusions or filters baked in
* When to use it vs. alternatives

This is capped at 1,024 characters per field. For longer guidance, move it to the view `description` / `zoe_description` or a skill.

See [Measures](../data-modeling/measure.md).

## 9. Create skills for complex recurring analysis patterns

Use a [Skill](../zenlytic-ui/skills.md) when you have a multi-step workflow, a fiscal calendar, an industry-specific analysis pattern, or brand/style guidance that's sometimes relevant but shouldn't run on every question.

Skills are loaded on demand based on their description, so they're the right home for long, situational context that would bloat the system prompt if it were always-on.

## Iterate, don't boil the ocean

Configure what you need to fix observed problems. Don't try to anticipate every edge case up front — it's slower and usually produces context that's never needed. When Zoë gets something wrong, classify the error (see [Fixing Zoë's Mistakes](fixing-zoes-mistakes.md)) and add the minimal context that prevents that class of error. Over time, the model gets smarter in exactly the places where it matters.
