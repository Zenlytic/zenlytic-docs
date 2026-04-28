# Enforce SSO-Only Login

In SSO-enabled workspaces, you can disable the default username and password sign-in path so that only your configured SSO providers can authenticate. This is useful when you want all access to flow through your identity provider (IdP) for security, compliance, or lifecycle-management reasons.

## What it does

By default, Zenlytic workspaces accept sign-ins from both:

* The **default Cognito provider** (username and password), and
* Any **SSO providers** you've configured (Microsoft Entra, Okta, Google Workload Identity Federation, etc.).

When the default Cognito provider is disabled for your workspace, only your SSO providers can authenticate users. Username/password sign-in is no longer available.

## When to use this

Common reasons to enforce SSO-only login:

* **Centralized identity management** — all access governed by your IdP, including MFA enforcement, conditional access policies, and group-based provisioning.
* **Lifecycle / offboarding** — when an employee leaves and you deprovision them in your IdP, they immediately lose access to Zenlytic without any cleanup in Zenlytic itself.
* **Audit and compliance** — sign-in events flow exclusively through your IdP's audit log.

## Prerequisites

* At least one SSO provider must be configured and verified working. See:
  * [Microsoft Entra Zenlytic](microsoft_entra_zenlytic.md)
  * [Okta Zenlytic](okta_zenlytic.md)
  * [Google Workload Identity Federation](google_workload_identity_federation.md)
* **Strongly recommended:** before requesting the change, confirm at least one administrator can successfully sign in via SSO. Once username/password is disabled, anyone whose SSO sign-in isn't working will be locked out.

## How to request the change

The toggle that controls this behavior is internal to Zenlytic and is not available in the workspace UI. To enable SSO-only login for your workspace:

1. Contact your Zenlytic account team or [support@zenlytic.com](mailto:support@zenlytic.com).
2. Confirm which workspace(s) you want the change applied to.
3. Confirm at least one administrator account can sign in via SSO.

Zenlytic will apply the change on your behalf.

## What happens to existing users

Disabling the default Cognito provider blocks any further authentication via username and password, but **existing user records are not removed from your workspace user list**. Their stored Cognito credentials persist, and those users continue to appear in your user list until you manually delete them.

If a user previously signed in with both username/password and SSO, they may show up as separate user records — one Cognito-backed, one SSO-backed.

To fully purge username/password identities so that only SSO-provisioned users exist in the workspace going forward:

1. Identify the username/password user records in your workspace.
2. Delete them manually from the user list.
3. The corresponding SSO-provisioned users will continue to appear normally and can sign in via your IdP.

## Recovery

If your IdP becomes unavailable after SSO-only login is enforced and your workspace administrators cannot sign in, contact [support@zenlytic.com](mailto:support@zenlytic.com). Zenlytic can temporarily restore the default Cognito provider so administrators can regain access while the IdP issue is resolved.

## Related

* [Microsoft Entra Zenlytic](microsoft_entra_zenlytic.md)
* [Okta Zenlytic](okta_zenlytic.md)
* [Google Workload Identity Federation](google_workload_identity_federation.md)
* [Login Troubleshooting](login_troubleshooting.md)
