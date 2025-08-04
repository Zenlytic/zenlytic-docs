# Formatting

Passing the `value_format_name` parameter to your [field](field.md) lets you easily format values in a way that's easy to read for business users.

## Options

There are several options. Broadly speaking, there is a format type followed by a number of decimal places. For example, `decimal_1` formats the number like a decimal and rounds to one decimal place.

<table><thead><tr><th>Value Format Name</th><th width="281.20703125">Unformatted Value</th><th>Formatted Value</th></tr></thead><tbody><tr><td>decimal</td><td>12345.678</td><td>12346</td></tr><tr><td>decimal_0</td><td>12345.678</td><td>12,346</td></tr><tr><td>decimal_1</td><td>12345.678</td><td>12,345.7</td></tr><tr><td>decimal_2</td><td>12345.67812</td><td>12,345.68</td></tr><tr><td>decimal_3</td><td>12345.67812</td><td>12,345.678</td></tr><tr><td>decimal_4</td><td>12345.67812</td><td>12,345.6781</td></tr><tr><td>decimal_pct_0</td><td>3.456</td><td>3%</td></tr><tr><td>decimal_pct_1</td><td>3.456</td><td>3.5%</td></tr><tr><td>decimal_pct_2</td><td>3.456</td><td>3.46%</td></tr><tr><td>decimal_pct_3</td><td>3.4561</td><td>3.456%</td></tr><tr><td>decimal_pct_4</td><td>3.4561</td><td>3.4561%</td></tr><tr><td>percent_0</td><td>0.3456</td><td>35%</td></tr><tr><td>percent_1</td><td>0.3456</td><td>34.6%</td></tr><tr><td>percent_2</td><td>0.3456</td><td>34.56%</td></tr><tr><td>percent_3</td><td>0.345612</td><td>34.561%</td></tr><tr><td>percent_4</td><td>0.345612</td><td>34.5612%</td></tr><tr><td>eur</td><td>12345.678</td><td>€12.3k</td></tr><tr><td>eur_0</td><td>12345.678</td><td>€12,346</td></tr><tr><td>eur_1</td><td>12345.678</td><td>€12,345.7</td></tr><tr><td>eur_2</td><td>12345.678</td><td>€12,345.68</td></tr><tr><td>usd</td><td>12345.678</td><td>$12.3k</td></tr><tr><td>usd_0</td><td>12345.678</td><td>$12,346</td></tr><tr><td>usd_1</td><td>12345.678</td><td>$12,345.7</td></tr><tr><td>usd_2</td><td>12345.678</td><td>$12,345.68</td></tr><tr><td>image_from_url</td><td>https://mydomain.com/myimage</td><td>(Rendered Image)</td></tr></tbody></table>

## Examples

Here's an examples of a field with `value_format_name` as a property.

```yaml
- name: avg_price
  field_type: measure
  type: average
  sql: ${price}
  value_format_name: usd
```
