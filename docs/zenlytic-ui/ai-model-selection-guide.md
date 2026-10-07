---
description: >-
  Choose the right Zoë model based on your data complexity, speed needs, and
  preference for autonomy versus transparency.
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---

# AI Model Selection Guide

Zoë supports multiple AI models that you can switch between using the model dropdown in the chat interface. Each model has different strengths, and the best choice depends on your data model complexity, the types of questions your team asks, and your preference for speed versus depth.

{% hint style="info" %}
**Default model:** Claude Sonnet 5.5 is the default for all workspaces.
{% endhint %}

{% hint style="info" %}
**Using your own model credentials?** Workspaces on enterprise or bring-your-own model credentials may stay pinned to a different model — Sonnet 5.5 is only selected by default where it's actually reachable. Check the model dropdown, or ask your Zenlytic representative, if your workspace shows something else.
{% endhint %}

## Recommended Models

### **Claude Sonnet 5.5 (Default)**

The current default and the right choice for almost every workspace. Sonnet 5.5 outperforms both earlier Sonnet models on the work Zoë does.

**Strengths:**

* **Fastest Sonnet model** — Anthropic reports over 30% faster output generation than Sonnet 5, which shows up directly in how quickly answers come back
* **Fewer round-trips to an answer** — reaches a result in meaningfully fewer tool calls, so multi-step questions resolve with less back-and-forth
* **Strongest instruction adherence** — follows guidance in field descriptions, topic descriptions, and system prompts more reliably than either earlier Sonnet
* **Self-correcting** — detects data quality issues mid-query and resolves them without user intervention
* **Highest query-complexity ceiling** — CTEs, window functions, and cross-table comparisons, with the most consistency on long analytical chains

**Best for:** Everything. Start here, and only switch if you have a specific reason to.

### Claude Sonnet 5

The previous default, still available in the model dropdown.

* Strong general-purpose analytics, superseded by Sonnet 5.5 on speed, consistency, and complex multi-step questions

### Claude Sonnet 4.6

An earlier model, still available for workspaces that standardized on it.

* Less capable than either newer Sonnet on complex joins, messy data, and long analytical chains

## Additional Available Models

### GPT-5.6 Luna

The current OpenAI model in the picker, replacing GPT-5.5. Available for teams that prefer or require an OpenAI model.

**Best for:** Teams with a policy or preference for OpenAI models.

{% hint style="info" %}
**Claude Opus is no longer offered for new chats.** Existing conversations and Proactive Agents pinned to an Opus model continue to work.
{% endhint %}

## How to Choose

| Scenario                                                              | Recommended Model        |
| --------------------------------------------------------------------- | ------------------------ |
| Almost everything                                                     | **Sonnet 5.5** (default) |
| Your team requires an OpenAI model                                    | **GPT-5.6 Luna**         |
| Your workspace is pinned to an earlier model by its own credentials   | **Sonnet 5** or **Sonnet 4.6** |
