---
sidebar_position: 10
---

# User Attributes


This section covers how to set user attributes. User attributes are how users are assigned permissions that control their access to data (using [access controls](../4_data_modeling/8_access_grants.md)).

To set a user attribute on a user, go to Workspace Settings, then go to Team Members

![team-members](../assets/settings-team-members-attrs.png)


To set a user attribute, click on User Attributes, and set the attribute on the user. This example sets the user attribute `department` to `Engineering` on this user.


![user-attribute](../assets/user-attribute.png)


Now that this user's `department` attribute is set, their permissions will be determined by that (and any other attributes) set on that user.

For example, since the user's attribute for `department` has been set to `Engineering`, not one of the allowed options (`Executive`, `Finance`, `Marketing`) this user will not have access to anything restricted by this access grant.


![access-grants](../assets/access-grant-example.png)


For example, this user will *not* have access to this `email` field because the field has the `pii_access` access grant as one of the `required_access_grant` selections.

![access-grant-on-field](../assets/access-grant-on-field.png)

For more information on how to apply access grants and filters, look at the documentation on [access controls](../4_data_modeling/8_access_grants.md).


### User attributes populated automatically 

There are certain user attributes that are populated automatically.

The following user attributes are populated automatically and cannot be overridden:
* `email`: the logged in user's email


### Reserved User Attributes

There are certain user attributes that have special behavior.

#### zenlytic_connection_name

The `zenlytic_connection_name` user attribute has the special property that it will override the connection that is used to run queries on the data warehouse. You will set this property to the name of the credential, and that credential will be used in the query.

In the product, the user attribute is applied as the connection to use in all querying situations instead of:
* Testing the connection itself
* Listing databases when adding a new view
* Listing tables when adding a new view


#### zenlytic_connection_database


The `zenlytic_connection_database` user attribute has the special property that it will override the "database" in the connection to the data warehouse. Not all warehouses handle the "database" idea in the same way, so this is exactly how that breaks down in each situation and for each database type.

In the product, the user attribute is applied as the database to use in all querying situations instead of:
* Testing the connection itself
* Listing databases when adding a new view
* Listing tables when adding a new view

The attribute only applies as the database chosen in the connection itself for:
* Postgres
* MySQL
* Redshift
* Azure Synapse
* SQL Server
* Trino

The attribute applies in the `USE DATABASE` clause for:
* DuckDB
* Snowflake

The attribute *does not apply* in databases where it is not applicable, which are:
* BigQuery
* Druid
* Databricks
