---
description: >-
  Connect Claude.ai to Zenlytic's MCP server so Claude can
  query your business data directly.
---

# Claude.ai

Claude.ai support MCP custom connectors with OAuth out of the box, so this is one of the easiest clients to connect to Zenlytic. See [MCP Server](./) for what you get once connected and general prerequisites.

## Before you start

You'll need Zenlytic's MCP URL for your workspace. URL: https://mcp.zenlytic.com/mcp

## Connect with OAuth (recommended)

1. Open **Settings → Connectors**
2. Click **Add**, then choose **Add custom connector**.
3. Paste in Zenlytic's MCP URL and click **Add**.
4. Click **Connect**, complete the OAuth login/approval flow in the browser window that opens, and pick your workspace.

Your connector is now authorized — you won't need to log in again unless you revoke access.

## Connect with a Personal Access Token (alternative)

If OAuth isn't available, you can authenticate with a static token instead:

1. In Zenlytic, go to **Workspace Settings → Personal Access Tokens** (`/workspace-settings/personal-access-tokens`), click **Create token**, and copy it immediately — it's only shown once.
2. In the **Add custom connector** dialog, open **Advanced settings**.
3. Add a request header named `Authorization` with the value `Bearer <your-personal-access-token>`, and mark it required.
4. Click **Add**, then **Connect**.

## Using it

Once connected, ask Claude a data question naturally, for example:

> "Hey Zoë, who were our top 5 customers by revenue last month?"

Claude will call the `ask_zoe` tool and return the answer along with a link back to the full conversation in Zenlytic.
