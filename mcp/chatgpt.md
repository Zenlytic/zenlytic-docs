---
description: >-
  Connect ChatGPT to Zenlytic's MCP server so it can query your business data
  directly from a chat.
---

# Connecting ChatGPT to Zenlytic

Connecting a custom MCP server to ChatGPT requires **Developer mode**, which is only available on ChatGPT Business, Enterprise, or Edu plans. See [MCP Server](connecting-to-zenlytic.md) for what you get once connected and general prerequisites.

## Before you start

You'll need:

* Zenlytic's MCP URL for your workspace, typically `https://<your-zenlytic-domain>/mcp` (ask your workspace admin if you're not sure)
* Developer mode enabled for your ChatGPT workspace — an admin may need to turn this on first under **Workspace Settings → Permissions & Roles → Connected Data → Create custom MCP connectors**

## Connect with OAuth (recommended)

1. In ChatGPT, go to **Settings → Apps & Connectors → Advanced settings** and turn on **Developer mode**.
2. Back in **Connectors**, click **Create**, give it a name (e.g. "Zenlytic"), and paste in Zenlytic's MCP URL.
3. Select **OAuth** as the authentication method and save.
4. In a chat, open the **+** menu, choose the Zenlytic connector, and complete the login/approval flow the first time you use it.

## Connect with a Personal Access Token (alternative)

If OAuth isn't available for your deployment, use a static header instead:

1. In Zenlytic, go to **Workspace Settings → Personal Access Tokens** (`/workspace-settings/personal-access-tokens`), click **Create token**, and copy it immediately — it's only shown once.
2. When creating the connector, choose **Custom headers** instead of OAuth.
3. Set the header name to `Authorization` and the value to `Bearer <your-personal-access-token>`.

Treat this token like a password — anyone with it can query Zenlytic on your behalf within your workspace's permissions. You can revoke it any time from the same Personal Access Tokens page.

## Using it

Once connected, enable the Zenlytic connector in a chat and ask a data question naturally, for example:

> "Ask Zenlytic what our top 5 customers by revenue were last month."

ChatGPT will call the `ask_zenlytic` tool and return the answer along with a link back to the full conversation in Zenlytic.

## Troubleshooting

* **Don't see Developer mode:** ask your workspace admin to enable **Connected Data → Create custom MCP connectors** in Workspace Settings — it's only available on Business, Enterprise, and Edu plans.
* **"Unauthorized" or repeated login prompts:** re-run the OAuth flow from the connector's settings, or generate a new Personal Access Token.
* **Not sure what got asked/answered:** open Zenlytic and check your conversation history — MCP conversations appear there just like conversations started in the app.
