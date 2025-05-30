
# Measures (or metrics)

Measures (or metrics) are aggregations performed inside of a SQL `group by` statement. A simple one is `sum(sales)`, which you could specify in your data model with `type: sum` and `sql: ${TABLE}.sales`. They can get highly complex and are as flexible as your data warehouse's SQL syntax.

