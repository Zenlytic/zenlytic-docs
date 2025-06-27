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

# Model

Models are references to a database connection. They serve as the data model's reference to the warehouses itself. That connection to the database is referenced by the model's `connection` property, which references the `name` property of the credentials specified in the Zenlytic interface.

Models, like all files in Zenlytic, are YAML text files.

## Properties

Models only have a few core properties:

`type`: (Required) The type of the file. For these model files is should always be `model`.

`name`: (Required) The name of the model. If you reference this model elsewhere this is the name you will use. Like all names, it follows [Zenlytic naming conventions](data_modeling.md#naming-conventions)

`label`: The label of the model is what shows up to the end users of your data model. If not specified it defaults to the name of the model.

`connection`: (Required) This is the name of the database connection that is being referenced in Zenlytic. You will specify this name when you enter the database credentials in Zenlytic, and it follows [Zenlytic's conventions for names](data_modeling.md#naming-conventions)

`fiscal_month_offset`: This controls the offset applied by Zenlytic to calculate "Fiscal" time frames. For example, if you set it to `1` then the `fiscal_quarter` will be set to start in `February` instead of `January`, which is the default. This takes any positive or negative integer. Default is `0`.

`week_start_day`: This controls which day of the week Zenlytic assumes your definition of "Week" starts on. The default value is `monday` (which is standard across ISO dates).

`timezone`: This controls which timezone Zenlytic uses when querying dates and times from your database. Zenlytic will automatically change the timezone from the database timezone to the timezone you set here. The default is to make no change to the timezone found in the database.

`default_convert_tz`: This field sets the default value for `convert_tz` in each [dimension group](dimension_group.md) in this model. This defaults to `true` so if you set a timezone, it will be applied, unless you either set this value to `false` or set `convert_tz: false` on the field itself.

`access_grants`: This field is a list of [access grants](access_grants.md). You can use access grants to control what data users of Zenlytic are allowed to see and access.

`mappings`: Mappings equate fields that mean the same thing but are in different, un-joinable tables. For example, you might have a `channel` field on the orders table and a `marketing_channel` field on the `marketing_spend` table, and they represent the same thing and have the same values. You can set up a mapping that connects those two fields in Zenlytic and leaves only one option for the end users to select. Zenlytic will dynamically figure out which field it should use or if it needs to use both. Find out more about mappings [in the join docs](join.md#merged-results--mappings) or in the example below.

## Examples

Here is an example of a model that also sets a timezone for all queries to the database.

```yaml
version: 1
type: model
name: my_model
connection: my_connection
timezone: America/New_York
```

This is an example of an access grant defined in a model. In this case, this access grant could be reused in a view or in fields to limit viewing to only users who have the their `department` user attribute equal to "Marketing". This model also sets the `week_start_day` property which tells which day to start weeks on (the default is monday).

The mapping example here maps the `marketing_spend.marketing_channel` to the `orders.channel` field so Zenlytic (and Zoë) know they are the same concept.

````yaml
version: 1
type: model
name: demo
week_start_day: sunday

# This defines the access grant
access_grants:
  - name: restrict_dept
    user_attribute: department
    allowed_values: ["Marketing"]

mappings:
  channel: 
    fields: [marketing_spend.marketing_channel, orders.channel]
    group_label: "Acquisition" # This controls the header under which the mapped field shows up in the UI
    description: "The channel the customer came to our site from"
    ```
````
