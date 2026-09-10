---
description: >-
  Connect Zoë to Google's Drive, Docs, Sheets, and Slides MCP servers so each
  user can work with their own Workspace files from chat.
---

# Google Workspace

Connect Zoë to Google's hosted Workspace MCP servers for **Drive**, **Docs**, **Sheets**, and **Slides** so she can search files, read and edit documents, and update spreadsheets and presentations directly from Zenlytic chats. Google Workspace is an **OAuth connector**: you register an OAuth client in your own Google Cloud project and paste its Client ID and Client Secret into Zenlytic. Every user then signs in with their own Google account, and Zoë acts as that user.

> Looking for BigQuery instead? See [Google](google.md). That guide covers Google's BigQuery MCP server, which uses a static bearer token rather than per-user OAuth.

## What Zoë can access

Each module is a separate Google-hosted MCP server with its own tools. Enable the modules you need when you create the connector.

| Module     | Tools Zoë can call                                                                                                                                          |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Drive**  | `search_files`, `list_recent_files`, `read_file_content`, `download_file_content`, `get_file_metadata`, `get_file_permissions`, `create_file`, `copy_file` |
| **Docs**   | `read_doc`, `update_doc`                                                                                                                                    |
| **Sheets** | `get_spreadsheet`, `get_values`, `update_spreadsheet`, `update_values`, `update_formulas`, `insert_dimension`                                               |
| **Slides** | `read_presentation`, `update_presentation`                                                                                                                  |

All tool calls run as the signed-in user, so Zoë can only see and change files that user can already see and change in Google Workspace. Docs, Sheets, and Slides include write tools, and modules are enabled or disabled as a whole, so enabling one of those modules lets Zoë make real edits to the user's files.

## How the OAuth connector works

Google Workspace differs from a custom MCP connection in a few ways:

* **Zenlytic supplies the endpoints.** You do not enter a server URL, authorize URL, token URL, or scopes. Zenlytic fills these in for each module.
* **Each user connects their own account.** Creating the connector does not authorize anyone. Each user clicks **Connect** in the chat tool menu and signs in with Google before the connector is available to them. Tokens are stored per user and per connector.
* **Credentials are fixed at creation.** The Client ID and Client Secret cannot be edited. To rotate them, delete the connector and create it again. Name, access grants, and the enabled-by-default setting remain editable.

## Prerequisites

Complete the following in **your own** Google Cloud project. Zenlytic only needs the resulting Client ID and Client Secret.

### 1. Enroll in the Google Workspace Developer Preview Program

Google's hosted Workspace MCP servers are available only to Google Cloud projects accepted into the [Google Workspace Developer Preview Program](https://developers.google.com/workspace/preview). Enrollment is an application tied to a specific Workspace account and Google Cloud project, and approval takes a few days. Service accounts cannot be enrolled.

{% hint style="warning" %}
If the project has not been accepted, the sign-in flow and tool list still succeed, but every tool call fails with `The caller does not have permission`. Zenlytic surfaces this error in chat with a hint pointing at preview enrollment and API setup.
{% endhint %}

{% hint style="info" %}
Google's preview terms restrict preview features from being used in public applications before general availability and from being exposed to end users outside your own organization. Review the program terms before rolling the connector out to your workspace.
{% endhint %}

### 2. Enable the APIs for each module

Enable **both** the base API and the MCP API for every module you plan to turn on. Enabling only the MCP API is not sufficient.

