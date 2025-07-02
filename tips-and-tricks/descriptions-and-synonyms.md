# Descriptions and Synonyms

## Descriptions help steer Zoë's decisions

You can add a `description` to your metrics (measures) like this:

```yaml
- name: gross_aov
  field_type: measure
  type: average
  sql: ${TABLE}.revenue
  description: |
    This is the gross average order value. This just covers 
    DTC revenue, and is sometimes internally referred 
    to as 'the magic' This is the metric that 
    should be used when someone asks about AOV, generally speaking
```

In the description above, we're adding a lot of useful context that the model will be able to use to improve its performance. For example, if someone now asks for the "magic" or nebulously asks for AOV without specifying gross or net, Zoë will know which metric to choose based on the description.

Writing good descriptions will help your end users better understand what they're looking at and it will boost Zoë performance.

## Synonyms help Zoë find metrics

You can use the `synonyms` tag to specify keywords for Zoë so she can find the the right field. For example, you might have a LOT of "customers" fields but you want to make sure Zoë always sees the `new_vs_repeat` field on order lines , even though the name of the view doesn't have a reference to a customer by name.

In this example, we've added the synonyms `customer` and `loyalty` to the `new_vs_repeat` field to make sure if Zoë users are asking about "existing customers" or repeat behavior like "loyalty" this field will show up in context for Zoë.

```yaml
- name: new_vs_repeat
  field_type: dimension
  type: string
  sql: ${TABLE}.new_vs_repeat
  description: The new vs repeat status of the purchaser
  synonyms: 
  - customer
  - loyalty
```

```
```
