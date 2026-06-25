# Artifact Folder Permissions

Artifact folder permissions control who can see and manage artifacts in workspace folders. They are designed for team-managed content: one folder, one access policy, many artifacts.

Use folder permissions when a group of artifacts should be managed together. Use direct artifact sharing when a personal artifact should be shared without moving it into a folder.

## The permission model

Zenlytic uses two related permission models for artifacts:

| Artifact state | Who controls access | What to manage |
| -------------- | ------------------- | -------------- |
| **Personal artifact** | The artifact owner, workspace admins, and direct artifact shares | Share the artifact with users or workspace groups. |
| **Folder artifact** | The folder the artifact is in | Share the folder with users or workspace groups. |

When an artifact is moved into a folder, folder permissions control access to that artifact. Direct artifact shares are removed when the move happens.

{% hint style="info" %}
If someone could access a personal artifact before it was moved into a folder, they need access to the destination folder to keep seeing it after the move.
{% endhint %}

## Access levels

Folder permissions use three access levels you can assign: **Viewer**, **Editor**, and **Owner**. Workspace admins and organization admins may also see **Admin** access, which comes from their workspace role and is not assigned from the folder sharing UI.

| Level | What users can do |
| ----- | ----------------- |
| **Viewer** | View the folder and open artifacts in it. |
| **Editor** | View the folder, open artifacts, and add or move artifacts into the folder. |
| **Owner** | Do everything an Editor can do, plus rename or delete the folder and manage folder permissions. |
| **Admin** | Workspace or organization admin access. Admin is automatic and cannot be granted as a folder permission. |

Only **Viewer**, **Editor**, and **Owner** can be assigned to users or groups.

## Sharing with users and groups

You can grant folder access to:

* Individual workspace users.
* Workspace groups.
* An **All Users** group, if your workspace uses one.

Groups are usually the best way to manage folder access because they keep permissions aligned with how people join, leave, and move between teams. For example, give the **Finance** group access to a Finance folder instead of adding each finance team member individually.

For more on creating and maintaining groups, see [Workspace Groups and Permissions](workspace_groups_and_permissions.md).

## How folder access affects artifacts

For artifacts in a folder, the user's artifact access matches their folder access. If a user is a **Viewer** on the folder, they are a viewer on the artifacts in that folder. If they are an **Owner** on the folder, they have owner-level access to the artifacts in that folder.

This has a few important consequences:

* The artifact creator does not keep special access after the artifact is moved into a folder. The folder controls access.
* Sharing the folder grants access to the artifacts inside it.
* Removing folder access removes access to the artifacts inside it.
* Moving an artifact to another folder changes the artifact's access to match the new folder.

## Direct artifact shares

Direct artifact shares are for personal artifacts. They let an owner share one artifact with specific users or groups without placing it in a folder.

Direct shares do not apply to artifacts in folders. If a personal artifact has direct shares and you move it into a folder, Zenlytic removes those shares because the folder is now responsible for access.

If you move that artifact back to personal later, the old direct shares do not come back automatically. Share the artifact again if other people still need access.

## Workspace admins

Workspace admins and organization admins have automatic admin access to workspace folders and the artifacts inside them. This access comes from their role, so it does not appear as a normal folder grant that can be edited or removed.

If an admin cannot see artifact folders at all, the feature may not be enabled for that workspace, or the user may be in the wrong workspace.

## Visibility and errors

Zenlytic hides folders and artifacts a user cannot access. If a user opens a folder or artifact they do not have access to, it may appear as if the item does not exist.

This behavior prevents the system from revealing the names or existence of private content. It also means permission problems often look like missing folders or missing artifacts.

If a user can see an item but cannot perform an action, they need a higher access level. For example:

* A **Viewer** may be able to open a folder but not move artifacts into it.
* An **Editor** may be able to add artifacts but not manage sharing.
* A user without folder access may not see the folder or its artifacts at all.

## Troubleshooting

### Someone lost access after an artifact was moved

Check the destination folder's permissions. Moving a personal artifact into a folder removes direct artifact shares, so the user needs access through the folder.

### The artifact creator cannot see their own artifact in a folder

Check the folder's permissions. Once an artifact is moved into a folder, the folder controls access; the creator does not keep access unless they also have folder access or are an admin.

### A group has access but a user does not

Confirm the user is a member of the workspace group that was granted access. If your workspace uses multiple groups with similar names, confirm the correct group was selected.

### A user can view a folder but cannot manage sharing

The user likely has **Viewer** or **Editor** access. Grant **Owner** if they should manage folder permissions.

### A folder or artifact appears to be missing

The user may not have access. Ask a folder owner or workspace admin to confirm the folder permissions.

## Related pages

* [Artifact Folders](artifact-folders.md) - organizing artifacts into shared folders
* [Artifacts](artifacts.md) - the main artifacts workflow
* [User Roles](user_roles.md) - workspace-level role permissions
* [Workspace Groups and Permissions](workspace_groups_and_permissions.md) - grouping users for access management
