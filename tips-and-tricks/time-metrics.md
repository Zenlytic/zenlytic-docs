# Time Metrics

Each metric in Zenlytic should be associated with a time dimension group. The associated dimension group with a metric is called that metric's `canon_date`.

> ⏱️ This let's Zoë apply time periods correctly and trend metrics over time while guaranteeing that we're using the right time dimension.

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

> 🛠 You can also use a `canon_date` or `default_date` that is not in the same table as your metric. To use that date, just make sure it is possible to join that field in, and reference it like `default_date: google_record_stats.recorded_at`, using the view name before the field name.

Using an example from subscription management:

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

The first measure inherits the `canon_date` of `created_at` from the `default_date` on the view, and the second one is set explicitly to be `canceled_at` because its definition needs to use another date to derive its meaning.
