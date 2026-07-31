# API Reference

{% hint style="warning" %}
**Placeholder.** Seeded from `api-reference/overview.md` (PR #124), which was never listed in `SUMMARY.md` and so never appeared on the site.

Before this can be published, the generated OpenAPI spec needs upstream fixes in `Zenlytic/zenlytic` — see PR #122. As generated today the spec:

* uses FastAPI's default `title: "FastAPI"` and `version: "0.1.0"`
* has no `servers` block, so interactive "Test it" has no base URL
* leaves all 203 operations untagged, producing one flat list of 126 endpoints
* includes internal surface (`/dev/*`, `/internal/*`, `/webhooks/stripe`, billing, workspace-manager, SAML and credential endpoints) that should be excluded with `include_in_schema=False`
{% endhint %}

Placeholder for the Zenlytic API reference documentation.
