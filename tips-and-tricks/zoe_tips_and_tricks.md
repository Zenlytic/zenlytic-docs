# Working with Zoë Tips and Tricks

When thinking about how you're defining your data model for use with Zoë, ask this question.

> **Key Question**
>
> Could a talented data analyst answer questions using this data model on their first day on the job before they have any other context on the business?

If the answer to that question is yes, then Zoë will perform great! If not, use some of the tips below to encode more business context, so Zoë knows what metrics to choose in which situations.

## Voice

You can also ask Zoë questions verbally as well as with text. You can do this by clicking on the microphone to start Zoë recording and clicking again to stop her listening. You can also use the keyboard shortcut `cmd + i` to start and stop Zoë's recording.

## Clear Naming

Clearly naming your metrics (measures) and dimensions is key for Zoë to perform well for you. If you have two revenue metrics defined as `Revenue first` and `Revenue second`, Zoë, like a human analyst, will have no idea which one to pick.

However, if you define those two values as `Gross revenue` and `Net revenue` Zoë will have no problem distinguishing between them and when to use one vs. the other. If an outside analyst could read all your metric definitions and understand which ones to use in the right cases, Zoë would also be able to.

## Let Zoë know about categorical values

Zoë will _never_ index your data unless you explicitly tell her to. This protects your privacy and makes sure we never index sensitive or regulated data.

Many times you'll want to be able to ask questions like "How many orders do we have in fulfillment placed more than a week ago?" But if the `fulfillment` category is hidden in a field nebulously called `status`, Zoë won't know how to find the right filter.

Add the `searchable` property to the `status` dimension like:

```yaml
- name: status
  field_type: dimension
  type: string
  sql: ${TABLE}.status
  searchable: true
```

This will tell Zoë to index the categories in this dimension (this works up to 10,000 categories, contact support for a use case with >10,000 unique categories).

Now Zoë will be able to answer the question "How many orders do we have in fulfillment placed more than a week ago?" by applying the right `status = 'fulfillment'` filter using the capitalization in the database to the query.

## Associate times with metrics

Each metric in Zenlytic should be associated with a time dimension group. The associated dimension group with a metric is called that metric's `canon_date`.

> **Important**
>
> This let's Zoë apply time periods correctly and trend metrics over time while guaranteeing that we're using the right time dimension.

You can associate a time dimension with a view using the `default_date` property.

```yaml
version: 1
type: view
name: google_ad_stats
model_name: my_company 
sql_table_name: PROD.GOOGLE_AD_STATS
default_date: ad_stat_recorded_at

fields:
...
- name: ad_stat_recorded_at
  field_type: dimension_group
  type: time
  datatype: date
  timeframes:
  - raw
  - date
  - week
  - month
  - quarter
  - year
  sql: ${TABLE}.DATE
...
```

Under the default date property you'll just reference the `name` of the time you want to use as the default date.

The default date will be the default `canon_date` for all metrics in that view unless their `canon_date` is set on the metric explicitly.

> **Tip**
>
> You can also use a `canon_date` or `default_date` that is not in the same table as your metric. To use that date, just make sure it is possible to join that field in, and reference it like `default_date: google_record_stats.recorded_at`, using the view name before the field name.

Using an example from subscription management

{% code overflow="wrap" %}
```yaml
version: 1
type: view
name: subscriptions
model_name: my_company
sql_table_name: PROD.SUBSCRIPTIONS
default_date: created_at

fields:
...
- name: created_at
  field_type: dimension_group
  type: time
  timeframes:
  - raw
  - date
  - week
  - month
  - quarter
  - year
  sql: ${TABLE}.CREATED_AT

- name: canceled_at
  field_type: dimension_group
  type: time
  timeframes:
  - raw
  - date
  - week
  - month
  - quarter
  - year
  sql: ${TABLE}.CANCELED_AT

- name: new_subscriptions
  field_type: measure
  type: count_distinct
	sql: ${subscription_id}
  description: "This is the unique number of subscriptions by the date created"

- name: canceled_subscriptions
  field_type: measure
  type: count_distinct
	sql: ${subscription_id}
  canon_date: canceled_at
  description: "This is the unique number of subscriptions by the date canceled"
...
```
{% endcode %}

The first measure inherits the `canon_date` of `created_at` from the `default_date` on the view, and the second one is set explicitly to be `canceled_at` because its definition needs to use another date to derive its meaning.

## Use drills to define your entities

You can use drills/entities in Zenlytic to let Zoë know about important entities in your data. Entities can be any group of fields that you want, and they can describe anything from `products` to `users` to `transactions` to `sales_reps`. Let’s look at an example of defining one of those entities for `sales_reps`:

```yaml
version: 1
type: view
name: sales_reps
model_name: my_company
sql_table_name: PROD.SALES_REPS
default_date: joined_at

fields:
...
- name: sales_rep_id
  field_type: dimension
  type: string
  sql: ${TABLE}.id
  tags: ['Sales Rep']
  drill_fields: [first_name, last_name, email, status]

- name: first_name
  field_type: dimension
  type: string
  sql: ${TABLE}.first_name

- name: last_name
  field_type: dimension
  type: string
  sql: ${TABLE}.last_name

- name: email
  field_type: dimension
  type: string
  sql: ${TABLE}.email

- name: status
  field_type: dimension
  type: string
  sql: ${TABLE}.status

- name: joined_at
  field_type: dimension_group
  type: time
  timeframes:
  - raw
  - date
  - week
  - month
  - quarter
  - year
  sql: ${TABLE}.JOINED_AT
  ...
```

This will let Zoë know that you have an entity called a “Sales rep” and that entity should typically include the fields `first_name`, `last_name`, `email`, and `status` when that entity is referenced.

This will also give you a drop down option on all Zenlytic plots for “Drill into sales reps” when it’;s possible to join these fields into your data.

## Descriptions help steer Zoë’s decisions

You can add a `description` to your metrics (measures) like this

```yaml
- name: gross_aov
  field_type: measure
  type: average
  sql: ${TABLE}.revenue
  description: |>
      This is the gross average order value. This just covers 
      DTC revenue, and is sometimes internally referred 
      to as 'the magic' This is the metric that 
      should be used when someone asks about AOV, generally speaking
```

In the description above, we’re adding a lot of useful context that the model will be able to use to improve its performance. For example, if someone now asks for the “magic” or nebulously asks for AOV without specifying gross or net, Zoë will know which metric to choose based on the description.

Writing good descriptions will help your end users better understand what they’re looking at and it will boost Zoë performance.

## Synonyms help Zoë find metrics

You can use the `synonyms` tag to specify keywords for Zoë so she can find the the right field. For example, you might have a LOT of “customers” fields but you want to make sure Zoë always sees the `new_vs_repeat` field on order lines , even though the name of the view doesn’t have a reference to a customer by name.

In this example, we’ve added the synonyms `customer` and `loyalty` to the `new_vs_repeat` field to make sure if Zoë users are asking about “existing customers” or repeat behavior like “loyalty” this field will show up in context for Zoë.

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
