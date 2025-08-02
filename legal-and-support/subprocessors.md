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

# Subprocessors

These are the subprocessors we use:

## Cloud Infrastructure

### Amazon Web Services (Cloud provider)

Amazon Web Services hosts our primary cloud infrastructure. This is where all our database, storage, and compute are all hosted.

### Azure (Cloud provider)

Azure hosts our code sandbox infrastructure. It processes data sent to the sandbox and executes code.

## Search and AI Services

### Algolia (Search index)

Algolia manages our search index for dashboards. It indexes metadata on dashboards and the data present on them, allowing the user to search for dashboards.

### OpenAI (LLM Provider)

OpenAI processes data and metadata sent to the LLM to power Zoë's reasoning capabilities.

## Developer and Analytics Tools

### Langfuse (developer logs)

Langfuse processes developer logs associated with requests sent to the LLM. This lets developers better address customer needs.

### LogRocket (developer logs)

LogRocket tracks user sessions so our customer success team and developers can assist when customers run into issues.

### Sentry (developer logs)

Sentry tracks exceptions in our code base and is a central spot the development team can see issues.

## Internal Analytics

### Segment (internal analytics)

Segment tracks user interactions with Zenlytic for our internal analytics.

### Snowflake (internal analytics)

Snowflake is the data warehouse we use for our internal analytics (it is the location of the Segment data).

### Airbyte (internal analytics)

Airbyte is used to transport data for our internal analytics.
