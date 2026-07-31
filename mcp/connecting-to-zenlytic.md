---
description: >-
  Connect AI tools like Claude Desktop, Claude Code, Cursor, GitHub Copilot,
  and ChatGPT to Zenlytic's MCP server so they can query your business data
  directly.
---

# MCP Server

Zenlytic supports the [Model Context Protocol (MCP)](https://modelcontextprotocol.io), which lets AI tools like **Claude Desktop**, **Claude Code**, **Cursor**, **GitHub Copilot**, and **ChatGPT** ask Zenlytic questions about your business data directly — no copy-pasting numbers back and forth. Once connected, you can ask your AI assistant things like "What was our revenue last quarter, broken out by region?" and it will query Zenlytic's governed semantic layer and return a real answer, grounded in your actual metrics.

This guide walks through connecting an MCP client to Zenlytic and what to expect once you do.

> This is the reverse of [MCP Client](client.md): here, **Zenlytic is the MCP server** and your AI tool is the client. If you're instead looking to connect Zoë to an external MCP server, see [MCP Client](client.md).

## What you get

Zenlytic exposes one tool to MCP clients: **`ask_zenlytic`**. Your AI assistant calls this tool whenever you ask it a question that requires querying your business data. Behind the scenes, it:

* Starts (or continues) a Zenlytic conversation with your question
* Waits for Zenlytic's AI analyst to answer, including running any needed queries
* Returns the answer, a link back to the full conversation in the Zenlytic app, and any resulting data/charts

Every conversation started this way shows up in Zenlytic's conversation history like any other, tagged as an **MCP** conversation, so you (and your workspace admins) can always see what was asked and how it was answered.

## Before you start

You'll need:

* A Zenlytic account with access to the workspace you want to query
* Chat permission in that workspace
* An MCP-capable client (Claude Desktop, Claude Code, Cursor, GitHub Copilot, ChatGPT, or similar)
* Zenlytic's MCP URL for your workspace, typically `https://<your-zenlytic-domain>/mcp` (ask your workspace admin if you're not sure)

## Option 1: Connect with OAuth (recommended for most clients)

If your client supports MCP connectors with OAuth (this includes Claude Desktop, Claude.ai, Claude Code, Cursor, VS Code/GitHub Copilot, and ChatGPT Developer mode), this is the easiest path — you don't need to generate or manage any tokens yourself.

1. In your MCP client, add a new connector/server pointing at Zenlytic's MCP URL (ask your workspace admin for the exact URL, typically something like `https://<your-zenlytic-domain>/mcp`).
2. Your client will open a browser window and redirect you to Zenlytic's login page.
3. Log in (if you aren't already), then pick the workspace you want to connect.
4. Approve the connection. Your client is now authorized — you won't need to log in again unless you revoke access.

## Option 2: Connect with a Personal Access Token (for static-config clients or when OAuth isn't available)

Some clients don't support the OAuth flow and instead want a static token in their config file.

1. In Zenlytic, go to **Workspace Settings → Personal Access Tokens** (`/workspace-settings/personal-access-tokens`).
2. Click **Create token**, give it a name (e.g. "Cursor MCP"), and save it.
3. **Copy the token immediately** — it's only shown once, right after creation.
4. Add it to your MCP client's config as a bearer token. For example:

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

5. Restart or reload your MCP client so it picks up the new server.

Treat this token like a password — anyone with it can query Zenlytic on your behalf within your workspace's permissions. You can revoke it any time from the same Personal Access Tokens page.

## Connecting from popular clients

The steps above are general — each client has its own place to add a connector and its own quirks. Follow the guide for your client:

* [Claude Desktop / Claude.ai](claude-desktop.md)
* [Claude Code](claude-code.md)
* [Cursor](cursor.md)
* [GitHub Copilot (VS Code)](github-copilot.md)
* [ChatGPT](chatgpt.md)

## Using it

Once connected, just ask your AI assistant a data question naturally — for example:

> "Ask Zenlytic what our top 5 customers by revenue were last month."

Your assistant will recognize this needs live data, call `ask_zenlytic`, and return the answer along with a link you can click to open the full conversation (and any charts or query results) in Zenlytic.

If your token is scoped to more than one workspace, you may occasionally be asked to specify which workspace a question applies to.

## Troubleshooting

* **"Unauthorized" or repeated login prompts:** your token may have expired or been revoked. Generate a new Personal Access Token, or re-run the OAuth connection flow.
* **Client can't find the server:** double-check the MCP URL with your workspace admin — it's a dedicated endpoint, separate from the main Zenlytic app URL.
* **Nothing happens for a while, then it works:** complex questions can take longer to answer while Zenlytic runs the underlying query — this is expected for questions involving large or complex queries.
* **Not sure what got asked/answered:** open Zenlytic and check your conversation history — MCP conversations appear there just like conversations started in the app.
