---
sidebar_position: 6
---

# dbt integration

To integrate Zenlytic's data model with your dbt models, you can simply reference your dbt models with `{{ ref('my_dbt_model_name') }}` in the [view files](../4_data_modeling/6_view.md) of your data model.

The validation step in the [cli](4_cli.md#validation) will catch any non-existent dbt models that are referenced in your data model. 

For this to work you need to have your data model and your dbt models in the same GitHub repo. 
