---
description: >-
  MCP works in both directions in Zenlytic — connect Zoë out to external
  tools, or connect your own AI tools in to Zenlytic.
---

# MCP Overview

The [Model Context Protocol](https://modelcontextprotocol.io) (MCP) is an open standard for exposing tools to LLM-powered agents. Zenlytic supports MCP in both directions, depending on which side you want Zenlytic to play:

* **[MCP Client](client.md)** — Zoë connects *out* to external MCP servers (Tableau, Snowflake, dbt, GitHub, and more), so she can pull data and trigger workflows from other systems directly from the Zenlytic chat experience.
* **[MCP Server](connecting-to-zenlytic.md)** — your own AI tools (Claude Desktop, Claude Code, ChatGPT, Cursor, GitHub Copilot) connect *in* to Zenlytic's MCP server to ask questions and query your governed business data.

```mermaid
flowchart LR
    subgraph client["MCP Client — Zoë connects out"]
        direction LR
        Zoe(["Zenlytic"]) -->|"tools/call"| Ext[["External MCP Servers<br/>Tableau · Snowflake · dbt · GitHub..."]]
        Ext -->|"results"| Zenlytic
    end

    subgraph server["MCP Server — AI tools connect in"]
        direction LR
        AI(["Your AI Tool<br/>Claude · Cursor · ChatGPT..."]) -->|"ask_zenlytic"| ZenSrv[["Zenlytic MCP Server<br/>governed semantic layer"]]
        Zenlytic MCP Server -->|"answer + data"| AI
    end
```
