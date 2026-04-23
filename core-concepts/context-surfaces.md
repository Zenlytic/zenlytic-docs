# Context Surfaces

When users ask "where do I put instructions for Zoë?", the answer depends on **when** Zoë needs to see the context. There's no strict hierarchy — Zoë sees all of your context and uses it as appropriate — but there is a visibility difference. Some context is present on every question, some appears only when a particular view is in scope, and some surfaces only after a field search.

This page is the canonical reference for which surface to reach for, how visible each one is, and how much you can fit in it.

## Surfaces at a glance

| Surface                               | Visibility                                     | Best for                                                                       | Char limit             |
| ------------------------------------- | ---------------------------------------------- | ------------------------------------------------------------------------------ | ---------------------- |
| **System prompt** (Settings → Prompt) | Every question, always                         | Universal rules, default behaviors, data freshness, join routing, terminology  | 20,000 chars           |
| **Skills** (Settings → Skills)        | On demand — Zoë decides when relevant          | Complex analysis patterns, fiscal calendars, domain-specific workflows         | No hard limit          |
| **View `description`**                | When the view is in context                    | Table-level business context shown to both users and Zoë                       | 10,000 chars           |
| **View `zoe_description`**            | When the view is in context                    | Agent-only table-level instructions (join paths, pitfalls, edge cases)         | 10,000 chars           |
| **Field `description`**               | After a field search; shown to users           | User-facing field documentation                                                | 1,024 chars            |
| **Field `zoe_description`**           | After a field search; not shown to users       | Agent-only field instructions and calculation notes                            | 1,024 chars            |
| **Field `synonyms`**                  | During search; boosted +20 in ranking          | Alternative names users actually say for this field                            | N/A                    |
| **Field `searchable: true`**          | During search; category values indexed         | Status, type, and category columns where values matter for filtering           | 10k categories default |
| **Memories** (Settings → Memory)      | Top 5 semantically matched per question        | **Legacy — avoid.** Being replaced by Skills.                                  | N/A                    |

## `description` vs. `zoe_description`

This is the single most asked-about distinction in Zenlytic's data model, so it's worth being explicit:

* **`description` is shown to users.** It appears in the UI and is also visible to Zoë. Put user-facing documentation here — what the table or field represents, business context, things an end user should know.
* **`zoe_description` is shown only to Zoë.** Users never see it. Put agent-specific instructions here — which join paths to prefer, how to disambiguate similar fields, when to use this field vs. an alternative, calculation notes.

If both are set, Zoë sees `zoe_description` (not both). If only `description` is set, Zoë sees that.

Both properties are available on views, fields (dimensions, measures, dimension groups), and topics. The character limits differ by level:

* **View-level** `description` and `zoe_description`: up to **10,000 characters** each.
* **Field-level** `description` and `zoe_description`: up to **1,024 characters** each.

If you need to write more than 1,024 characters about a single field, move the broader context up to the view's `description` or `zoe_description`, or into a skill.

## How to pick a surface

Use the following mental model:

1. **Is the rule universal — true for every question, not just ones about a particular table?** → **System prompt.**
   Examples: default time range for "this year", default to net revenue over gross, data freshness ("our warehouse is updated nightly at 2am UTC"), terminology mapping.
2. **Is it a complex pattern that only applies sometimes — a fiscal calendar, an industry-specific analysis, a multi-step workflow?** → **Skill.**
   Skills load on demand. They're for long-form, situational context.
3. **Is it about a specific table — which joins are valid, fan-out pitfalls, data caveats?** → **View `description` / `zoe_description`.**
4. **Is it about a specific field — how it's calculated, when to use it vs. an alternative?** → **Field `description` / `zoe_description`.**
5. **Is it about what users call the field — alternative phrasings, industry terms?** → **`synonyms`** on the field. Boosts search ranking +20.
6. **Is it about what values exist in a column — statuses, categories, types?** → **`searchable: true`** on the dimension. Skip this on high-cardinality columns like IDs or timestamps.

## Principles for placing context

* **Don't shy away from putting important logic in the system prompt.** It's appropriate for always-applicable rules: default time ranges, terminology definitions, data freshness rules, assumption guidelines, join-routing preferences.
* **Field-specific instructions belong on the field, not in the system prompt.** If an instruction only applies to one field or one view, put it there. The system prompt should be for universally applicable guidance.
* **Skills are for complex patterns you decide when to load.** They are optional context, not always-on.
* **Memories are legacy.** Any memories you already have will be migrated to skills automatically. For new context, create a skill.

## Memories (legacy)

Memories are retained for backward compatibility and will be migrated to skills in a future release. Do not add new context to memories. See [Memories](../zenlytic-ui/memories.md) for the existing reference and [Migrating from Memories and Topics](../migrations/migrating-from-memories-and-topics.md) for the recommended replacement.

## Related pages

* [Skills](../zenlytic-ui/skills.md) — how to create and use skills
* [Views](../data-modeling/view.md) — view-level descriptions
* [Dimensions](../data-modeling/dimension.md) — field-level descriptions, synonyms, searchable
* [Measures](../data-modeling/measure.md) — measure-level descriptions and calculation notes
* [How to Steer Zoë's Answers](../tips-and-tricks/zoe_context_ingestion.md) — the older tips-and-tricks entry point for this same material
