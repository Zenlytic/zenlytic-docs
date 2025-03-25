---
sidebar_position: 16
---

# Referenceable Attributes

Referenceable attributes are attributes that can be used in queries either on views or dimensions, dimension groups or measures. 

The include all user attributes that you pass in via the API (in embedding) or user attributes you have on the user that you've assigned through the UI.

In addition to those user attributes, these are also default user attributes that will be present on the user or query without any additions on your part.

### Defaults 

These are two objects you can interact with that are populated by default.

#### User Attributes

The first is the `user_attributes` object. This object will include all the values you pass, and will additionally include:

`email`: The email for the user making the query, as defined in their Zenlytic account.

#### Query Attributes

The second is the `query_attributes` object. This object will show attributes of the query that is being run, and will include:

`dimension_group`: This is the dimension group of the query (only applicable for fields that are of `field_type: dimension_group`). It will be the value of the dimension group (e.g. `raw`, `date`, `week`, `month_of_year`, etc)
