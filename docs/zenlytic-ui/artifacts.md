---
description: >-
  Create, organize, share, and rebuild the artifacts Zoë builds across your
  conversations.
---

# Artifacts

Artifacts are rich, interactive outputs that Zoë creates for you. They can be a wide variety of types — interactive apps, written documents, data spreadsheets, slide presentations, and more. Use the Artifacts page to organize, revisit, and share everything Zoë has built across your conversations.

## What makes up an artifact

Each artifact bundles together four components:

* **Output file** — The document you see and share (an HTML dashboard, chart, spreadsheet, PDF, or image).
* **Source code** — The code Zoë used to generate it.
* **Data** — The [Live Queries](artifacts.md#live-queries) an artifact runs to get its data, and any CSVs or uploaded files included in it.
* **Memory** — An auto-generated summary of the artifact's purpose, context, and change history.

## Live Queries

Live Queries keep an artifact's numbers current. Dashboards, charts, and other HTML artifacts don't store the results Zoë pulled — they store the queries behind them and re-run those queries against your warehouse every time you open the artifact. Open a dashboard Zoë built last month and you see this morning's data, with no action on your part.

{% hint style="info" %}
**Live Queries run with your permissions.** When you open an artifact, its Live Queries run as you, scoped to the data you're allowed to see. Two people can open the same artifact and see different numbers, and you will never see data in an artifact that you couldn't query yourself.
{% endhint %}

Because Live Queries only run inside Zenlytic, an artifact that uses them can't be [published to the web](artifacts.md#publishing-to-the-web).

### Interactive controls

Zoë can build controls into an artifact and templatize the SQL behind it, so the controls feed the query directly instead of just filtering numbers that were already fetched. Change a control and the Live Queries it drives re-run with your new selections, and every tile fed by those queries reloads in place.

Ask for the controls you want and Zoë wires them into the SQL — date ranges and presets, time granularity, a comparison period, or filter menus for the dimensions you care about. In the example below, the artifact offers date range presets, a **Day**/**Week**/**Month**/**Qtr** granularity toggle, a **Prior period** or **Last year** comparison, and searchable multi-select menus for account, tier, company size, role, and feature area.

<figure><img src="../.gitbook/assets/artifact-interactive-controls.png" alt="An artifact header with date range presets, a granularity toggle, comparison options, and filter menus, with a company size filter open and the tiles below reloading"><figcaption><p>Changing a filter re-runs the Live Queries behind every affected tile</p></figcaption></figure>

Selections you've made appear as chips beneath the controls, so you can see the current state of the artifact at a glance and remove any one of them, or click **Reset all** to start over. The header shows a **Data as of** timestamp with a **Refresh** button, so you can re-run everything without changing a selection.

Because the queries are parameterized rather than rewritten, you're exploring inside the analysis Zoë already built — no new chat turn, and no rebuild. When you want the analysis itself to change, ask Zoë in a chat instead.

### Making a query static

Live Queries are the default for HTML artifacts. Unless you say otherwise, Zoë builds dashboards, charts, and apps to re-query when they open.

If you'd rather have fixed numbers, ask Zoë to make the query static. She bakes the results into the artifact when she builds it, so it shows the same numbers every time anyone opens it. Reach for this when you want a snapshot that can't move underneath you — a month-end figure you're circulating for review, or an artifact you want to [publish to the web](artifacts.md#publishing-to-the-web), which only works without Live Queries.

Asking Zoë to make a static query live again works the same way. Either change is an edit to the artifact, so it creates a new version in the [update history](artifacts.md#update-history).

### Output types without Live Queries

Presentations (`.pptx`), spreadsheets (`.xlsx`), PDFs, and images are finished files — they can't run a query when someone opens them, so their numbers are captured when Zoë builds them. Reopening a presentation next quarter shows the same numbers it showed the day it was created.

To bring one up to date, use [Auto-Rebuild](artifacts.md#auto-rebuild) to regenerate it on a schedule, or click **Rebuild Now** to regenerate it immediately.

## Organizing artifacts with folders

Artifact folders let teams organize saved artifacts into shared workspace areas. A personal artifact can be shared directly with users or groups; once it is moved into a folder, the folder controls who can access it.

For more on how folders work, see [Artifact Folders](artifact-folders.md). For access levels, direct shares, groups, and troubleshooting, see [Artifact Folder Permissions](artifact-folder-permissions.md).

## Artifacts in chat

Zoë creates artifacts automatically whenever a visual output would be helpful — or when you ask her to build something. Artifacts appear inline in the chat, and you can click on one to expand it in the side drawer.

<figure><img src="../.gitbook/assets/artifact-in-chat.png" alt=""><figcaption></figcaption></figure>

If an artifact is something you'd like to keep and come back to, click **Save to my artifacts**. The artifact will then appear in your Artifacts gallery alongside everything else you've saved.

<figure><img src="../.gitbook/assets/artifact-save-to-gallery.png" alt=""><figcaption></figcaption></figure>

## Creating a new artifact

You can also create artifacts directly from the Artifacts page. Click the **+ Create New Artifact** button in the upper right corner. A dropdown lets you choose the type of artifact to create:

* **App** — An interactive application.
* **Document** — A rich text document.
* **Spreadsheet** — A data spreadsheet.
* **Presentation** — A slide presentation.
* **Other** — Any other artifact type.

Selecting a type opens a new chat with Zoë where you can describe what you'd like to create.

<figure><img src="../.gitbook/assets/artifact-create-dropdown.png" alt=""><figcaption></figcaption></figure>

## Opening and editing an artifact

Click any artifact on the Artifacts page to open it in a side drawer. From the drawer you can preview the artifact, share it with others in your organization, or schedule it to rebuild automatically.

<figure><img src="../.gitbook/assets/artifact-drawer.png" alt=""><figcaption></figcaption></figure>

To edit an artifact, click **Edit in a new chat** from the three-dot menu in the drawer header. This opens a new chat with the artifact attached, so you can tell Zoë what you'd like to change. Zoë will update the artifact and a new version will appear in the [update history](artifacts.md#update-history).

<figure><img src="../.gitbook/assets/artifact-edit-in-chat.png" alt=""><figcaption></figcaption></figure>

## Visual Editor

{% hint style="info" %}
**The Visual Editor is only available for HTML-based artifacts.** Use it for artifacts like dashboards, charts, and other custom apps.
{% endhint %}

Open the **Visual Editor** from the artifact menu bar to make targeted changes directly on the artifact. Move your mouse around the document to see a blue rectangle around the element you are selecting. Click the element you want to change, write a short description of the change, and click **Queue change**.

<figure><img src="../.gitbook/assets/visual-editor-making-an-edit.png" alt="Visual Editor selection rectangle and Queue change prompt"><figcaption></figcaption></figure>

You can queue up to 20 changes before applying them. Open the queued changes menu to review everything you have queued, edit a change, or remove a change before applying it.

<figure><img src="../.gitbook/assets/visual-editor-queued-changes-menu.png" alt="Queued changes menu with three pending edits"><figcaption></figcaption></figure>

When your queued changes are ready, click **Apply Queued Changes**. Review the updated artifact, then click **Save Changes** if you are happy with the result. Saving creates a new version of the artifact in the [update history](artifacts.md#update-history).

<figure><img src="../.gitbook/assets/visual-editor-saving-changes.png" alt="Updated artifact with unsaved changes and Save Changes button"><figcaption></figcaption></figure>

If you do not like the result, queue more changes and apply them again, or close the Visual Editor without saving.

## Update history

Every artifact uses immutable, append-only versioning — nothing is overwritten or deleted. New versions are created when you edit the artifact and save your changes, or when a scheduled [rebuild](artifacts.md#auto-rebuild) runs. Live Queries pulling fresh data do not create a version; only changes to the artifact itself do.

Click the **Updated** timestamp on an artifact to open its update history. The history panel displays every version of the artifact, letting you time-travel through past states. Each version includes an edit message describing what changed.

From the three-dot menu on any version, you can:

* **View Artifact Memory** — See the context Zoë used when creating that version.
* **Download** — Download the artifact as it existed at that point in time.
* **Edit from this version** — Start a new edit based on an older version of the artifact.

<figure><img src="../.gitbook/assets/artifact-update-history.png" alt=""><figcaption></figcaption></figure>

## Auto-Rebuild

Auto-Rebuild completely regenerates an artifact on a schedule — Zoë re-runs the analysis, regenerates the sources, and saves a new version.

Use it to keep [output types without Live Queries](artifacts.md#output-types-without-live-queries) current, since their numbers won't change on their own. You can also use it on an artifact that does use Live Queries when you want Zoë to revisit the analysis itself, not just the numbers — to simply see the latest data, reload the page.

Click the **Auto-Rebuild Off** button in the artifact drawer header to open the Auto-Rebuild settings. Toggle **Enable Auto-Rebuild**, then configure:

* **Frequency** — How often to rebuild (daily, weekly, monthly, or a custom cron expression).
* **Time** — What time of day to run the rebuild, shown in your local timezone.
* **Instructions** — Optional directions for Zoë to follow during each rebuild. For example: "Highlight any outliers in the data and write short blurbs about their trends."

Click **Save** to apply the schedule.

<figure><img src="../.gitbook/assets/artifact-auto-refresh.png" alt=""><figcaption></figcaption></figure>

To rebuild immediately without waiting for the next scheduled time, click **Rebuild Now**.

Every rebuild appears in the artifact's [update history](artifacts.md#update-history), so you can see how the artifact has changed over time.

## Delivery

Artifacts can be delivered on a recurring schedule to **email** or **Slack**. A single artifact can have multiple delivery schedules — for example, email to leadership on Mondays and Slack to #data-team daily.

Before each delivery, Zenlytic re-runs any Live Queries in the artifact and renders it with the results, so recipients get current data. Those queries run as the person who owns the delivery schedule, using that person's permissions — so everyone on the schedule sees the schedule owner's view of the data. Keep that in mind when adding recipients whose own access is narrower.

### Email delivery

* Inline image preview of the artifact. Wide or scrollable content may be cropped in the preview.
* Optional attachment of the artifact’s current output file in its original format. Attachments are not converted; HTML remains HTML, and PDF is attached only when the output is already a PDF. Artifacts that use Live Queries are not attached — see [Delivering artifacts with Live Queries](artifacts.md#delivering-artifacts-with-live-queries).
* Optional “View in Zenlytic” link. Recipients must have access to the artifact.

### Slack delivery

* Message with the artifact name and description.
* Optional file upload to the channel.

### Delivering artifacts with Live Queries

An artifact's file can't run its Live Queries outside Zenlytic, so deliveries skip the attachment even when **Include attachments** is on. Recipients get the preview image and a **View in Zenlytic** link instead, along with a short note explaining why no file was attached. Opening the artifact from that link runs the Live Queries with the recipient's own permissions.

### Run history

From the **Schedule Artifact Delivery** modal, click the **Run History** tab to review every past delivery run for the artifact. Use the run history to confirm that a scheduled delivery went out, troubleshoot a missed send, or jump back to the chat that produced a particular delivery.

Each row in the table represents a single run and shows:

* **Schedule** — The delivery schedule that triggered the run.
* **Triggered** — When the run started, in your local timezone.
* **Finished** — When the run completed, with the total duration in parentheses. A dash (`—`) means the run is still in progress.
* **Status** — The current state of the run: **Processing** while it is running, **Delivered** once it has been sent, or an error state if it failed. Hover over the "Failed" chip to see technical details about the issue.
* **Chat** — A **View chat** link that opens the Zoë conversation behind the run, so you can inspect what Zoë did to generate and send the delivery.

Use the search bar above the table to filter by schedule name, and use the column headers to sort or filter — for example, sort by **Triggered** to see the most recent runs first, or filter **Status** to show only failed runs.

Run history covers deliveries that rebuild the artifact. Deliveries that only re-run Live Queries and re-render the artifact have no Zoë conversation behind them, so they don't appear in the table.

<figure><img src="../.gitbook/assets/artifact-delivery-run-history.png" alt="Run History tab in the Schedule Artifact modal, listing past delivery runs with their triggered time, finished time, status, and a link to the originating chat"><figcaption><p>The Run History tab showing recent delivery runs for an artifact</p></figcaption></figure>

## Sharing and permissions

Click the **Share** button in the artifact drawer to share an artifact with others in your organization. From the Share tab, select a user group and assign a permission level. Click **+ Add Group** to grant access to additional groups.

<figure><img src="../.gitbook/assets/artifact-share.png" alt=""><figcaption></figcaption></figure>

### Access levels

| Role       | Capabilities                                                          |
| ---------- | --------------------------------------------------------------------- |
| **Owner**  | Full control — edit, delete, share, configure Auto-Rebuild and delivery |
| **Editor** | Edit name and description, create new versions                        |
| **Viewer** | Read-only access                                                      |

You can share with workspace groups (including "All Users") or with individual users. Workspace admins always have access.

These access levels control who can open and manage an artifact. They don't widen anyone's data access: when someone opens an artifact, its [Live Queries](artifacts.md#live-queries) run with that person's own data permissions, so they only see data they could query themselves.

## Publishing to the web

{% hint style="warning" %}
**You can't publish an artifact that uses Live Queries.** A published artifact is served outside Zenlytic to people who may not have a Zenlytic account, so there is no way to run those queries or apply anyone's data permissions — it would publish as an empty shell. Publishing is disabled for artifacts that use Live Queries, and the **Publish** button explains why when you hover it.

To publish something to the web, ask Zoë for a version without Live Queries, or publish an [output type that doesn't use them](artifacts.md#output-types-without-live-queries).
{% endhint %}

To make an artifact publicly accessible, click the **Share** button and open the **Publish** tab. Click **Publish** to generate a unique public URL and an embed script that anyone can use to access the artifact — no Zenlytic account required.

<figure><img src="../.gitbook/assets/artifact-publish.png" alt=""><figcaption></figcaption></figure>

Once published, the artifact displays a **Public** chip on the Artifacts page. A public link and an iframe embed script are provided so you can share the artifact or embed it on another site.

<figure><img src="../.gitbook/assets/artifact-published.png" alt=""><figcaption></figcaption></figure>

Editing or rebuilding an artifact does not automatically update the published version. When you're ready for the latest version to go live, click **Publish latest version**. To remove public access entirely, click **Unpublish**.

If you edit a published artifact and the new version starts using Live Queries, the existing public link keeps working — it's a snapshot of the version you published — but **Publish latest version** is disabled, because the newer version can't run outside Zenlytic.

<figure><img src="../.gitbook/assets/artifact-publish-new-version.png" alt=""><figcaption></figcaption></figure>

## Artifact memory

Every artifact has an artifact memory — a detailed summary of the artifact's purpose, your instructions, version history, and key context. Zoë references this memory whenever you work with the artifact in a chat, so she understands what the artifact is, what you like and dislike about it, and how it has evolved over time.

To view an artifact's memory, click the three-dot menu in the artifact drawer header and select **View Artifact Memory**.

<figure><img src="../.gitbook/assets/artifact-memory.png" alt=""><figcaption></figcaption></figure>

## Sources

Click the **Sources** button in the artifact drawer header to see every data source behind an artifact and how fresh each one is.

<figure><img src="../.gitbook/assets/citations-artifacts.png" alt="Sources panel open in the artifact drawer, listing the data sources behind the dashboard"><figcaption><p>The Sources panel listing an artifact's data sources</p></figcaption></figure>

Sources are grouped by how they get their data:

* **Live** — A [Live Query](artifacts.md#live-queries), re-run every time you open the artifact. Updates automatically, so no manual refresh is needed.
* **Static** — Data captured when the artifact was built, such as query result files, uploaded files, and intermediary files Zoë created. It does not refresh, so it may be outdated.

The panel header shows **Data as of** with the time the Live Queries last ran. Click the refresh icon to re-run every Live Query and pull current data without rebuilding the artifact.

### Inspecting a Live Query source

Open a Live Query source to see exactly what it asked your warehouse for. The **Explanation** tab describes the query in plain language and names every field it uses; switch to the **SQL** tab to read the SQL Zenlytic ran. Below the description:

* **Fields** — Each metric and dimension the query selected.
* **Filters** — The filters applied, including the date ranges that define the periods being compared.
* **Results** — The rows the query returned. Search within them, adjust which columns are shown, or click **Download Data** to export them.

The source also reports how many rows came back and how long ago it ran. If a query fails, the source shows the error and a red chip appears on the affected part of the artifact, so a single broken query doesn't take down the rest.

<figure><img src="../.gitbook/assets/artifact-sources-live-query-detail.png" alt="An open Live Query source showing its explanation, fields, filters, and returned rows, with the dashboard tile it feeds spotlighted and marked with a lettered chip"><figcaption><p>A Live Query source opened next to the tile it feeds</p></figcaption></figure>

### Inline sources

Every source is tied to the part of the artifact it powers, so you can trace any number on screen back to the query behind it:

* Hover a source in the list to outline the chart, table, or tile it feeds.
* Open a source to spotlight that element — everything else in the artifact dims, so you can see at a glance how much of the result one query is responsible for.
* While the panel is open, each connected element wears a lettered chip matching its source, letting you read the artifact and the source list side by side.

Because the mapping runs both directions, you can start from a number you want to check and open the source that produced it, or start from a source and see everything it feeds.

Inline sources appear only when the artifact supports them. An older artifact may still list its sources in the panel without tying them to individual elements — rebuild it, or ask Zoë to update it, to get the inline behavior.

### Editing a source

Click **Edit this data source** on a source to change the query behind it. Describe what you want and click **Queue change**. Source edits queue alongside your other [Visual Editor](artifacts.md#visual-editor) changes, so click **Apply Queued Changes** to run them and **Save Changes** to keep the result.

Use the Sources panel to review where an artifact's data came from, confirm how current it is, and verify the numbers behind any part of the result.

## Supported output types

These are formats Zoë can create as artifact outputs. They are not export or email-conversion options.

| Output type                | Data                                                                       |
| -------------------------- | -------------------------------------------------------------------------- |
| HTML apps and dashboards   | [Live Queries](artifacts.md#live-queries) — re-run every time you open it   |
| Charts and visualizations  | [Live Queries](artifacts.md#live-queries) — re-run every time you open it   |
| Spreadsheets (.xlsx)       | Captured at build time                                                     |
| Presentations (.pptx)      | Captured at build time                                                     |
| PDFs                       | Captured at build time                                                     |
| Images                     | Captured at build time                                                     |

Scheduled delivery attaches the output file as-is for output types without Live Queries. Artifacts that use Live Queries are delivered as a preview and a link instead — see [Delivering artifacts with Live Queries](artifacts.md#delivering-artifacts-with-live-queries).

## Limitations

* Artifacts that use Live Queries cannot be published to the web.
* An individual Live Query times out after about 2 minutes.
* Rebuild timeout is 1 hour per run.
* Public share links are pinned to a specific version — they do not auto-update when new versions are created.
