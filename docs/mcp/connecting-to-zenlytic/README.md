---
description: >-
  Connect AI tools like Claude.ai, Claude Code, and
  ChatGPT to Zenlytic's MCP server so they can query your business data
  directly.
---

# MCP Server

Zenlytic supports the [Model Context Protocol (MCP)](https://modelcontextprotocol.io), which lets AI tools like **Claude.ai**, **Claude Code**, and **ChatGPT** ask Zoë questions about your business data directly — no copy-pasting numbers back and forth. Once connected, you can ask your AI assistant things like "What was our revenue last quarter, broken out by region?" and it will query Zenlytic's governed semantic layer and return a real answer, grounded in your actual metrics.

This guide walks through connecting an MCP client to Zenlytic and what to expect once you do.

> This is the reverse of [MCP Client](../client/): here, **Zenlytic is the MCP server** and your AI tool is the client. If you're instead looking to connect Zoë to an external MCP server, see [MCP Client](../client/).

## What you get

Zenlytic exposes one tool to MCP clients: **`ask_zoe`**. Your AI assistant calls this tool whenever you ask it a question that requires querying your business data. Behind the scenes, it:

* Starts (or continues) a Zenlytic conversation with your question
* Waits for Zenlytic's AI analyst to answer, including running any needed queries
* Returns the answer, a link back to the full conversation in the Zenlytic app, and any resulting data/charts

Every conversation started this way shows up in Zenlytic's conversation history like any other, tagged as an **MCP** conversation, so you (and your workspace admins) can always see what was asked and how it was answered.

## Before you start

You'll need:

* A Zenlytic account with access to the workspace you want to query
* Chat permission in that workspace
* An MCP-capable client (Claude.ai, Claude Code, ChatGPT, or similar)
* Zenlytic's MCP URL for your workspace. URL: https://mcp.zenlytic.com/mcp

## Option 1: Connect with OAuth (recommended for most clients)

If your client supports MCP connectors with OAuth (this includes Claude.ai, Claude.ai, Claude Code, and ChatGPT Developer mode), this is the easiest path — you don't need to generate or manage any tokens yourself.

1. In your MCP client, add a new connector/server pointing at Zenlytic's MCP URL
2. Your client will open a browser window and redirect you to Zenlytic's login page.
3. Log in (if you aren't already), then pick the workspace you want to connect.
4. Approve the connection. Your client is now authorized — you won't need to log in again unless you revoke access.

## Option 2: Connect with a Personal Access Token (for static-config clients or when OAuth isn't available)

Some clients don't support the OAuth flow and instead want a static token in their config file.

1. In Zenlytic, go to **Workspace Settings → Personal Access Tokens** (`/workspace-settings/personal-access-tokens`).
2. Click **Create token**, give it a name (e.g. "Claude MCP"), and save it.
3. **Copy the token immediately** — it's only shown once, right after creation.
4. Add it to your MCP client's config as a bearer token. For example:

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

5. Restart or reload your MCP client so it picks up the new server.

## Connecting from popular clients

The steps above are general — each client has its own place to add a connector and its own quirks. Follow the guide for your client:

* [Claude.ai](claude-ai.md)
* [Claude Code](claude-code.md)

## Using it

Once connected, just ask your AI assistant a data question naturally — for example:

> "Hey Zoë, who were our top 5 customers by revenue last month?"

Your assistant will recognize this needs live data, call `ask_zoe`, and return the answer along with a link you can click to open the full conversation (and any charts or query results) in Zenlytic.

## Which data model MCP uses

An MCP conversation is pinned to the branch your workspace is set to when the conversation starts, exactly like a conversation started in the app. If you've switched to a development branch, `ask_zoe` answers from that branch, not production.

To check which branch you're on, ask:

> "Which branch are you using?"

To switch branches, change the branch in the Zenlytic UI, then start a new conversation in your MCP client.

{% hint style="warning" %}
Answers you get through MCP won't match what your users see in production while you're on a development branch. Confirm your branch before you act on an MCP answer, and before you make a change based on one.
{% endhint %}

If your workspace has [Context Editing](../../data-modeling/asking-zoe-for-recommendations.md) disabled, Zoë has no branch awareness and can't answer that question. Open the conversation in Zenlytic using the link `ask_zoe` returns to see which branch it ran against.

After you change a branch's data model, start a new conversation. An ongoing conversation keeps using the version of the model it cached when it started, so your change won't appear until you start a fresh one.

If a new conversation still returns the old model, the change was most likely pushed straight to git rather than made through the UI. See [Cache Refresh](../../data-modeling/cache-refresh.md).
