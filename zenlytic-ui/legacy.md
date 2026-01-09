---
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
---

# Unsupported Conversations

The Zenlytic web application currently supports `v2` conversations and workflows. For various reasons, a previous conversation may become no longer supported to continue. These reasons include:
- updated workspace preferences and network security rules
- changes to underlying LLM model availability and compatibility
- updates to Zenlytic services

While you can still navigate to unsupported conversations, interact with their tool calls and contents, and download linked files and data, unsupported conversations will have a banner on the bottom of the screen preventing access to the chat input. In order to continue the unsupported conversation with new messages, select a new LLM model and click the Arrow button to migrate the unsupported conversation into a supported conversation. The dropdown list of LLM models will only contain the models that are compatible with the current conversation and latest version of Zenlytic. When the Arrow button is pressed, a new conversation will be created from each user message as it is re-played with the new LLM model. The chat input will become available again when Zoe has finished running.

![Unsupported Conversations](../.gitbook/assets/unsupported_conversations.png)