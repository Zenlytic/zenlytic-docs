---
description: >-
  Connect Zoë to Google's BigQuery MCP server to inspect schemas and run SQL
  from chat.
---

# Google

Connect Zoë to [Google's BigQuery remote MCP server](https://docs.cloud.google.com/bigquery/docs/use-bigquery-mcp) — a Google-hosted MCP endpoint at `https://bigquery.googleapis.com/mcp` that exposes BigQuery metadata and SQL execution as MCP tools — so she can explore datasets and run SQL in natural language. Zenlytic acts as an MCP client and forwards a Google Cloud OAuth 2.0 access token to the server on every call, so Zoë's actions inherit the underlying IAM identity's BigQuery permissions. Authenticate with a static `Authorization` header.

> If you only need BigQuery as a data warehouse for the Zenlytic semantic layer, follow [BigQuery setup](../data-sources/bigquery_setup.md) instead. MCP is purpose-built for agentic, on-demand access from Zoë.

## What Zoë can access

Through the BigQuery remote MCP server, Zoë can:

* List projects, datasets, and tables visible to the connected identity.
* Inspect dataset and table schemas, including column types and descriptions.
* Run ad-hoc SQL with `execute_sql` (read/write) and `execute_sql_readonly` (read-only — blocks DML, DDL, and Python UDFs).

Tool calls run as the IAM identity behind the access token, so Zoë can only see and query what that identity has BigQuery permissions for. Google caps results at **3,000 rows** and query time at **3 minutes**, and Drive external tables aren't supported by either SQL tool.

## Prerequisites

* **The BigQuery API enabled** on your Google Cloud project.
* **A service account (or user) with the right IAM roles** on every project Zoë should reach:
  * `[roles/mcp.toolUser](https://docs.cloud.google.com/iam/docs/roles-permissions/mcp#mcp.toolUser)` — make MCP tool calls.
  * `[roles/bigquery.jobUser](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.jobUser)` — run BigQuery jobs.
  * `[roles/bigquery.dataViewer](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataViewer)` — query data.
* **A way to mint OAuth access tokens** scoped to `https://www.googleapis.com/auth/bigquery` for that identity (see `gcloud` CLI in [Configure request headers](google.md#configure-request-headers)).
* **Zenlytic requirements.** The `mcp-client` flag enabled on your workspace and `admin` role. See the [MCP overview](overview.md) for the full list.

## Set up the connection in Zenlytic

1. Open **Workspace Settings → Extensions → MCP** and click **Add Connection**.
2. Fill out the form:

* **Name** — a label that will appear in the chat tool menu, for example `BigQuery`.
* **URL** — `https://bigquery.googleapis.com/mcp`.

3. Add the `Authorization` header (see [Configure request headers](google.md#configure-request-headers)).
4. Click **Test Connection**. Zenlytic opens an MCP session against the server and lists the tools it advertises.
5. Review the tool list and toggle off any tools Zoë shouldn't be able to call.
6. Click **Add Connection** to save.

## Configure request headers

| Header          | Value                                                                                            |
| --------------- | ------------------------------------------------------------------------------------------------ |
| `Authorization` | `Bearer YOUR_GCP_ACCESS_TOKEN`. Include the `Bearer` scheme and a single space before the token. |

BigQuery requires an IAM principal, so the MCP server only accepts OAuth 2.0 bearer tokens — API keys are not supported. For the full set of supported authentication methods, see Google's [Authenticate to Google and Google Cloud MCP servers](https://docs.cloud.google.com/mcp/authenticate-mcp) guide.

### Use your user identity (testing)

For local development and testing, authenticate as yourself with [Application Default Credentials](https://docs.cloud.google.com/mcp/authenticate-mcp#user_credentials_and_adc_for_mcp_servers), then print an access token:

```bash
gcloud auth application-default login
gcloud auth print-access-token --scopes=https://www.googleapis.com/auth/bigquery
```

Tool calls made with this token are attributed to your user account and inherit your permissions.

### Use an agent identity (production)

For production, Google recommends a dedicated [agent identity](https://docs.cloud.google.com/mcp/authenticate-mcp#agent_identity) — either a service account or an OAuth client — so the agent's actions are observable and permissioned independently of any individual user. To mint a token by impersonating a service account from the `gcloud` CLI:

```bash
gcloud auth print-access-token \
  --impersonate-service-account=YOUR_SA@YOUR_PROJECT.iam.gserviceaccount.com \
  --scopes=https://www.googleapis.com/auth/bigquery
```

Google access tokens expire after **one hour**. Header values are masked in the Zenlytic UI and encrypted at rest.

## Use the connection in chat

Once the connection has at least one selected tool, it appears in the chat tool menu. Toggle it on for any conversation where you want Zoë to have access to BigQuery.

A few tips:

* **Be specific about projects and datasets.** Including the full project ID and dataset name produces more reliable SQL than vague references. For example: "List the tables in dataset `analytics` in project `my-project-id`."
* **Mind the row and time caps.** Query results are capped at 3,000 rows and 3-minute execution time. Ask Zoë to add `LIMIT`s, `WHERE` filters, or aggregations for anything that would scan large tables.
* **Prefer `execute_sql_readonly` for production setups.** It blocks DML, DDL, and Python UDFs. To enforce this at the platform level, restrict access to the writable `execute_sql` tool with an [IAM deny policy](https://docs.cloud.google.com/mcp/control-mcp-use-iam#deny_read-write_mcp_tool_use).

## Troubleshooting

* `**401 Unauthorized` from BigQuery:\*\* The access token is missing, malformed, or expired (tokens last one hour). Mint a fresh one with `gcloud auth print-access-token` and replace the `Authorization` value.
* `**Permission denied` on a specific dataset:\*\* The identity behind the token is missing `roles/bigquery.dataViewer` (or equivalent) on that dataset. Grant it in Google Cloud IAM and try again.
* `**MCP tool calls not allowed`:\*\* The identity is missing `roles/mcp.toolUser`. Grant the role at the project level.
* **Query results look truncated:** You're hitting the 3,000-row cap. Ask Zoë to filter or aggregate further.
* **Drive external tables fail:** Known limitation — `execute_sql` and `execute_sql_readonly` don't support querying Google Drive external tables.
