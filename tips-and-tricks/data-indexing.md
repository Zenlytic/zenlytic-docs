# Data Indexing

Let Zoë know about categorical values

Zoë will _never_ index your data unless you explicitly tell her to. This protects your privacy and makes sure we never index sensitive or regulated data.

Many times you'll want to be able to ask questions like "How many orders do we have in fulfillment placed more than a week ago?" But if the `fulfillment` category is hidden in a field nebulously called `status`, Zoë won't know how to find the right filter.

Add the `searchable` property to the `status` dimension like:

```yml
- name: status
  field_type: dimension
  type: string
  sql: ${TABLE}.status
  searchable: true
```

This will tell Zoë to index the categories in this dimension (this works up to 10,000 categories, contact support for a use case with >10,000 unique categories).

Now Zoë will be able to answer the question "How many orders do we have in fulfillment placed more than a week ago?" by applying the right `status = 'fulfillment'` filter using the capitalization in the database to the query.

{% hint style="info" %}
If the index hits the 10k default row limit, it will _not_ index any of the values in the column, you can override the limit using the `allow_higher_searchable_max` property, which will increase the indexing to 500k rows.
{% endhint %}

```yml
- name: status
  field_type: dimension
  type: string
  sql: ${TABLE}.status
  searchable: true
  allow_higher_searchable_max: true
```
