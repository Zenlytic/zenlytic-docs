# Personal access tokens (admin)

Personal access tokens (PATs) authenticate API requests to Zenlytic on behalf of your user account, without requiring an interactive login for each request. Use a PAT for scripts, CI pipelines, BI tool integrations, and other automated access to admin endpoints.

## What is a personal access token?

A personal access token is a long-lived credential tied to your user account and scoped to a specific workspace. Use it to authenticate API requests in place of a session login.

- **Scope:** Tied to the workspace that was active when you created the token. Authenticates requests to `/workspaces/...` endpoints for that workspace only.
- **Access:** Has the same permissions as your user account within that workspace.

## Creating a personal access token

1. Click your user avatar/name in the bottom-left corner of the navigation bar.
2. Select **API Access** from the user menu.

   ![](.gitbook/assets/pat-user-menu.png)

3. On the Personal Access Tokens page, click **Create Token**.

4. Enter a descriptive name for the token so you can identify its purpose later.

   ![](.gitbook/assets/pat-create-token-modal.png)

5. Click **Create**. Your new token displays once.
6. Copy the token immediately and store it somewhere secure, such as a secrets manager or password manager. Zenlytic does not store the raw token, and you cannot view it again after closing this dialog.

## Using your token

Include the token as a bearer token in the `Authorization` header of your API requests:

```
Authorization: Bearer <your_personal_access_token>
```

Example using `curl`:

```bash
curl -H "Authorization: Bearer <your_personal_access_token>" \
  https://api.zenlytic.com/v2/workspaces/<workspace_id>/...
```

## Managing existing tokens

The Personal Access Tokens page lists all tokens associated with your account, including their name and creation date.

Tokens are identified only by name and metadata. The raw token value is never shown again after creation, so keep your own record of which token is used where.

## Revoking a token

1. Go to **API Access**
2. Find the token to revoke in the list and click the delete (trash) icon.
3. Confirm the deletion in the dialog.

This action is immediate and permanent. Once deleted:

- The token can no longer authenticate; future API requests using it are rejected.
- You cannot view or restore the token.

## FAQ
**What permissions does my token have?**

The same permissions your user account has in the scoped workspace. A PAT does not grant elevated access beyond what you can already do when logged in.
