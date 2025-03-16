---
sidebar_position: 6
---

# Workflows in Embedding (beta)


You can add workflows to the embedding experience by creating the workflows in the UI, and then sharing those workflows with "all users" as Viewer (which only gives the ability to run the workflow).

![sharing-workflow](../assets/sharing-workflow.png)

Once you have those workflows created, and shared you will see the lightening bolt option in the embedded UI to run the workflow.

:::tip Use the right role

Only the `embedded_with_scheduling` role has access to workflows, so you will not see the option to run workflows if you only use the `embed` role.

:::

In the chat UI, that will look like this

![workflow-in-chat](../assets/run-workflow-in-chat.png)


### Running automatically


To run workflows without making the user pick which workflow they want to run, you will pass query parameters to select the workflow you want to use. 

You can get the workflow id from the 3 dot menu on the workflow creation page, or from the url on the workflow creation page. You will pass query parameters like this to run a workflow

`https://app.zenlytic.com/chat/my-conversation-id?workflowId=<my-workflow-id>`

That will kick off the run of the workflow. If the workflow requires inputs, it will open a modal asking the user for the inputs. If it does not require inputs, the workflow will start running immediately.

Note: you can also run a normal chat question via query parameters as well. To do that you will pass query parameters in the URL like this:

`https://app.zenlytic.com/chat/my-conversation-id?q=hello`

This will initiate the conversation with the user's question `"hello"`.
