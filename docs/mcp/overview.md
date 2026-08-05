---
description: >-
  MCP works in both directions in Zenlytic — connect Zoë out to external
  tools, or connect your own AI tools in to Zenlytic.
---

# MCP Overview (Experimental)

The [Model Context Protocol](https://modelcontextprotocol.io) (MCP) is an open standard for exposing tools to LLM-powered agents. Zenlytic supports MCP in both directions, depending on which side you want Zenlytic to play:

* **[MCP Client](client.md)** — Zoë connects *out* to external MCP servers (Tableau, Snowflake, dbt, GitHub, and more), so she can pull data and trigger workflows from other systems directly from the Zenlytic chat experience.
* **[MCP Server](connecting-to-zenlytic.md)** — your own AI tools (Claude Desktop, Claude Code, ChatGPT, Cursor, GitHub Copilot) connect *in* to Zenlytic's MCP server to ask questions and query your governed business data.

```mermaid
flowchart LR
    subgraph mcpclient[MCP Client: Zoe connects out]
        Zoe[Zoe, Zenlytic]
        Ext[External MCP Servers: Tableau, Snowflake, dbt, GitHub]
        Zoe -->|tools/call| Ext
    end

    subgraph mcpserver[MCP Server: AI tools connect in]
        AITool[Your AI Tool: Claude, Cursor, ChatGPT]
        ZenServer[Zenlytic MCP Server]
        AITool -->|ask_zoe| ZenServer
    end
```
