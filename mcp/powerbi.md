# Power BI MCP integration

Connect Zoë to the [remote Power BI MCP server](https://learn.microsoft.com/en-us/power-bi/developer/mcp/remote-mcp-server-get-started) — Microsoft's hosted MCP endpoint for Power BI semantic models — to let her chat with your published models in natural language. The server translates Zoë's prompts into DAX queries against the semantic models you point her at, executes them, and returns results. Authenticate with a static `Authorization` header.

## What Zoë can access

Through the Power BI remote MCP server, Zoë can:

- Discover and inspect tables, columns, measures, and relationships in any Power BI semantic model the connection's identity has **Build** access to.
- Generate and execute DAX queries against those models (for example, "Show me the top 10 products by sales last quarter").
- Read AI instructions and verified answers attached to optimized semantic models, which improves query quality.

The connection is scoped to whatever the underlying Microsoft Entra identity (user or service principal) can see in your instance — Zoë never has more access than that identity does.

## Prerequisites

Before you start, confirm the following:

- **Admin enabled the instance setting.** Your Power BI admin must turn on **"Users can use the Power BI Model Context Protocol server endpoint (preview)"** in the Power BI admin portal. Without this, the endpoint refuses calls from your instance.
- **Build permissions on at least one semantic model.** The identity you authenticate with needs **Build** permission on every semantic model you want Zoë to query.
- **(Recommended) Optimized semantic models.** Follow Microsoft's guide to [prepare your semantic models for AI](https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-prepare-data-ai) — adding AI instructions and verified answers materially improves DAX generation quality.
- **Zenlytic requirements.** The `mcp-client` flag enabled on your workspace and `edit_settings` permission. See the [MCP overview](overview.md) for the full list.

## Set up the connection in Zenlytic

1. Open **Workspace Settings → Extensions → MCP** and click **Add Connection**.
2. Fill out the form:
   - **Name** — a label that will appear in the chat tool menu, for example `Power BI`.
   - **URL** — the remote Power BI MCP endpoint, either Microsoft's directly or your proxy:
     - Direct: `https://api.fabric.microsoft.com/v1/mcp/powerbi`
     - Proxy: whatever HTTPS URL your gateway exposes.
3. Add the `Authorization` header (see [Configure request headers](#configure-request-headers)).
4. Click **Test Connection**. Zenlytic opens an MCP session against the server and lists the tools it advertises.
5. Review the tool list and toggle off any tools Zoë shouldn't be able to call.
6. Click **Add Connection** to save.

## Configure request headers

Add the following in the **Headers** section of the Zenlytic connection modal. Header values are masked in the UI and encrypted at rest.

| Header | Value |
| --- | --- |
| `Authorization` | `Bearer YOUR_POWER_BI_ACCESS_TOKEN`. Include the `Bearer ` scheme and a single space before the token. If you're going through an OAuth proxy, use whatever static credential the proxy expects (for example, `Bearer YOUR_PROXY_KEY` or `X-API-Key: YOUR_PROXY_KEY`). |

## Use the connection in chat

Once the connection has at least one selected tool, it appears in the chat tool menu. Toggle it on for any conversation where you want Zoë to have access to Power BI tools.

A few specifics to share with your users:

- **You'll usually need a semantic model ID.** Most Power BI MCP tools operate on a single semantic model at a time. To query one, share the model ID with Zoë in your message — for example, "Using semantic model `00000000-1111-2222-3333-444444444444`, show me the top 10 products by sales." Find the ID in the Power BI service URL when you open the model.
- **Be specific in prompts.** The server generates DAX from natural language; questions that name tables, columns, or measures explicitly produce more reliable results than vague ones.
- **Permissions still apply.** Zoë can only see and query semantic models the connection's identity has Build access to — even if a user toggles the connection on, they won't see data they wouldn't see in Power BI directly.

## Troubleshooting

- **`401 Unauthorized` from Power BI:** The access token is missing, malformed, or expired. Confirm the `Authorization` header includes the `Bearer ` scheme with a single space, and mint a fresh token if it's been more than an hour since you last set it.
- **"Tenant setting not enabled" errors:** Your Power BI admin hasn't turned on **"Users can use the Power BI Model Context Protocol server endpoint (preview)"**. Until that's enabled, every call from your tenant is refused regardless of credentials.
- **"Insufficient permissions" on a specific semantic model:** The identity behind the token doesn't have **Build** permission on that model. Grant it in the Power BI service and try again.
- **Zoë can't find a model by name:** Share the semantic model ID explicitly in the prompt rather than relying on the name. IDs are GUIDs visible in the Power BI service URL.
- **DAX results look off:** Walk through Microsoft's [prepare your semantic models for AI](https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-prepare-data-ai) checklist — most quality issues come from missing descriptions, ambiguous measure names, or lack of verified answers on the underlying model.
