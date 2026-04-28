# Start Here

Welcome to Zenlytic. This page walks you from a blank workspace to asking Zoë your first real question. The shortest version:

1. **Connect your data warehouse.**
2. **Import a few raw tables.**
3. **Ask Zoë a question.**
4. **When something's wrong, add the smallest piece of context that fixes it — then ask again.**

You don't need a fully built-out data model before you start getting value. The fastest path to a good experience is to import the tables you care about, ask real questions, and let the mistakes tell you what to configure next.

## Step 1 — Connect your data warehouse

Click **+ Add Connection** under **Database Connections** in the Settings menu. Pick your warehouse type, give the connection a name, and fill in the credentials.

The name matters. It's how Zenlytic links your credentials to your data model — the name here must match the `connection` property on your [model](../data-modeling/model.md) file (or your dbt `profile` if you're integrating via dbt MetricFlow without a Zenlytic model file).

For a reference, see the [demo data model](https://github.com/Zenlytic/demo-data-model). It uses the connection name `demo` because that's the value of `connection` on the [model file](https://github.com/Zenlytic/demo-data-model/blob/master/models/pure_organics_model.yml).

![Finish Connection](../assets/5_data_modeling/finish-connection.png)

## Step 2 — Git for your data model

Git is already connected by default. Keep using Zenlytic's **Managed Repo** unless you have a reason to switch — it requires zero setup. If you later need to switch to your own repo, contact support.

## Step 3 — Import raw tables and ask a question

Open [Context Manager](../zenlytic-ui/context_manager.md) from the workspace navigation or from chat. Add a view from the **Context** tab — you can either upload a CSV or pick tables from your database connection. Zenlytic reads the `information_schema` to pull in metadata and, on warehouses like Snowflake, BigQuery, and Databricks, imports column and table descriptions too.

Once the tables are imported:

* Each imported table becomes a [view](../data-modeling/view.md) with dimensions auto-generated from the columns.
* Pick a sensible `default_date` for each view that has time-series data. This one property has an outsized effect on temporal questions.
* **That's enough to start.** Go ask Zoë a question.

You don't need to define every metric, write every description, or set up relationships before testing. Raw tables with decent names will get you surprisingly far. The full walkthrough for the editor, branch workflows, diffs, and deployment lives on the [Context Manager](../zenlytic-ui/context_manager.md) page.

## Step 4 — Iterate based on what goes wrong

When Zoë answers something incorrectly — picks the wrong field, constructs a wrong join, uses the wrong aggregation — **don't guess at a fix**. Classify the error first, then add the smallest piece of context that would have prevented it.

The full diagnostic router lives at [Fixing Zoë's Mistakes](../core-concepts/fixing-zoes-mistakes.md). In short:

* **Wrong field picked?** Add `synonyms` for the term your users said.
* **Right field, used wrong?** Add a `zoe_description` clarifying when to use it vs. alternatives.
* **Wrong join or fan-out?** Define a [Relationship](../data-modeling/relationships.md) on the model file, or add join-path guidance to the view `description`.
* **Wrong date or date range?** Check `default_date`; use `canon_date` sparingly on individual measures.
* **Invalid measure?** Check the valid/invalid patterns on the [Measures](../data-modeling/measure.md) page.

After you make the change, re-ask the original question to verify. Over time, your model ends up configured in exactly the places where it matters, not in places that turned out not to.

See [Progressive Enrichment](../core-concepts/progressive-enrichment.md) for the priority order of what to reach for, and [Context Surfaces](../core-concepts/context-surfaces.md) for where each kind of context lives.

## Step 5 — Ship it

When your changes are on a development branch and you're ready to make them live, use the **Deploy to production** action in [Context Manager](../zenlytic-ui/context_manager.md). That publishes the branch so Zoë (and the rest of your org) is using the latest version. Resolve any validation errors first.

If changes were pushed to git directly rather than through the UI, use the [force-refresh](../data-modeling/cache-refresh.md) button to rebuild the cache.

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

* Learn the UI — [Using Zenlytic](../zenlytic-ui/using_zenlytic.md)
* Learn the data model — [Data Modeling Overview](../data-modeling/data_modeling.md)
* Start steering Zoë — [Context Surfaces](../core-concepts/context-surfaces.md)
* Fix specific errors — [Fixing Zoë's Mistakes](../core-concepts/fixing-zoes-mistakes.md)

As always, feel free to reach out to your Zenlytic contact or [email support](mailto:support@zenlytic.com) if anything here doesn't match what you're seeing.
