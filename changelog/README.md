---
description: What's new in Zenlytic — product updates, new features, and notable changes.
---

# Changelog

{% updates format="full" %}

{% update date="2026-07-26" tags="new-releases,improvements,fixes" %}
## Proactive Agents for all workspaces

Proactive Agents are now available to all workspaces, plus refreshed signup screens, HTML uploads, and chat and query fixes.

### New features

* **Proactive Agents for all workspaces** — Schedule agents that pull context from your MCP connections and data sources, decide whether a result is worth sending, and alert you by email or Slack only when something matters — not on every run.
* **Create a Proactive Agent from chat** — Save a chat as a Proactive Agent using the conversation title, prompts, and attachments.
* **Share Proactive Agents** — Share agents with users or groups and assign viewer, editor, or owner access.
* **Cancel running agent runs** — Cancel an active Proactive Agent run directly from run history.
* **MCP connections enabled by default for new chats** — Admins can configure an MCP connection to start enabled in each new conversation for users who have access.
* **HTML file uploads** — Upload .html files as context in chat and Proactive Agents.

### Improvements

* **Refreshed signed-out and signup screens** — Signup, workspace invitation, and unauthenticated pages use a cleaner, consistent account flow, and campaign or partner signup links can show tailored copy.
* **More tables in chat answers** — Zoë now uses compact Markdown tables more often when they communicate query results more clearly.

### Bug fixes

* **Welcome-message edits save reliably** — Editing a workspace's chat welcome message enables Save immediately.
* **Wide SQL queries no longer time out** — Very wide queries, including large SELECT \* results, skip a detection step that could previously delay or fail responses.
{% endupdate %}

{% update date="2026-07-19" tags="improvements,fixes" %}
## Refreshed signup flow and smarter documentation search

A refreshed signup flow, smarter Zoë documentation searches, and fixes across artifact sharing, Slack deliveries, and warehouse queries.

### Improvements

* **Updated signup flow** — New-user signup has a revised email/password flow, clearer terms links, and moves profile personalization to after signup.
* **Fewer repeated Zoë documentation searches** — Zoë stops searching product docs once it has an answer, instead of repeating searches.

### Bug fixes

* **Fixed Microsoft Teams sign-in** — Teams users now get the Entra login flow and no longer see a blank screen after signing out.
* **Fixed case-sensitive warehouse queries** — Queries no longer lowercase quoted mixed-case identifiers on Fabric and Synapse, which caused failures on case-sensitive warehouses.
* **Accurate upload-type validation** — The upload picker now matches supported file types, adds .webp and .ppt uploads, removes unsupported RTF, XML, and GIF options, and shows readable errors.
* **Web search preserved across run steps** — Follow-up steps in a run keep the web-search setting instead of dropping it.
* **Artifact sharing dialogs stay open** — Sharing and access-management popovers no longer close prematurely, and focus and scrolling behave correctly.
* **Slack respects workspace web-search policy** — Slack conversations now honor whether web search is enabled for the workspace. (Slack)
* **Longer BigQuery Data Project IDs** — The Data Project ID(s) field accepts the full 256 characters.
* **No duplicate artifact refreshes** — Repeated scheduling actions no longer create duplicate refresh entries.
* **Cleaner new-chat drawers** — Explore and context drawers initialize and clear correctly for deep-linked questions, without leaking prior-chat state.
{% endupdate %}

{% update date="2026-07-12" tags="new-releases,improvements,fixes" %}
## Zoë looks up product docs before answering

Workspace switching from Add Data, Zoë checking product docs before answering how-to questions, a refreshed login and signup experience, and fixes across MCP connection errors, data model reviews, daily refresh scheduling, SQL generation, and large-workspace exports.

### New features

* **Zoë looks up product docs** — Zoë checks Zenlytic's product documentation before answering how-to questions, so answers reflect what's actually documented. (Slack, docs)

### Improvements

* **Switch workspaces from Add Data** — Users with access to multiple workspaces can now switch workspaces directly from the Add Data flow.
* **Refreshed login and signup pages** — Login and signup pages now show an updated brand panel with customer logos and security badges.
* **Admin chat filter for Proactive Agent runs** — Admin chat lists can now include or exclude Proactive Agent run conversations when filtering.

