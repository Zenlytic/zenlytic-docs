---
layout:
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# Table Calculation Syntax

This is a reference for the functions available to the table calculations, including examples of usage in practice.

`sum`: The sum function sums up the numeric column it operates on. For example, you could use this function like `[orders.total_revenue] / sum([orders.total_revenue])` to get the percent of the total for the total revenue column. This will divide each row of the total revenue column by the sum of it's total using this function.

| total revenue | fx (percent of total revenue) |
| ------------- | ----------------------------- |
| 5             | 36%                           |
| 3             | 21%                           |
| 6             | 43%                           |

`cumulativesum`: The cumulative sum function creates a running total of the column going in the sort order of the column. For example, if you used `cumulativesum([orders.total_revenue])` on the below table, you'd see this result. Note: You cannot pass an expression to the `cumulativesum` function, you can only pass the reference to the column itself (e.g. passing \[orders.total\_revenue] will work as expected, but passing \[orders.total\_revenue] \* 2 will not)

| total revenue | fx (cumulativesum of total revenue) |
| ------------- | ----------------------------------- |
| 5             | 5                                   |
| 3             | 8                                   |
| 6             | 14                                  |

`+ - * /`: You can use the arithmetic operations `+`, `-`, `*`, and `/` to combine scalar values or other columns. For example, you could multiply the total revenue column by `.78` then add in the shipping value `[orders.total_revenue] * .78 + [orders.total_shipping]`.

| total revenue | total shipping | fx (total revenue \* .78 + total shipping) |
| ------------- | -------------- | ------------------------------------------ |
| 5             | 0              | 3.9                                        |
| 3             | 2              | 4.34                                       |
| 6             | 1              | 5.68                                       |
