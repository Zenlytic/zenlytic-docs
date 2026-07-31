# API Reference

{% hint style="warning" %}
**Placeholder — nothing here is published yet.** Keep the Developer section in Draft until this holds a real spec.
{% endhint %}

Placeholder for the Zenlytic API reference documentation.

## Before this can go live

An earlier auto-generated spec was reviewed and discarded as a test. Whenever the real one lands, these need resolving first — all of them are changes in `Zenlytic/zenlytic`, not in this repo, because a generated file edited here is overwritten on the next run.

**Write the spec into this section.** The generator opened PRs writing `openapi.json` to the docs repo **root**. Root no longer holds content, so the target must be `developer/openapi.json` — otherwise regeneration lands where no section reads it, with no visible symptom.

**Set the API's identity.** The spec inherited FastAPI's defaults — `title: "FastAPI"`, `version: "0.1.0"` — which would publish as the section heading. Set `title`, `version`, and a `servers` block on the `FastAPI(...)` app; without `servers` the interactive "Test it" panel has no base URL.

**Tag the operations.** Every operation was untagged, which renders as one flat list of 126 endpoints. GitBook groups API reference pages by tag, so `tags=[...]` on the routers is what turns this into something navigable.

**Exclude internal surface.** The generated spec covered the whole application, including `/dev/*`, `/internal/*`, `/webhooks/stripe`, billing, workspace-manager, SAML provider and credential endpoints. Publishing those discloses internal API surface to anyone reading the docs. Mark them `include_in_schema=False`.

A CI guard in this repo is worth adding alongside the upstream fix, so a future internal route can't leak silently:

```bash
jq -e '[.paths | keys[] | select(test("^/(dev|internal|webhooks)/"))] | length == 0' developer/openapi.json
```
