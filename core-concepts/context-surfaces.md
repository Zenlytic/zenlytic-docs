# Context Surfaces

When users ask "where do I put instructions for Zoë?", the answer depends on **when** Zoë needs to see the context. There's no strict hierarchy — Zoë sees all of your context and uses it as appropriate — but there is a visibility difference. Some context is present on every question, some appears only when a particular view is in scope, and some surfaces only after a field search.

This page is the canonical reference for which surface to reach for, how visible each one is, and how much you can fit in it.

{% hint style="info" %}
**A useful heuristic.** Could a talented data analyst, on their first day, answer real business questions using only your data model — with no other context? If yes, Zoë will do great. If not, the gap between "what the model says" and "what an analyst would need to know" is exactly the context you need to encode.
{% endhint %}

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

A concrete example — a `description` that encodes both the user-facing meaning and a disambiguation rule:

```yaml
- name: gross_aov
  field_type: measure
  type: average
  sql: ${TABLE}.revenue
  description: |>
      This is the gross average order value. This just covers
      DTC revenue, and is sometimes internally referred
      to as 'the magic'. This is the metric that
      should be used when someone asks about AOV, generally speaking.
```

With that description, Zoë can answer "what's the magic this month?" or a generic "what's our AOV?" and pick `gross_aov` — the description gives her both the synonym (`magic`) and the default-pick rule.

### `synonyms` — what users actually call the field

Use `synonyms` for alternative phrasings that don't belong in the field name or description prose. For example, if users ask about "existing customers" or "loyalty," you want a `new_vs_repeat` dimension on order lines to surface even though the name doesn't mention "customer":

```yaml
- name: new_vs_repeat
  field_type: dimension
  type: string
  sql: ${TABLE}.new_vs_repeat
  description: The new vs repeat status of the purchaser
  synonyms:
  - customer
  - loyalty
```

Synonyms get a +20 boost in search ranking, so they are the highest-impact lever for discoverability. See [Descriptions and Synonyms](../tips-and-tricks/descriptions-and-synonyms.md) for more patterns.

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

## Letting Zoë edit context for you

Zoë can do more than recommend changes — she can also create and edit your workspace context directly from chat when you ask her to. The surfaces she can write to:

* **Data model YAML** under `views/`, `models/`, `topics/`, and `dashboards/`, plus `zenlytic_project.yml`
* **The workspace `system_prompt.md`** — universal rules and shared domain knowledge
* **Workspace `skills/`** — `skills/<skill-name>/SKILL.md` and supporting files for recurring workflows

When you ask Zoë to make a change, she follows a consistent workflow: she reads the relevant files, drafts the smallest correct edit, validates the result against the data model, commits the change to your repository on the current branch, and then runs a quick sample query to confirm the edit behaves as expected. If validation fails she reads the error, fixes the referenced files, and tries again before saving.

She can also do this in **review-only mode** without saving anything. If you ask Zoë to "audit the model", "find improvements", or "check whether you have enough context", she'll inspect the data model and report targeted recommendations without editing or committing.

### Branch and permission rules

Zoë respects the same branch-and-role rules as a human editor in [Context Manager](../zenlytic-ui/context_manager.md):

* **Non-production branches:** users with `develop_without_deploy` (or higher) can have Zoë edit any file in the data model.
* **Production branch:** edits require both `deploy_to_production` permission **and** the workspace's "Allow editing production" setting to be enabled. If either is missing, Zoë will refuse the edit and explain how to either switch to a development branch or get the right permission.
* **Below `develop_without_deploy`:** Zoë treats the workspace as read-only and will not save anything. She'll still recommend changes; you can apply them yourself in [Context Manager](../zenlytic-ui/context_manager.md), or ask a workspace admin.

### Turn it on or off

The feature is on by default for workspaces that have access to it. You can toggle it per workspace at:

**Workspace Settings → Chat Settings → Context Editing**

When the toggle is **on**, Zoë can sync, validate, and save changes to your data model context from chat. When it's **off**, Zoë can still recommend changes — she just won't write them — and you apply the recommendations yourself.

For the full recommend-vs-apply workflow with concrete examples, see [Ask Zoë for Data Model Recommendations](../data-modeling/asking-zoe-for-recommendations.md).

## Related pages

* [Ask Zoë for Data Model Recommendations](../data-modeling/asking-zoe-for-recommendations.md) — the recommend vs. apply flow with concrete examples
* [Context Manager](../zenlytic-ui/context_manager.md) — the UI for browsing, editing, and deploying context manually
* [Skills](../zenlytic-ui/skills.md) — how to create and use skills
* [Views](../data-modeling/view.md) — view-level descriptions
* [Dimensions](../data-modeling/dimension.md) — field-level descriptions, synonyms, searchable
* [Measures](../data-modeling/measure.md) — measure-level descriptions and calculation notes
* [How to Steer Zoë's Answers](../tips-and-tricks/zoe_context_ingestion.md) — the older tips-and-tricks entry point for this same material
