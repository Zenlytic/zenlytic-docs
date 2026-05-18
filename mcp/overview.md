# MCP overview

The [Model Context Protocol](https://modelcontextprotocol.io) (MCP) is an open standard for exposing tools to LLM-powered agents like Zoë. Zenlytic acts as an **MCP client**: point Zoë at a compatible remote MCP server, and the tools that server advertises become available alongside Zoë's native ones. When enabled, Zoë can then pull data and trigger workflows from external systems directly from the Zenlytic chat experience.

## What you can do with MCP

- Pull live metadata, schemas, and lineage from your data warehouse or transformation layer.
- Read workbook, dataset, and report context from your BI tools so Zoë can ground answers in published assets.
- Expose internal APIs and operational workflows to Zoë through your own MCP server, with per-tool control over what she can call.
- Mix and match connections per conversation, so different chats can pull from different combinations of systems.

## How MCP works in Zenlytic

At a high level, every connection follows the same lifecycle:

1. **Add the server.** You register the server's HTTPS endpoint (and any authentication headers) in workspace settings.
2. **Discover tools.** Zenlytic opens an MCP session, calls `tools/list`, and stores a snapshot of the discovered tools — names, descriptions, and JSON schemas — in your workspace.
3. **Select tools.** You can toggle individual tools on or off. Only enabled tools are exposed to Zoë; deselected tools are never described to the model.
4. **Use in chat.** From the chat tool menu, toggle the connection on per message. Zoë sees the enabled tools alongside her native ones for the rest of the conversation.
5. **Call tools.** When Zoë invokes one of your tools, Zenlytic forwards a `tools/call` request to your server, captures the response, and feeds the result back into the conversation.

## Available integrations

Use the following setup guides to connect Zoë to popular tools via their existing MCP servers:

- [Tableau](tableau.md) — read workbook, view, and data source metadata.
- [Power BI](powerbi.md) — connect to workspaces, datasets, and reports.
- [BigQuery](bigquery.md) — query tables and inspect schemas directly.
- [dbt](dbt.md) — explore models, metrics, exposures, and lineage.

These guides are experimental and intended for early testing. You can also bring your own MCP server. Any server that implements the streamable HTTP transport for protocol version `2025-03-26` and exposes `initialize`, `tools/list`, and `tools/call` will work.

## Before you begin

To connect any MCP server, confirm the following:

| Requirement | Detail |
| --- | --- |
| **Deployment** | Outbound MCP connections are available on **Zenlytic-hosted** deployments. Self-hosted and on-prem deployments cannot currently make outbound MCP requests. |
| **Feature flag** | The `mcp-client` flag must be enabled for your workspace. If you don't see an **MCP** entry under **Workspace Settings → Extensions**, ask your Zenlytic contact to enable it. |
| **Workspace permission** | You need `edit_settings` permission to add, edit, delete, or refresh connections. Members with only `view_content` can see existing connections but can't modify them. |
| **A reachable server** | Your server (or the vendor's) must be publicly reachable over HTTPS from Zenlytic's infrastructure. Plain `http://` URLs are rejected at save time. |
| **Credentials** | Most production servers require authentication. Have a bearer token, API key, or other static credential ready — we pass these through as custom request headers on every call. |

## Get started

1. Open **Workspace Settings → Extensions → MCP** in Zenlytic.
2. To connect one of the tools listed above, follow the linked experimental setup guide.
3. To connect a custom server, click **Add Connection**, fill in the name, HTTPS endpoint, and any authentication headers, then click **Test Connection**.
4. Review the discovered tools and toggle off any that Zoë shouldn't be able to call.
5. Click **Add Connection** to save.

Once a connection is active, open any chat, toggle the connection on from the tool menu, and ask Zoë a question that uses it. You can manage, rotate credentials, refresh tools, or delete any MCP connection at any time from the same settings page.
