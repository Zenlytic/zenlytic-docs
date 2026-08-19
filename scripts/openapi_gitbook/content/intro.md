## Servers & Authentication

### Servers

Zenlytic runs separate API hosts per region. Use the host matching where your organization is hosted.

{{SERVERS_TABS}}

### Authentication

Include your personal access token as a bearer token in the `Authorization` header:

```
Authorization: Bearer YOUR_TOKEN
```

{% hint style="info" %}
A token's scope — a single workspace (**Admin**) or your entire organization (**Org admin**) — is fixed when the token is created, based on your role in the workspace you created it from. It isn't visible from the token itself, so call `GET /me` to see what a given token can actually reach before building against it. See [Overview](README.md#discovering-your-tokens-scope) for the full scope table.
{% endhint %}

## Getting Started

{% stepper %}
{% step %}
## Create a Personal Access Token
See [Overview](README.md#creating-a-personal-access-token) for how to create one from your user menu.
{% endstep %}

{% step %}
## Check Your Token's Scope
Call `GET /me` with your new token. It returns your organization and the workspaces the token can see — one workspace for an admin-scoped token, or every workspace in the organization for an org admin token.
{% endstep %}

{% step %}
## Make Your First Request
Org admin token: call `GET /workspaces` to list every workspace in your organization. Admin token: call `GET /workspaces/{workspace_id}/groups` for a workspace your token can see.
{% endstep %}
{% endstepper %}

## Response Envelope

Every response, success or error, is wrapped in the same `meta` envelope:

```json
{
  "data": { ... },
  "meta": {
    "status": "success",
    "errors": [],
    "warnings": []
  }
}
```

`meta.warnings` can carry non-fatal notices alongside a successful response — for example, two groups in a workspace sharing the same `user_attribute_precedence`.

## Error Responses

Errors set `meta.status` to `"error"` and populate `meta.errors` with one entry per problem:

```json
{
  "meta": {
    "status": "error",
    "errors": [
      {
        "message": "Workspace not found",
        "status_code": 404,
        "error_code": "not_found",
        "occurred_at": "2026-08-05T12:00:00Z"
      }
    ],
    "warnings": []
  }
}
```

{% hint style="warning" %}
`occurred_at`, `error_code`, and `error_metadata` are optional and may be `null` — key off `status_code` and `message` first.
{% endhint %}

| Code | Meaning | When it happens |
| --- | --- | --- |
| `400` | Bad Request | An application-level validation rule failed — not a schema/type error, but a business rule (e.g. a value out of range, an inferred setting with no valid value). |
| `401` | Invalid token | The bearer token fails gateway-level verification — wrong issuer/key-id, wrong signing algorithm, bad signature, failed claims, or an empty subject. |
| `403` | Forbidden | Any authentication or authorization failure — missing/invalid credential, a PAT used against a workspace outside its scope, insufficient permission, or a `workspace_id`/`group_id`/etc. that doesn't exist or isn't visible to this token. These deliberately share one generic message — the API does not reveal which case applies. |
| `404` | Not Found | A specific named resource wasn't found within a scope you can otherwise access — distinct from the 403 case above, which covers the *scope itself* (e.g. the `workspace_id`) being inaccessible. Also returned for a request path that doesn't match any route. |
| `405` | Method Not Allowed | Valid path, wrong HTTP verb (e.g. `PUT` on a route that only defines `GET`/`POST`). |
| `409` | Conflict | Trying to create something that already exists in a way that would collide — a duplicate attribute-definition name in a workspace, an attribute already set on this group/member, or an existing group membership. |
| `422` | Unprocessable Entity | The request itself doesn't match the expected shape — malformed JSON, a required field missing, or a field of the wrong type — caught by schema validation before any application logic runs. |
| `429` | Too Many Requests | Rate limit exceeded. |
| `500` | Internal Server Error | An unexpected, unhandled error. The message is always the same generic string — no internal detail is ever leaked to the client. |

## Rate Limiting

The API enforces rate limits, keyed by your personal access token. Limits vary by endpoint, so don't assume a single number applies everywhere — check your current quota from the response headers instead of a fixed value from documentation:

- `X-RateLimit-Limit` — your quota for the current window
- `X-RateLimit-Remaining` — requests left in the current window
- `X-RateLimit-Reset` — seconds until the window resets

When a request is rejected, the API returns `429` with the standard error envelope:

```json
{
  "meta": {
    "status": "error",
    "errors": [
      {
        "message": "Rate limit exceeded",
        "status_code": 429
      }
    ],
    "warnings": []
  }
}
```

{% hint style="info" %}
On a `429`, back off exponentially and use `X-RateLimit-Reset` to know when it's safe to retry, rather than a fixed retry delay.
{% endhint %}
