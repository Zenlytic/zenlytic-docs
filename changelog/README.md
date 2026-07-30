---
description: What's new in Zenlytic — product updates, new features, and notable changes.
---

# Changelog

{% hint style="info" %}
**Scaffold for section testing.** The entries below are real but abbreviated, and exist to verify that this section syncs, renders, and generates an RSS feed. Replace with the maintained changelog before publishing.
{% endhint %}

{% updates %}

{% update date="2026-07-30" tags="Git" %}
## Commit identity documented for GitHub deploy keys

Zenlytic commits as `Zenlytic <hello@zenlytic.com>` on every save from Context Manager. Organizations enforcing commit-metadata rules now have setup guidance to allow this before connecting, rather than discovering it through failed saves.

See [Connecting to GitHub with a deploy key](https://docs.zenlytic.com/authentication-and-security/connecting_to_github_with_a_deploy_key).
{% endupdate %}

{% update date="2026-07-15" tags="Context Manager" %}
## Pull from Remote

Pushed changes directly to your data model repo and Zoë isn't seeing them? **Account settings → Pull from Remote** rebuilds the cache from your remote branch.
{% endupdate %}

{% update date="2026-06-20" tags="Data Modeling" %}
## Relationships replace identifiers

Joins are now defined with `relationships:` on the model file. Existing `identifiers:` configurations continue to work, but new joins should use Relationships.
{% endupdate %}

{% endupdates %}
