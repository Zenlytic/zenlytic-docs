# Access Grants

Access control is managed in Zenlytic through two concepts.

1. [Access grants](access_grants.md#access-grants) cover _column-based_ access control
2. [Access filters](access_grants.md#access-filters) cover _row-based_ access control

## How access grants are evaluated

Access grants are checked against the user attribute named in the grant's `user_attribute` property.

If the user has a value for that attribute, the grant is evaluated by comparing the user's value with the grant's `allowed_values`. A matching value grants access. A non-matching value denies access.

If the user does not have that attribute at all, that grant is not triggered and does not block access. Missing attributes are not treated as denied values.

For default-deny behavior, give every governed user a default value that does not grant access. The usual pattern is to set a non-granting value on the All Users group, such as `revenue: no_revenue`, then set the granting value only on the users or groups that should have access, such as `revenue: has_revenue`.

```yaml
access_grants:
  - name: revenue_access
    user_attribute: revenue
    allowed_values: ["has_revenue"]
```

With this grant:

| User's `revenue` attribute | Result |
| -------------------------- | ------ |
| `has_revenue`              | Access granted |
| `no_revenue`               | Access denied |
| No `revenue` attribute     | Grant is not triggered and does not block access |

When multiple grants are listed in `required_access_grants`, all triggered grants must pass. A missing user attribute on a grant is non-blocking for that grant.

## Access grants

Access grants are restrictions for certain users on the ability to see various fields and query them in the Zenlytic interface. These access restrictions are based on access to _columns,_ _views,_ and _topics_. For row-based access control look at [access filters](access_grants.md#access-filters).

They are specified in [model](model.md) files, like the following example:

```yaml
access_grants:
  - name: financial_grant
    user_attribute: department
    allowed_values: ["finance", "executive"]
  - name: pii_grant
    user_attribute: department
    allowed_values: ["finance", "customer_support"]
```

## Properties

`name`: (Required) The name of the access grants. If you reference this access grant elsewhere this is the name you will use. Like all names, it follows [Zenlytic naming conventions](data_modeling.md#naming-conventions).

`user_attribute`: This is the name of the user attribute to access for comparison with `allowed_values`. If you defined a user attribute in the Zenlytic UI named `department` it might have values like `finance`, `marketing, finance`, or `ops` each assigned to an individual user. E.g. John Doe has a user attribute `department` which is `marketing, finance` and Jane Doe has a user attribute `department` which is `finance`. For more information, check out [user attributes](access_grants.md#user-attributes) below.

`allowed_values`: This is a list of values which, if any are equal to the requesting person's user attribute given in the property above, will grant them access to the data being restricted by the access grant. For example, John Doe has a user attribute `department` which is `marketing`. If `user_attribute` (the property above) is set to `department` and `allowed_values` is `["marketing", "finance"]` John _will_ have access to the data. However, in the same scenario, if `allowed_values` is `["finance", "ops"]` he will not have access, and will not be able to even see the fields in his interface.

## Examples

Access grants are defined and applied as follows. They're defined in models, and can be applied to any topic, view, or field using the `required_access_grants` property. If you specify multiple access grants in that property they must _all_ be true for that user to have access, except that a missing user attribute on a grant is non-blocking for that grant.

```yaml
version: 1
type: model
name: demo

# This defines the access grant
access_grants:
  - name: restrict_dept
    user_attribute: department
    allowed_values: ["Marketing", "Exec"]
  - name: exec_only
    user_attribute: department
    allowed_values: ["Exec"]
```

This is the view file that applies the `restrict_dept` access grant to restrict access to the entire view (every field in the view) to only people with the department "Marketing" or "Exec".

Additionally, it defines the `exec_only` access grant (used below) to ensure _only_ users with the department "Exec" have access to the `email` field.

As a result, a user with the department "Finance" won't be able to access any field in this view, a user with the department "Marketing" will access every field except for the `email` field, and a user with the "Exec" department will access every field in the view, including the `email` field. A user with no `department` attribute would not be blocked by these grants, because the grants would not be triggered for that user.

```yaml
version: 1
type: view
name: sample_view
model_name: demo
required_access_grants: [restrict_dept]


fields:
  - name: number_of_orders
    field_type: measure
    type: count_distinct
    sql: ${TABLE}.order_id

  - name: email
    required_access_grants: [exec_only]
    field_type: dimension
    type: string
    sql: ${TABLE}.email
  
```

## Access filters

Access filters are restrictions for certain users on the ability to see various rows and query them in the Zenlytic interface. These access filters protect data access based on access to _rows_ in a view. For column-based access control look at [access grants](access_grants.md#access-grants).

They are specified in [view](view.md) files and apply to all queries that reference that view.

## Properties

`field`: (Required) The fully qualified name of the field used in the access filter. For example, if you're in the view `orders` just putting `product` for the `field` property will not work, you have to specify `orders.product`, the fully qualified name.

`user_attribute`: (Required) This is the name of the user attribute to access for comparison with `allowed_values`. If you defined a user attribute in the Zenlytic UI named `department` it might have values like `finance`, `marketing, finance`, or `ops` each assigned to an individual user. E.g. John Doe has a user attribute `department` which is `marketing, finance` and Jane Doe has a user attribute `department` which is `finance`. For more information, check out [user attributes](access_grants.md#user-attributes) below.

## Examples

Access filters are defined and applied as follows. They're defined in view, and apply to the view in which they're defined. If you specify multiple access filters they must _all_ be true for that user to have access.

This is the view file that corresponds with a access filter using the `products` user attribute.

In this example, the user has a user attribute named `products` with the value `Blue Pants, White Shoes`. In the following access filter with this user attribute this user will have the where filter clause `orders.product is in ('Blue Pants', 'White Shoes')` force-added to all queries this user issues that include this view. If the user attribute's value was instead `Green shirt`, the where filter clause would be `orders.product = 'Green shirt'`.

Note: You have to fully qualify the `field` property for the access filter. In this example, just putting `product` for the `field` property will not work, you have to specify `orders.product`, the fully qualified name.

```yaml
version: 1
type: view
name: orders
model_name: demo

access_filters:
  - field: orders.product
    user_attribute: 'products'

fields:
  - name: product
    field_type: dimension
    type: string
    sql: ${TABLE}.product

```

## User attributes

You can set user attributes by going to the "Team Members" section of the workspace settings and adding user attributes there under the "User Attributes" header, for each team member.

![team-members](../.gitbook/assets/settings-team-members-attrs.png)

User attributes are strings that can handle [filter syntax](field_filter.md) for specifying complex comparisons or inclusions in either access grants (column level security) or access filters (row level security).
