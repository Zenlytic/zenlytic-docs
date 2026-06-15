# User Roles

Permissions sets that give users the ability to take certain actions in Zenlytic. Each role bundles a set of underlying permissions; roles also determine how much latitude a user has to query data that isn't formally defined in the semantic layer.

## Tiered ad-hoc SQL access

Beyond the per-permission bundles below, Zenlytic enforces a tiered model for how much direct warehouse access each role has:

| Roles                                                                                     | Ad-hoc SQL access                                                                 |
| ----------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| **Admin** (Organization Admin, Admin)                                                     | Full access, including ad-hoc SQL on any table the underlying SQL role can reach. |
| **Developer** (Develop, Develop without Deploy)                                           | Full access, including ad-hoc SQL on any table the underlying SQL role can reach. |
| **Explorer** (Explore, View, Restricted, Embed, Embed with SQL, Embedded with Scheduling) | Limited to tables defined in the semantic layer.                                  |

**Enforce permissions for admins toggle.** A workspace-level toggle controls whether Admins are also restricted to the semantic layer or retain full ad-hoc access. When the toggle is **off** (default), Admins can query any table their SQL role can reach, even ones not modeled in Zenlytic. When **on**, Admins follow the same semantic-layer restrictions as everyone else.

If you need Explorer-style users to have access to a specific warehouse table, define it in the semantic layer. If you need Developers to be able to poke at unlisted tables for investigation, leave them at the Developer tier.

## Permissions reference

Each of the role bundles below is built from the following individual permissions.

`save_content`: This is the ability to save a query result to a dashboard or modify an existing dashboard.

`schedule_content`: This is the ability to schedule a dashboard, artifact, or Proactive Agent for delivery in Slack or email. **Included in: Organization Admin, Admin, Develop, Develop without Deploy, Explore, View, and Embedded with Scheduling.**

`view_content`: This is the ability to view dashboards.

`explore_from_here`: This is the ability to "Explore from here" to the graphical UI to change a query found on a dashboard or in Zoë.

`edit_settings`: This is the admin permission to edit the settings of the workspace itself. With this permission, a user can grant him/herself any permission.

`change_branch`: This is the ability to change the branch the workspace is looking at. By default, the branch will always be the production branch.

`download_with_limit`: The ability to download data with a limit applied.

`download_without_limit`: The ability to download data without a limit applied (the max is 1 million in this case).

`see_sql`: The ability to see the SQL that was used to create the plot or table the user is looking at.

`run_sql`: The ability to run arbitrary SQL on the warehouse. This effectively gives the user access to all data that is in the warehouse (subject to the ad-hoc SQL tier above).

`chat`: The ability to chat with Zoë.

`data_model_edit`: The ability to edit the data model.

`create_workflow`: The ability to create a Proactive Agent (previously branded as a 'workflow').

`deploy_to_production`: The ability to deploy the data model from one branch to the production branch.

`create_dynamic_field`: The ability to create a dynamic field (does not include the ability to promote it to the data model).

`view_workspace_users`: The ability to view the names of other users in the workspace.

`workspace_management`: Grants the ability to create, archive, and manage workspaces and credentials across an organization.

## Roles

There are eight role bundles in Zenlytic. Each bundle combines a set of the permissions above and maps to one of the ad-hoc SQL tiers.

### Organization Admin

The organization admin has _all_ of the above permissions. Subject to the "enforce permissions for admins" toggle described above.

Explicit list: `save_content`, `schedule_content`, `view_content`, `explore_from_here`, `edit_settings`, `change_branch`, `download_with_limit`, `download_without_limit`, `see_sql`, `run_sql`, `chat`, `data_model_edit`, `create_workflow`, `deploy_to_production`, `create_dynamic_field`, `view_workspace_users`, `workspace_management`.

The organization admin also automatically has organization admin level access on _all_ the workspaces inside of an organization. So, if a user has organization admin-level access on any of the workspaces inside of your organization, they will automatically have organization admin-level access on _all_ of the workspaces inside of your organization.

In addition to all standard Admin capabilities, Organization Admins can:

* Manage workspaces across the organization: create new workspaces, archive existing ones, and configure SSO provisioning settings for each workspace.
* Manage credentials across the organization: view all credentials and copy them between workspaces.

When an Organization Admin creates a new workspace, they are automatically assigned the Organization Admin role in that workspace.

_Note: The Organization Admin role only appears as an option in the role selector for users who already have the workspace\_management permission. If your workspace is not part of an organization, this role will not be available._

### Admin

The Admin role has every permission except `workspace_management`. Subject to the "enforce permissions for admins" toggle described above.

Explicit list: `save_content`, `schedule_content`, `view_content`, `explore_from_here`, `edit_settings`, `change_branch`, `download_with_limit`, `download_without_limit`, `see_sql`, `run_sql`, `chat`, `data_model_edit`, `create_workflow`, `deploy_to_production`, `create_dynamic_field`, `view_workspace_users`.

### Develop

Develop has every Admin permission except `edit_settings`.

Explicit list: `save_content`, `schedule_content`, `view_content`, `explore_from_here`, `change_branch`, `download_with_limit`, `download_without_limit`, `see_sql`, `run_sql`, `chat`, `data_model_edit`, `create_workflow`, `deploy_to_production`, `create_dynamic_field`, `view_workspace_users`.

### Develop without Deploy

Develop without Deploy has every Develop permission except `deploy_to_production`.

Explicit list: `save_content`, `schedule_content`, `view_content`, `explore_from_here`, `change_branch`, `download_with_limit`, `download_without_limit`, `see_sql`, `run_sql`, `chat`, `data_model_edit`, `create_workflow`, `create_dynamic_field`, `view_workspace_users`.

