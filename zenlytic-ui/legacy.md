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

# Unsupported Chats

The Zenlytic web application currently supports `v2` conversations and proactive agents (workflows). For various reasons that we try to prevent from impacting your experience, a previous conversation may become no longer supported to continue running. These reasons include:
- new workspace preferences and network security rules
- changes to underlying LLM agent availability and compatibility
- planned updates to Zenlytic services
- unrecoverable errors that occur during runtime

While you can still navigate to unsupported conversations, interact with their tool call contents, and download linked files and data, unsupported conversations will have a banner at the bottom of the screen preventing access to the chat input. In order to continue the unsupported conversation with new follow-up messages, the conversation must be migrated to the latest version.

### How To Migrate An Unsupported Chat

1. From the unsupported conversation banner, select a model and click the Submit button to migrate the unsupported conversation into a supported conversation.

- The dropdown list of agent models will only contain the models that are compatible with the current conversation and the latest version of Zenlytic.
- When the Submit button is pressed, a new conversation will be created from each user message as they are re-played with the selected agent model.
- The chat input will become available again when Zoë has finished running.
- The unsupported conversation will not be automatically deleted once it has been migrated.

![Unsupported Conversations](../.gitbook/assets/unsupported_conversations.png)