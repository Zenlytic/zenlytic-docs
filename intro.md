# Zenlytic Documentation

Zenlytic is a business intelligence platform where a conversational AI analyst — **Zoë** — answers questions against your data model. These docs cover how to set Zenlytic up, how to steer Zoë's answers, and how to embed the experience in your own applications.

## Pick your path

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>New and setting up</strong></td><td>Connect your warehouse, import your first tables, and ask Zoë a question.</td><td><a href="getting-started/start_here.md">start_here.md</a></td></tr><tr><td><strong>Zoë got something wrong</strong></td><td>Diagnose what went wrong and add the smallest piece of context that fixes it.</td><td><a href="core-concepts/fixing-zoes-mistakes.md">fixing-zoes-mistakes.md</a></td></tr><tr><td><strong>Learning the app</strong></td><td>A tour of Zenlytic's UI — chats, skills, dashboards, attachments, exploring.</td><td><a href="zenlytic-ui/using_zenlytic.md">using_zenlytic.md</a></td></tr><tr><td><strong>Embedding Zenlytic</strong></td><td>Put Zenlytic inside your own product with signed embedding and custom styling.</td><td><a href="embedding/embedding_overview.md">embedding_overview.md</a></td></tr><tr><td><strong>Managing permissions</strong></td><td>Configure user roles, access grants, and workspace-level permissions.</td><td><a href="zenlytic-ui/user_roles.md">user_roles.md</a></td></tr></tbody></table>

## Core concepts

If you're here to understand how Zenlytic works at a conceptual level:

* [Context Surfaces](core-concepts/context-surfaces.md) — where context lives (system prompt, skills, descriptions, synonyms) and when Zoë sees each one.
* [Progressive Enrichment](core-concepts/progressive-enrichment.md) — what to configure first, and why "import-then-iterate" beats "build-everything-up-front."
* [Fixing Zoë's Mistakes](core-concepts/fixing-zoes-mistakes.md) — a diagnostic router from observed errors to targeted fixes.

## Reference by area

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Data Modeling</strong></td><td>Models, views, fields, relationships, and the full YAML reference.</td><td><a href="data-modeling/data_modeling.md">data_modeling.md</a></td></tr><tr><td><strong>Tips &#x26; Tricks</strong></td><td>Practical guidance for steering Zoë — descriptions, synonyms, entity drills.</td><td><a href="tips-and-tricks/zoe_tips_and_tricks.md">zoe_tips_and_tricks.md</a></td></tr><tr><td><strong>Proactive Analytics</strong></td><td>Proactive Agents — Zenlytic's scheduled, agentic reporting layer.</td><td><a href="proactive-analytics/getting-started.md">getting-started.md</a></td></tr><tr><td><strong>Data Sources</strong></td><td>Warehouse setup for Snowflake, BigQuery, Redshift, Databricks, and more.</td><td><a href="data-sources/integrations.md">integrations.md</a></td></tr><tr><td><strong>Authentication &#x26; Security</strong></td><td>SSO, IP whitelisting, deploy keys, and troubleshooting.</td><td><a href="authentication-and-security/microsoft_entra_zenlytic.md">microsoft_entra_zenlytic.md</a></td></tr><tr><td><strong>Legal &#x26; Support</strong></td><td>Zenlytic's support policy, ToS, DPA, and subprocessors.</td><td><a href="legal-and-support/customer-support-policy.md">customer-support-policy.md</a></td></tr></tbody></table>

As always, feel free to reach out to your Zenlytic contact or [email Zenlytic Support](mailto:support@zenlytic.com) if you have questions that aren't answered in the documentation.
