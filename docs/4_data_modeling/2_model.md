---
sidebar_position: 2
---

# Models

Models are references to a database connection. They serve as the data model's reference to the warehouses itself. That connection to the database is referenced by the model's `connection` property and it references the `name` property of the credentials specified in the Zenlytic interface.

Models, like all files in Zenlytic, are yaml text files.

---

### Properties

Models only have a few core properties:

`type`: (Required) The type of the file. For these model files is should always be `model`.

`name`: (Required) The name of the model. If you reference this model elsewhere this is the name you will use. Like all names, it follows [Zenlytic naming conventions](1_data_modeling.md#naming-conventions)


`label`: The label of the model is what shows up to the end users of your data model. If not specified it defaults to the name of the model.


`connection`: (Required) This is the name of the database connection that is being referenced in Zenlytic. You will specify this name when you enter the database credentials in Zenlytic, and it follows [Zenlytic's conventions for names](1_data_modeling.md#naming-conventions)

`week_start_day`: This controls which day of the week Zenlytic assumes your definition of "Week" starts on. The default value is `monday` (which is standard across ISO dates).

`timezone`: This controls which timezone Zenlytic uses when querying dates and times from your database. Zenlytic will automatically change the timezone from the database timezone to the timezone you set here. The default is to make no change to the timezone found in the database.

`access_grants`: This field is a list of [access grants](8_access_grants.md). You can use access grants to control what data users of Zenlytic are allowed to see and access.

### Examples 

Here is an example of a model that also sets a timezone for all queries to the database.

```
version: 1
type: model
name: my_model
connection: my_connection
timezone: America/New_York
```

This is an example of an access grant defined in a model. In this case, this access grant could be reused in a view or in fields to limit viewing to only users who have the their `department` user attribute equal to "Marketing". 

```
version: 1
type: model
name: demo

# This defines the access grant
access_grants:
  - name: restrict_dept
    user_attribute: department
    allowed_values: ["Marketing"]

```
