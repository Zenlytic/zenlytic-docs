# Tableau MCP integration

Connect Zoë to a self-hosted [Tableau MCP server](https://github.com/tableau/tableau-mcp) so she can browse Tableau content and query data sources in natural language, right inside Zenlytic. Zenlytic acts as an MCP client and forwards your Tableau credentials to the server on every call, so Zoë's actions inherit the underlying Tableau identity's permissions. Authenticate with a Tableau Personal Access Token (PAT) or a static `Authorization` header.

## What Zoë can access

Through the Tableau MCP server, Zoë can:

- List and inspect workbooks, views, and projects on your Tableau Server site.
- Discover published data sources, browse their schemas, and execute queries via VizQL Data Service.
- Read metadata (descriptions, tags, lineage) from Tableau's Metadata API.

The exact tool surface depends on your Tableau MCP server's configuration. You can further narrow what Zoë sees with per-tool toggles in the Zenlytic connection modal.

## Prerequisites

- **A deployed Tableau MCP server with a public HTTPS URL.** Follow Tableau's [deployment guide for Tableau Server customers](https://github.com/tableau/tableau-mcp/blob/main/docs/getting-started.md) to install and expose the server. The endpoint typically ends in `/tableau-mcp` (for example, `https://tableau-mcp.example.com/tableau-mcp`).
- **Credentials to call the server.** Either a Tableau [Personal Access Token](https://help.tableau.com/current/server/en-us/security_personal_access_tokens.htm) (PAT) or a static credential expected by a proxy in front of your MCP server. See [Configure request headers](#configure-request-headers).
- **Zenlytic requirements.** The `mcp-client` flag enabled on your workspace and `admin` role. See the [MCP overview](overview.md) for the full list.

## Set up the connection in Zenlytic

1. Open **Workspace Settings → Extensions → MCP** and click **Add Connection**.
2. Fill out the form:
   - **Name** — a label that will appear in the chat tool menu, for example `Tableau`.
   - **URL** — the full HTTPS endpoint of your Tableau MCP server, including the `/tableau-mcp` path.
3. Add credentials (see [Configure request headers](#configure-request-headers)).
4. Click **Test Connection**. Zenlytic opens an MCP session against the server and lists the tools it advertises.
5. Review the tool list and toggle off any tools Zoë shouldn't be able to call.
6. Click **Add Connection** to save.

## Configure request headers

Pick the path that matches your setup. Header values are masked in the Zenlytic UI and encrypted at rest.

### Option 1: Personal Access Token (PAT)

Use this when your Tableau MCP server is configured with passthrough authentication (`ENABLE_PASSTHROUGH_AUTH=true`). Zenlytic forwards a Tableau session token on every call, which the MCP server uses to talk to Tableau's REST APIs as you.

1. Create a PAT in Tableau, following [Personal Access Tokens — Tableau](https://help.tableau.com/current/server/en-us/security_personal_access_tokens.htm).
2. Sign into the Tableau REST API once with that PAT (`POST /api/{version}/auth/signin`) and copy the `token` returned in the response.
3. Add the header below in Zenlytic:

| Header | Value |
| --- | --- |
| `X-Tableau-Auth` | The session token from step 2. |

Session tokens expire after a few hours of inactivity. When that happens, sign in again and overwrite the header value, or stand up a small proxy in front of the MCP server that refreshes the token automatically.

### Option 2: Authorization header

Use this when your Tableau MCP server sits behind a reverse proxy, gateway, or other auth layer that issues its own credentials.

| Header | Value |
| --- | --- |
| `Authorization` | The credential your proxy expects, exactly as it expects it. For example: `Bearer YOUR_PROXY_KEY`. |

## Use the connection in chat

Once the connection has at least one selected tool, it appears in the chat tool menu. Toggle it on for any conversation where you want Zoë to have access to Tableau.

A few tips:

- **Be specific about content.** Naming the workbook, view, project, or data source explicitly produces more reliable tool calls than vague prompts.
- **Scope at the server when you can.** Tableau MCP's `INCLUDE_*` and `EXCLUDE_*` environment variables (such as `INCLUDE_PROJECT_IDS` and `INCLUDE_DATASOURCE_IDS`) narrow the tool surface upstream. Refresh the connection in Zenlytic after you change them.
- **Permissions follow the underlying identity.** Whichever Tableau identity authenticates the request is the one Zoë sees the world through — not the Zenlytic user asking the question.

## Troubleshooting

- **`401 Unauthorized`:** The credentials are missing, malformed, or expired. For Option 1, sign into the Tableau REST API again and replace the `X-Tableau-Auth` value. For Option 2, double-check the `Authorization` value matches what your proxy expects.
- **`Authorization required. Use OAuth 2.1 flow.`** The Tableau MCP server has OAuth enabled and won't accept static-header calls. Reconfigure the server with `DANGEROUSLY_DISABLE_OAUTH=true`, or front it with a proxy that handles the OAuth handshake.
- **`Method not allowed`:** Expected if you open the URL in a browser — the server only accepts `POST`. If it shows up during **Test Connection**, verify the URL ends in `/tableau-mcp`.
- **Tools changed after a server upgrade:** Open the connection, click **Refresh Tools**, review the new set of tools, and **Save Changes**.