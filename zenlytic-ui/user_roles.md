# User Roles

Permissions sets that give users the ability to take certain actions in Zenlytic. Each role bundles a set of underlying permissions; roles also determine how much latitude a user has to query data that isn't formally defined in the semantic layer.

## Tiered ad-hoc SQL access

Beyond the per-permission bundles below, Zenlytic enforces a tiered model for how much direct warehouse access each role has:

| Roles                                                                                | Ad-hoc SQL access                                                                 |
| ------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------- |
| **Admin** (Organization Admin, Admin)                                                | Full access, including ad-hoc SQL on any table the underlying SQL role can reach. |
| **Developer** (Develop, Develop without Deploy)                                      | Full access, including ad-hoc SQL on any table the underlying SQL role can reach. |
| **Explorer** (Explore, View, Restricted, Embed, Embed with SQL, Embedded with Scheduling) | Limited to tables defined in the semantic layer.                              |

**Enforce permissions for admins toggle.** A workspace-level toggle controls whether Admins are also restricted to the semantic layer or retain full ad-hoc access. When the toggle is **off** (default), Admins can query any table their SQL role can reach, even ones not modeled in Zenlytic. When **on**, Admins follow the same semantic-layer restrictions as everyone else.

If you need Explorer-style users to have access to a specific warehouse table, define it in the semantic layer. If you need Developers to be able to poke at unlisted tables for investigation, leave them at the Developer tier.

## Permissions reference

Each of the role bundles below is built from the following individual permissions.

`save_content`: This is the ability to save a query result to a dashboard or modify an existing dashboard.

`schedule_content`: This is the ability to schedule a dashboard for delivery in Slack or email.

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

In addition to all standard Admin capabilities, Organization Admins can:

* Manage workspaces across the organization: create new workspaces, archive existing ones, and configure SSO provisioning settings for each workspace.
* Manage credentials across the organization: view all credentials and copy them between workspaces.

When an Organization Admin creates a new workspace, they are automatically assigned the Organization Admin role in that workspace.

_Note: The Organization Admin role only appears as an option in the role selector for users who already have the workspace\_management permission. If your workspace is not part of an organization, this role will not be available._

### Admin

The admin has all of the above permissions _except_ `workspace_management`. Subject to the "enforce permissions for admins" toggle described above.

### Develop

Develop has all of the admin permissions except the ability to edit the workspace settings (`edit_settings`).

### Develop without Deploy

Develop without Deploy has all of the Develop permissions except the ability to deploy the data model to production (`deploy_to_production`).

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

## Related pages

* [Access Grants](../data-modeling/access_grants.md) — row-level and column-level access control in the data model
* [Workspace Groups and Permissions](workspace_groups_and_permissions.md) — grouping users and assigning roles at scale
