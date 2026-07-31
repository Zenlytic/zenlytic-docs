# API Reference

{% hint style="warning" %}
**Placeholder — not yet publishable.**

Before this section can go live, the generated OpenAPI spec needs upstream fixes in `Zenlytic/zenlytic` — see PR #122. As generated today the spec:

* uses FastAPI's default `title: "FastAPI"` and `version: "0.1.0"`
* has no `servers` block, so interactive "Test it" has no base URL
* leaves all 203 operations untagged, producing one flat list of 126 endpoints
* includes internal surface (`/dev/*`, `/internal/*`, `/webhooks/stripe`, billing, workspace-manager, SAML and credential endpoints) that should be excluded with `include_in_schema=False`

**The generator also needs a new target path.** The workflow in `Zenlytic/zenlytic` currently opens PRs that write `openapi.json` to the **repository root**. After this restructure the root holds no content, so it must write to `developer/openapi.json` instead — otherwise every regeneration lands the spec somewhere no section reads.
{% endhint %}

Placeholder for the Zenlytic API reference documentation.
