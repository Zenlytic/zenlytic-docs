---
description: >-
  Connect Claude Code to Zenlytic's MCP server so it can query your business
  data directly from the command line.
---

# Connecting Claude Code to Zenlytic

Claude Code connects to remote MCP servers over HTTP transport from the command line. See [MCP Server](connecting-to-zenlytic.md) for what you get once connected and general prerequisites.

## Before you start

You'll need Zenlytic's MCP URL for your workspace. URL: <TBD>

## Connect with OAuth (recommended)

1. Add the server:

```bash
claude mcp add --transport http zenlytic <TBD>
```

2. Inside Claude Code, run `/mcp`, select **zenlytic**, and click **Authenticate**.
3. Complete the OAuth login/approval flow in the browser window that opens, and pick your workspace.

Claude Code stores the token and refreshes it automatically, so you shouldn't need to re-authenticate unless you revoke access.

## Connect with a Personal Access Token (alternative)

If OAuth isn't available, add the server with a static bearer header instead:

1. In Zenlytic, go to **Workspace Settings → Personal Access Tokens** (`/workspace-settings/personal-access-tokens`), click **Create token**, and copy it immediately — it's only shown once.
2. Add the server with the token as a header:

```bash
claude mcp add --transport http zenlytic <TBD> \
  --header "Authorization: Bearer <your-personal-access-token>"

## Using it

Once connected, ask Claude Code a data question naturally, for example:

> "Hey Zoe, who were our top 5 customers by revenue last month?"

Claude will call the `ask_zoe` tool and return the answer along with a link back to the full conversation in Zenlytic.

## Troubleshooting

* **"Unauthorized" or repeated login prompts:** run `/mcp`, select **zenlytic**, and re-authenticate, or generate a new Personal Access Token.
* **Server not found:** double-check the URL with `claude mcp list`, and confirm it with your workspace admin.
* **Not sure what got asked/answered:** open Zenlytic and check your conversation history — MCP conversations appear there just like conversations started in the app.
