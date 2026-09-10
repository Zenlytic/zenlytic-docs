---
description: >-
  Connect Zoë to Microsoft's SharePoint MCP server so each user can search and
  read their own sites, files, and lists from chat.
---

# SharePoint

Connect Zoë to [Microsoft's remote SharePoint MCP server](https://learn.microsoft.com/en-us/microsoft-copilot-studio/mcp-sharepoint-tools) so she can find sites, files, folders, and list items in your SharePoint and OneDrive content directly from Zenlytic chats. SharePoint is an **OAuth connector**: Zenlytic supplies the server endpoints and the OAuth application, and you supply your Microsoft Entra tenant ID. Every user then signs in with their own Microsoft account, and Zoë acts as that user.

## What Zoë can access

Microsoft's SharePoint MCP server exposes tools for both files and lists, including `findSite`, `findFileOrFolder`, `readSmallTextFile`, and `listListItems`. See the [SharePoint MCP server reference](https://learn.microsoft.com/en-us/microsoft-copilot-studio/mcp-sharepoint-tools) for the full list and parameters.

All tool calls run as the signed-in user, so Zoë can only see content that user can already open in SharePoint or OneDrive.

Microsoft flags the SharePoint MCP server as a **preview** feature:

* Tool names and parameters may change.
* File operations are limited to files of **5 MB or less**.
* Search results return the **top 20** items.

## How the OAuth connector works

SharePoint differs from a custom MCP connection in a few ways:

* **Zenlytic supplies the endpoints and the app.** You do not enter a server URL, client ID, or client secret. Zenlytic uses a single multi-tenant Microsoft Entra application and fills in the tenant-scoped endpoints from the tenant ID you provide.
* **Each user connects their own account.** Creating the connector does not authorize anyone. Each user clicks **Connect** in the chat tool menu and signs in with Microsoft before the connector is available to them. Tokens are stored per user and per connector.
* **Tenant ID is fixed at creation.** To change it, delete the connector and create it again. Name, access grants, and the enabled-by-default setting remain editable.

## Prerequisites

* **Your Microsoft Entra tenant ID.** A GUID that identifies your Microsoft 365 tenant. Both the MCP server URL and the Microsoft sign-in endpoints are tenant-scoped, so Zenlytic requires a real tenant GUID and rejects `common`. See [How to find your Microsoft Entra tenant ID](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-find-tenant).
* **Consent for Zenlytic's application in your tenant.** On first connect, each user sees a Microsoft consent prompt for the following delegated permissions on the **Agent 365 Tools** resource:
  * `McpServers.OneDriveSharepoint.All`
  * `McpServers.SharepointLists.All`
  * `offline_access`

  Depending on your tenant's user-consent policy, a Global Administrator or Application Administrator may need to grant **tenant-wide admin consent** to the Zenlytic application, or approve an admin-consent request, before regular users can connect. See [Grant tenant-wide admin consent to an application](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent).
* **A Microsoft 365 tenant where the SharePoint MCP server is available.** The server runs on Microsoft's Agent 365 platform. See [MCP authentication for Agent 365 tools](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/mcp-authentication) for Microsoft's requirements.
* **Zenlytic requirements.** The `mcp-client` and `mcp-oauth` flags enabled on your workspace, and `admin` role. If you don't see **OAuth** as a method when adding a connector, ask your Zenlytic contact to enable it. See [MCP Client](./) for the full list.

{% hint style="info" %}
The SharePoint connector is not available on VPC deployments of Zenlytic, because it relies on Zenlytic's shared Microsoft Entra application.
{% endhint %}

## Set up the connector in Zenlytic

1. Open **Workspace Settings → Extensions → MCP Connectors** and click **Add a New Connector**.
2. Under **Method**, choose **OAuth**, then choose **SharePoint** as the provider.
3. Fill out the form:
   * **Name** — a label that will appear in the chat tool menu, for example `SharePoint`.
   * **Tenant ID** — your Microsoft Entra tenant ID.
   * **Access** — the users or groups who can see and connect this connector.
   * **Enabled by default** (optional) — turn the connector on automatically in new chats for users who have already connected their account.
4. Click **Add Connection** to save.
5. Click **Connect** in the connector modal and sign in with your Microsoft account. This seeds the tool list so users see the available tools immediately. If Microsoft shows **Need admin approval**, grant admin consent as described in [Prerequisites](sharepoint.md#prerequisites).

Use **Refresh Tools** at any time to re-sync the tool list. Refresh uses the token of a user who has already connected.

## Use the connector in chat

1. Open the tool menu in any chat. Until you connect your account, SharePoint appears as a **Connect** row instead of a toggle.
2. Click **Connect**. Zenlytic opens Microsoft sign-in in a popup. Sign in and accept the requested permissions.
3. The popup closes and the connector becomes a toggle. Turn it on for any conversation where Zoë should have access to your SharePoint content.

A few specifics to share with your users:

* **Your content, your permissions.** Zoë sees exactly what your Microsoft account can see. Another user connecting the same connector sees their own sites and files, not yours.
* **Name the site or file.** Prompts that include the site name, file name, or list name produce more reliable tool calls than vague references. For example: "In the `Marketing` site, find the latest campaign brief and summarize it."
* **Mind the preview limits.** Zoë cannot read files larger than 5 MB, and searches return at most 20 results. Ask her to narrow the search if the item you want is missing.


## Troubleshoot

* **"A tenant ID is required" or "'common' is not valid":** The Tenant ID field is blank or set to `common`. Enter your tenant's GUID.
* **"Need admin approval" during sign-in:** Your tenant requires admin consent for Zenlytic's application. Ask a Global Administrator or Application Administrator to grant tenant-wide consent, then click **Connect** again.
* **"SharePoint connections are not configured on this server":** Your Zenlytic deployment does not have the SharePoint connector enabled. Contact your Zenlytic contact.
* **"Invalid or expired OAuth state":** More than 10 minutes passed between clicking **Connect** and completing sign-in, or the sign-in link was reused. Click **Connect** again.
* **The popup opens and nothing happens:** Your browser blocked the popup. Allow popups for Zenlytic and click **Connect** again.
* **A file will not open:** The file is larger than 5 MB, which the preview server does not support. Ask Zoë for a smaller file or a summary from search results instead.
