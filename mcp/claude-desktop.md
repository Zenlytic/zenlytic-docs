---
description: >-
  Connect Claude Desktop or Claude.ai to Zenlytic's MCP server so Claude can
  query your business data directly.
---

# Connecting Claude Desktop / Claude.ai to Zenlytic

Claude Desktop and Claude.ai support MCP custom connectors with OAuth out of the box, so this is one of the easiest clients to connect to Zenlytic. See [MCP Server](connecting-to-zenlytic.md) for what you get once connected and general prerequisites.

## Before you start

You'll need Zenlytic's MCP URL for your workspace, typically `https://<your-zenlytic-domain>/mcp` (ask your workspace admin if you're not sure).

## Connect with OAuth (recommended)

1. Open **Settings → Connectors** (or press `Ctrl+,`).
2. Click **Add**, then choose **Add custom connector**.
3. Paste in Zenlytic's MCP URL and click **Add**.
4. Click **Connect**, complete the OAuth login/approval flow in the browser window that opens, and pick your workspace.

Your connector is now authorized — you won't need to log in again unless you revoke access.

> Claude connects to custom connectors from Anthropic's cloud infrastructure, not your local machine — make sure your MCP URL is reachable over the public internet.

## Connect with a Personal Access Token (alternative)

If OAuth isn't available for your deployment, you can authenticate with a static token instead:

1. In Zenlytic, go to **Workspace Settings → Personal Access Tokens** (`/workspace-settings/personal-access-tokens`), click **Create token**, and copy it immediately — it's only shown once.
2. In the **Add custom connector** dialog, open **Advanced settings**.
3. Add a request header named `Authorization` with the value `Bearer <your-personal-access-token>`, and mark it required.
4. Click **Add**, then **Connect**.

Treat this token like a password — anyone with it can query Zenlytic on your behalf within your workspace's permissions. You can revoke it any time from the same Personal Access Tokens page.

## Using it

Once connected, ask Claude a data question naturally, for example:

> "Ask Zenlytic what our top 5 customers by revenue were last month."

Claude will call the `ask_zenlytic` tool and return the answer along with a link back to the full conversation in Zenlytic.

## Troubleshooting

* **"Unauthorized" or repeated login prompts:** your token may have expired or been revoked. Generate a new Personal Access Token, or re-run the OAuth connection flow.
* **Connector can't reach the server:** Claude connects from Anthropic's cloud, not your device — confirm the MCP URL is publicly reachable over HTTPS.
* **Not sure what got asked/answered:** open Zenlytic and check your conversation history — MCP conversations appear there just like conversations started in the app.
