---
description: >-
  Connect ChatGPT to Zenlytic's MCP server so it can query your business data
  directly from a chat.
---

# ChatGPT

Connecting a custom MCP server to ChatGPT requires **Developer mode**, which is only available on ChatGPT Business, Enterprise, or Edu plans. See [MCP Server](./) for what you get once connected and general prerequisites.

## Before you start

You'll need:

* Zenlytic's MCP URL for your workspace. URL: https://mcp.zenlytic.com/mcp
* Developer mode enabled for your ChatGPT workspace — an admin may need to turn this on first under **Workspace Settings → Permissions & Roles → Connected Data → Create custom MCP connectors**

## Connect with OAuth (recommended)

1. In ChatGPT, go to **Settings → Apps & Connectors → Advanced settings** and turn on **Developer mode**.
2. Back in **Connectors**, click **Create**, give it a name (e.g. "Zenlytic"), and paste in Zenlytic's MCP URL.
3. Select **OAuth** as the authentication method and save.
4. In a chat, open the **+** menu, choose the Zenlytic connector, and complete the login/approval flow the first time you use it.

## Connect with a Personal Access Token (alternative)

If OAuth isn't available, use a static header instead:

1. In Zenlytic, go to **Workspace Settings → Personal Access Tokens** (`/workspace-settings/personal-access-tokens`), click **Create token**, and copy it immediately — it's only shown once.
2. When creating the connector, choose **Custom headers** instead of OAuth.
3. Set the header name to `Authorization` and the value to `Bearer <your-personal-access-token>`.

## Using it

Once connected, enable the Zenlytic connector in a chat and ask a data question naturally, for example:

> "Hey Zoe, who were our top 5 customers by revenue last month?"

ChatGPT will call the `ask_zoe` tool and return the answer along with a link back to the full conversation in Zenlytic.
