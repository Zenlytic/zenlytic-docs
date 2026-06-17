# Jira MCP integration

Connect Zoë to the [Atlassian Rovo remote MCP server](https://github.com/atlassian/atlassian-mcp-server) — Atlassian's official hosted endpoint for AI tools — so she can search and create Jira issues, run JQL queries, and interact with Confluence and Compass content directly from Zenlytic chats. Authenticate with a static `Authorization` header containing a Base64-encoded Atlassian API token.

> Zenlytic does not currently support OAuth-based MCP connections. The API token path described here is the supported authentication method. API token authentication must be enabled by an Atlassian organization admin before it can be used.

## What Zoë can access

The Atlassian Rovo MCP server exposes tools across Jira, Confluence, and Compass. With the default configuration, Zoë can:

- **Jira** — search issues using JQL, read issue details, create issues and stories, bulk-create issues from notes, and update existing tickets.
- **Confluence** — summarize pages, create new pages, and browse accessible spaces.
- **Compass** — create service components, bulk-import from CSV or JSON, and query service dependencies.

All tool calls run as the Atlassian user whose API token is configured, so Zoë's reach into Atlassian is exactly what that user can see and do. Zoë cannot access content the token's owner cannot access.

## Prerequisites

Before you start, confirm the following:

- An **Atlassian Cloud** site with Jira (and optionally Confluence or Compass). The Rovo remote MCP server **does not support Jira Server or Jira Data Center**.
- A **dedicated Atlassian account** scoped to the least-privileged set of Jira projects and Confluence spaces Zoë needs. You'll create the API token against this account.
- An **Atlassian organization admin** who has enabled API token authentication in the Rovo MCP server settings. Admins can toggle this under **admin.atlassian.com → Security → Atlassian Rovo MCP server → Authentication**.
- **Zenlytic requirements.** The `mcp-client` flag enabled on your workspace and `admin` role. See the [MCP overview](overview.md) for the full list.

## Create an Atlassian API token

API tokens replace passwords for programmatic access to Atlassian Cloud. Each token is tied to a single Atlassian user account.

1. Sign in to the Atlassian account you want Zoë to run as, then open [Atlassian ID → Security → API tokens](https://id.atlassian.com/manage-profile/security/api-tokens).
2. Click **Create API token**, give it a recognizable label (for example `zenlytic-mcp`), and click **Create**.
3. Copy the token value immediately — Atlassian only shows it once. Store it in your secrets manager.
4. Base64-encode your credentials in `email:token` format. On macOS or Linux:

    ```bash
    echo -n "you@example.com:YOUR_API_TOKEN" | base64
    ```

    Copy the resulting string. You'll use it as the `Authorization` header value in the next step.

> Use a dedicated service account rather than a personal account so that the connection doesn't break when someone leaves your organization or rotates their personal token.

## Set up the connection in Zenlytic

1. Open **Workspace Settings → Extensions → MCP** and click **Add Connection**.
2. Fill out the form:
   - **Name** — a label that will appear in the chat tool menu, for example `Jira`.
   - **URL** — the Atlassian Rovo MCP endpoint:

     ```
     https://mcp.atlassian.com/v1/mcp
     ```

3. Add the `Authorization` header (see [Configure request headers](#configure-request-headers)).
4. Click **Test Connection**. Zenlytic opens an MCP session against the Atlassian server and lists the tools it advertises.
5. Review the tool list and toggle off any tools Zoë shouldn't be able to call. Newly-discovered tools are pre-selected.
6. Click **Add Connection** to save.

> Enabling write access means Zoë can create or modify real Jira issues, Confluence pages, and Compass components. Use read-only toggles on write tools unless you specifically need Zoë to make changes.

## Configure request headers

Add the following in the **Headers** section of the Zenlytic connection modal. Header values are masked in the UI and encrypted at rest.

| Header          | Value                                                                                                  |
| --------------- | ------------------------------------------------------------------------------------------------------ |
| `Authorization` | `Basic BASE64_ENCODED_EMAIL_AND_TOKEN`. Include the `Basic` scheme and a single space before the value. |

A `200` response that lists the available tools means the credentials and URL are wired up correctly.

## Use the connection in chat

Once the connection has at least one selected tool, it appears in the chat tool menu. Toggle it on for any conversation where you want Zoë to use Jira tools. The toggle is per-conversation, so different chats can mix Jira with other MCP connections as needed.

A few specifics to share with your users:

- **One account, one permission set.** Every user sharing the connection sees whatever Jira content the API token's account can access. If you need different access for different teams, create a separate Atlassian account with the appropriate project permissions and wire it up as its own Zenlytic connection.
- **Be specific in prompts.** Naming the Jira project key and issue key (for example: "In project `ACME`, find all open bugs assigned to the backend team") produces more reliable tool calls than vague references.
- **Write tools make real changes.** Tools like issue creation and update run against live Jira data. Toggle them off in the connection modal unless you've deliberately decided Zoë should write to Jira.

## Manage the integration

- **Rotate the API token:** In [Atlassian ID → Security → API tokens](https://id.atlassian.com/manage-profile/security/api-tokens), revoke the old token and create a new one, re-encode `email:new_token` in Base64, then **Edit** the connection in Zenlytic and overwrite the `Authorization` header value.
- **Change permissions:** Adjust the Atlassian account's project roles or space permissions in your Atlassian admin console. Changes take effect on the next tool call — no Zenlytic update needed.
- **Refresh tools:** If Atlassian adds new tools or changes existing tool schemas, the next call may fail with a "tools have changed" error. Open the connection, click **Refresh Tools**, review the new set, and **Save Changes**.
- **Disable the integration:** Click **Delete** on the connection card to remove it immediately. Zoë stops seeing the Jira tools in any new conversation. Also revoke the API token in Atlassian ID for belt-and-suspenders.

## Limitations

- **Atlassian Cloud only.** Jira Server and Jira Data Center are not supported by the Rovo remote MCP server.
- **No OAuth in Zenlytic.** Zenlytic does not yet support OAuth-based MCP connections. The API token Basic auth path described here is the only supported authentication method.
- **API token auth must be admin-enabled.** An Atlassian org admin must explicitly enable API token authentication in the Rovo MCP server settings before this setup will work.
- **Token scope is user-wide.** API tokens aren't restricted to specific Atlassian sites or projects. All access is governed by the Atlassian account's existing project roles and space permissions.

## Troubleshoot

- **`401 Unauthorized`:** The `Authorization` header is missing, malformed, or the API token has been revoked. Confirm the header value is `Basic <base64>` (with a single space) and that the token is still active in [Atlassian ID → Security → API tokens](https://id.atlassian.com/manage-profile/security/api-tokens). Re-encode `email:token` and replace the header value.
- **`403 Forbidden` on a tool call:** The Atlassian account doesn't have the Jira project role or Confluence space permission required for that action. Grant the needed role in your Atlassian admin console and retry.
- **`403 Forbidden` on all calls / API token auth not accepted:** API token authentication is disabled in your organization's Rovo MCP server settings. Ask an Atlassian org admin to enable it under **admin.atlassian.com → Security → Atlassian Rovo MCP server → Authentication**.
- **Tool list is empty or missing Jira tools:** The Atlassian account may not have access to any Jira projects, or the Rovo MCP server settings restrict which products are exposed. Confirm the account has at least one Jira project role.
- **Connection works in Test Connection but fails in chat:** The API token may have been revoked between test and use. Generate a fresh token, re-encode, and update the `Authorization` header.
