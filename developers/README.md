# Overview

Use the Zenlytic API to manage workspaces, groups, and user attributes programmatically. The API is organized into two endpoint groups:

* **Org admin endpoints** (`GET /workspaces`, `POST /workspaces`, `DELETE /workspaces/{workspace_id}`): List, create, and archive workspaces in your organization. The organization is always the calling token's own organization — none of these endpoints take an organization ID. Org admins also have admin permissions in every workspace, so an org admin token can call the admin endpoints below to manage groups and user attributes across any workspace. Authenticate with an [org admin personal access token](authentication.md).
* **Admin endpoints** (`/workspaces/{workspace_id}/...`): Manage a single workspace, including groups, user attribute definitions, and user attribute assignments for groups and members. Authenticate with an [admin personal access token](authentication.md).
