---
description: >-
  Connect GitHub Copilot Chat in VS Code to Zenlytic's MCP server so it can
  query your business data directly from your editor.
---

# Connecting GitHub Copilot to Zenlytic

GitHub Copilot Chat in VS Code reads MCP servers from an `mcp.json` file. See [MCP Server](connecting-to-zenlytic.md) for what you get once connected and general prerequisites.

> Note the top-level key here is `servers`, not `mcpServers` like Cursor and Claude Desktop use — a common copy-paste mistake.

## Before you start

You'll need Zenlytic's MCP URL for your workspace. URL: <TBD>

## Connect with OAuth (recommended)

1. Open the Command Palette and run **MCP: Open User Configuration** (for a config available in every workspace), or create `.vscode/mcp.json` in your project for a project-scoped config.
2. Add an entry for Zenlytic:

```json
{
  "servers": {
    "zenlytic": {
      "type": "http",
      "url": "<TBD>"
    }
  }
}
```

3. VS Code will prompt you to trust the server the first time it starts — approve it.
4. Click **Auth** in the CodeLens above the server entry in `mcp.json` to complete the OAuth flow in your browser.

## Connect with a Personal Access Token (alternative)

If OAuth isn't available for your deployment, add the token as a static header instead:

1. In Zenlytic, go to **Workspace Settings → Personal Access Tokens** (`/workspace-settings/personal-access-tokens`), click **Create token**, and copy it immediately — it's only shown once.
2. Add it to `mcp.json`:

```json
{
  "servers": {
    "zenlytic": {
      "type": "http",
      "url": "<TBD>",
      "headers": {
        "Authorization": "Bearer <your-personal-access-token>"
      }
    }
  }
}
```
## Using it

Once connected, ask Copilot Chat a data question naturally, for example:

> "Ask Zenlytic what our top 5 customers by revenue were last month."

It will call the `ask_zenlytic` tool and return the answer along with a link back to the full conversation in Zenlytic.
