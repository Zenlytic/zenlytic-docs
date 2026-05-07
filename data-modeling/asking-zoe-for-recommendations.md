# Ask Zoë for Data Model Recommendations

You don't have to author your data model alone. Zoë can recommend specific changes directly from chat, and if you've allowed her to, she can also make those changes for you and save them to your repository. The catalog of things she can help with is the same either way: new measures, new dimensions, new relationships, calculation logic, view and field documentation, workspace skills, the `system_prompt.md`, or restructuring something that isn't answering questions the way you'd like.

Ask in plain English. Either let Zoë draft a snippet for you to paste in [Context Manager](../zenlytic-ui/context_manager.md), or tell her to make the change for you on the current branch.

## When to ask Zoë instead of authoring from scratch

Good questions to bring to Zoë:

* **"How do I add a measure for X?"** — e.g. "How do I add a measure for repeat order rate?" or "How do I define customer lifetime value?"
* **"How should I write this calculation?"** — e.g. "Write me the SQL for days between first and second order" or "How do I compute rolling 30-day revenue?"
* **"How should these tables be joined?"** — e.g. "What's the right relationship between `orders` and `shipments`?"
* **"Why did you pick the wrong field?"** — Zoë can often diagnose why she chose the wrong field and recommend adding a `synonym`, `zoe_description`, or a new measure to prevent it next time. See also [Fixing Zoë's Mistakes](../core-concepts/fixing-zoes-mistakes.md).
* **"What should I add to this view to make it more useful?"** — Zoë can look at a view and recommend missing measures, synonyms, or descriptions.

## Letting Zoë make the change for you

You can allow Zoë to directly make changes to your data model and tell her to save them. When this is on, you can ask her to "add the measure", "fix the join", "update the system prompt to say...", or "create a skill for our fiscal calendar", and she will:

1. Read the current state of the relevant files.
2. Draft the smallest correct edit, such as a new field, an updated `zoe_description`, or a new skill.
3. Validate the data model with `validate_context` so YAML errors are caught before anything is committed.
4. Save the change to your repository with `save_context`, which commits and pushes on the current branch.
5. Run a sample query against any new or modified measure, dimension, or dimension group, so you can sanity-check the result.
6. Report back with what changed and suggest you re-ask the original question.

If validation fails, Zoë reads the error, fixes the referenced files, and validates again before saving, so no partial commits land.

The surfaces Zoë can edit:

* Data model YAML under `views/`, `models/`, `topics/`, and `dashboards/`, plus `zenlytic_project.yml`
* The workspace `system_prompt.md`, for shared, always-on rules
* Workspace `skills/`, including `skills/<skill-name>/SKILL.md` and any supporting files

She follows the same authoring rules a human editor would: flat `fields:` lists, valid measure patterns, conservative use of `searchable: true`, and `zoe_description` rather than `description` for agent-only guidance. See [Context Surfaces](../core-concepts/context-surfaces.md) for the full decision tree.

If you ask Zoë to "audit the model", "recommend changes", or "check whether she has enough context", she will inspect the data model and report findings without editing or committing. She only saves when you explicitly ask her to make the change.

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

If Zoë's edits are turned off, or you'd rather review the change before it lands, apply her snippet by hand:

1. Open [Context Manager](../zenlytic-ui/context_manager.md).
2. Navigate to the file Zoë named (view, model, topic, system prompt, or skill).
3. Paste the snippet in the right place and save.
4. If the change is significant, deploy to production when you're ready.
5. Re-ask your original question to confirm the change works end-to-end.

## Turning Zoë's edits on or off

Zoë's edits are on by default for workspaces that have access to the feature. You can toggle the behavior per workspace at:

**Workspace Settings → Zoë → Context Editing**

* When the toggle is **on**, Zoë can save changes to your data model from chat, subject to the permission rules below.
* When the toggle is **off**, Zoë will still draft snippets when you ask, but she will not write them to your repository.

## Zoë inherits your permissions

When edits are turned on, Zoë's editing permissions match your own. The data model is governed by the same role-based rules whether you edit by hand in Context Manager or ask Zoë to do it from chat:

* If you are an **Explore**, **View**, or **Restricted** user (or any role without `data_model_edit`), Zoë cannot edit the data model. She will draft recommendations and explain that you or a workspace admin needs to apply them.
* If you are **Develop**, **Develop without Deploy**, or **Admin**, Zoë can edit the data model on the branch you are currently on, as long as that branch is not the production branch.
* Only workspace **Admins** and users with the **Develop** role can deploy a development branch to the production branch. Deployment happens in [Context Manager](../zenlytic-ui/context_manager.md), not from chat.

### Editing the production branch directly

Asking Zoë to save a change while you're on the production branch is a separate, gated flow on top of the rules above. Zoë will only save edits on the production branch when **both** of the following are true:

* You have `deploy_to_production` (so you are an **Admin** or **Develop** user).
* The workspace's **Allow Edit Production** toggle is on.

If either is missing, Zoë will refuse the edit and ask you to switch to a development branch.

The Allow Edit Production toggle is on by default, and lives at:

**Workspace Settings → Git Settings → Allow Edit Production**

Turn it off to enforce a branch-and-deploy workflow where every production change goes through a development branch followed by an explicit deploy step. Turn it on if you want users with `deploy_to_production` to be able to edit the production branch directly, including from chat.

See [User Roles](../zenlytic-ui/user_roles.md) for the full role and permission reference.

## What Zoë won't do

Even with edits turned on, Zoë holds the line on a few things:

* Edit production when blocked. If you don't have `deploy_to_production`, or "Allow editing production" is off, Zoë will refuse production edits and suggest switching to a development branch or asking a workspace admin.
* Edit without `data_model_edit`. If your role doesn't include data model edit access, Zoë will recommend the change and tell you who can apply it.
* Recommend Memories or Topics for new context. Memories are legacy and being retired in favor of Skills. Topics are legacy/backwards-compatibility only. Zoë will route new context to view and field properties, skills, or the system prompt instead.
* Rewrite a whole file when a small edit will do. Zoë makes the smallest correct change to fix the issue you reported, rather than restructuring on speculation.

## Iterate based on what goes wrong

Zoë's edits and recommendations aren't always perfect on the first try. If a change doesn't produce the right answer when you test it, tell her (for example, "that measure gave the wrong number, the denominator should exclude internal test accounts") and she'll refine, re-validate, and, when edits are on, commit the fix. This is the same iterative philosophy the whole data model is built on: add context to fix the specific error you observed, rather than trying to anticipate every edge case up front. See [Progressive Enrichment](../core-concepts/progressive-enrichment.md) for the broader playbook.

## Related

* [Context Manager](../zenlytic-ui/context_manager.md): where you apply Zoë's recommendations or review her commits
* [Context Surfaces](../core-concepts/context-surfaces.md): when to use `description`, `zoe_description`, synonyms, or the system prompt; also covers the enable/disable toggle and the surfaces Zoë can edit
* [User Roles](../zenlytic-ui/user_roles.md): the role and permission reference Zoë inherits from
* [Fixing Zoë's Mistakes](../core-concepts/fixing-zoes-mistakes.md) — diagnostic flow when Zoë gives a wrong answer
* [Measures](measure.md) — valid/invalid aggregation patterns for measure SQL