| Module     | Base API                | MCP API                    | Google setup guide                                                                                                  |
| ---------- | ----------------------- | -------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Drive**  | `drive.googleapis.com`  | `drivemcp.googleapis.com`  | [Configure the Drive MCP server](https://developers.google.com/workspace/drive/api/guides/configure-mcp-server)     |
| **Docs**   | `docs.googleapis.com`   | `docsmcp.googleapis.com`   | [Configure the Docs MCP server](https://developers.google.com/workspace/docs/api/guides/configure-mcp-server)       |
| **Sheets** | `sheets.googleapis.com` | `sheetsmcp.googleapis.com` | [Configure the Sheets MCP server](https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server)   |
| **Slides** | `slides.googleapis.com` | `slidesmcp.googleapis.com` | [Configure the Slides MCP server](https://developers.google.com/workspace/slides/api/guides/configure-mcp-server)   |

Each Google guide includes console links and `gcloud services enable` commands.

### 3. Configure the OAuth consent screen and scopes

Follow [Configure the OAuth consent screen](https://developers.google.com/workspace/guides/configure-oauth-consent) in the Google Auth Platform, then add the scopes for each module you enable:

| Module     | Scopes                                                                                                 |
| ---------- | ------------------------------------------------------------------------------------------------------ |
| **Drive**  | `https://www.googleapis.com/auth/drive.readonly`, `https://www.googleapis.com/auth/drive.file`         |
| **Docs**   | `https://www.googleapis.com/auth/documents`, `https://www.googleapis.com/auth/drive.readonly`          |
| **Sheets** | `https://www.googleapis.com/auth/spreadsheets`, `https://www.googleapis.com/auth/drive.readonly`      |
| **Slides** | `https://www.googleapis.com/auth/presentations`, `https://www.googleapis.com/auth/drive.readonly`     |

Set the audience to **Internal**. This is the correct choice for a Workspace organization: no app verification and no test-user list. If you choose **External**, every user must be added as a test user until Google verifies the app.

Docs, Sheets, and Slides use the read/write scopes because their `update_*` tools require them. The connector UI does not expose scope editing.

### 4. Create an OAuth client

Follow [Create access credentials](https://developers.google.com/workspace/guides/create-credentials) to create an **OAuth client ID** of type **Web application**. Under **Authorized redirect URIs**, add Zenlytic's callback URL:

```
https://devapi.zenlytic.com/api/v2/mcp_connections/oauth/callback
```

The value must match exactly. No authorized JavaScript origin is required. If your workspace runs on a dedicated or VPC deployment, ask your Zenlytic contact for the callback URL for your environment.

Copy the **Client ID** and **Client Secret**. Client IDs look like `1234567890-abc123.apps.googleusercontent.com`.

### 5. Review Google's security guidance

Read Google's [Configure security for Google Workspace MCP servers](https://developers.google.com/workspace/guides/configure-mcp-security) guide, which covers prompt-injection risk when an agent reads user-controlled file content.

### 6. Zenlytic requirements

* The `mcp-client` and `mcp-oauth` flags enabled on your workspace. If you don't see **OAuth** as a method when adding a connector, ask your Zenlytic contact to enable it.
* `admin` role in the workspace. See [MCP Client](./) for the full list.

## Set up the connector in Zenlytic

1. Open **Workspace Settings → Extensions → MCP Connectors** and click **Add a New Connector**.
2. Under **Method**, choose **OAuth**, then choose **Google Workspace** as the provider.
3. Fill out the form:
   * **Name** — a label that will appear in the chat tool menu, for example `Google Workspace`.
   * **Client ID** — the OAuth client ID from your Google Cloud project. If your mail or chat client turned it into a link, paste it anyway; Zenlytic strips a leading `https://` and trailing `/`.
   * **Client Secret** — the OAuth client secret. The secret is write-only and is never shown again.
   * **Modules** — switch on Drive, Docs, Sheets, or Slides. Each module lists the tools it exposes. Enable only modules whose APIs and scopes you configured above.
   * **Access** — the users or groups who can see and connect this connector.
   * **Enabled by default** (optional) — turn the connector on automatically in new chats for users who have already connected their account.
4. Click **Add Connection** to save.
5. Click **Connect** in the connector modal and sign in with your Google account to confirm everything is working as expected.

## Use the connector in chat

1. Open the tool menu in any chat. Until you connect your account, Google Workspace appears as a **Connect** row instead of a toggle.
2. Click **Connect**. Zenlytic opens Google sign-in in a popup. Sign in and grant the requested permissions.
3. The popup closes and the connector becomes a toggle. Turn it on for any conversation where Zoë should have access to your files.

A few specifics to share with your users:

* **Your files, your permissions.** Zoë sees exactly what your Google account can see. Another user connecting the same connector sees their own files, not yours.
* **Name the file.** Prompts that include the file name or a Drive link produce more reliable tool calls than vague references. For example: "Read the `Q3 Planning` doc and summarize the open decisions."
* **Write tools make real changes.** With Docs, Sheets, or Slides enabled, Zoë can edit your documents. Review changes she makes.

## Troubleshoot

* **`invalid_client` or "The OAuth client was not found":** The Client ID is wrong, or the OAuth client lives in a different Google Cloud project than the one whose APIs you enabled. Confirm the Client ID and project, then recreate the connector.
* **`redirect_uri_mismatch`:** Zenlytic's callback URL is missing from the OAuth client's **Authorized redirect URIs**, or does not match exactly. Add `https://devapi.zenlytic.com/api/v2/mcp_connections/oauth/callback` (or the URL for your deployment) and try again.
* **Sign-in and tool list work, but every tool call fails with `The caller does not have permission`:** The Google Cloud project has not been accepted into the Developer Preview Program, or the base API or MCP API for that module is not enabled. See steps 1 and 2 above.
* **"This app is blocked" or a request to add test users:** The consent screen audience is **External** and the app is unverified. Switch the audience to **Internal** or add each user as a test user.
* **"Invalid or expired OAuth state":** More than 10 minutes passed between clicking **Connect** and completing sign-in, or the sign-in link was reused. Click **Connect** again.
* **The popup opens and nothing happens:** Your browser blocked the popup. Allow popups for Zenlytic and click **Connect** again.
