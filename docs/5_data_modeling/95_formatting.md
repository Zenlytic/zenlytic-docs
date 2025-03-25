---
sidebar_position: 14
---

# Field formatting

Passing the `value_format_name` parameter to your [field](9_field.md) lets you easily format values in a way that's easy to read for business users.

---

### Options

There are several options. Broadly speaking, there is a format type followed by a number of decimal places. For example, `decimal_1` formats the number like a decimal and rounds to one decimal place.

Value Format Name | Unformatted Value | Formatted Value
---|---|---
decimal | 12345.678 | 12346
decimal_0 | 12345.678 | 12,346
decimal_1 | 12345.678 | 12,345.7
decimal_2 | 12345.67812 | 12,345.68
decimal_3 | 12345.67812 | 12,345.678
decimal_4 | 12345.67812 | 12,345.6781
decimal_pct_0 | 3.456 | 3%
decimal_pct_1 | 3.456 | 3.5%
decimal_pct_2 | 3.456 | 3.46%
decimal_pct_3 | 3.4561 | 3.456%
decimal_pct_4 | 3.4561 | 3.4561%
percent_0 | 0.3456 | 35%
percent_1 | 0.3456 | 34.6%
percent_2 | 0.3456 | 34.56%
percent_3 | 0.345612 | 34.561%
percent_4 | 0.345612 | 34.5612%
eur | 12345.678 | €12.3k
eur_0 | 12345.678 | €12,346
eur_1 | 12345.678 | €12,345.7
eur_2 | 12345.678 | €12,345.68
usd | 12345.678 | $12.3k
usd_0 | 12345.678 | $12,346
usd_1 | 12345.678 | $12,345.7
usd_2 | 12345.678 | $12,345.68
image_from_url | https://mydomain.com/myimage | (Rendered Image)


### Examples

Here's an examples of a field with `value_format_name` as a property.

```
- name: avg_price
  field_type: measure
  type: average
  sql: ${price}
  value_format_name: usd 
```

