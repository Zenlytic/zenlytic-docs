# How to Steer Zoë's Answers

{% hint style="info" %}
**This page has moved.** The canonical home for how Zoë ingests context — the surfaces, their visibility, character limits, and when to use each — is now [Context Surfaces](../core-concepts/context-surfaces.md).
{% endhint %}

Zoë uses multiple sources of context to answer questions accurately — the system prompt, skills, view and field descriptions, synonyms, and searchable values. Each source has different visibility and different character limits.

For the full reference, see [Context Surfaces](../core-concepts/context-surfaces.md), which covers:

* The complete surfaces/visibility/char-limits table
* When to reach for each surface
* The `description` vs. `zoe_description` distinction with char limits per level
* How Skills fit alongside the system prompt and view/field context
* Why Memories are being retired in favor of Skills

## Quick reference

The shortest version:

* **Universal rules?** System prompt.
* **Complex, sometimes-relevant patterns?** A [Skill](../zenlytic-ui/skills.md).
* **Table-specific guidance?** View `description` (user-facing) or `zoe_description` (agent-only).
* **Field-specific guidance?** Field `description` or `zoe_description`.
* **What users call the field?** `synonyms` on the field.
* **What values exist in a column?** `searchable: true` on the dimension.

See [Context Surfaces](../core-concepts/context-surfaces.md) for the detailed version.