### Bug fixes

* **Clearer MCP connection errors in chat** — When an MCP connection is stale or misconfigured, chat now shows a clear error telling you to refresh the connection instead of hanging or retrying silently.
* **Data model reviews skip deprecated Topics** — Data model review guidance no longer recommends legacy Topics unless the project actually contains topic files. (Data Model Editor)
* **Daily refresh no longer blocks chat** — Background daily refresh jobs are now capped so they don't crowd out chat tasks, reducing queued or expired requests.
* **Fixed duplicate-column SQL errors** — Access-filter SQL generation no longer produces ambiguous-column errors from duplicate quoted or cased references to the same column. (Data Model Editor)
* **Fixed a Claude runtime error** — Resolved a runtime error that could affect some Claude-powered chat and agent runs.
* **More reliable large-workspace exports** — Screenshot, PDF, and CSV rendering for large dashboards and questions is more reliable and less likely to crash.
{% endupdate %}

{% update date="2026-07-01" tags="new-releases,improvements" %}
## Artifact folders are generally available

Artifact folders are now generally available, along with table-selection, skill-error, and skill-metadata improvements.

### New features

* **Organize artifacts into folders** — Browse artifacts in table or gallery view, organize them into workspace folders, and manage folder-based access.

### Improvements

* **More visible table selection** — Row-selection checkboxes now have stronger contrast and stay visible on mobile gallery cards.
* **Clearer skill and code error messages** — Zoë now tells you when a failure comes from a workspace-authored skill or uploaded code, including the skill or file and the actual error. (Data Model Editor)
* **Git-backed skill metadata** — Git-backed workspace skills now show their name, description, required status, and file location in Zoë's skills list. (Data Model Editor)
{% endupdate %}

{% update date="2026-06-30" tags="new-releases,improvements" %}
## Claude Sonnet 5 in the model picker

Claude Sonnet 5 in the model picker, plus clearer MCP connection error messages.

### New features

* **Claude Sonnet 5** — Sonnet 5 is now the default active model in the chat model picker; existing chats are unaffected.

### Improvements

* **Clearer MCP setup errors** — MCP server connection and setup failures now show specific, useful error messages instead of a generic failure.
{% endupdate %}

{% update date="2026-06-26" tags="improvements,fixes" %}
## Expanded file uploads and smarter warehouse location handling

Expanded file upload support, smarter warehouse location handling, and SSO and MCP fixes.

### Improvements

* **Expanded file uploads** — Upload macro-enabled Excel files (.xlsm) and structured text and code files (.py, .json, .md) across chat, agents, workflows, document preview, and file analysis.
* **Warehouse location handling** — Zoë treats "schema," "database," "catalog," and "dataset" more flexibly and retries alternate warehouse hierarchy levels before reporting data as unavailable.

### Bug fixes

* **Vanity-host SSO redirects** — Vanity-domain auth redirects work correctly for EU and other non-app.zenlytic.com environments.
* **MCP tool discovery** — MCP server tool discovery completes the initialization handshake and parses SSE responses correctly, fixing cases where connected MCP servers showed no tools.
{% endupdate %}

{% update date="2026-06-25" tags="improvements,fixes" %}
## Shared-chat and MCP connection fixes

Shared-chat copy and MCP connection fixes.

### Improvements

* **Shared chat copy navigation** — Copying a shared chat now opens the copied conversation through in-app navigation.

### Bug fixes

* **MCP protocol version header** — MCP connections send the negotiated MCP-Protocol-Version header after initialization, fixing tool calls against servers that require it. (API)
{% endupdate %}

{% update date="2026-06-24" tags="new-releases,improvements,fixes" %}
## Source-data citations on dashboards

Source-data citations on dashboards, Context Manager in chat, plus upload and artifact fixes.

### New features

* **Source-data citations for dashboards** — On request, dashboard visuals can show source-data badges, an underlying-rows view, and CSV downloads.

### Improvements

* **Context Manager in chat** — Context Manager now opens in a chat-side drawer by default, so you stay in the conversation.

