---
sidebar_position: 1
---

# Connecting

First, we'll go through how to set up a `profiles.yml` file, which is the best solution for an individual using Zenlytic's metrics layer on his or her local machine. Second, we'll look at other ways of passing the configuration into the metrics layer.

## Profile set up

There are three ways to set up a profile, that is access the data model and find credentials for your data warehouse:

1. Local repo
2. Explicitly passed values

Metrics Layer gets this information by looking for the same `profiles.yml` file that [dbt](https://www.getdbt.com) uses.

### Local repo

This is the best method when the repo with your LookML or [zenlytic data model](../../4_data_modeling/1_data_modeling.md) is on your local machine. Your `profiles.yml` will looks like this with a connection to Snowflake.

The `demo_connection` name, which is the same name that dbt references, is the value you'd use for your [connection](../../4_data_modeling/2_model.md#properties) property in your model file.

```
demo_connection:  # This references the connection property in the YAML model or dbt project
  target: dev
  outputs:
    dev:
      type: snowflake
      account: 123p0iwe.us-east-1
      user: demo_user
      password: very_secure_password
      warehouse: compute_wh             # optional
      database: demo                    # optional (required by dbt, but not your data model)
      schema: analytics                 # optional (required by dbt, but not your data model)

```

You will be able to connect with the following python code, if you are in the repo of the Zenlytic data model project (or LookML).

```
from metrics_layer import MetricsLayerConnection

conn = MetricsLayerConnection('./')

df = conn.query(metrics=["total_revenue"], dimensions=["channel", "region"])
```


### Explicitly passed values

This is the best method for connecting if you're using a local jupyter notebook, hosted notebook, or production back end. You can either connect by referencing a local repo on your machine (first example below) or by connecting to a github repo and pulling a repo and branch in that repo (second example below).

Here's an example with a local repo.

```
from metrics_layer import MetricsLayerConnection

# Give metrics_layer the info to connect to your data model and warehouse
config = {
  "location": "~/Desktop/my-lookml-repo",
  "connections": [
    {
      "name": "mycompany",              # The name of the connection in LookML or yaml (you'll see this in model files)
      "type": "snowflake",
      "account": "2e12ewdq.us-east-1",
      "username": "demo_user",
      "password": "q23e13erfwefqw",
      "database": "ANALYTICS",          # Optional
      "schema": "DEV",                  # Optional
    }
  ],
}
conn = MetricsLayerConnection(**config)

# You're off to the races. Query away!
df = conn.query(metrics=["total_revenue"], dimensions=["channel", "region"])
```

Here's another example pulling a repo from GitHub.

```
from metrics_layer import MetricsLayerConnection

# Give metrics_layer the info to connect to your data model and warehouse
config = {
  "location": "https://{YOUR_GITHUB_USERNAME}:{YOUR_GITHUB_ACCESS_TOKEN}@github.com/my_company/my_company_data_model",
  "branch": "dev",
  "connections": [
    {
      "name": "mycompany",              # The name of the connection in yaml (you'll see this in model files), or name of dbt profile
      "type": "snowflake",
      "account": "2e12ewdq.us-east-1",
      "username": "demo_user",
      "password": "q23e13erfwefqw",
      "database": "ANALYTICS",          # Optional
      "schema": "DEV",                  # Optional
    }
  ],
}
conn = MetricsLayerConnection(**config)

# You're off to the races. Query away!
df = conn.query(metrics=["total_revenue"], dimensions=["channel", "region"])
```

