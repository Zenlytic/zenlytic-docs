---
sidebar_position: 1
---

# Models

Models are collections of explores that contain exactly one connection to a database. That connection to the database is referenced by the model's `connection` property and it references the `name` property of the credentials specified in the Zenlytic interface.

Models, like all files in Zenlytic, are yaml text files.

---

### Properties

Models only have a few core properties:

`type`: (Required) The type of the file. For these model files is should always be `model`.

`name`: (Required) The name of the model. If you reference this model elsewhere this is the name you will use. Like all names, it follows [Zenlytic naming conventions](1_data_modeling.md#naming-conventions)


`label`: The label of the model is what shows up to the end users of your data model. If not specified it defaults to the name of the model.


`connection`: (Required) This is the name of the database connection that is being referenced in Zenlytic. You will specify this name when you enter the database credentials in Zenlytic, and it follows [Zenlytic's conventions for names](1_data_modeling.md#naming-conventions)

`week_start_day`: This controls which day of the week Zenlytic assumes your definition of "Week" starts on. The default value is `monday` (which is standard across ISO dates).


`access_grants`: This field is a list of [access grants](8_access_grants.md). You can use access grants to control what data users of Zenlytic are allowed to see and access.

explores: This is a list of [explores](4_explore.md). Each explore must have all required parameters included.

