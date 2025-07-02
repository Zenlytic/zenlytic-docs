# Formatting

Passing the `value_format_name` parameter to your [field](field.md) lets you easily format values in a way that's easy to read for business users.

## Options

There are several options. Broadly speaking, there is a format type followed by a number of decimal places. For example, `decimal_1` formats the number like a decimal and rounds to one decimal place.

| Value Format Name | Unformatted Value            | Formatted Value  |
| ----------------- | ---------------------------- | ---------------- |
| decimal           | 12345.678                    | 12346            |
| decimal\_0        | 12345.678                    | 12,346           |
| decimal\_1        | 12345.678                    | 12,345.7         |
| decimal\_2        | 12345.67812                  | 12,345.68        |
| decimal\_3        | 12345.67812                  | 12,345.678       |
| decimal\_4        | 12345.67812                  | 12,345.6781      |
| decimal\_pct\_0   | 3.456                        | 3%               |
| decimal\_pct\_1   | 3.456                        | 3.5%             |
| decimal\_pct\_2   | 3.456                        | 3.46%            |
| decimal\_pct\_3   | 3.4561                       | 3.456%           |
| decimal\_pct\_4   | 3.4561                       | 3.4561%          |
| percent\_0        | 0.3456                       | 35%              |
| percent\_1        | 0.3456                       | 34.6%            |
| percent\_2        | 0.3456                       | 34.56%           |
| percent\_3        | 0.345612                     | 34.561%          |
| percent\_4        | 0.345612                     | 34.5612%         |
| eur               | 12345.678                    | €12.3k           |
| eur\_0            | 12345.678                    | €12,346          |
| eur\_1            | 12345.678                    | €12,345.7        |
| eur\_2            | 12345.678                    | €12,345.68       |
| usd               | 12345.678                    | $12.3k           |
| usd\_0            | 12345.678                    | $12,346          |
| usd\_1            | 12345.678                    | $12,345.7        |
| usd\_2            | 12345.678                    | $12,345.68       |
| image\_from\_url  | https://mydomain.com/myimage | (Rendered Image) |

## Examples

Here's an examples of a field with `value_format_name` as a property.

```yaml
- name: avg_price
  field_type: measure
  type: average
  sql: ${price}
  value_format_name: usd
```
