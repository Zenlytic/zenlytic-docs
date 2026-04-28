# Ask Zoë for Data Model Recommendations

You don't have to author your data model alone. Zoë can recommend specific changes directly from chat — new measures, new dimensions, new relationships, calculation logic, or how to restructure something that isn't answering questions the way you'd like.

This is often the fastest way to extend your model. Ask in plain English, take Zoë's recommendation, and apply it in [Context Manager](../zenlytic-ui/context_manager.md).

## When to ask Zoë instead of authoring from scratch

Good questions to bring to Zoë:

* **"How do I add a measure for X?"** — e.g. "How do I add a measure for repeat order rate?" or "How do I define customer lifetime value?"
* **"How should I write this calculation?"** — e.g. "Write me the SQL for days between first and second order" or "How do I compute rolling 30-day revenue?"
* **"How should these tables be joined?"** — e.g. "What's the right relationship between `orders` and `shipments`?"
* **"Why did you pick the wrong field?"** — Zoë can often diagnose why she chose the wrong field and recommend adding a `synonym`, `zoe_description`, or a new measure to prevent it next time. See also [Fixing Zoë's Mistakes](../core-concepts/fixing-zoes-mistakes.md).
* **"What should I add to this view to make it more useful?"** — Zoë can look at a view and recommend missing measures, synonyms, or descriptions.

## What Zoë gives you back

Depending on the question, Zoë will return one or more of:

* **A YAML snippet** to paste into the relevant view, model, or topic file
* **A plain-English explanation** of what the change does and why
* **A note** about where the change should go (view `description` vs. field `zoe_description` vs. the system prompt) — see [Context Surfaces](../core-concepts/context-surfaces.md) for the decision framework
* **Follow-up questions** if she needs more detail (e.g., "Do you want this measure to exclude returned orders?")

Zoë's recommendations are suggestions, not automatic changes — she doesn't edit your data model files directly. You stay in control of what actually ships.

## Example: adding a measure

You ask:

> How do I add a measure for repeat purchase rate in the `orders` view?

Zoë might respond with something like:

```yaml
- name: repeat_purchase_rate
  field_type: measure
  type: number
  sql: "{% raw %}${number_of_repeat_customers} / nullif(${total_customers}, 0){% endraw %}"
  value_format_name: percent_1
  description: The share of customers who placed more than one order.
  zoe_description: Use this for retention questions. Numerator is customers with 2+ orders; denominator excludes null customer_ids.
```

…along with a note explaining that she used `type: number` with a ratio SQL expression (one of the two valid measure patterns — see [Measures](measure.md) for the full rule), and a pointer to add synonyms like "retention rate" or "repeat rate" so she picks this measure on future questions.

## Example: asking about a relationship

You ask:

> How should I join the `orders` table to the `shipments` table?

Zoë will inspect both views and recommend a [relationship](relationships.md) block for the model file with the right `relationship` cardinality and `sql_on` condition, plus a note if the join risks fan-out.

## Applying the recommendation

1. Open [Context Manager](../zenlytic-ui/context_manager.md).
2. Navigate to the file Zoë named (view, model, or topic).
3. Paste the snippet in the right place and save.
4. If the change is significant, deploy to production when you're ready.
5. Re-ask your original question to confirm the change works end-to-end.

## Iterate based on what goes wrong

Zoë's recommendations aren't always perfect on the first try. If her suggestion doesn't produce the right answer when you test it, tell her — "that measure gave the wrong number, the denominator should exclude internal test accounts" — and she'll refine the recommendation. This is the same iterative philosophy the whole data model is built on: add context to fix the specific error you observed, rather than trying to anticipate every edge case up front. See [Progressive Enrichment](../core-concepts/progressive-enrichment.md) for the broader playbook.

## Related

* [Context Manager](../zenlytic-ui/context_manager.md) — where you apply Zoë's recommendations
* [Context Surfaces](../core-concepts/context-surfaces.md) — when to use `description`, `zoe_description`, synonyms, or the system prompt
* [Fixing Zoë's Mistakes](../core-concepts/fixing-zoes-mistakes.md) — diagnostic flow when Zoë gives a wrong answer
* [Measures](measure.md) — valid/invalid aggregation patterns for measure SQL
