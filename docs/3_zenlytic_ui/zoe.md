---
sidebar_position: 2
---

# Zoë


Zoë is an AI data analyst who uses your cognitive layer to answer questions about your data for you. This will describe some of her capabilities, and how to use her. 


## Just ask.

To get started using Zoë, just ask her a question. If you don't know what you can ask about, simply ask her what data she can see and what some good questions for that data would be. She will be even more helpful with this if you share your job title and what you're trying to accomplish. 

When you're asking for data, you can be specific (e.g. "Show me sales YTD compared to the prior YTD, broken out by product type") or general (e.g. "I don't really know what I want to see, but tell me about channel and campaign performance"). Zoë can handle both type of questions, and will ask you follow up questions, if she isn't able to make reasonable assumptions about what you intend from your question.

Tip: If you have her perform a complex set of analysis, she can re-do that entire analyses with an additional filter in just a few seconds, so don't be afraid to ask things like "Do all of this but add a filter for the state California" to have her scope down a whole body of work.

## Querying

When Zoë creates queries, she doesn't do Text-to-SQL, she uses the governed measures and dimensions that are present in your Cognitive Layer. This guarantees that Zoë can *never* lie to you. She may misunderstand what you are asking about, but you will always be able to see exactly what data she is pulling because you'll see the measures, dimensions, and filters she used in her query, which map 1:1 to the SQL query she creates.

## Code Interpreter

Zoë also has access to a code interpreter. This is a sandbox environment where she can write and run python code to use on top of governed results from cognitive layer queries she runs.

This gives her a huge amount of flexibility to answer complex questions that involve merging results of separate queries, plugging in assumptions to scenarios, and doing clustering, correlation, or regression analysis.


## Personal Fields

In addition to creating queries on your existing measures and dimensions, Zoë can (for Develop and above roles, and when the feature is turned on) create Personal fields, which are measures and dimensions that are assigned to the person who created them, instead of the global data model. Those Personal Fields can be "promoted" into the global data model, but *Zoë cannot promote them*. You must do that in the UI.

We, very intentionally, have not given Zoë the ability to modify the global cognitive layer, to ensure your end users are always getting a consistent and governed experience. 


## Dashboards

Zoë can create new dashboards and add plots to those dashboards or add plots to existing dashboards. She can also search your dashboards for terms so you can answer questions like "What dashboards do we have for revenue and plan?"


## Slack & Teams

Zoë integrates with both Slack and Microsoft Teams. You can ask questions, and she will respond to them in either interface.


### Slack 

To set up the Slack integration, you can install it from the "Slack Integration" tab of the Workspace Settings menu. 

To make Zoë receive a message you must tag `@Zenlytic` in every message you want Zoë to see. Unfortunately, Zoë does not automatically see messages that are added to a thread without that tag.

Additionally, you can schedule dashboards for delivery in Slack, through the scheduled reports functionality in the dashboard options or the admin panel.


### Teams 

To set up the Teams integration, contact Zenlytic support, following [these instructions](https://zenlytics.notion.site/Installing-the-Zenlytic-Bot-in-Microsoft-Teams-b5eb4f7ac7eb4a45bc350bcd9931dc4b)

Zoë is available in DMs and in channels, but not in group DMs.

