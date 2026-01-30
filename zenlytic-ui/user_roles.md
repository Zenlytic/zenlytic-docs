# User Roles

Permissions sets that give users the ability to take certain actions in Zenlytic

There are eight (8) roles in Zenlytic that a user can have. Each role corresponds to a permission set. Available permissions and their actions are as follows:

`save_content`: This is the ability to save a query result to a dashboard or modify an existing dashboard.

`schedule_content`: This is the ability to schedule a dashboard for delivery in Slack or email.

`view_content`: This is the ability to view dashboards.

`explore_from_here`: This is the ability to "Explore from here" to the graphical UI to change a query found on a dashboard or in Zoë.

`edit_settings`: This is the admin permission to edit the settings of the workspace itself. With this permission, a user can grant him/herself any permission.

`change_branch`: This is the ability to change the branch the workspace is looking at. By default, the branch will always be the production branch

`download_with_limit`: The ability to download data with a limit applied.

`download_without_limit`: The ability to download data without a limit applied (The max is 1 million in this case).

`see_sql`: The ability to see the SQL that was used to create the plot or table the user is looking at.

`run_sql`: The ability to run arbitrary SQL on the warehouse. This effectively gives the user access to all data that is in the warehouse.

`chat`: The ability to chat with Zoë.

`data_model_edit`: The ability to edit the data model.

`deploy_to_production`: The ability to deploy the data model from one branch to the production branch.

`create_personal_field`: The ability to create a personal field (does not include the ability to promote it to the data model).

## Admin

The admin has _all_ of the above permissions.

## Develop

Develop has all of the admin permissions except the ability to edit the workspace settings (`edit_settings`).

\##Develop without Deploy

Develop without Deploy has all of the Develop permissions except the ability to deploy the data model to production (`deploy_to_production`).

## Explore

The Explore role is the most common, and we recommend it as the default. It has `save_content`, `schedule_content`, `view_content`, `explore_from_here`, `download_with_limit`, `download_without_limit`, `see_sql`, and `chat`.

## View

View has the same permissions as Explore but without `download_without_limit`.

## Restricted

Restricted has ONLY the `view_content` permission. This means the user can only see dashboards, and cannot follow up or ask Zoë questions.

_Note:_ This user can change filters on dashboards which means in terms of API access, they have the ability to run queries that are not just the queries present on the dashboard. You should use this role in conjunction with [data access controls](../data-modeling/access_grants.md), not instead of data access controls.

## Embed

This permission set is not available in the UI but is the default for embedded users. It has `view_content`, `explore_from_here`, `download_with_limit`, and `chat` permissions.

## Embed with SQL

This permission set is not available in the UI but is the default for embedded users. It has `view_content`, `explore_from_here`, `download_with_limit`, `see_sql`, and `chat` permissions.

## Embedded with Scheduling

This permission set is not available in the UI but is the default for embedded users. It (predictably) has `schedule_content`, `view_content`, `see_sql`, `explore_from_here`, `download_with_limit`, and `chat` permissions.
