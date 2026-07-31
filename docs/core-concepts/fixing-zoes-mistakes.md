---
description: >-
  Diagnose wrong answers by error type, then add the smallest context or
  modeling change that fixes the issue.
---

# Fixing Zoë's Mistakes

When Zoë produces a wrong answer, resist the urge to guess at a fix. Classify the error first, then add the smallest piece of context that prevents that class of error in the future. This page is a diagnostic router — pick the category that matches what went wrong and follow the link to the specific fix.

## The diagnostic process

1. **Look at what happened.** What question did the user ask? What fields did Zoë search for? What SQL did she write?
2. **Identify where she went wrong.** Wrong field? Wrong join? Missing filter? Wrong aggregation? Wrong date?
3. **Classify the error** into one of the categories below.
4. **Make the minimal context addition** that prevents that class of error. Don't try to anticipate every edge case — fix observed problems.
5. **Re-ask the original question** to verify the fix works.

## Error categories

### Discoverability — Zoë couldn't find the right field

Symptom: Zoë answered using the wrong field, or said she couldn't find a metric you know exists.

Most common fixes, in order:

* **Add `synonyms`** to the field with the terms your users actually say. This is the single highest-impact change — synonyms get a +20 boost in search ranking.
* **Check `hidden`.** The field may be hidden when it shouldn't be.
* **Improve `description` or `zoe_description`** so the field's description mentions the concept using the user's vocabulary.

See [Descriptions and Synonyms](../tips-and-tricks/descriptions-and-synonyms.md) and [Dimensions](../data-modeling/dimension.md).

### Reasoning — Zoë found the field but used it wrong

Symptom: Zoë picked a plausible field but it's the wrong one for this question (e.g., used gross revenue when net was meant).

Fixes:

* **Add `zoe_description`** clarifying when to use this field vs. alternatives. "Use this for net revenue after returns. For gross revenue before returns, use `gross_revenue`."
* **Set `searchable: true`** if the issue is about not knowing what values exist in a status/type/category column.
* **Add to the system prompt** if the rule is universal across all questions (e.g., "always default to net revenue unless the user asks for gross").
* **Add to the field's `zoe_description`** if the instruction is specific to one field.

See [Context Surfaces](context-surfaces.md) for picking the right surface.

### Join — wrong joins or fan-outs

Symptom: Zoë joined the wrong tables, or the result is inflated because of a fan-out.

Fixes:

* **Define a** [**Relationship**](../data-modeling/relationships.md) on the model file for non-obvious joins.
* **Add prose context** in the view `description` / `zoe_description` or the system prompt explaining which join paths are valid, which are invalid, and what pitfalls exist.
* **Improve view labels and descriptions** if table names are cryptic — Zoë needs readable names to reason about joins correctly.
* **For one-to-many or many-to-many joins**, aggregate in separate CTEs to avoid fan-outs. Document this pattern in the view `zoe_description` or the system prompt.
* **For time-granularity mismatches** (daily vs. hourly), explain in prose that the tables must be aggregated to a common level before joining.

### Time and date handling

Symptom: Zoë used the wrong date field, scoped the wrong date range, or produced an off-by-one fiscal result.

Fixes:

* **Set `default_date` on every view** with time-series measures. This is the single most impactful structural property for temporal queries.
* **Check the dimension group** — verify `type`, `timeframes`, `datatype`, and `convert_tz` are correct. See [Dimension Groups](../data-modeling/dimension_group.md).
* **If a date was imported as `type: string`**, cast it in `sql` and convert the field to a dimension group.
* **Use `canon_date` sparingly** — only on individual measures that genuinely need a different date than the view default. Overuse causes problems.
* **For fiscal calendars**, especially 4-5-4 or other non-standard ones, create a [Skill](../zenlytic-ui/skills.md) with the fiscal logic.
* **Avoid reserved words** in dimension group names (`__time`, `date`, `time`) — they produce reserved-word aliases that break SQL. Use `order_date` or `created_at` instead.

### Metric — wrong aggregation or invalid measure

Symptom: Zoë produced a sum when you expected a distinct sum, or verification failed on a new measure.

Fixes:

* **Check the measure pattern.** Only two are valid: `type: sum` + `sql: field`, or `type: number` + `sql: SUM(field)`. See the valid/invalid table on [Measures](../data-modeling/measure.md).
* **If the KPI can't fit in a single SELECT aggregate**, add calculation guidance to the view `description` or the relevant measure's `zoe_description` rather than forcing it into a single measure.
* **Document the measure's meaning** in `zoe_description` — what it excludes, when to use it, what to compare it to.

## Related pages

* [Context Surfaces](context-surfaces.md) — where context lives and when Zoë sees it
* [Relationships](../data-modeling/relationships.md) — structured join definitions
* [Skills](../zenlytic-ui/skills.md) — on-demand context for complex patterns
* [Measures](../data-modeling/measure.md) — valid measure patterns and `canon_date` guidance
