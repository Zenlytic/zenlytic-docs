---
sidebar_position: 1
---

# Explores

Explores are collections of tables (views) that can be joined together using foreign keys. They are specified in a model file under the `explores` property. Each explore uses its model's `connection` that it is defined in to get data.

---

### Properties

`name`: (Required) The name of the explore. This can be the name of the [view](../_2_data_modeling_view.md) you want to create the explore from, or any name you choose. Note, if this name does not reference a view, you must specify the `from` parameter. If you reference this explore elsewhere this is the name you will use. Like all names, it follows [Zenlytic naming conventions](../_2_data_modeling.md#naming-conventions)

`from`: This is the [view](../_2_data_modeling_view.md) name to reference for the base of the explore. This parameter is optional, but it must be specified if the name of the explore does not reference a view.

`label`: The label of the explore is what shows up to the end users of your data model. If not specified it defaults to the name of the explore.

`description`: This is the description of the explore. This is helpful to let business users know what data is referenced here.

`fields`: This is an optional parameter that you can use to limit the fields that are visible in the explore. For syntax look at the documentation for [field syntax in sets](../2_data_modeling_set.md#field-syntax).

`join_for_analysis`: This is a list of [join](../_2_data_modeling_join.md) names which you would like to be automatically performed when running analysis like `Explain Change`. The list of joins is meant to balance query speed and depth of information searched. Lots of joins will search many variables, but the query will take a long time to run. Very few joins will mean the queries run faster but look at fewer variables.

`always_join`: This is a list of [join](../_2_data_modeling_join.md) names which you would like to always be joined in for queries to this explore, whether they are required by the query or not.

`sql_always_where`: This a SQL `where` statement that will *always* be applied to queries run in this explore. This is not removable by the end users of the platform. A good example of the parameter's value is `"email not ilike %mycompanyname.com%"`.

`required_access_grants`: This is a list of [access grant](../_2_data_modeling_access_grants.md) names that are required to access this explore. The grant names are always an `OR` condition. For example, if you listed `human_resources` and `executive` under this parameter, users who qualified for `human_resources`, `executive` or both would all be able to access data in this explore.

`access_filter`: This field adds a dynamic SQL `where` clause to the query based on a [user attribute](../data_modeling_access_grants.md#user-attributes). The name of the user attribute is set in the Zenlytic interface, and the name of the field references the view the field is in, and the name of the field itself. Note that the `where` filter condition is always: the field `=` to the value of the user attribute. It is specified as a list with two properties in the list's elements, as follows.
```
  field: my_view_name.my_field_name
  user_attribute: user_attribute_name
```

`always_filter`: This property is nested under another `filters` property and is a list of [field filters](../_2_data_modeling_field_filter), which have two properties, `field` and `value`. These filters will be applied to all queries on the explore by default, and they will be made visible to the user in the Zenlytic interface, with the option for the user to alter them there. This is an example of how to specify these parameters under the `always_filter` property.
```
filters:
    - field: field_name
      value:  "value"
```

`extra`: The extra property is like dbt `meta` property, and you can put whatever additional properties you want in here. For example, under this property you could add a property like this `maintainer: "jane doe"`
