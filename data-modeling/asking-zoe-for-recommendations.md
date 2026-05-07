# Ask Zoë for Data Model Recommendations

You don't have to author your data model alone. Zoë can recommend — and, when you ask her to, **apply** — specific changes to your context directly from chat. That includes new measures, new dimensions, new relationships, calculation logic, view and field documentation, workspace skills, the `system_prompt.md`, or restructuring something that isn't answering questions the way you'd like.

This is often the fastest way to extend your model. Ask in plain English, and either let Zoë make the change for you on the current branch or take her recommendation and apply it yourself in [Context Manager](../zenlytic-ui/context_manager.md).

## When to ask Zoë instead of authoring from scratch

Good questions to bring to Zoë:

* **"How do I add a measure for X?"** — e.g. "How do I add a measure for repeat order rate?" or "How do I define customer lifetime value?"
* **"How should I write this calculation?"** — e.g. "Write me the SQL for days between first and second order" or "How do I compute rolling 30-day revenue?"
* **"How should these tables be joined?"** — e.g. "What's the right relationship between `orders` and `shipments`?"
* **"Why did you pick the wrong field?"** — Zoë can often diagnose why she chose the wrong field and recommend adding a `synonym`, `zoe_description`, or a new measure to prevent it next time. See also [Fixing Zoë's Mistakes](../core-concepts/fixing-zoes-mistakes.md).
* **"What should I add to this view to make it more useful?"** — Zoë can look at a view and recommend missing measures, synonyms, or descriptions.

## Two modes: recommend vs. apply

Zoë operates in one of two modes depending on what you ask for and what permissions are in play.

### Recommend mode

In recommend mode Zoë drafts the change and hands it back to you. Use this when you're exploring options, when you want to review the change before it lands, or when context editing isn't available for your role or workspace. Depending on the question, she'll return one or more of:

* **A YAML snippet** to paste into the relevant view, model, or topic file
* **A plain-English explanation** of what the change does and why
* **A note** about where the change should go (view `description` vs. field `zoe_description` vs. the system prompt) — see [Context Surfaces](../core-concepts/context-surfaces.md) for the decision framework
* **Follow-up questions** if she needs more detail (e.g., "Do you want this measure to exclude returned orders?")

You apply the recommendation in [Context Manager](../zenlytic-ui/context_manager.md).

### Apply mode

When you tell Zoë to make the change ("add the measure", "fix the join", "update the system prompt to say…"), she'll do it on the branch you're working on. The full workflow:

1. **Read** the current state of the relevant files.
2. **Draft** the smallest correct edit — a new field, an updated `zoe_description`, a new skill, etc.
3. **Validate** the data model with `validate_context` so YAML errors are caught before anything is committed.
4. **Save** the change to your repository with `save_context`, which commits and pushes on the current branch.
5. **Sample-query** the change for new or modified measures, dimensions, or dimension groups, so you can sanity-check the result.
6. **Report back** with what changed, the commit, and a suggestion to re-ask the original question.

If validation fails Zoë reads the error, fixes the referenced files, and validates again before saving. No partial commits land.

The surfaces Zoë can edit in apply mode:

* **Data model YAML** under `views/`, `models/`, `topics/`, and `dashboards/`, plus `zenlytic_project.yml`
* **The workspace `system_prompt.md`** for shared, always-on rules
* **Workspace `skills/`** — `skills/<skill-name>/SKILL.md` plus its supporting files

She follows the same authoring rules a human editor would: flat `fields:` lists, valid measure patterns, conservative use of `searchable: true`, and `zoe_description` rather than `description` for agent-only guidance. See [Context Surfaces](../core-concepts/context-surfaces.md) for the full decision tree.

### Review-only requests

If you ask Zoë to "audit the model", "recommend changes", or "check whether she has enough context", she stays in recommend mode by default — inspecting the current data model and reporting targeted recommendations without editing or committing. She'll only switch to apply mode when you explicitly ask her to make the changes.

## Example: adding a measure

You ask:

> How do I add a measure for repeat purchase rate in the `orders` view?

Zoë might respond with something like:

```yaml
- name: repeat_purchase_rate
  field_type: measure
  type: number
  sql: "{% raw %}${number_of_repeat_customers} / nullif(${total_customers}, 0){% endraw %}"
  value_format_name: percent_1
  description: The share of customers who placed more than one order.
  zoe_description: Use this for retention questions. Numerator is customers with 2+ orders; denominator excludes null customer_ids.
```

…along with a note explaining that she used `type: number` with a ratio SQL expression (one of the two valid measure patterns — see [Measures](measure.md) for the full rule), and a pointer to add synonyms like "retention rate" or "repeat rate" so she picks this measure on future questions.

## Example: asking about a relationship

You ask:

> How should I join the `orders` table to the `shipments` table?

Zoë will inspect both views and recommend a [relationship](relationships.md) block for the model file with the right `relationship` cardinality and `sql_on` condition, plus a note if the join risks fan-out.

## Applying a recommendation yourself

If you're working in recommend mode (or you want to review before saving), apply the snippet manually:

1. Open [Context Manager](../zenlytic-ui/context_manager.md).
2. Navigate to the file Zoë named (view, model, topic, system prompt, or skill).
3. Paste the snippet in the right place and save.
4. If the change is significant, deploy to production when you're ready.
5. Re-ask your original question to confirm the change works end-to-end.

## Enabling or disabling Zoë's edits

Apply mode is on by default for workspaces that have access to it, but you can turn it on or off per workspace:

**Workspace Settings → Chat Settings → Context Editing**

When the toggle is **off**, Zoë stays in recommend mode no matter what you ask her — she'll still draft snippets, but she won't write them to your repository.

A few additional rules govern when apply mode is available even with the toggle on:

* **Permissions:** Zoë needs you to have `develop_without_deploy` (or higher) on the workspace. Below that, she behaves as read-only and will only recommend.
* **Branches:** edits on a non-production branch are always allowed for users with `develop_without_deploy`. Edits on the production branch additionally require `deploy_to_production` permission **and** the workspace's "Allow editing production" setting to be enabled.
* **Validation:** if the change is in data model YAML and the model is invalid, Zoë won't save until she's fixed the referenced files. She'll tell you what failed.

## What Zoë won't do

Even in apply mode, Zoë holds the line on a few things:

* **Edit production when blocked.** If you don't have `deploy_to_production` or "Allow editing production" is off, Zoë will refuse production edits and suggest switching to a development branch or asking a workspace admin.
* **Edit without `data_model_edit`.** If your role doesn't have data-model edit access, Zoë will recommend the change and tell you who can apply it.
* **Recommend Memories or Topics for new context.** Memories are legacy and being retired in favor of Skills. Topics are legacy/backwards-compatibility only. Zoë will route new context to view/field properties, skills, or the system prompt instead.
* **Rewrite a whole file when a small edit will do.** Zoë makes the smallest correct change to fix the issue you reported, rather than restructuring on speculation.

## Iterate based on what goes wrong

Zoë's edits and recommendations aren't always perfect on the first try. If a change doesn't produce the right answer when you test it, tell her — "that measure gave the wrong number, the denominator should exclude internal test accounts" — and she'll refine, re-validate, and (in apply mode) commit the fix. This is the same iterative philosophy the whole data model is built on: add context to fix the specific error you observed, rather than trying to anticipate every edge case up front. See [Progressive Enrichment](../core-concepts/progressive-enrichment.md) for the broader playbook.

## Related

* [Context Manager](../zenlytic-ui/context_manager.md) — where you apply Zoë's recommendations or review her commits
* [Context Surfaces](../core-concepts/context-surfaces.md) — when to use `description`, `zoe_description`, synonyms, or the system prompt; also covers the enable/disable toggle and the surfaces Zoë can edit
* [Fixing Zoë's Mistakes](../core-concepts/fixing-zoes-mistakes.md) — diagnostic flow when Zoë gives a wrong answer
* [Measures](measure.md) — valid/invalid aggregation patterns for measure SQL
