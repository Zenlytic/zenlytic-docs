# Atlan MCP integration

Connect Zoë to [Atlan's hosted remote MCP server](https://docs.atlan.com/product/capabilities/atlan-ai/how-tos/atlan-mcp-overview) so she can search assets, explore lineage, read and update metadata, and create glossary terms in Atlan — without leaving Zenlytic. This integration uses **API-key authentication** against Atlan's hosted MCP endpoint.

## What Zoë can access

Through the Atlan remote MCP server, Zoë can:

- Search for assets across your Atlan catalog (tables, columns, dashboards, terms, and more).
- Explore upstream and downstream lineage between assets.
- Read asset metadata — owners, descriptions, certifications, classifications, and custom attributes.
- Update metadata on assets the API key has permission to edit.
- Create and manage glossary terms.

The exact tool surface is set by Atlan and may grow over time. See [Atlan MCP tools](https://docs.atlan.com/product/capabilities/atlan-ai/how-tos/atlan-mcp-overview) for the current list.

## Prerequisites

Before you start, confirm the following:

- An **Atlan tenant** with **Remote MCP enabled**. If you don't see Remote MCP options in your tenant, contact Atlan Support to turn it on.
- An Atlan user with **admin** access (or someone who can generate an API key for you) to issue an API key.
- The `mcp-client` flag enabled on your Zenlytic workspace and `admin` role. See the [MCP overview](overview.md) for full prerequisites.

## Generate an Atlan API key

1. In Atlan, go to **Admin Settings → API Keys / Tokens**.
2. Create a new key with a descriptive name, for example `zenlytic-zoe-mcp`.
3. Scope the key to the **minimum permissions** Zoë needs:
  - Read-only on assets and lineage is enough for search and exploration workflows.
  - Add edit permissions only if you want Zoë to update metadata or create glossary terms on your behalf.
4. Copy the generated key immediately — Atlan only shows it once. Store it somewhere you can retrieve it during the next step (a password manager is ideal).

> **Use a dedicated key, not a personal one.** Tie the key to a service account or a clearly-named bot user so you can rotate or revoke Zoë's access independently of any human user.

## Set up the connection in Zenlytic

1. Open **Workspace Settings → Extensions → MCP** and click **Add Connection**.
2. Fill out the form:
  - **Name** — a label that will appear in the chat tool menu, for example `Atlan (prod)`.
  - **URL** — `https://mcp.atlan.com/mcp/api-key`. Must use `https://`.
3. Add the required header (see [Configure request headers](#configure-request-headers)).
4. Click **Test Connection**. Zenlytic opens an MCP session and lists the tools the Atlan server advertises.
5. Review the tool list and toggle off any tools Zoë shouldn't be able to call — for example, you may want to disable write tools (metadata updates, glossary creation) for read-only workflows. Newly-discovered tools are pre-selected.
6. Click **Add Connection** to save.

## Configure request headers

The Atlan API-key endpoint is controlled through HTTP headers. Add the header in the **Headers** section of the Zenlytic connection modal. Header values are masked in the UI and encrypted at rest.

### Required for every connection

| Header          | Value                                                                                                                                                                       |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Authorization` | Your Atlan API key, pasted as-is. **Do not** prefix the value with `Bearer` or `Token` — Atlan's API-key endpoint expects the raw key, unlike most MCP servers. |

> **Use the API key, not a tenant URL or username.** Pasting your Atlan tenant URL (for example `https://yourcompany.atlan.com`) or a username into the `Authorization` header causes the connection to fail with a `401 Unauthorized`. The header value must be the API key you copied from **Admin Settings → API Keys / Tokens**.

## Use the connection in chat

Once the connection has at least one selected tool, it appears in the chat tool menu. Toggle it on for any conversation where you want Zoë to use Atlan tools that turn. The toggle is per-conversation, so different chats can mix Atlan with other MCP connections as needed.

## Manage the integration

- **Rotate the key:** In Atlan, **Admin Settings → API Keys / Tokens**, generate a new key, then **Edit** the connection in Zenlytic and overwrite the `Authorization` header value. Revoke the old key in Atlan once you've confirmed the new one works.
- **Refresh tools:** If Atlan adds new tools or changes existing tool schemas, the next call may fail with a "tools have changed" error. Open the connection, click **Refresh Tools**, review the new set of tools, and **Save Changes**.
- **Adjust permissions:** Edit the API key's permissions in Atlan if you need to broaden or restrict what Zoë can do. The change takes effect on the next request — no Zenlytic update needed.
- **Disable the integration:** Click **Delete** on the connection card to remove it immediately. Zoë stops seeing the Atlan tools in any new conversation. For belt-and-suspenders, also revoke the API key in Atlan.

## Troubleshoot

- **`401 Unauthorized` from Atlan:** Confirm the `Authorization` header contains the raw API key with no `Bearer` or `Token` prefix and no leading/trailing whitespace, and that the key is still active in **Admin Settings → API Keys / Tokens**.
- **`403 Forbidden` on a tool call:** The API key doesn't have permission for the action Zoë attempted. Either tighten the tool list in the Zenlytic connection modal so Zoë can't call that tool, or expand the key's permissions in Atlan.
- **`Tool list looks short`:** Remote MCP may not be enabled on your Atlan tenant, or the API key has limited scopes. Contact Atlan Support to confirm Remote MCP is on, and double-check the key's permissions.
- **Connection works in Test Connection but fails in chat:** Atlan's tool surface has likely changed since you saved. Open the connection in workspace settings and click **Refresh Tools**.
- **Can't reach the MCP endpoint:** Confirm outbound HTTPS to `mcp.atlan.com` is allowed from Zenlytic's network. If your Atlan tenant is on a private VPC or restricted egress, contact Atlan Support — the public `mcp.atlan.com` endpoint must be reachable from Zenlytic.
