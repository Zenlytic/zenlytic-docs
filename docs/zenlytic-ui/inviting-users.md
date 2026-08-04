---
description: >-
  Invite people to a workspace, assign their role, and manage existing members
  from the Team page.
---

# Inviting and Managing Users

Every person who uses Zenlytic belongs to one or more workspaces. You add them from **Workspace Settings → Team**.

## Invite someone

1. Go to **Workspace Settings → Team**.
2. Click **+ Team Member**.
3. Enter their **email address**.
4. Choose a **role**. This is required — there's no default.
5. Optionally add them to one or more **groups**.
6. Click **Submit**.

They receive an email with a link to join the workspace. Until they accept, the invitation sits under the **Invites** tab.

You don't have to get the role right at invite time. It can be changed later from **Team → Users**.

{% hint style="info" %}
**Who can invite:** Admins and Organization Admins. Other roles don't see the **+ Team Member** button.
{% endhint %}

## Access is granted per workspace

**Inviting someone to a workspace gives them access to that workspace only.** If your organization has three workspaces and someone needs all three, they have to be invited to each one, and their role is set separately in each.

**Organization Admin is the one exception.** It applies across every workspace in the organization automatically — grant it in one place and it takes effect everywhere. That's also why it's the only role that can create new workspaces.

For what each role can do, see [User Roles](user_roles.md).

## Manage existing members

**Team → Users** lists everyone in the workspace, with their role, login method, and whether MFA is enabled.

From here you can:

* **Change someone's role** — use the role dropdown on their row. The change takes effect immediately.
* **Change or remove several people at once** — select them with the checkboxes, then apply a role change or removal to the whole selection.
* **Remove someone** — this revokes their access to this workspace. It does not affect their access to any other workspace, and it does not delete their Zenlytic account.

Use [groups](workspace_groups_and_permissions.md) rather than per-person changes when you're managing access at any scale.

## New workspaces and SSO provisioning

Only Organization Admins can create workspaces, and the first step asks whether to enable **SSO User Provisioning**.

* **Enabled** — the new workspace inherits all the users from your main organization workspace. They arrive with access already granted.
* **Disabled** (the default) — the new workspace starts empty and every member has to be invited manually.

Turning it on is the difference between a workspace your team can use immediately and one you have to populate by hand, so decide deliberately at creation time.

Provisioning can also be toggled later for an existing workspace from [Workspace Manager](workspace-manager.md).

{% hint style="warning" %}
If your organization signs in through SSO, workspace access can also be driven by claims in the SSO assertion. Workspaces removed from a user's claim are revoked on their next sign-in **even if access was originally granted by invitation**. See the [SSO Custom Claims Reference](../authentication-and-security/sso-custom-claims-reference.md).
{% endhint %}

## Related pages

* [User Roles](user_roles.md) — what each role can do, and the permissions behind them
* [Workspace Groups and Permissions](workspace_groups_and_permissions.md) — grouping users and assigning access at scale
* [Workspace Manager](workspace-manager.md) — creating workspaces and managing them across an organization
* [User Attributes](user_attributes.md) — controlling which data a user can see
