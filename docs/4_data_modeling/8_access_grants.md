---
sidebar_position: 8
---

# Access grants

Access grants are restrictions for certain users on the ability to see various fields and query them in the Zenlytic interface.

They are specified in [model](2_model.md) files, like the following example:

```
access_grants:
  - name: financial_grant
    user_attribute: department
    allowed_values: ["finance", "executive"]
  - name: pii_grant
    user_attribute: department
    allowed_values: ["finance", "customer_support"]
```

### Properties

`name`:  (Required) The name of the access grants. If you reference this access grants elsewhere this is the name you will use. Like all names, it follows [Zenlytic naming conventions](1_data_modeling.md#naming-conventions).

`user_attribute`: This is the name of the user attribute to access for comparison with `allowed_values`. If you defined a user attribute in the Zenlytic UI named `department` it might have values like `finance`, `marketing`, or `ops` each assigned to an individual user. E.g. John Doe has a user attribute `department` which is `marketing` and Jane Doe has a user attribute `department` which is `finance`.

`allowed_values`: This is a list of values which, if any are equal to the requesting person's user attribute given in the property above, will grant them access to the data being restricted by the access grant. For example, John Doe has a user attribute `department` which is `marketing`. If `user_attribute` (the property above) is set to `department` and `allowed_values` is `["marketing", "finance"]` John *will* have access to the data. However, in the same scenario, if `allowed_values` is `["finance", "ops"]` he will not have access, and will not be able to even see the fields in his interface.


# User attributes

You can set user attributes by going to the "Team Members" section of the workspace settings and adding user attributes there under the "User Attributes" header, for each team member.


### Examples

Access grants are defined and applied as follows. They're defined in models, and can be applied to any view or field using the `required_access_grants` property. If you specify multiple access grants in that property they must *all* be true for that user to have access.

```
version: 1
type: model
name: demo

# This defines the access grant
access_grants:
  - name: restrict_dept
    user_attribute: department
    allowed_values: ["Marketing"]


This is the view file 

```
version: 1
type: view
name: sample_view
model_name: demo
required_access_grants: [restrict_dept]

access_filters:
  - field: orders.product
    user_attribute: 'owned_product'

fields:
  - name: orders
  .
  .
  .
```
