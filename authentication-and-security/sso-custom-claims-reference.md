---
description: Detailed information on SSO JWT claims.
---

# SSO Custom Claims Reference

When users sign in to Zenlytic through an SSO provider (Microsoft Entra, Okta, etc.), the identity provider can include custom claims in the JWT token. These claims allow you to control workspace access, user roles, and data-level permissions directly from your identity provider.

This page documents all supported custom claims, their format, behavior, and how they interact with each other.

***

### Overview of Available Claims

<table><thead><tr><th width="263.94921875">Claim Name</th><th width="235.25">Purpose</th><th width="174.33203125">Used At</th><th>Required</th></tr></thead><tbody><tr><td><code>zenlytic_workspaces</code></td><td>Controls which workspaces a user can access and their role in each</td><td>Every sign-in</td><td>No</td></tr><tr><td><code>zenlytic_role</code></td><td>Sets the user's role across all default-provisioned workspaces</td><td>First sign-in only</td><td>No</td></tr><tr><td><code>zenlytic_user_attributes</code></td><td>Sets user attributes for data-level access control</td><td>First sign-in only</td><td>No</td></tr></tbody></table>



> **Important:** There are two provisioning modes, and they are mutually exclusive. You must choose one:
>
> * **Claim-based provisioning** — Use `zenlytic_workspaces` to explicitly control which workspaces each user can access.
> * **Default provisioning** — Omit `zenlytic_workspaces` entirely. Users are auto-provisioned into all workspaces marked as "provision by default" in the organization. Use `zenlytic_role` and `zenlytic_user_attributes` to control their role and data access.
>
> If `zenlytic_workspaces` is present on the token, `zenlytic_role` and `zenlytic_user_attributes` are ignored.

***

### `zenlytic_workspaces`

Controls exactly which workspaces a user has access to within an organization, and what role they have in each workspace.

#### Format

A comma-separated list of `workspace_id:role` pairs.

```
workspace_id:role
workspace_id:role, workspace_id:role
```

**Example:**

```
workspace-9e49r:develop, workspace-1geh0y:view
```

This grants the user the `develop` role in workspace workspace-9e49r and the `view` role in workspace workspace-1geh0y.

#### Valid Roles

| Role Name                | Description                                                        |
| ------------------------ | ------------------------------------------------------------------ |
| `organization_admin`     | Full access including workspace management across the organization |
| `admin`                  | Full access to the workspace except workspace management           |
| `develop`                | All admin permissions except editing workspace settings            |
| `develop_without_deploy` | Same as develop, without the ability to deploy to production       |
| `explore`                | Can view dashboards, explore data, download, and chat with Zoe     |
| `view`                   | Same as explore but without unlimited downloads                    |
| `restricted`             | Can only view dashboards; no chat, no explore, no downloads        |

Roles are case-insensitive (`Develop`, `DEVELOP`, and `develop` are all valid).

For a full description of the permissions each role grants, see User Roles.

#### Behavior

**On first sign-in (signup):**

* The user is created and provisioned into exactly the workspaces listed in the claim.
* Each workspace entry specifies the role for that workspace.
* Workspaces marked "provision by default" in the organization are **not** used. The claim is the sole source of truth.
* The user's initial active workspace is set to the first workspace in the claim.

**On every subsequent sign-in:**

* Zenlytic syncs the user's workspace access to match the current claim value. This means:
  * **Workspaces added to the claim** since the last sign-in are granted to the user.
  * **Workspaces removed from the claim** since the last sign-in are revoked, even if access was originally granted by invitation.
  * **Role changes** in the claim are applied to the user's existing workspace access.
* Only workspaces within the SSO provider's organization are affected. Workspaces in other organizations the user has access to are never touched.

**Absent claim (not set on the token):**

* If the claim is not present at all, claim-based provisioning is not active. The user falls through to default provisioning behavior.

#### Validation Rules

* Each entry must contain a colon (`:`) separating workspace ID and role. Entries without a colon are silently skipped.
* The role must be one of the valid roles listed above. Entries with unrecognized roles are silently skipped.
* The workspace must exist, belong to the SSO provider's organization, and not be archived. Invalid workspaces are silently skipped.
* If a workspace ID appears more than once, the last entry wins.

***

### `zenlytic_role`

Sets the user's role when they are provisioned into workspaces via default provisioning (i.e., when `zenlytic_workspaces` is **not** present).

#### Format

A single role name as a string.

```
develop
```

#### Valid Values

`admin`, `develop`, `develop_without_deploy`, `explore`, `view`

