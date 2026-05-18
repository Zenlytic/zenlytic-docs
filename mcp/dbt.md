# dbt MCP integration

Connect Zoë to the [dbt remote MCP server](https://docs.getdbt.com/docs/dbt-ai/setup-remote-mcp) to let her explore your transformation layer — models, metrics, lineage, and (optionally) ad-hoc SQL — without leaving Zenlytic. This integration uses **token-based authentication** with a dbt Personal Access Token (PAT) or service token.

> For semantic-layer-specific workflows, see [dbt MetricFlow integration](../data-modeling/dbt_metricflow.md). The MCP integration covers project-wide metadata and tool execution, while the MetricFlow integration focuses on querying semantic models.

## What Zoë can access

Through the dbt remote MCP server, Zoë can call the tool surfaces dbt exposes — including the Discovery, Administrative, and Semantic Layer APIs — to:

- Look up models, sources, seeds, snapshots, and exposures defined in your dbt project.
- Read descriptions, tests, tags, and column-level documentation from your manifest.
- Query metrics, dimensions, and entities through the dbt Semantic Layer.
- Trace lineage between dbt nodes.
- Run ad-hoc SQL against your warehouse with `execute_sql` (PAT-only — see [Choose a token type](#choose-a-token-type)).

## Prerequisites

Before you start, confirm the following:

- A **dbt Cloud** account with [AI features](https://docs.getdbt.com/docs/cloud/enable-dbt-copilot) enabled.
- A **production environment** in dbt Cloud (and a **development environment** if you plan to use `execute_sql` or Fusion tools).
- A **PAT or service token** with at minimum **Semantic Layer**, **Metadata**, and **Developer** permissions.
- The `mcp-client` flag enabled on your Zenlytic workspace and `edit_settings` permission. See the [MCP overview](overview.md) for full prerequisites.

## Choose a token type

Token-based authentication accepts either a Personal Access Token or a service token. Pick based on what Zoë needs to do:


| If you need...                                           | Use...                                                                                            |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `execute_sql` (run ad-hoc warehouse queries through Zoë) | **PAT** — service tokens don't work with `execute_sql` or any tool that requires `x-dbt-user-id`. |
| Shared team setup, CI, or automation                     | **Service token** — easier to rotate and not tied to one user, but no `execute_sql`.              |
| Semantic Layer and Discovery only                        | Either works.                                                                                     |


> When using a service token, make sure it has at least the **Semantic Layer Only**, **Metadata Only**, and **Developer** permissions. PATs inherit the user's permissions; the user must have Semantic Layer and Developer access.

## Gather your dbt connection details

From your dbt Cloud account, collect:

1. **Host URL** — your dbt Cloud host, used to form the full MCP endpoint. Examples:
  - Single-tenant: `https://cloud.getdbt.com/api/ai/v1/mcp/`
  - Multi-cell: `https://ACCOUNT_PREFIX.us1.dbt.com/api/ai/v1/mcp/`
  - See [dbt's Access, Regions, & IP addresses](https://docs.getdbt.com/docs/platform/about-platform/access-regions-ip-addresses) if you're unsure.
2. **Production environment ID** — find it on the **Orchestration** page in dbt Cloud. You'll pass it as `x-dbt-prod-environment-id`.
3. **Development environment ID** — only needed for `execute_sql` and Fusion tools. Same location in dbt Cloud.
4. **User ID** — only needed for `execute_sql` and Fusion tools. See [Find your user ID](https://docs.getdbt.com/faqs/Accounts/find-user-id).
5. **Token** — generate a [PAT](https://docs.getdbt.com/docs/dbt-apis/user-tokens) or [service token](https://docs.getdbt.com/docs/dbt-apis/service-tokens) per the table above.

## Set up the connection in Zenlytic

1. Open **Workspace Settings → Extensions → MCP** and click **Add Connection**.
2. Fill out the form:
  - **Name** — a label that will appear in the chat tool menu, for example `dbt (prod)`.
  - **URL** — the full MCP endpoint, for example `https://cloud.getdbt.com/api/ai/v1/mcp/`. Must use `https://` and include the `/api/ai/v1/mcp/` path.
3. Add the required headers (see [Configure request headers](#configure-request-headers)).
4. Click **Test Connection**. Zenlytic opens an MCP session and lists the tools the dbt server advertises.
5. Review the tool list and toggle off any tools Zoë shouldn't be able to call. Newly-discovered tools are pre-selected.
6. Click **Add Connection** to save.

## Configure request headers

The dbt remote MCP server is controlled through HTTP headers. Add each one in the **Headers** section of the Zenlytic connection modal. Header values are masked in the UI and encrypted at rest.

### Required for every connection


| Header                      | Value                                                                                                                                          |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `Authorization`             | `Token YOUR_DBT_ACCESS_TOKEN` or `Bearer YOUR_DBT_ACCESS_TOKEN`. Include the scheme (`Token` or `Bearer`) and a single space before the token. |
| `x-dbt-prod-environment-id` | Your dbt production environment ID, as a number (for example `54321`).                                                                         |


### Required for `execute_sql`

Add these in addition to the headers above if you want Zoë to run SQL through dbt:


| Header                     | Value                                             |
| -------------------------- | ------------------------------------------------- |
| `x-dbt-dev-environment-id` | Your dbt development environment ID, as a number. |
| `x-dbt-user-id`            | Your dbt user ID, as a number. Requires a PAT.    |


### Required for Fusion tools

Fusion tools default to the production environment for model and table metadata. To use them, add:


| Header                       | Value                                                                                                                                                       |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `x-dbt-dev-environment-id`   | Your dbt development environment ID, as a number.                                                                                                           |
| `x-dbt-user-id`              | Your dbt user ID, as a number. Requires a PAT.                                                                                                              |
| `x-dbt-fusion-disable-defer` | Optional. Set to `true` to make Fusion tools use the development environment's models and metadata instead of deferring to production. Defaults to `false`. |


### Optional: disable specific tools or toolsets

Use these to narrow the surface dbt exposes, in addition to the per-tool toggles in the Zenlytic connection modal:


| Header                   | Value                                                                                                  |
| ------------------------ | ------------------------------------------------------------------------------------------------------ |
| `x-dbt-disable-tools`    | Comma-separated list of tool names to disable, for example `get_all_models,text_to_sql,list_entities`. |
| `x-dbt-disable-toolsets` | Comma-separated list of toolsets to disable, for example `semantic_layer,sql,discovery`.               |


> **Use numeric IDs, not full URLs.** The `x-dbt-prod-environment-id`, `x-dbt-dev-environment-id`, and `x-dbt-user-id` headers expect integers only. Pasting a full dbt URL (for example `https://cloud.getdbt.com/deploy/12345/projects/67890/environments/54321`) will cause the connection to fail.

## Use the connection in chat

Once the connection has at least one selected tool, it appears in the chat tool menu. Toggle it on for any conversation where you want Zoë to use dbt tools that turn. The toggle is per-conversation, so different chats can mix dbt with other MCP connections as needed.

## Manage the integration

- **Rotate the token:** Generate a new PAT or service token in dbt Cloud, then **Edit** the connection in Zenlytic and overwrite the `Authorization` header value. Old tokens remain valid in dbt until you revoke them there.
- **Refresh tools:** If dbt releases new tools or changes existing tool schemas, the next call fails with a "tools have changed" error. Open the connection, click **Refresh Tools**, review the diff, and **Save Changes**.
- **Disable the integration:** Click **Delete** on the connection card to remove it immediately. Zoë stops seeing the dbt tools in any new conversation.

## Troubleshoot

- `**401 Unauthorized` from dbt:** Confirm the `Authorization` header includes the scheme (`Token`  or `Bearer` ) with a single space before the token, and that the token is still active in dbt Cloud.
- `**execute_sql` is not callable:** You're authenticating with a service token. Switch the `Authorization` header to a PAT and add `x-dbt-user-id` and `x-dbt-dev-environment-id`.
- **"Invalid environment" errors:** Make sure the environment ID headers contain numeric IDs only, not full dbt URLs.
- **Tool list looks short:** Check the `x-dbt-disable-tools` and `x-dbt-disable-toolsets` headers — they remove tools before Zenlytic ever sees them. Per-tool toggles in the Zenlytic UI act on top of whatever dbt returns.
- **Connection works in Test Connection but fails in chat:** dbt's tool surface has likely changed since you saved. Open the connection in workspace settings and click **Refresh Tools**.

