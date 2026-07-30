---
description: >-
  Connect Zoë to Snowflake's MCP server to query Cortex tools, SQL, and custom
  functions from chat.
---

# Snowflake

Connect Zoë to a [Snowflake-managed MCP server](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp) — a server object you create directly inside your Snowflake account — so she can query Cortex Analyst semantic views, search Cortex Search services, run SQL, invoke Cortex Agents, and call your own UDFs or stored procedures, all without leaving Zenlytic. Authenticate with a static `Authorization` header containing a Snowflake [Programmatic Access Token](https://docs.snowflake.com/en/user-guide/programmatic-access-tokens) (PAT).

## What Zoë can access

A Snowflake MCP server only exposes the tools you list in its specification when you create it. Depending on what you configure, Zoë can:

* **Cortex Analyst** — ask natural-language questions against a [semantic view](https://docs.snowflake.com/en/user-guide/views-semantic/overview); Snowflake returns the generated SQL and results.
* **Cortex Search** — query a Cortex Search Service over your unstructured data (documents, tickets, product catalogs).
* **SQL execution** — run ad-hoc SQL against the warehouse you configure on the tool.
* **Cortex Agents** — invoke a Cortex Agent that orchestrates multiple Snowflake capabilities behind a single tool call.
* **Custom UDFs and stored procedures** — expose any Python (or other) UDF or stored procedure in your account as a tool, with a typed input schema.

Every tool call runs as the Snowflake role attached to the PAT, so Zoë's permissions in Snowflake are whatever that role can see and do.

## Prerequisites

Before you start, confirm the following:

* A **Snowflake account** in a [supported region](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp) (the MCP server is generally available but **not supported in government regions**).
* An identity with **`CREATE MCP SERVER`** on the database/schema where you'll put the server, and the privileges below on each underlying object you want to expose (Cortex Search Service, semantic view, agent, UDF, or stored procedure).
* A **dedicated Snowflake role** scoped to the **least-privileged** set of grants Zoë needs. You'll attach this role to the PAT.
* A **warehouse** that has the privileges to run any SQL-execution or UDF/procedure tools you plan to expose.
* **Zenlytic requirements.** The `mcp-client` flag enabled on your workspace and `admin` role. See the [MCP overview](overview.md) for the full list.

## Create the MCP server in Snowflake

The MCP server is a first-class Snowflake object. You define which tools it exposes in a YAML specification, then create it with SQL. MCP clients (including Zenlytic) discover and invoke those tools through the server's HTTPS endpoint.

### Pick which tools to expose

Snowflake supports five tool types in an MCP server specification:

| Type                          | Use it to expose...                                                                                          |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------ |
| `CORTEX_ANALYST_MESSAGE`      | A semantic view, queried with natural language. Semantic **views** only — semantic models are not supported. |
| `CORTEX_SEARCH_SERVICE_QUERY` | A Cortex Search Service.                                                                                     |
| `SYSTEM_EXECUTE_SQL`          | Ad-hoc SQL execution against a configured warehouse.                                                         |
| `CORTEX_AGENT_RUN`            | A Cortex Agent.                                                                                              |
| `GENERIC`                     | A user-defined function or stored procedure, with an explicit input schema.                                  |

### Create the server

Run the following in a worksheet from a role that has `CREATE MCP SERVER` on the target schema. The example exposes one Cortex Search service and one Cortex Analyst semantic view:

```sql
CREATE OR REPLACE MCP SERVER zenlytic_mcp
  FROM SPECIFICATION $$
    tools:
      - name: "product-search"
        type: "CORTEX_SEARCH_SERVICE_QUERY"
        identifier: "ANALYTICS.SEARCH.PRODUCT_SEARCH_SVC"
        description: "Cortex Search service for all products."
        title: "Product Search"

      - name: "revenue-semantic-view"
        type: "CORTEX_ANALYST_MESSAGE"
        identifier: "ANALYTICS.SEMANTIC.REVENUE_VIEW"
        description: "Semantic view for all revenue tables."
        title: "Revenue semantic view"
  $$;
```

Add additional tools to the same `tools:` list as needed. A few common configurations:

```yaml
# SQL execution against a specific warehouse.
- title: "SQL Execution Tool"
  name: "sql_exec_tool"
  type: "SYSTEM_EXECUTE_SQL"
  description: "Execute SQL queries against the connected Snowflake database."
  config:
    read_only: true
    query_timeout: 600
    warehouse: "ZENLYTIC_WH"

# Cortex Agent.
- title: "Sales Agent"
  name: "sales_agent"
  type: "CORTEX_AGENT_RUN"
  identifier: "ANALYTICS.AGENTS.SALES_AGENT"
  description: "Agent that answers sales-pipeline questions."

# Python UDF, exposed as a tool with a typed input schema.
- title: "Multiply by ten"
  name: "multiply_by_ten"
  identifier: "ANALYTICS.AGENTS.MULTIPLY_BY_TEN"
  type: "GENERIC"
  description: "Multiplies the input value by ten."
  config:
    type: "function"
    warehouse: "ZENLYTIC_WH"
    input_schema:
      type: "object"
      properties:
        x:
          description: "A number to be multiplied by ten."
          type: "number"
```

For the full reference — including stored-procedure examples and a worked end-to-end specification — see [Snowflake's MCP server documentation](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp).

### Grant access to the role on the PAT

The role attached to your PAT (see [Generate a Programmatic Access Token](snowflake.md#generate-a-programmatic-access-token)) needs `USAGE` on the MCP server **and** the underlying privilege on every tool you exposed. Granting access to the server alone is not enough — Snowflake checks each tool individually.

| Privilege | Object                  | Why                                                                           |
| --------- | ----------------------- | ----------------------------------------------------------------------------- |
| `USAGE`   | MCP server              | Connect with the server and discover tools.                                   |
| `USAGE`   | Cortex Search Service   | Invoke a `CORTEX_SEARCH_SERVICE_QUERY` tool.                                  |
| `SELECT`  | Semantic view           | Invoke a `CORTEX_ANALYST_MESSAGE` tool.                                       |
| `USAGE`   | Cortex Agent            | Invoke a `CORTEX_AGENT_RUN` tool.                                             |
| `USAGE`   | UDF or stored procedure | Invoke a `GENERIC` tool.                                                      |
| `USAGE`   | Warehouse               | Run any `SYSTEM_EXECUTE_SQL` or `GENERIC` tool that specifies that warehouse. |

For example:

```sql
GRANT USAGE ON MCP SERVER analytics.public.zenlytic_mcp TO ROLE zenlytic_mcp_role;
GRANT USAGE ON CORTEX SEARCH SERVICE analytics.search.product_search_svc TO ROLE zenlytic_mcp_role;
GRANT SELECT ON SEMANTIC VIEW analytics.semantic.revenue_view TO ROLE zenlytic_mcp_role;
GRANT USAGE ON WAREHOUSE zenlytic_wh TO ROLE zenlytic_mcp_role;
```

### Inspect or update the server

```sql
SHOW MCP SERVERS IN SCHEMA analytics.public;
DESCRIBE MCP SERVER analytics.public.zenlytic_mcp;
```

To change the tool list, re-run `CREATE OR REPLACE MCP SERVER` with the updated specification. To remove the server, run `DROP MCP SERVER analytics.public.zenlytic_mcp;`.

## Generate a Programmatic Access Token

PATs replace passwords for programmatic access to Snowflake. Each PAT is tied to a single Snowflake user and a single role, which is the role Zoë will run as in Snowflake.

1. In Snowsight, open **Admin → Users & Roles → Users** and select the dedicated service user you want Zoë to run as (create one if you don't have one). Avoid using a personal user account so you can rotate or revoke Zoë's access independently.
2. Open the **Programmatic access tokens** tab and click **Generate new token**.
3. Set the token's **Role** to the least-privileged role you granted MCP access to above — for example, `ZENLYTIC_MCP_ROLE`. Do not use `ACCOUNTADMIN` or other broadly-privileged roles.
4. Set an expiration that matches your rotation policy.
5. Copy the generated token immediately — Snowflake only shows it once. Store it in your secrets manager.

For details and CLI options, see [Snowflake's Programmatic Access Token guide](https://docs.snowflake.com/en/user-guide/programmatic-access-tokens).

## Set up the connection in Zenlytic

1. Open **Workspace Settings → Extensions → MCP** and click **Add Connection**.
2. Fill out the form:

* **Name** — a label that will appear in the chat tool menu, for example `Snowflake (prod)`.
*   **URL** — the MCP server endpoint for the server you created, in the format:

    ```
    https://<account_url>/api/v2/databases/<database>/schemas/<schema>/mcp-servers/<server_name>
    ```

    For example: `https://acme-analytics.snowflakecomputing.com/api/v2/databases/ANALYTICS/schemas/PUBLIC/mcp-servers/ZENLYTIC_MCP`. See Snowflake's [account identifiers guide](https://docs.snowflake.com/en/user-guide/admin-account-identifier) for the right host format. Must use `https://`.

    > **Use hyphens, not underscores, in the hostname.** Snowflake's MCP server has connection issues with hostnames that contain underscores. If your account identifier contains an underscore, use the hyphenated form (for example `acme-analytics`, not `acme_analytics`).

3. Add the required headers (see [Configure request headers](snowflake.md#configure-request-headers)).
4. Click **Test Connection**. Zenlytic opens an MCP session against your Snowflake server and lists the tools it advertises.
5. Review the tool list and toggle off any tools Zoë shouldn't be able to call. Newly-discovered tools are pre-selected.
6. Click **Add Connection** to save.

## Configure request headers

Add the following in the **Headers** section of the Zenlytic connection modal. Header values are masked in the UI and encrypted at rest.

| Header                                 | Value                                                                                         |
| -------------------------------------- | --------------------------------------------------------------------------------------------- |
| `Authorization`                        | `Bearer YOUR_SNOWFLAKE_PAT`. Include the `Bearer` scheme and a single space before the token. |
| `X-Snowflake-Authorization-Token-Type` | `PROGRAMMATIC_ACCESS_TOKEN`. Tells Snowflake to validate the bearer credential as a PAT.      |

### Verify the token

Before saving the connection, sanity-check the PAT against Snowflake's REST API:

```bash
curl -X POST \
  -H "Authorization: Bearer $PAT" \
  -H "X-Snowflake-Authorization-Token-Type: PROGRAMMATIC_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}' \
  https://<account_url>/api/v2/databases/<database>/schemas/<schema>/mcp-servers/<server_name>
```

A `200` response that lists your tools means the PAT, role grants, and URL are all wired up correctly — the MCP server will accept the same credentials.

## Use the connection in chat

Once the connection has at least one selected tool, it appears in the chat tool menu. Toggle it on for any conversation where you want Zoë to have access to Snowflake. The toggle is per-conversation, so different chats can mix Snowflake with other MCP connections as needed.

A few specifics to share with your users:

* **One role, one permission set.** Every user sharing the connection sees whatever Snowflake content the PAT's role can see. If you need different access for different teams, create a separate MCP server (or reuse one) with a separate PAT scoped to a different role, and wire each up as its own Zenlytic connection.
* **Be specific in prompts.** Naming the semantic view, search service, or agent explicitly produces more reliable tool calls than vague references. For example: "Using the `revenue-semantic-view` tool, show me revenue by product category last quarter."
* **SQL execution can write.** A `SYSTEM_EXECUTE_SQL` tool with `read_only: false` lets Zoë run DML and DDL. Set `read_only: true` in the tool config (or omit the tool) unless you've explicitly decided Zoë should write to the warehouse.

## Manage the integration

* **Rotate the PAT:** In Snowsight, **Admin → Users & Roles → Users → \[your user] → Programmatic access tokens**, generate a new token, then **Edit** the connection in Zenlytic and overwrite the `Authorization` header value. Revoke the old PAT in Snowflake once you've confirmed the new one works.
* **Add or remove tools:** Re-run `CREATE OR REPLACE MCP SERVER` in Snowflake with the updated specification, grant the role any new privileges it needs, then open the connection in Zenlytic and click **Refresh Tools**.
* **Refresh tools:** If you change the MCP server's specification, the next call may fail with a "tools have changed" error. Open the connection, click **Refresh Tools**, review the new set, and **Save Changes**.
* **Adjust permissions:** Grant or revoke privileges on the role attached to the PAT in Snowflake. Changes take effect on the next request — no Zenlytic update needed.
* **Disable the integration:** Click **Delete** on the connection card to remove it immediately. Zoë stops seeing the Snowflake tools in any new conversation. For belt-and-suspenders, also drop the MCP server or revoke the PAT in Snowflake.

## Limitations

Inherited from Snowflake's MCP server:

* **Tools only.** The MCP server does not support resources, prompts, roots, notifications, version negotiation, life-cycle phases, or sampling.
* **No streaming.** Only non-streaming responses are supported.
* **Cortex Analyst uses semantic views, not models.** A `CORTEX_ANALYST_MESSAGE` tool must point at a semantic **view**.
* **Not available in government regions.**

## Troubleshoot

* **`401 Unauthorized` from Snowflake:** The PAT is missing, malformed, expired, or the `X-Snowflake-Authorization-Token-Type: PROGRAMMATIC_ACCESS_TOKEN` header is missing. Confirm the `Authorization` header is `Bearer <PAT>` (with a single space), the type header is set, and the PAT is still active in Snowsight.
* **`403 Forbidden` on a tool call:** The role attached to the PAT doesn't have the privilege required to invoke that tool (`USAGE` on the Search service or agent, `SELECT` on the semantic view, `USAGE` on the UDF/procedure or warehouse). Grant the missing privilege and retry — no Zenlytic update needed.
* **Connection times out or refuses TLS:** Confirm the account identifier in the URL uses hyphens, not underscores. Snowflake MCP endpoints have known connection issues with underscored hostnames.
* **Tool list looks short or empty:** Re-check the MCP server specification with `DESCRIBE MCP SERVER` and confirm the role on the PAT has `USAGE` on the server. The server returns only the tools the caller has privileges to see.
* **Connection works in Test Connection but fails in chat:** The MCP server's specification has likely changed since you saved. Open the connection in workspace settings and click **Refresh Tools**.
* **`Semantic model is not supported` error from a Cortex Analyst tool:** The tool's `identifier` points at a semantic model, not a semantic view. The Snowflake-managed MCP server only supports semantic views with Cortex Analyst.
