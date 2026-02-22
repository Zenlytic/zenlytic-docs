---
description: >-
  The Workspace Manager is where organization admins can manage their workspaces
  (agents).
---

# Workspace Manager



The Workspace Manager lets you create new workspaces, manage existing ones, and control how users are provisioned across your organization, all from a single, self-service interface.

***

### Who Can Use It

The Workspace Manager is available to **Organization Admins,** a role that sits above the existing Admin role. To see the Workspace Manager, you must be an Organization Admin in a workspace that belongs to an organization.

#### Organization Admin vs. Admin

There are now two levels of admin:

* **Organization Admin** — Can manage all workspaces across the organization: create and delete workspaces, copy database connections between them, control SSO provisioning settings, and promote other users to Organization Admin.
* **Admin** (Workspace Admin) — Can manage users and settings within a single workspace, just like before. Cannot perform cross-workspace operations or modify Organization Admin users.

Only an Organization Admin can change or remove another Organization Admin's role.

***

### Managing Workspaces

You can find the Workspace Manager from the navigation bar, next to Settings. The main page shows a table of all active workspaces in your organization. You can search by name to filter the list.

For each workspace, you can:

* **Toggle SSO User Provisioning** — When enabled, users who sign in through SSO are automatically added to this workspace. When disabled, users must be manually invited.
* **Delete a workspace** — Removes the workspace from active use. You'll be asked to type the workspace name to confirm. Deleted workspaces are deactivated and hidden but not permanently destroyed. You cannot delete the workspace you are currently signed into.

***

### Creating a New Workspace

Click **"Create New Workspace"** to walk through a guided setup:

#### Step 1: Name and Provisioning

* Enter a name for the new workspace.
* Choose whether to enable **SSO User Provisioning** (off by default).

#### Step 2: Add Database Connections

You can set up database connections for the new workspace in two ways:

* **Copy from existing workspaces:** Browse all database connections across your organization and select the ones you want to reuse. They'll be securely copied into the new workspace.
* **Create a new connection:** Fill out a fresh database connection form. The connection is tested automatically before it's saved.

#### Step 3: Set Up GitHub

Choose how to manage the workspace's data model repository:

* **Managed Repository:** Zenlytic creates and manages the repository for you. One click to finish.
* **Connected Repository:** Link an existing GitHub repository by providing the URL and branch. You can optionally generate a deploy key or enter a personal access token. The connection is verified before completing setup.

This step can be skipped, but well need to be completed before you can use Zoë in your new workspace.

***

### Managing the Organization Admin Role

When you invite a new member or edit an existing member's role, you'll see **Organization Admin** as a role option. Regular Admins do not see this option.

A few rules apply:

* Only Organization Admins can assign or revoke the Organization Admin role.
* An Admin cannot change, demote, or remove an Organization Admin, that action is reserved for other Organization Admins.