### Explore

The Explore role is the most common, and we recommend it as the default. It has `save_content`, `schedule_content`, `view_content`, `explore_from_here`, `download_with_limit`, `download_without_limit`, `see_sql`, `create_workflow`, `create_dynamic_field`, `view_workspace_users`, and `chat`.

### View

View has the same permissions as Explore but without `download_without_limit`.

### Restricted

Restricted has ONLY the `view_content` permission. This means the user can only see dashboards, and cannot follow up or ask Zoë questions.

_Note:_ This user can change filters on dashboards which means in terms of API access, they have the ability to run queries that are not just the queries present on the dashboard. You should use this role in conjunction with [data access controls](../data-modeling/access_grants.md), not instead of data access controls.

### Embed

This permission set is not available in the UI but is the default for embedded users. It has `view_content`, `explore_from_here`, `download_with_limit`, and `chat` permissions.

### Embed with SQL

This permission set is not available in the UI but is the default for embedded users. It has `view_content`, `explore_from_here`, `download_with_limit`, `see_sql`, and `chat` permissions.

### Embedded with Scheduling

This permission set is not available in the UI but is the default for embedded users. It (predictably) has `schedule_content`, `view_content`, `see_sql`, `explore_from_here`, `download_with_limit`, and `chat` permissions.

## Permissions × roles matrix

Cross-reference any permission against any role. ✓ means the role includes that permission. Blank means it doesn't.

### User-facing roles

| Permission                | Org Admin | Admin | Develop | Develop w/o Deploy | Explore | View | Restricted |
| ------------------------- | :-------: | :---: | :-----: | :----------------: | :-----: | :--: | :--------: |
| `save_content`            | ✓         | ✓     | ✓       | ✓                  | ✓       | ✓    |            |
| `schedule_content`        | ✓         | ✓     | ✓       | ✓                  | ✓       | ✓    |            |
| `view_content`            | ✓         | ✓     | ✓       | ✓                  | ✓       | ✓    | ✓          |
| `explore_from_here`       | ✓         | ✓     | ✓       | ✓                  | ✓       | ✓    |            |
| `edit_settings`           | ✓         | ✓     |         |                    |         |      |            |
| `change_branch`           | ✓         | ✓     | ✓       | ✓                  |         |      |            |
| `download_with_limit`     | ✓         | ✓     | ✓       | ✓                  | ✓       | ✓    |            |
| `download_without_limit`  | ✓         | ✓     | ✓       | ✓                  | ✓       |      |            |
| `see_sql`                 | ✓         | ✓     | ✓       | ✓                  | ✓       | ✓    |            |
| `run_sql`                 | ✓         | ✓     | ✓       | ✓                  |         |      |            |
| `chat`                    | ✓         | ✓     | ✓       | ✓                  | ✓       | ✓    |            |
| `data_model_edit`         | ✓         | ✓     | ✓       | ✓                  |         |      |            |
| `create_workflow`         | ✓         | ✓     | ✓       | ✓                  | ✓       | ✓    |            |
| `deploy_to_production`    | ✓         | ✓     | ✓       |                    |         |      |            |
| `create_dynamic_field`    | ✓         | ✓     | ✓       | ✓                  | ✓       | ✓    |            |
| `view_workspace_users`    | ✓         | ✓     | ✓       | ✓                  | ✓       | ✓    |            |
| `workspace_management`    | ✓         |       |         |                    |         |      |            |

### Embed roles

Not available in the role selector — assigned automatically to embedded users.

| Permission                | Embed | Embed with SQL | Embedded with Scheduling |
| ------------------------- | :---: | :------------: | :----------------------: |
| `schedule_content`        |       |                | ✓                        |
| `view_content`            | ✓     | ✓              | ✓                        |
| `explore_from_here`       | ✓     | ✓              | ✓                        |
| `download_with_limit`     | ✓     | ✓              | ✓                        |
| `see_sql`                 |       | ✓              | ✓                        |
| `chat`                    | ✓     | ✓              | ✓                        |

All other permissions are unavailable to embed roles.

## Troubleshooting

### I have the role but I don't see a feature

Role permissions are necessary but not always sufficient — a feature can be gated by both a role permission and a workspace-level configuration. If your role includes the right permission and you still don't see the feature in the UI:

* **Schedule Delivery on a Proactive Agent or artifact.** Confirm the artifact has been saved (scheduling is not available on unsaved artifacts), and that the workspace has Proactive Agents enabled.
* **Schedule Delivery on a dashboard.** Legacy dashboards have their own delivery setup — see [Dashboard Scheduled Delivery](../legacy/dashboard/dashboard-scheduled-delivery.md).
* **Chat with Zoë.** Confirm the workspace has chat enabled and that you have the `chat` permission for your role.
* **Edit the data model in Context Manager.** Confirm you're on a non-production branch, or that **Allow Edit Production** is enabled in workspace settings for your role.
* **Workspace-by-workspace inconsistency.** If a feature appears in some workspaces but not others, the missing workspace likely has the feature toggled off in settings. Compare workspace settings, or ask a workspace Admin to check.

If none of the above explains it, contact support — there may be a workspace-level feature flag we need to check.

### Organization Admin still can't see a feature

Organization Admin has every permission, so if a feature is missing for an Organization Admin, the cause is almost always **workspace-level configuration** (the feature is disabled in that workspace), not the role. Start by comparing settings against a workspace where the feature does appear.

## Related pages

* [Access Grants](../data-modeling/access_grants.md) — row-level and column-level access control in the data model
* [Workspace Groups and Permissions](workspace_groups_and_permissions.md) — grouping users and assigning roles at scale
