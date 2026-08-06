# Developers (Beta)

Use the Zenlytic API to manage workspaces, groups, and user attributes programmatically. The API is organized into two endpoint groups:

- **Org admin endpoints** (`/workspace-manager/...`): Manage workspaces at the organization level, including creating and archiving workspaces, copying credentials, requiring SSO, and managing org admins. Org admins also have admin permissions in every workspace, so an org admin token can call the admin endpoints below to manage groups and user attributes across any workspace. Authenticate with an [org admin personal access token](authentication.md).
- **Admin endpoints** (`/workspaces/...`): Manage a single workspace, including groups, user attribute definitions, and user attribute assignments for groups and members. Authenticate with an [admin personal access token](authentication.md).
