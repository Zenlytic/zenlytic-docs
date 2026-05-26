# Looker MCP integration

Connect Zoë to a self-hosted Looker MCP server — deployed via [MCP Toolbox for Databases](https://mcp-toolbox.dev/) on Google Cloud Run — so she can explore your Looker content (models, explores, fields, dashboards, and queries) without leaving Zenlytic. The MCP Toolbox container holds a Looker API3 credential and proxies Zoë's calls to your Looker instance. Authenticate with a static `Authorization` header containing a Google identity token.

> Looker doesn't publish an official hosted remote MCP endpoint. The supported path is to deploy [MCP Toolbox by Google](https://mcp-toolbox.dev/integrations/looker/samples/looker_cloud_run/) in Cloud Run and point Zenlytic at it. Most of the setup happens in Google Cloud and Looker, not in Zenlytic.

## What Zoë can access

Through the Looker MCP server, Zoë can call the Looker API surface that MCP Toolbox exposes through its `looker` and `looker-dev` toolsets to:

- List models, explores, and views in your Looker instance.
- Read field metadata, labels, and descriptions.
- Run ad-hoc queries against explores and return results.
- Look up dashboards and Looks the credential's user has access to.
- Inspect users, groups, and other admin objects via the Looker API (subject to the credential's permissions).

The exact tool surface depends on which prebuilt toolsets you enable when you deploy MCP Toolbox. Every Zoë action runs as the Looker user behind the API3 credential baked into Toolbox, so all users sharing the connection see the same scope of Looker content.

## Prerequisites

Before you start, confirm the following:

- A **Looker instance** with API access enabled and a **Looker API3 Client ID and Client Secret** for the user (typically a dedicated service account) whose permissions Zoë should inherit.
- A **Google Cloud project** where you can deploy services to **Cloud Run** and manage **Secret Manager** and **IAM**.
- A way to mint **Google identity tokens** scoped to your Cloud Run service URL (see `gcloud` CLI in [Configure request headers](#configure-request-headers)).
- **Zenlytic requirements.** The `mcp-client` flag enabled on your workspace and `admin` role. See the [MCP overview](overview.md) for the full list.

## Create a Looker API3 credential

In your Looker instance, open **Admin → Users**, choose the user account Zoë should run as (create a dedicated service account if you don't already have one), and click **Edit Keys → New API3 Key**. Save the Client ID and Client Secret somewhere safe — you'll store both as Secret Manager secrets in the next step.

The MCP Toolbox container uses this credential to call the Looker API on every tool call, so Zoë's permissions in Looker are whatever this user can see and do.

## Deploy MCP Toolbox to Cloud Run

These steps adapt the [MCP Toolbox guide for Looker on Cloud Run](https://mcp-toolbox.dev/integrations/looker/samples/looker_cloud_run/) to use a baked-in API3 credential instead of client OAuth.

1. In **Google Cloud Console → Cloud Run**, click **Deploy container**.
2. Configure the container:
  - **Container image URL** — `us-central1-docker.pkg.dev/database-toolbox/toolbox/toolbox:latest`
  - **Service name** — `looker-mcp-toolbox` (or any name you prefer).
  - **Region** — pick a region close to your Looker instance.
  - **Authentication** — **Require authentication**. Zenlytic signs requests with a Google identity token; see [Configure request headers](#configure-request-headers).
  - Note the **Endpoint URL**; you'll paste it into Zenlytic with `/mcp` appended.
3. Under **Service scaling**, choose **Auto** with a minimum of **1** instance to keep cold starts off the hot path. Set **Ingress** to **All**.
4. Open **Containers, Networking, Security**:
  - **Container arguments** — add each on its own line:
    - `--prebuilt=looker,looker-dev` — loads the standard Looker toolset plus the `looker-dev` toolset for LookML / dev-mode editing.
    - `--port=8080` and `--address=0.0.0.0` — make Toolbox listen on the port and interface Cloud Run expects.
  - **Variables & Secrets** —
    - `LOOKER_BASE_URL` — the URL of your Looker instance, for example `https://yourcompany.looker.com`.
    - `LOOKER_CLIENT_ID` — the Client ID from the API3 key. Store it as a Secret Manager secret and reference it here.
    - `LOOKER_CLIENT_SECRET` — the Client Secret from the API3 key. Store it as a Secret Manager secret and reference it here.
    - `LOOKER_USE_CLIENT_OAUTH` — `false`. Tells Toolbox to authenticate to Looker with the API3 credential above instead of expecting the caller to bring an OAuth token.
5. In **IAM**, grant the **Secret Manager Secret Accessor** role to the Cloud Run compute service account so the container can read the API3 secrets at startup.
6. Click **Done**, then **Create**.
7. Once the service is deployed, grant the identity you'll use to call it (your user account or a dedicated service account) the **Cloud Run Invoker** (`roles/run.invoker`) role on the Cloud Run service.

> Review the **Hardening Toolbox** section of the [MCP Toolbox CLI reference](https://mcp-toolbox.dev/reference/cli/) before using this in production. Tighten container arguments (logging level, allowed origins, request size limits, etc.), restrict ingress to known sources, and rotate the Looker API3 credential on a schedule.

## Set up the connection in Zenlytic

1. Open **Workspace Settings → Extensions → MCP** and click **Add Connection**.
2. Fill out the form:
  - **Name** — a label that will appear in the chat tool menu, for example `Looker`.
  - **URL** — your Cloud Run endpoint with `/mcp` appended, for example `https://looker-mcp-toolbox-abc123-uc.a.run.app/mcp`. Must use `https://`.
3. Add the `Authorization` header (see [Configure request headers](#configure-request-headers)).
4. Click **Test Connection**. Zenlytic opens an MCP session against the server and lists the tools MCP Toolbox advertises (based on the `--prebuilt` toolsets you enabled).
5. Review the tool list and toggle off any tools Zoë shouldn't be able to call.
6. Click **Add Connection** to save.

## Configure request headers

Add the following in the **Headers** section of the Zenlytic connection modal. Header values are masked in the UI and encrypted at rest.


| Header          | Value                                                                                                                                                                |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Authorization` | `Bearer YOUR_GCP_IDENTITY_TOKEN`. Include the `Bearer` scheme and a single space before the token. Cloud Run validates the token's audience and invoker permission. |


Cloud Run expects a Google-issued **ID token** whose `audience` claim matches your service URL — not an OAuth access token. ID tokens expire after **one hour**.

### Use your user identity (testing)

For local development and testing, sign in with the [gcloud CLI](https://cloud.google.com/sdk/docs/install) and print an identity token scoped to your Cloud Run service:

```bash
gcloud auth login
gcloud auth print-identity-token --audiences=https://<your-cloud-run-url>
```

Tool calls made with this token are attributed to your user account. Your user needs `roles/run.invoker` on the Cloud Run service.

### Use a service account (production)

For production, mint an identity token by impersonating a dedicated service account so Zoë's traffic is observable independently of any individual user:

```bash
gcloud auth print-identity-token \
  --impersonate-service-account=YOUR_SA@YOUR_PROJECT.iam.gserviceaccount.com \
  --audiences=https://<your-cloud-run-url>
```

Two extra grants are easy to miss on the service-account path: the impersonated service account needs `roles/run.invoker` on the Cloud Run service, and your local identity needs `roles/iam.serviceAccountTokenCreator` on the service account. If either is missing, the token mints fine but tool calls fail with `403 Forbidden`.

### Verify the token

Before saving the connection, sanity-check the token against the Cloud Run service:

```bash
curl -I -H "Authorization: Bearer $TOKEN" https://<your-cloud-run-url>/mcp
```

Anything other than `401` or `403` means Cloud Run accepted the credential — the MCP endpoint will accept it too.

## Use the connection in chat

Once the connection has at least one selected tool, it appears in the chat tool menu. Toggle it on for any conversation where you want Zoë to have access to Looker tools. The toggle is per-conversation, so different chats can mix Looker with other MCP connections as needed.

A few specifics to share with your users:

- **One identity, one permission set.** Every user sharing the connection sees whatever Looker content the API3 credential's user can see. If you need different access for different teams, create separate Toolbox deployments backed by separate API3 credentials and wire each up as its own Zenlytic connection.
- **Be specific about models and explores.** Including the model name and explore name produces more reliable queries than vague references. For example: "In model `ecommerce`, query the `order_items` explore for total sales by month last year."

## Manage the integration

- **Rotate the identity token:** Mint a fresh token with `gcloud auth print-identity-token`, then **Edit** the connection in Zenlytic and overwrite the `Authorization` header value.
- **Rotate the Looker credential:** Generate a new API3 key in **Looker Admin → Users**, update the `LOOKER_CLIENT_ID` and `LOOKER_CLIENT_SECRET` secrets in Secret Manager, and roll a new Cloud Run revision. Delete the old API3 key once the new revision is healthy.
- **Refresh tools:** If you change `--prebuilt` toolsets or MCP Toolbox is upgraded in Cloud Run, the next call may fail with a "tools have changed" error. Open the connection, click **Refresh Tools**, review the new set, and **Save Changes**.
- **Update the Cloud Run deployment:** Push a new revision in Cloud Run if you need to change toolsets, environment variables, or the API3 secrets. The MCP URL stays the same.
- **Disable the integration:** Click **Delete** on the connection card to remove it immediately. Zoë stops seeing the Looker tools in any new conversation.

## Troubleshoot

- **`401 Unauthorized` from Cloud Run:** The identity token is missing, malformed, expired (tokens last one hour), or its audience doesn't match the Cloud Run URL. Mint a fresh one with `gcloud auth print-identity-token --audiences=https://<your-cloud-run-url>` and replace the `Authorization` value.
- **`403 Forbidden` from Cloud Run:** The identity behind the token doesn't have `roles/run.invoker` on the service. Grant it in Google Cloud IAM and try again.
- **`401 Unauthorized` from Looker (visible in Cloud Run logs):** The `LOOKER_CLIENT_ID` or `LOOKER_CLIENT_SECRET` is wrong, or the API3 key was disabled in Looker. Regenerate the key, update the Secret Manager secrets, and redeploy.
- **Tool list is empty:** Check the `--prebuilt` container argument — it must include at least one Looker toolset (`looker` or `looker-dev`).
- **Tool calls return permission errors from Looker:** The API3 user lacks the Looker permissions to do what Zoë asked. Grant the needed roles or permission sets in **Looker Admin → Roles**.
- **Can't reach the MCP endpoint at all:** Confirm the Cloud Run service has **Ingress: All** and that no VPC controls block your network. If you've intentionally restricted ingress, make sure Zenlytic's egress IPs are on the allow-list.
