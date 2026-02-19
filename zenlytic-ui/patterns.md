---
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
---

# Patterns

{% hint style="info" %}
**Beta:** Patterns is currently in beta. During the beta period, only Snowflake connections are supported. Expanded warehouse support is in development.
{% endhint %}

Every analytical query your team has run — across dashboards, reports, and ad hoc analysis — reflects institutional knowledge about your data: trusted tables, correct joins, proper filters, and how raw columns map to business metrics.

Patterns index that query history so Zoë can use it. When the governed data model fields aren't enough to fully answer a question, Zoë searches your indexed patterns for similar SQL, adapts the best match, and uses it to generate an accurate result. Governed field definitions always take precedence — Patterns complement your data model, not replace it.

### How it works

{% stepper %}
{% step %}
### Sync

Zenlytic connects to your data warehouse and pulls recent analytical queries. Queries are normalized, deduplicated, and indexed using semantic embeddings so they can be searched by meaning, not just keyword.
{% endstep %}

{% step %}
### Search

During a conversation, when Zoë determines that the data model fields alone can't answer a question, she automatically searches the indexed patterns for similar queries. She selects the most relevant matches, adapts them to the current question, and uses them to generate SQL.
{% endstep %}
{% endstepper %}

### Where Patterns fits

Patterns, memories, and system prompts each serve a different role in shaping how Zoë answers questions.

* **Patterns** are the lowest-effort starting point — especially early in your Zenlytic setup when institutional knowledge lives implicitly in your query history rather than in a formal data model. No curation required; Zoë starts learning from SQL your team has already written. As your workspace matures, Patterns keeps filling the gaps for concepts that haven't been formalized yet.
* **Memories** are for explicit, curated knowledge — when you've seen a correct answer and want Zoë to reproduce it consistently. Best for pinning specific metric definitions or query patterns that matter enough to deliberately save.
* **System prompts** shape how Zoë behaves globally — tone, response format, and general business context that should apply to every conversation.

### Setting up Patterns

{% stepper %}
{% step %}
Go to **Settings → External Context**.
{% endstep %}

{% step %}
Under the **Query History** tab, you'll see a table of all your workspace connections.
{% endstep %}

{% step %}
Toggle on the connection(s) you want to use as a source for Patterns.
{% endstep %}

{% step %}
Click **Sync** to run the first sync for that connection.

Once a connection is enabled, Zenlytic automatically syncs new queries from that connection every 24 hours.

> **Note:** The connection role must have access to `ACCOUNT_USAGE` in Snowflake.
{% endstep %}
{% endstepper %}

### What gets synced

Zenlytic only indexes analytical queries — specifically, `SELECT` and `WITH` statements that reference tables in your workspace's data model. All other query types are filtered out during sync, including:

* DDL and DML statements (`CREATE`, `INSERT`, `UPDATE`, `DELETE`, etc.)
* Queries from ETL and data pipeline service accounts (Fivetran, Airbyte, dbt, and similar)
* Queries against system and metadata schemas (`INFORMATION_SCHEMA`, `ACCOUNT_USAGE`, etc.)
* Queries referencing staging, temporary, or dbt-intermediate tables
* Trivial or non-analytical queries (e.g. `SELECT 1`)
* Queries that don't reference any table in your data model

During the beta, Zenlytic indexes up to 10,000 query patterns per workspace. When the limit is reached, the oldest and least-frequently-run patterns are pruned automatically to make room for newer ones.

### Managing syncs

The Query History table shows the sync status and last successful sync time for each enabled connection. You can manually trigger a sync at any time by clicking **Sync** — useful after a major schema change or when you want to pull in a recent batch of queries without waiting for the next automatic sync.

Sync status options:

* **Never synced** — the connection has been enabled, but no sync has run yet.
* **Syncing** — a sync is currently in progress.
* **Last Successful Sync: \[time]** — the most recent sync completed successfully.

### How Zoë uses Patterns in chat

When Patterns is active, Zoë automatically decides when to use it — no prompting required. If she determines that the data model fields available aren't sufficient to answer the question, she searches your indexed patterns.

In the chat thread, this appears as an interactive tool call labeled **Searching for \[topic] queries and definitions**. Click it to expand and see which keywords Zoë searched for, which patterns were returned, and a plain-language description of what each query does.

Zoë then adapts the most relevant pattern — preserving the correct joins, aggregations, and filters — to match the exact question being asked.

### Limitations

<details>

<summary>View limitations</summary>

* **Beta:** Only Snowflake connections are supported during the beta period.
* **Query coverage:** Patterns is only as useful as the queries your analysts have run. If a question requires SQL that no one on your team has written before, Patterns won't have a relevant match.
* **Access-controlled:** Zoë won't surface a pattern to a user if that user doesn't have access to the fields or tables referenced in the query.
* **Capacity:** Up to 10,000 query patterns are indexed per workspace during the beta. Older and less-frequently-used patterns are pruned automatically when the limit is reached.

</details>