> Note: `organization_admin` and `restricted` are not supported for this claim.

#### Behavior

* **Only applies on first sign-in (signup).** This claim is not read on subsequent sign-ins.
* The role is applied to every workspace the user is auto-provisioned into.
* If the role value is invalid or cannot be resolved, Zenlytic falls back to the workspace's configured default role. If no default role is set, the user receives the `explore` role.
* **Ignored when `zenlytic_workspaces` is present.** Use the per-workspace role in the workspaces claim instead.

***

### `zenlytic_user_attributes`

Sets user attributes on the user's workspace memberships for data-level access control (e.g., restricting which rows or fields a user can see).

#### Format

A JSON-encoded array of key-value pair objects.

```
[{"key": "department", "value": "Engineering"}, {"key": "region", "value": "US"}]
```

> Note: This value is a JSON **string** — the entire array must be serialized as a single string value in the JWT claim.

#### Behavior

* **Only applies on first sign-in (signup).** This claim is not read on subsequent sign-ins. To update user attributes after initial provisioning, use the Zenlytic UI or API.
* The attributes are applied to every workspace the user is auto-provisioned into.
* User attributes work with Access Grants to control data access. See User Attributes for more detail.
* If the JSON cannot be parsed, the attributes are set to empty and a warning is logged.
* **Ignored when `zenlytic_workspaces` is present.**

***

### How the Claims Interact

#### Decision Flow

When a user signs in via SSO, Zenlytic evaluates the claims in the following order:

```
Is zenlytic_workspaces present on the token?
 |
 ├── YES → Claim-based provisioning
 |         • Workspace access and roles come from the claim
 |         • zenlytic_role is IGNORED
 |         • zenlytic_attributes is IGNORED
 |         • Synced on every sign-in
 |
 └── NO  → Default provisioning
           • User is provisioned into organization's default workspaces
           • zenlytic_role sets the role (first sign-in only)
           • zenlytic_user_attributes sets data access (first sign-in only)
```

#### Compatibility Matrix

| Claim Combination                                                    | Supported | Notes                                                             |
| -------------------------------------------------------------------- | --------- | ----------------------------------------------------------------- |
| `zenlytic_workspaces` alone                                          | Yes       | Full control over workspace access and roles per workspace        |
| `zenlytic_role` alone                                                | Yes       | Sets role in all default-provisioned workspaces                   |
| `zenlytic_user_attributes` alone                                     | Yes       | Sets data access attributes in all default-provisioned workspaces |
| `zenlytic_role` + `zenlytic_user_attributes`                         | Yes       | Sets both role and data access in default-provisioned workspaces  |
| `zenlytic_workspaces` + `zenlytic_role`                              | No        | Error on signup. On login, `zenlytic_role` is ignored.            |
| `zenlytic_workspaces` + `zenlytic_user_attributes`                   | No        | Error on signup. On login, `zenlytic_user_attributes` is ignored. |
| `zenlytic_workspaces` + `zenlytic_role` + `zenlytic_user_attributes` | No        | Error on signup. On login, only `zenlytic_workspaces` is used.    |



***

### Configuration by Identity Provider

#### Microsoft Entra

Custom claims are configured in the **Attributes & Claims** section of your Zenlytic Enterprise Application. See the How-to Set up Custom Claims in Entra section for step-by-step instructions.

For `zenlytic_workspaces`, create a new claim with:

* **Name:** `zenlytic_workspaces`
* **Value:** A claim condition or transform that produces the `workspace_id:role` format described above.

#### Okta

Custom claims are configured in the **Profile Editor** for your Zenlytic application in Okta. See the Okta Zenlytic setup guide for details.

Add the attribute `zenlytic_workspaces` to your Okta app's profile and map it to the appropriate value for each user or group.

***

### Examples

#### Example 1: Single workspace, develop role

User should have develop access to workspace 42.

```
zenlytic_workspaces = "42:develop"
```

#### Example 2: Multiple workspaces, different roles

User is an admin in the production workspace and has view-only access to the staging workspace.

```
zenlytic_workspaces = "42:admin, 99:view"
```

#### Example 3: Revoking all access

User should no longer have access to any workspaces in the organization, but their account should remain.

```
zenlytic_workspaces = ""
```

#### Example 4: Default provisioning with role and attributes

User should be provisioned into all default workspaces with the `view` role and restricted to the Marketing department.

```
zenlytic_role = "view"
zenlytic_attributes = "[{\"key\": \"department\", \"value\": \"Marketing\"}]"
```

Do **not** set `zenlytic_workspaces` in this case.
