---
description: >-
  Connect Cursor to Zenlytic's MCP server so it can query your business data
  directly from your editor.
---

# Connecting Cursor to Zenlytic

Cursor supports both native OAuth and static tokens for remote MCP servers, configured in an `mcp.json` file. See [MCP Server](connecting-to-zenlytic.md) for what you get once connected and general prerequisites.

## Before you start

You'll need Zenlytic's MCP URL for your workspace, typically `https://<your-zenlytic-domain>/mcp` (ask your workspace admin if you're not sure).

## Connect with OAuth (recommended)

1. Create or open `.cursor/mcp.json` in your project (or `~/.cursor/mcp.json` for a config available in every project).
2. Add an entry for Zenlytic:

```json
{
  "mcpServers": {
    "zenlytic": {
      "url": "https://<your-zenlytic-domain>/mcp"
    }
  }
}
```

3. Open **Cursor Settings → MCP**, find **zenlytic**, and click **Connect** — Cursor will detect that OAuth is supported, open a browser window to log in, and handle token storage and refresh for you.

## Connect with a Personal Access Token (alternative)

If OAuth isn't available for your deployment, add the token as a static header instead:

1. In Zenlytic, go to **Workspace Settings → Personal Access Tokens** (`/workspace-settings/personal-access-tokens`), click **Create token**, and copy it immediately — it's only shown once.
2. Add it to `mcp.json`:

```json
{
  "mcpServers": {
    "zenlytic": {
      "url": "https://<your-zenlytic-domain>/mcp",
      "headers": {
        "Authorization": "Bearer <your-personal-access-token>"
      }
    }
  }
}
```

Avoid committing the raw token to a shared repo — reference an environment variable instead (e.g. `"Bearer ${env:ZENLYTIC_TOKEN}"`) if your `mcp.json` is checked into version control. Treat this token like a password — anyone with it can query Zenlytic on your behalf within your workspace's permissions. You can revoke it any time from the same Personal Access Tokens page.

## Using it

Once connected, ask Cursor's agent a data question naturally, for example:

> "Ask Zenlytic what our top 5 customers by revenue were last month."

It will call the `ask_zenlytic` tool and return the answer along with a link back to the full conversation in Zenlytic.

## Troubleshooting

* **"Unauthorized" or repeated login prompts:** reconnect from **Cursor Settings → MCP**, or generate a new Personal Access Token.
* **Server doesn't appear:** confirm `mcp.json` is valid JSON and in the right location (`.cursor/mcp.json` for project-scoped, `~/.cursor/mcp.json` for global), then reload Cursor.
* **Not sure what got asked/answered:** open Zenlytic and check your conversation history — MCP conversations appear there just like conversations started in the app.
