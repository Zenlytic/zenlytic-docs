---
sidebar_position: 7
---

# Metricflow (dbt Semantic Layer) integration

To integrate Zenlytic's data model with your dbt models, define the dimensions and measures (metrics) in semantic models section of dbt. Follow this page to get started with [Metricflow (dbt Semantic Layer)](https://docs.getdbt.com/docs/build/sl-getting-started).

## Limitations

Here let's talk through some limitations of Zenlytic's integration with Metricflow.

Zenlytic does not support the following concepts in Metricflow:
1. The `percentile` aggregation on a measure
2. The `non_additive_dimension` property
3. The usage of [natural keys](https://docs.getdbt.com/docs/build/entities) in joins (using an array of fields to join instead of 1 field or custom SQL)
4. `window` and `grain_to_date` on cumulative metrics
5. `offset_window` in derived metrics