### Bug fixes

* **Managed MotherDuck uploads** — Stale MotherDuck secrets are cleared automatically, so managed database uploads stop failing as credentials accumulate.
* **Artifact thumbnails in sandboxes** — Thumbnails now generate correctly for artifacts created in agent sandboxes.
{% endupdate %}

{% update date="2026-06-23" tags="new-releases,improvements,fixes" %}
## Context Manager reaches more surfaces

Context manager reaches more surfaces, plus sandbox and chat-accuracy fixes.

### New features

* **Context manager across more surfaces** — Context manager now works in chat, the Data Model Editor, and artifact citation and editing.

### Improvements

* **Numeric answer guardrails** — Stronger guidance against reporting numbers that didn't come from tool results.

### Bug fixes

* **Schema visibility in context** — Schemas that weren't appearing in context selection now show up. (Data Model Editor)
* **Sandbox timeouts** — Sandbox soft timeouts now surface instead of being swallowed, so chats don't hang.
* **Nested sandbox restore** — Nested directories are restored correctly during sandbox file restore.
{% endupdate %}

{% update date="2026-06-19" tags="new-releases,fixes" %}
## Org-admin management and SQL interpretability

Org-admin management and an optional SQL interpretability toggle.

### New features

* **Organization admin management** — Workspace Manager now lets org admins view and manage other organization admins.
* **SQL interpretability toggle** — New workspace setting to turn off SQL interpretability in chat.

### Bug fixes

* **Discover fixes** — Resolves runtime issues in Discover.
{% endupdate %}

{% update date="2026-06-17" tags="improvements,fixes" %}
## Scheduling, picker, and permissions improvements

Scheduling, picker, and permissions improvements, plus chat and SSO fixes.

### Improvements

* **Model and database pagination** — Large model and database lists page in instead of loading all at once. (Data Model Editor)
* **Larger scheduled artifact modal** — More room in the schedule-artifact modal.
* **Restricted-permission messaging** — Clearer message for users with restricted permissions instead of a blank or failed state.

### Bug fixes

* **Deleted chats filter** — Deleted conversations now appear under All Chats → Deleted.
* **Sandbox file re-uploads** — Re-uploading a file with the same name overwrites the old sandbox copy instead of keeping stale content.
* **SSO group assignment** — Re-adding SSO users to groups no longer creates duplicate or errored adds.
{% endupdate %}

{% update date="2026-06-16" tags="new-releases" %}
## Try Zenlytic with sample data

A quicker way to try Zenlytic with sample data.

### New features

* **Demo datasets in self-serve** — Self-service setup now offers demo datasets to start from.
{% endupdate %}

{% update date="2026-06-15" tags="improvements,fixes" %}
## Connection setup polish

Connection setup polish.

### Improvements

* **Trino HTTP scheme field** — Clearer placeholder text for the Trino HTTP scheme field.

### Bug fixes

* **BigQuery dataset field** — Fixes the dataset textbox in the BigQuery browse step. (Data Model Editor)
{% endupdate %}

{% update date="2026-06-12" tags="new-releases,improvements,fixes" %}
## Live editing and onboarding updates

Live editing, onboarding, sharing, and connection fixes.

### New features

* **Select/inspect toggle in the HTML editor** — Switch between select and inspect modes in the live HTML editor.
* **Department in onboarding** — Onboarding now collects the user's department.

### Improvements

* **Connection name validation** — Tighter validation for connection names.
* **Artifact save/present behavior** — Clearer guidance on when artifacts are presented versus saved.
* **Regional processing routing** — Workspace processing routes to the matching Vertex region. (API)

### Bug fixes

* **Shared artifact file access** — Files shared through an artifact are now accessible via that artifact.
* **Delete group with shared artifacts** — Deleting a group that has shared artifacts now works.
* **File-link rewriting** — Removes incorrect /mnt/data signed-URL rewriting in conversation display and citations.
* **Fabric quoting** — Fixes quoting issues in Fabric connections. (Data Model Editor)
{% endupdate %}

{% update date="2026-06-10" tags="improvements,fixes" %}
## Recent Updates and citations redesign

