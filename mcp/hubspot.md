# HubSpot MCP integration

Connect Zoë to a self-hosted HubSpot MCP server — backed by HubSpot's official [`@hubspot/mcp-server`](https://www.npmjs.com/package/@hubspot/mcp-server) package and a HubSpot [Private App](https://developers.hubspot.com/docs/guides/apps/private-apps/overview) access token — so she can read and update CRM records, activities, and content directly from Zenlytic chats. The server holds your Private App token and proxies Zoë's calls to HubSpot's REST APIs. Authenticate the Zenlytic → server hop with a static `Authorization` header.

> HubSpot also runs an official hosted remote MCP server at `https://mcp.hubspot.com`. That endpoint only accepts [OAuth 2.1 with PKCE](https://developers.hubspot.com/docs/apps/developer-platform/build-apps/integrate-with-the-remote-hubspot-mcp-server), which Zenlytic doesn't yet implement as an MCP client. Until OAuth is supported, the self-hosted path below is the way in. OAuth support is on the roadmap.

## What Zoë can access

Through the official HubSpot MCP server, Zoë can:

- Read **CRM records:** contacts, companies, deals, tickets, line items, products, quotes, orders, invoices, carts, subscriptions, segments (lists), and users.
- Read **activities:** calls, emails, meetings, notes, and tasks.
- Read **content and marketing:** blog posts, landing pages, site pages, campaigns, and marketing events.
- Write to **CRM records** (contacts, companies, deals, tickets, line items, products) and **activities** (calls, emails, meetings, notes, tasks).

Every tool call respects the scopes you grant the Private App. Granting only read scopes is the safest starting point — add write scopes when you decide Zoë should be able to update records.

> **Sensitive Data:** If your HubSpot account has [Sensitive Data](https://developers.hubspot.com/docs/api-reference/latest/crm/properties/sensitive-data) turned on, activity objects (calls, emails, meetings, notes, tasks) are blocked from MCP access by HubSpot. This restriction is specific to MCP and doesn't apply to standard CRM APIs.

## Prerequisites

Before you start, confirm the following:

- A **HubSpot account** where you can create a Private App. Private Apps require **Super Admin** access by default.
- Infrastructure to **host an MCP server** with a public HTTPS URL — typically a container platform (Cloud Run, ECS, Fly.io, Render, Railway, etc.) and a way to terminate TLS.
- A way to **mint or pre-share a credential** that the reverse proxy in front of your MCP server will validate on every request. The HubSpot MCP server itself doesn't authenticate inbound requests — you must front it with an auth layer or restrict ingress.
- **Zenlytic requirements.** The `mcp-client` flag enabled on your workspace and `admin` role. See the [MCP overview](overview.md) for the full list.

## Create a HubSpot Private App

A Private App gives you a long-lived access token (`pat-...`) scoped to a single HubSpot account. The MCP server uses this token to call HubSpot's REST APIs as your selected scopes.

1. In HubSpot, open **Settings → Integrations → Private Apps** and click **Create a private app**.
2. On the **Basic Info** tab, give the app a descriptive name (for example, `zenlytic-zoe-mcp`) and a short description.
3. On the **Scopes** tab, enable the **minimum** scopes Zoë needs. A read-only starting point for CRM and activities looks like this:
  - `crm.objects.contacts.read`
  - `crm.objects.companies.read`
  - `crm.objects.deals.read`
  - `crm.objects.line_items.read`
  - `crm.schemas.contacts.read` (and the matching `*.schemas.*` reads for any objects above)
  - `tickets` (read tickets — HubSpot exposes a single combined scope)
  - `sales-email-read` (read sales emails)
  - `content` (read content and marketing assets — required if you want Zoë to look at blog posts, pages, campaigns, or events)

  Add write equivalents (`*.write`) only for the objects you want Zoë to update.
4. Click **Create app** and confirm the warning dialog.
5. On the app details page, open the **Auth** tab and copy the **Access token** (starts with `pat-na1-...`). HubSpot only shows it in plain text once — store it in your secrets manager.

> **Use a dedicated Private App, not a personal one.** Tie the app to a clearly-named service entry so you can rotate or revoke Zoë's access independently of any human user.

## Deploy a HubSpot MCP server

HubSpot publishes [`@hubspot/mcp-server`](https://www.npmjs.com/package/@hubspot/mcp-server) — the official MCP server backed by your Private App token — but it ships with **stdio transport only**, intended for local clients like Claude Desktop. Zenlytic connects over HTTPS, so you need a thin layer that exposes the server over **streamable HTTP**. Two pragmatic options:

- **Wrap the official package yourself** — run `@hubspot/mcp-server` behind a small HTTP server (Hono, Express, or the MCP TypeScript SDK's [`StreamableHTTPServerTransport`](https://github.com/modelcontextprotocol/typescript-sdk)) on the platform of your choice. Pass the Private App token in via the `PRIVATE_APP_ACCESS_TOKEN` environment variable. This is the most maintainable long-term path because you stay current with HubSpot's official release.
- **Use a community wrapper.** Containers like [`sanketskasar/hubspot-mcp-server`](https://github.com/sanketskasar/hubspot-mcp-server) bundle the official package with an HTTP / streamable-HTTP transport out of the box. Treat any community wrapper as third-party code: pin a known-good image digest, review changes before upgrading, and don't grant scopes you wouldn't grant the maintainer's source.

Whichever you pick, the deployment shape is the same:

1. Build (or pull) a container that runs the server with **streamable HTTP** transport, listening on a port of your choice (`3000` is conventional). Pass these environment variables:
  - `PRIVATE_APP_ACCESS_TOKEN` (or `HUBSPOT_PRIVATE_APP_ACCESS_TOKEN`, depending on the package) — your `pat-...` token.
  - `TRANSPORT=streamable-http` (or the equivalent flag for your wrapper).
2. Deploy the container behind **HTTPS**. Cloud Run, ECS-with-ALB, Fly.io, Render, and Railway all terminate TLS for you.
3. Put a **reverse proxy or platform auth check in front of the MCP endpoint**, validating a static credential on every request. Without this, anyone who can reach the HTTPS URL can use Zoë's HubSpot Private App. The simplest setups are:
  - **Bearer-token check.** Configure the proxy (Cloud Run service auth, an API gateway, Nginx, Cloudflare Worker, etc.) to require `Authorization: Bearer <SHARED_SECRET>` and reject anything else. Generate a long random secret and treat it like a password.
  - **Platform-native auth.** Cloud Run's Google identity tokens, AWS IAM-signed requests, or Cloudflare Access Service Tokens all work. Match whatever you already use for internal services.
4. Note the final HTTPS URL Zenlytic will hit, including the MCP path (typically `/mcp` or `/`). You'll paste it into the connection in the next step.

> **The Private App token never leaves your infrastructure.** It lives only in the MCP server's environment. The credential Zenlytic sends is the proxy's static secret, not the HubSpot token — rotate them independently.

## Set up the connection in Zenlytic

1. Open **Workspace Settings → Extensions → MCP** and click **Add Connection**.
2. Fill out the form:
  - **Name** — a label that will appear in the chat tool menu, for example `HubSpot (prod)`.
  - **URL** — the full HTTPS endpoint of your MCP server, including the path, for example `https://hubspot-mcp.example.com/mcp`. Must use `https://`.
3. Add the `Authorization` header (see [Configure request headers](#configure-request-headers)).
4. Click **Test Connection**. Zenlytic opens an MCP session against your server and lists the tools the HubSpot package advertises.
5. Review the tool list and toggle off any tools Zoë shouldn't be able to call — for example, you may want to disable write tools (object create/update) for read-only workflows. Newly-discovered tools are pre-selected.
6. Click **Add Connection** to save.

## Configure request headers

Add the following in the **Headers** section of the Zenlytic connection modal. Header values are masked in the UI and encrypted at rest.

| Header          | Value                                                                                                                            |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `Authorization` | The credential your reverse proxy expects, exactly as it expects it. For example, `Bearer YOUR_PROXY_SHARED_SECRET`. |

Do **not** put the HubSpot Private App token (`pat-na1-...`) in the `Authorization` header — that token lives only inside the MCP server's environment, and Zenlytic doesn't forward it to HubSpot directly. Sending it as a Bearer token to HubSpot's API works, but is irrelevant to the self-hosted MCP path documented here.

If you fronted the server with platform-native auth (Cloud Run identity tokens, AWS Sigv4, Cloudflare Access tokens), follow the matching token-minting steps for that platform. The pattern is the same as the [Looker MCP integration](looker.md#configure-request-headers) — mint a token, paste it as the `Authorization` value, and refresh it when it expires.

## Use the connection in chat

Once the connection has at least one selected tool, it appears in the chat tool menu. Toggle it on for any conversation where you want Zoë to use HubSpot tools. The toggle is per-conversation, so different chats can mix HubSpot with other MCP connections as needed.

A few specifics to share with your users:

- **One Private App, one permission set.** Every user sharing the connection sees whatever HubSpot data the Private App's scopes allow. If you need different access for different teams (read-only for marketing, write for sales ops), stand up a second MCP server backed by a second Private App and wire it up as its own Zenlytic connection.
- **Be specific in prompts.** Naming the object type and properties explicitly produces more reliable tool calls. For example, "Show me the top 10 deals by amount in the `closedwon` stage created this quarter."
- **No vector search.** HubSpot's MCP server is built on the [CRM search API](https://developers.hubspot.com/docs/api-reference/latest/crm/search-the-crm), which doesn't support semantic search. Use exact-match filters, ranges, and property names rather than fuzzy descriptions.

## Manage the integration

- **Rotate the Private App token:** In HubSpot, **Settings → Integrations → Private Apps → [your app] → Auth**, click **Rotate access token**. Update the `PRIVATE_APP_ACCESS_TOKEN` environment variable on your MCP server and redeploy. The Zenlytic-side credential doesn't change.
- **Rotate the proxy credential:** Generate a new shared secret (or platform token), update the reverse proxy's allow-list, then **Edit** the connection in Zenlytic and overwrite the `Authorization` header value. Revoke the old credential on the proxy once the new one works.
- **Adjust scopes:** Edit the Private App's scopes in HubSpot, then redeploy the MCP server (some wrappers cache the scope set at startup). The HubSpot MCP server's advertised tool list adapts to the granted scopes — open the connection and click **Refresh Tools** to pick up changes.
- **Upgrade the server:** When a new version of `@hubspot/mcp-server` (or your wrapper) ships, redeploy and click **Refresh Tools** in Zenlytic to pick up any new or renamed tools.
- **Disable the integration:** Click **Delete** on the connection card to remove it immediately. Zoë stops seeing the HubSpot tools in any new conversation. For belt-and-suspenders, also revoke the Private App in HubSpot.

## Troubleshoot

- **`401 Unauthorized` from your proxy:** The `Authorization` header value doesn't match what the proxy expects. Confirm the scheme (`Bearer`, `Token`, etc.) and check for stray whitespace. If you're using a short-lived platform token (Cloud Run identity, Cloudflare Access), mint a fresh one and overwrite the header value.
- **`401 Unauthorized` or `403 Forbidden` from HubSpot (visible in MCP server logs):** The Private App's access token is wrong, rotated, or missing scopes for the call. Re-issue the token in **Settings → Integrations → Private Apps**, update the server's environment variable, and redeploy.
- **Tool list looks short:** The Private App is missing scopes. Add the read or write scopes Zoë needs in HubSpot, redeploy the server, and click **Refresh Tools** in Zenlytic.
- **Activities (calls, emails, meetings, notes, tasks) come back empty:** Your HubSpot account has [Sensitive Data](https://developers.hubspot.com/docs/api-reference/latest/crm/properties/sensitive-data) turned on, which blocks activity access through MCP. The restriction is on HubSpot's side and doesn't apply to the standard CRM APIs.
- **"No vector / semantic match" surprises:** HubSpot's MCP server uses the CRM search API, which is exact-match and property-based. Rephrase prompts with explicit property names, operators, and ranges instead of fuzzy descriptions.
- **Connection works in Test Connection but fails in chat:** The MCP server's advertised tool list has changed since you saved (most often after a `@hubspot/mcp-server` upgrade). Open the connection in workspace settings and click **Refresh Tools**.
