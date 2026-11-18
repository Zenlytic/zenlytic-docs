---
description: >-
  Use user and query attributes inside SQL for dynamic filtering and query
  behavior.
---

# Referenceable Attributes

Referenceable attributes are attributes that can be used in queries either on views or dimensions, dimension groups or measures.

The include all user attributes that you pass in via the API (in embedding) or user attributes you have on the user that you've assigned through the UI.

In addition to those user attributes, these are also default user attributes that will be present on the user or query without any additions on your part.

## Defaults

These are two objects you can interact with that are populated by default.

### User Attributes

The first is the `user_attributes` object. This object will include all the values you pass, and will additionally include:

`email`: The email for the user making the query, as defined in their Zenlytic account.

### Query Attributes

The second is the `query_attributes` object. This object will show attributes of the query that is being run, and will include:

`dimension_group`: This is the dimension group of the query (only applicable for fields that are of `field_type: dimension_group`). It will be the value of the dimension group (e.g. `raw`, `date`, `week`, `month_of_year`, etc)

## Choose a table or value by user attribute

Use an `{% raw %}{% if %}{% endraw %}` block to pick between tables or values based on a user attribute. This works in `sql_table_name`, `derived_table` SQL, and field `sql`. Both Jinja-style and Looker-style syntax are supported:

```yaml
# Jinja style
sql_table_name: "{% raw %}{% if 'EAST' in user_attributes['region_codes'] %}analytics.orders{% else %}analytics.orders_limited{% endif %}{% endraw %}"

# Looker style
sql_table_name: "{% raw %}{% if _user_attributes['region_codes'] contains 'EAST' %}analytics.orders{% else %}analytics.orders_limited{% endif %}{% endraw %}"
```

### Users without the attribute

If the user running the query has no value for the attribute the template references, Zenlytic doesn't choose either table. The template isn't filled in, and queries on the view return an error instead of falling back to the `else` branch.

To send these users to the `else` table instead, set a default value for the attribute on the All Users group, then set other values on the users or groups that need them. See [User Attributes](../zenlytic-ui/user_attributes.md).

{% hint style="info" %}
If a user with the `run_sql` permission writes SQL that names the view directly while the **Enforce permissions for admins** toggle is off, Zenlytic doesn't replace the view name with either table. The view name is sent to your warehouse as written. See [User Roles](../zenlytic-ui/user_roles.md).
{% endhint %}
