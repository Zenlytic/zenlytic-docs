# Artifact Folders

Artifact folders help teams organize saved artifacts into shared workspace areas. Use folders for artifacts that should be managed by a team, department, project, or recurring business process.

Folders are part of the Artifacts page. They sit alongside personal artifacts, but they change how access works: once an artifact is in a folder, the folder controls who can access it.

## Personal artifacts and folder artifacts

Artifacts can be in one of two states:

| State | What it means | How access works |
| ----- | ------------- | ---------------- |
| **Personal artifact** | The artifact does not live inside a folder. It can be shared directly with users or groups. | The creator, workspace admins, and direct shares can access it. |
| **Folder artifact** | The artifact has been moved into a workspace folder. | The folder's permissions control access. Direct artifact shares do not apply. |

An artifact can only live in one folder at a time. Moving it to another folder changes which folder controls access.

{% hint style="warning" %}
When you move a personal artifact into a folder, Zenlytic removes its direct artifact shares. Anyone who needs access must have access to the destination folder.
{% endhint %}

## When to use folders

Use folders when an artifact should be managed as part of a shared collection instead of one person's personal artifact.

Common patterns include:

* **Department folders** such as Finance, Sales, Marketing, or Customer Success.
* **Executive reporting folders** for artifacts used in weekly or monthly business reviews.
* **Project folders** for artifacts connected to a launch, analysis sprint, or cross-functional initiative.
* **Operational folders** for dashboards, documents, and spreadsheets that several people need to revisit.

If an artifact is experimental, private, or only shared with a few people temporarily, keep it personal until it is ready for a shared folder.

## Folder structure

Artifact folders are flat in the current release. You can create workspace-level folders, but you cannot create folders inside folders.

This means:

* A folder can contain artifacts.
* A folder cannot contain another folder.
* Each artifact can be in one folder, or in no folder.
* Folder names should be clear enough to stand on their own, since there is no nested path for extra context.

## Creating folders

From the Artifacts page, create a folder when you want a shared place for a set of artifacts. Give the folder a short, recognizable name that matches how your team talks about the work.

Good folder names are specific and durable:

* **Finance**
* **Weekly Business Review**
* **Customer Health**
* **FY26 Planning**

Avoid vague names like **Reports**, **Stuff**, or **Shared** unless your workspace has a clear convention for them.

## Moving artifacts into folders

Moving an artifact into a folder means the folder controls access to that artifact. Before moving, check that the destination folder is shared with the right users and groups.

When an artifact is moved into a folder:

* The artifact appears in that folder.
* The artifact inherits the folder's access.
* Direct shares on the artifact are removed.
* Users who do not have folder access lose access to the artifact.
* Users who have folder access may gain access, depending on their folder level.

This is useful when you are promoting a personal artifact into a shared team space. It is also the main behavior to review before moving sensitive artifacts.

## Worked example

Suppose Dana creates a personal artifact called **FY26 Revenue Dashboard** and shares it directly with Marco.

Later, Dana moves the artifact into the **Finance** folder:

* The artifact becomes a folder artifact.
* Marco's direct share is removed.
* Anyone with access to the **Finance** folder can access the artifact.
* Anyone without access to the **Finance** folder cannot access the artifact, even if they had a direct share before.

If Priya is an **Owner** on the **Finance** folder, Priya can manage the folder and its artifact permissions. If the **Finance Team** group is a **Viewer** on the folder, everyone in that group can open the artifact but cannot manage folder sharing.

If Dana later moves **FY26 Revenue Dashboard** into the **Executive Reporting** folder, the Finance folder permissions no longer apply. The artifact immediately uses the **Executive Reporting** folder permissions instead.

## Moving artifacts between folders

Moving an artifact from one folder to another switches which folder controls access. The artifact no longer uses the old folder's permissions and immediately uses the new folder's permissions.

Before moving between folders, confirm:

* The destination folder has the intended audience.
* Any users who still need access are included directly or through a workspace group.
* The new folder's access level is appropriate for what users should be able to do.

## Moving artifacts out of folders

Moving an artifact out of a folder makes it personal again. The person who moves it becomes the artifact owner, and folder permissions no longer apply.

Direct shares are not restored when an artifact is moved out of a folder. If other users still need access, share the personal artifact again after moving it.

## Deleting folders

You can delete a folder only after its artifacts have been moved elsewhere. This prevents accidental permission changes for artifacts that still need a home.

Before deleting a folder:

* Move artifacts to another folder if they should remain shared.
* Move artifacts out of folders if they should become individually owned.
* Confirm that the folder is no longer part of your team's reporting or review process.

## Related pages

* [Artifacts](artifacts.md) - creating, editing, refreshing, delivering, and publishing artifacts
* [Artifact Folder Permissions](artifact-folder-permissions.md) - how folder access levels work
* [Workspace Groups and Permissions](workspace_groups_and_permissions.md) - creating groups for shared access
