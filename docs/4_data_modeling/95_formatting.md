---
sidebar_position: 14
---

# Field formatting

Passing the `value_format_name` parameter to your [field](9_field.md) let's you easily format values in a way that's easy to read for business users.

---

### Options

There are several options. Broadly speaking, there is a format type followed by a number of decimal places. For example, `decimal_1` formats the number like a decimal and rounds to one decimal place.

Value Format Name | Unformatted Value | Formatted Value
---|---|---
decimal_0 | 12345.678 | 12,346
decimal_1 | 12345.678 | 12,345.7
decimal_2 | 12345.678 | 12,345.68
decimal_pct_0 | 3.456 | 3%
decimal_pct_1 | 3.456 | 3.5%
decimal_pct_2 | 3.456 | 3.46%
percent_0 | 0.3456 | 35%
percent_1 | 0.3456 | 34.6%
percent_2 | 0.3456 | 34.56%
usd | 12345.678 | $12,345.68
usd_0 | 12345.678 | $12,346
usd_1 | 12345.678 | $12,345.7
usd_2 | 12345.678 | $12,345.68


### Examples

Here's an examples of a field with `value_format_name` as a property.

```
- name: avg_price
  field_type: measure
  type: average
  sql: ${price}
  value_format_name: usd 
```

