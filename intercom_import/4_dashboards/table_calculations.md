# Table Calculations

Table calculations let you perform calculations on the results of your query. You can add, edit, and delete columns in the table view.

![Table Calculations 1](/assets/table-calculations-1.png)

## Adding a Column

To add a column, click the "+" button in the table header. You can then enter a formula for your calculation.

![An example of using Zenlytic's autocomplete to find columns](/assets/table-calculations-2.png)

## Editing and Deleting Columns

You edit and delete a column by hovering the column in the table and then clicking on the column menu button.

![Column menu options](/assets/table-calculations-3.png)

## Example Calculations

Here are some examples of table calculations you can perform:

![Example calculations](/assets/table-calculations-4.png)

General Tips
============

#### Use autocomplete to find columns and functions. You can click or using your keyboard's arrow keys/enter to make a selection.

![An example of using Zenlytic's autocomplete to find columns](/assets/image.png)#### You edit and delete a column by hovering the column in the table and then clicking on the column menu button

![Image](/assets/image.png)

#### There's a collection of common formulas available in the column menu for columns that are `measures`.

![Image](/assets/image.png)

Functions
=========
* sum
* [cumulativesum](#h_8083404370)
* [offset](#h_a97997c0a0)
* [cell\_value](#h_325a463256)
* [arithmetic operators](#h_b069e4b503)

sum

The `sum` function sums up the numeric column it operates on. For example, you could use this function like `[orders.total_revenue] / sum([orders.total_revenue])` to get the percent of the total for the total revenue column. This will divide each row of the total revenue column by the sum of its total using this function.

#### Example Formula

```
[orders.total_revenue] / sum([orders.total_revenue])
```

#### Result

| | |
| --- | --- |
| **total revenue** | **fx (percent of total revenue)** |
| 5 | 36% |
| 3 | 21% |
| 6 | 43% |

cumulativesum

The `cumulativesum` function creates a running total of the column going in the sort order of the column. For example, if you used `cumulativesum([orders.total_revenue])`, each cell in your calculated column will be the summed up total of all previous cells in the `orders.total_revenue` column.

#### Example Formula

```
cumulativesum([orders.total_revenue])
```

#### Result

| | |
| --- | --- |
| **total revenue** | **fx (cumulativesum of total revenue)** |
| 5 | 5 |
| 3 | 8 |
| 6 | 14 |

offset

The `offset` function allows you to access the value of a cell that is a certain number of rows away from the current cell. For example, if you used `offset([orders.total_revenue], 1)`, each cell in your calculated column would be the value of the cell in `orders.total_revenue` that is `1 rows` away from the current cell.

#### Example Formula

```
offset([orders.total_revenue], 1)
```

#### Result

| | |
| --- | --- |
| **total revenue** | **fx (offset of total revenue)** |
| 5 | NAN (because there is no previous value

 |
| 3 | 5 |
| 6 | 3 |

cell\_value

The `cell_value` function allows you to access the value of a fixed cell at a specific row number. For example, if you used `cell_value([orders.total_revenue], 1)`, all cells in your calculated column would be the value of the cell in column `orders.total_revenue` at `row 5`.

#### Example Formula

```
cell_value([orders.total_revenue], 1)
```

#### Result

| | |
| --- | --- |
| **total revenue** | **fx (cell\_value of total revenue)** |
| 5 | 5 |
| 3 | 5 |
| 6 | 5 |

Arithmetic Operators (+ - / \*)

You can use the arithmetic operations `+`, `-`, `*`, and `/` to combine scalar values or other columns. For example, you could multiply the total revenue column by `.78` then add in the shipping value `[orders.total_revenue] * .78 + [orders.total_shipping]`.

#### Example Formula

```
[orders.total_revenue] * .78 + [orders.total_shipping]
```

#### Result

| | | |
| --- | --- | --- |
| **total revenue** | **total shipping** | **fx (total revenue \* .78 + total shipping)** |
| 5 | 0 | 3.9 |
| 3 | 2 | 4.34 |
| 6 | 1 | 5.68 |

If you have additional questions about the types of formulas and functions you can use in table calculations, you can reference the developer docs [here](/data_modeling/table_calculation_syntax).
