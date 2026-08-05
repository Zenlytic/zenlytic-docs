---
description: >-
  Connect Cursor to Zenlytic's MCP server so it can query your business data
  directly from your editor.
---

# Connecting Cursor to Zenlytic

Cursor supports both native OAuth and static tokens for remote MCP servers, configured in an `mcp.json` file. See [MCP Server](connecting-to-zenlytic.md) for what you get once connected and general prerequisites.

## Before you start

You'll need Zenlytic's MCP URL for your workspace. URL: https://mcp.zenlytic.com/mcp

## Connect with OAuth (recommended)

1. Create or open `.cursor/mcp.json` in your project (or `~/.cursor/mcp.json` for a config available in every project).
2. Add an entry for Zenlytic:

```json
{
  "mcpServers": {
    "zenlytic": {
      "url": "https://mcp.zenlytic.com/mcp"
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
      "url": "https://mcp.zenlytic.com/mcp",
      "headers": {
        "Authorization": "Bearer <your-personal-access-token>"
      }
    }
  }
}
```

## Using it

Once connected, ask Cursor's agent a data question naturally, for example:

> "Hey Zoe, who were our top 5 customers by revenue last month?"

It will call the `ask_zoe` tool and return the answer along with a link back to the full conversation in Zenlytic.
