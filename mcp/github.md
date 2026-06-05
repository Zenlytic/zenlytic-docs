# GitHub MCP integration

Connect Zoë to the [GitHub-hosted remote MCP server](https://github.com/github/github-mcp-server) — GitHub's official endpoint for AI tools — so she can browse repositories, read code, triage issues and pull requests, monitor GitHub Actions, and investigate security alerts directly from Zenlytic chats. Authenticate with a static `Authorization` header containing a GitHub [Personal Access Token](https://github.com/settings/personal-access-tokens/new) (PAT).


## What Zoë can access

The GitHub remote MCP server groups tools into **toolsets**. When no toolset filter is configured, Zoë gets the **default** toolset:

- `context` — information about the authenticated user and the current GitHub context.
- `repos` — browse repositories, list branches and tags, read files, search code and commits.
- `issues` — list, read, create, update, and search issues, sub-issues, and labels.
- `pull_requests` — list, read, create, review, update, and merge pull requests.
- `users` — search users.

Optional toolsets you can enable per-connection include `actions` (Actions workflows and CI/CD), `code_security` (code scanning alerts), `copilot` (Copilot coding agent and code reviews), `dependabot` (Dependabot alerts), `discussions`, `gists`, `git` (repository trees), `labels`, `notifications`, `orgs`, `projects`, `secret_protection`, `security_advisories`, `stargazers`, `copilot_spaces`, and `github_support_docs_search`. See [Available Toolsets](https://github.com/github/github-mcp-server#available-toolsets) for the full list and tool inventory.

Every tool call runs as the GitHub user who owns the PAT (and is scoped by the PAT's permissions), so Zoë's reach into GitHub is exactly what that token can see and do.

## Prerequisites

Before you start, confirm the following:

- A **GitHub.com** account or a **GitHub Enterprise Cloud** tenant (with or without data residency). The remote MCP server **does not support GitHub Enterprise Server**.
- A **dedicated GitHub user account** scoped to the **least-privileged** set of permissions Zoë needs. You'll mint the PAT against this account.
- For organization-owned content, any applicable [organization policies](https://github.com/github/github-mcp-server/blob/main/docs/policies-and-governance.md) that allow MCP access.
- **Zenlytic requirements.** The `mcp-client` flag enabled on your workspace and `admin` role. See the [MCP overview](overview.md) for the full list.

## Generate a GitHub Personal Access Token

PATs replace passwords for programmatic access to GitHub. Each PAT is tied to a single GitHub user, and the scopes you select are exactly what Zoë can do in GitHub.

1. Sign in to your GitHub account, then open [Settings → Developer settings → Personal access tokens → Fine-grained tokens](https://github.com/settings/personal-access-tokens/new).
2. Give the token a recognizable name (for example `zenlytic-mcp`), set an expiration that matches your rotation policy, and pick the **resource owner** (your user account or the organization that owns the repositories Zoë should reach).
3. Select the **repositories** the token can access. Limiting access to a specific set of repositories is recommended over **All repositories**.
4. Grant the **minimum permissions** Zoë needs for the toolsets you plan to enable. Common starting points:
  - **Repository permissions** — `Contents: Read-only` and `Metadata: Read-only` cover the `repos` and `git` toolsets.
  - **Issues: Read and write** — required for the `issues` toolset.
  - **Pull requests: Read and write** — required for the `pull_requests` toolset.
  - **Actions: Read-only** — required for the `actions` toolset.
  - **Code scanning alerts**, **Dependabot alerts**, **Secret scanning alerts** — required for the corresponding security toolsets.
  - **Administration: Read-only** — required for `get_teams` and `get_team_members` in the `context` toolset.
5. Click **Generate token** and copy the value immediately — GitHub only shows it once. Store it in your secrets manager.

> Classic PATs work too, but fine-grained tokens are recommended because you can scope them to specific repositories and grant just the permissions you need. If you use a classic PAT, the minimum scopes are `repo`, `read:org`, and `read:packages`; add `notifications`, `security_events`, `gist`, or `project` for the matching toolsets.

## Set up the connection in Zenlytic

1. Open **Workspace Settings → Extensions → MCP** and click **Add Connection**.
2. Fill out the form:
  - **Name** — a label that will appear in the chat tool menu, for example `GitHub`.
  - **URL** — the GitHub remote MCP endpoint:

    ```
    https://api.githubcopilot.com/mcp/
    ```

    For **GitHub Enterprise Cloud with data residency**, replace the host with your tenant's Copilot API host — for example `https://copilot-api.<your-subdomain>.ghe.com/mcp`. Must use `https://`.
3. Add the `Authorization` header (see [Configure request headers](#configure-request-headers)).
4. Optionally restrict the toolset (see [Customize the toolset](#customize-the-toolset)).
5. Click **Test Connection**. Zenlytic opens an MCP session against the GitHub server and lists the tools it advertises.
6. Review the tool list and toggle off any tools Zoë shouldn't be able to call. Newly-discovered tools are pre-selected.
7. Click **Add Connection** to save.

> Enabling write access means Zoe can create, modify, or delete real data in your connected systems. A miscommunication or unexpected instruction could trigger hard-to-reverse data loss or expose sensitive data to the wrong place. Use read-only mode unless you specifically need write capabilities.

## Configure request headers

Add the following in the **Headers** section of the Zenlytic connection modal. Header values are masked in the UI and encrypted at rest.

| Header          | Value                                                                                          |
| --------------- | ---------------------------------------------------------------------------------------------- |
| `Authorization` | `Bearer YOUR_GITHUB_PAT`. Include the `Bearer` scheme and a single space before the token.     |

### Verify the token

Before saving the connection, sanity-check the PAT against the GitHub MCP endpoint:

```bash
curl -X POST \
  -H "Authorization: Bearer $PAT" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}' \
  https://api.githubcopilot.com/mcp/
```

A `200` response that lists the available tools means the PAT, scopes, and URL are wired up correctly — the MCP server will accept the same credentials.

## Customize the toolset

By default, the GitHub MCP server exposes the `context`, `repos`, `issues`, `pull_requests`, and `users` toolsets. To narrow or expand the surface Zoë sees, change the URL path or add a header in the Zenlytic connection modal:

- **Restrict via URL path** — append `/x/<toolset>` to the endpoint. For example, `https://api.githubcopilot.com/mcp/x/repos` exposes only the `repos` toolset. Use `https://api.githubcopilot.com/mcp/x/repos/readonly` to also enforce read-only mode.
- **Restrict via header** — add `X-MCP-Toolsets` with a comma-separated list, for example `repos,issues,pull_requests,actions`. The value `all` enables every available toolset.
- **Read-only mode** — add `X-MCP-Readonly: true` to disable every write tool, regardless of which toolsets are enabled.
- **Insiders mode** — opt into early-access tools with `X-MCP-Insiders: true` (or use the `https://api.githubcopilot.com/mcp/insiders` URL).

You can also toggle individual tools off after **Test Connection** lists them, which works regardless of how the toolset is configured upstream. See [Remote Server Documentation](https://github.com/github/github-mcp-server/blob/main/docs/remote-server.md) for advanced configuration.

## Use the connection in chat

Once the connection has at least one selected tool, it appears in the chat tool menu. Toggle it on for any conversation where you want Zoë to use GitHub tools. The toggle is per-conversation, so different chats can mix GitHub with other MCP connections as needed.

A few specifics to share with your users:

- **One PAT, one permission set.** Every user sharing the connection sees whatever GitHub content the PAT can see. If you need different access for different teams, mint a separate PAT scoped to a different set of repositories and wire it up as its own Zenlytic connection.
- **Be specific in prompts.** Naming the owner, repo, and resource explicitly produces more reliable tool calls than vague references. For example: "In `acme-co/web`, list the open pull requests targeting `main` and summarize the failing checks."
- **Write tools can change GitHub.** Tools like `create_pull_request`, `issue_write`, and `merge_pull_request` make real changes against the repositories the PAT can access. Toggle them off, scope the PAT to read-only permissions, or set the `X-MCP-Readonly: true` header unless you've explicitly decided Zoë should write to GitHub.

## Manage the integration

- **Rotate the PAT:** In GitHub, open [Settings → Developer settings → Personal access tokens](https://github.com/settings/tokens), regenerate or create a fresh token, then **Edit** the connection in Zenlytic and overwrite the `Authorization` header value. Revoke the old PAT in GitHub once you've confirmed the new one works.
- **Change toolsets or permissions:** Update the PAT's permissions in GitHub or update the URL path / `X-MCP-Toolsets` header in Zenlytic, then click **Refresh Tools** on the connection.
- **Refresh tools:** If GitHub adds new tools or changes existing tool schemas, the next call may fail with a "tools have changed" error. Open the connection, click **Refresh Tools**, review the new set, and **Save Changes**.
- **Adjust repository access:** Edit the **resource owner** or selected repositories on the PAT in GitHub if you need to broaden or restrict what Zoë can reach. The change takes effect on the next request — no Zenlytic update needed.
- **Disable the integration:** Click **Delete** on the connection card to remove it immediately. Zoë stops seeing the GitHub tools in any new conversation. For belt-and-suspenders, also revoke the PAT in GitHub.

## Limitations

Inherited from GitHub's remote MCP server:

- **No OAuth in Zenlytic.** Zenlytic does not yet support OAuth-based MCP connections. The PAT path described here is the supported authentication method.
- **GitHub Enterprise Server is not supported on the remote server.** GHES customers must self-host the local Docker-based GitHub MCP server, which Zenlytic cannot currently reach.
- **Organization policies can block access.** Org admins can disable PAT access or restrict the GitHub MCP server through [policies and governance](https://github.com/github/github-mcp-server/blob/main/docs/policies-and-governance.md). Confirm the relevant policies are enabled if `tools/list` returns an empty result for org content.
- **Lockdown mode filters public-repo content.** If the server is running in lockdown mode, comments and content from users without push access to the repository are filtered out of public-repo responses.

## Troubleshoot

- **`401 Unauthorized` from GitHub:** The PAT is missing, malformed, or expired. Confirm the `Authorization` header is `Bearer <PAT>` (with a single space) and that the token is still active in **Settings → Developer settings → Personal access tokens**.
- **`403 Forbidden` on a tool call:** The PAT doesn't have the permission required to invoke that tool (for example, `Issues: Write` for `issue_write`, or `Actions: Read` for the `actions_*` tools). Grant the missing permission on the PAT and retry — no Zenlytic update needed.
- **Tool list looks short or empty:** The PAT's scopes only enable a subset of toolsets, or the URL path / `X-MCP-Toolsets` header is narrower than expected. Widen the PAT permissions or remove the restriction and click **Refresh Tools**.
- **Org-owned repositories or teams are invisible:** SSO or fine-grained PAT authorization may be missing. Open the PAT in GitHub and click **Configure SSO** (for classic PATs) or confirm the **resource owner** is the organization (for fine-grained PATs). Org admins may also need to approve the token under **Organization settings → Personal access tokens**.
- **Connection works in Test Connection but fails in chat:** Either the PAT expired between test and use, or GitHub's tool surface has changed since you saved. Generate a fresh token if needed, then open the connection in workspace settings and click **Refresh Tools**.
- **GitHub Enterprise Server URL is rejected or unreachable:** The remote server does not support GHES. GHES customers must self-host the local GitHub MCP server, which Zenlytic cannot reach today.
