---
description: >-
  Connect your warehouse, import tables, and ask your first Zoë question in a
  new workspace.
---

# Start Here

Welcome to Zenlytic. The shortest path from a blank workspace to a working AI analyst:

1. **Connect** your data warehouse.
2. **Import a few tables** — or ask Zoë which ones to start with.
3. **Ask Zoë a real question** — and check her work.
4. **Ask Zoë how to make herself better** — and let her recommend (or apply) the changes.

The whole onboarding is a conversation. You don't need to build a finished data model before getting value, and you don't have to author context from scratch — Zoë can recommend, and with permission save, most of the changes you'd otherwise write by hand.

## Step 1 — Connect your data warehouse

Click **+ Add Connection** under **Database Connections** in the Settings menu. Pick your warehouse type, give the connection a name, and fill in the credentials.

The name matters. It's how Zenlytic links your credentials to your data model — the name here must match the `connection` property on your [model](../data-modeling/model.md) file (or your dbt `profile` if you're integrating via dbt MetricFlow without a Zenlytic model file).

For a reference, see the [demo data model](https://github.com/Zenlytic/demo-data-model). It uses the connection name `demo` because that's the value of `connection` on the [model file](https://github.com/Zenlytic/demo-data-model/blob/master/models/pure_organics_model.yml).

![Finish Connection](../.gitbook/assets/finish-connection.png)

## Step 2 — Import tables (or ask Zoë to)

The traditional path: open [Context Manager](../zenlytic-ui/context_manager.md), click **Add → Add view → Add from a database connection**, and pick the tables you want.

The faster path: **just ask Zoë.** Once your warehouse is connected, Zoë can read your `information_schema` — she sees every table available through that connection, not just the ones already imported. Try:

* "Which tables should I import to answer questions about retention?"
* "Add the orders, customers, and shipments tables to my model."
* "What's a good first set of tables to start with for revenue analysis?"

### Migrating from another BI tool

If you're moving from Power BI, Tableau, Looker, or another reporting platform, you don't have to figure out the mapping yourself. **Paste a screenshot of an existing report into chat and ask Zoë what data she'd need to recreate it.** She'll match the report's metrics and dimensions to your warehouse tables, tell you what to import, and — with edits enabled — do the import.

You can also describe the question without a screenshot — _"what data would I need to track new vs. repeat customer revenue by channel?"_ — and Zoë will identify the relevant tables and fields the same way.

See [Ask Zoë for Data Model Recommendations](../data-modeling/asking-zoe-for-recommendations.md) for the full workflow.

### Once tables are imported

Each imported table becomes a [view](../data-modeling/view.md) with dimensions auto-generated from the columns. **Set `default_date` on any time-series views** — that one property has an outsized effect on temporal questions and is the highest-leverage thing you can do early.

You don't need to define every metric or write every description before testing. Raw tables with decent names will get you surprisingly far. The full walkthrough for the editor, branch workflows, diffs, and deployment lives on the [Context Manager](../zenlytic-ui/context_manager.md) page.

## Step 3 — Ask Zoë a real question (and check her work)

Open Zoë and ask something you actually want answered:

* "What was revenue last quarter compared to the quarter before?"
* "Which products had the biggest YoY drop in margin?"
* "Show me sessions by channel for the last 30 days."

When she responds, **check her work**. Every chart and table has citations showing which fields and joins backed the answer. Click into them. Does the SQL match what you expected? Is she using the right field? Joining the right tables?

If something looks off, that's the signal for Step 4.

## Step 4 — Ask Zoë how to improve

When Zoë gets something wrong — and she will, at first — **don't guess at a fix**. Ask her:

* "Why did you pick that field?"
* "What context would help you answer this correctly next time?"
* "How should I model the join between orders and shipments?"
* "Add a measure for repeat purchase rate."
* "Create a skill for our fiscal calendar."

She'll diagnose the specific cause and recommend the smallest change that prevents the same mistake — a better `zoe_description`, a synonym, a missing measure, a new relationship, a system-prompt rule, or a skill for complex domain logic. With edits enabled, she can apply the change directly to your repo on the current branch.

This is the loop:

> Ask → check → ask Zoë what would help → save the fix → ask again.

Over time your model ends up configured exactly where it matters, not in places that turned out not to. **There is no separate "training" step for Zoë.** Your data model grows in response to real questions.

For shortcuts:

* **Wrong field picked?** Add `synonyms` for the term your users said.
* **Right field, used wrong?** Add a `zoe_description` clarifying when to use it vs. alternatives.
* **Wrong join or fan-out?** Define a [Relationship](../data-modeling/relationships.md) on the model file, or add join-path guidance to the view `description`.
* **Wrong date or date range?** Check `default_date`; use `canon_date` sparingly on individual measures.
* **Invalid measure?** Check the valid/invalid patterns on the [Measures](../data-modeling/measure.md) page.

See [Progressive Enrichment](../core-concepts/progressive-enrichment.md) for the priority order of what to reach for, [Context Surfaces](../core-concepts/context-surfaces.md) for where each kind of context lives, and [Fixing Zoë's Mistakes](../core-concepts/fixing-zoes-mistakes.md) for the full diagnostic flow.

## Step 5 — Ship it

When your changes are on a development branch and you're ready to make them live, use the **Deploy to production** action in [Context Manager](../zenlytic-ui/context_manager.md). That publishes the branch so Zoë (and the rest of your org) is using the latest version. Resolve any validation errors first.

If changes were pushed to git directly rather than through the UI, use [Pull from Remote](../data-modeling/cache-refresh.md) to rebuild the cache.

## Git for your data model

Git is connected by default. Keep using Zenlytic's **Managed Repo** unless you have a reason to switch — it requires zero setup. If you later need to switch to your own repo, contact support.

## FAQ

**Not seeing metrics in the Zenlytic interface?**

* If you have the `hidden` property set to `true`, you won't see those metrics or dimensions anywhere in the UI. Make sure you remove the hidden property or set it to `false` if you want those metrics to show up in the UI.

```yaml
# This metric won't show up in the UI because hidden is set to true
- name: number_of_orders
  field_type: measure
  type: count_distinct
  sql: ${order_id}
  description: "The unique number of orders placed"
  value_format_name: decimal_0
  hidden: true
```

## Where do I go from here?

* [Ask Zoë for Data Model Recommendations](../data-modeling/asking-zoe-for-recommendations.md) — the most important page if you want Zoë to help you build context
* [Context Surfaces](../core-concepts/context-surfaces.md) — where each kind of context lives
* [Fixing Zoë's Mistakes](../core-concepts/fixing-zoes-mistakes.md) — diagnostic flow when answers are off
* [Zoë](../zenlytic-ui/zoe.md) — the rest of the chat experience
* [Data Modeling Overview](../data-modeling/data_modeling.md) — for hands-on data model authoring

As always, feel free to reach out to your Zenlytic contact or [email support](mailto:support@zenlytic.com) if anything here doesn't match what you're seeing.