Recent Updates and citations redesign, plus several display fixes.

### Improvements

* **Recent Updates redesign** — A reworked Recent Updates experience.
* **Collapsed citations** — Citations collapse into a single, cleaner display.

### Bug fixes

* **Artifact popups** — Artifact iframe popups can open as normal top-level windows.
* **Uploaded image previews** — Fixes broken-image display for images uploaded in chat.
* **Workflow final state** — Fixes a race where a workflow run could show the wrong final state.
* **Remove all users** — Fixes the remove-all-users option in group and user management.
* **Managed table creation** — Prevents query races right after a managed database table is created. (Data Model Editor)
* **Duplicate table error** — Clearer error when YAML defines duplicate tables. (Data Model Editor)
{% endupdate %}

{% update date="2026-06-09" tags="new-releases,improvements,fixes" %}
## MCP, model, and reliability updates

A large batch of MCP, model, and reliability updates.

### New features

* **MCP for proactive agents** — Proactive agents can now use MCP connections.
* **Font uploads in skills** — Skills accept .ttf and .otf font uploads.

### Improvements

* **Chat starts responding sooner** — Reduced time to first token when a chat begins.
* **GPT model lineup** — Updated GPT model choices.
* **MCP tool descriptions** — Clearer connection context in MCP tool descriptions.
* **MCP tool-selection help** — Added tooltip help for MCP tool selection.
* **Stale sandbox warning** — The agent is warned when sandbox context may be stale.
* **Scheduled report context** — Clearer scheduled-report instructions for the agent.
* **Scrollable errors and warnings** — Long error and warning panels are now scrollable. (Data Model Editor)
* **API conversation tagging** — Conversations created through the API are tagged source=api. (API)

### Bug fixes

* **Oversized prompts** — Oversized inputs fail cleanly instead of retrying without effect.
* **MCP connection selector** — Chat MCP connection options use the correct non-admin endpoint.
* **Clarity setup routing** — Clarity workspaces route through the setup-workspace flow.
* **SQL Server casing** — Fixes table-name normalization for SQL Server while preserving Synapse behavior. (Data Model Editor)
* **Context manager tooltip** — Fixes tooltip positioning in the context manager. (Data Model Editor)
* **Artifact CSV recovery** — Missing CSVs are regenerated before an artifact rebuilds.
{% endupdate %}

{% update date="2026-06-04" tags="new-releases,improvements,fixes" %}
## Connectors settings redesign

Connectors settings redesign, BigQuery improvements, and context manager rework.

### New features

* **Connectors settings page** — A redesigned connectors and MCP connections settings page.
* **MCP access management** — Access-management controls in the MCP modal.
* **BigQuery project selector** — Choose a project when browsing BigQuery data. (Data Model Editor)
* **Fabric service-principal auth** — Fabric connections support Microsoft Entra service-principal authentication.

### Improvements

* **Context manager redesign** — A reworked context manager experience. (Data Model Editor)
* **BigQuery multi-project** — Handles multiple BigQuery project IDs when browsing data. (Data Model Editor)
* **Branch selector limit** — Caps branch selector choices so large repos stay usable. (Data Model Editor)
* **Agent list pagination** — Agent lists paginate so they load more reliably.
* **Scheduled artifact copy** — Updated scheduled-artifact and proactive-agent descriptions.

### Bug fixes

* **Long chat titles** — Retries or truncates chat-title generation when a conversation exceeds context limits.
{% endupdate %}

{% update date="2026-06-03" tags="new-releases,improvements,fixes" %}
## Opus 4 and scheduled-delivery run history

Opus 4, scheduled-delivery run history, and context editing settings.

### New features

* **Claude Opus 4** — Opus 4 is available as a model option.
* **Scheduled delivery run history** — A run-history tab for scheduled artifact deliveries.
* **Context editing setting** — A settings-page toggle for context editing.

### Improvements

* **Email attachment limits** — Clearer maximum attachment size in scheduled-delivery emails.
* **Proactive agent test runs** — Better storage and display of proactive agent test runs.

### Bug fixes

* **Artifact citations** — Restores citation generation for artifacts.
{% endupdate %}

{% endupdates %}
