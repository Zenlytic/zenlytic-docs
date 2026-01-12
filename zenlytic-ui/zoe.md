# Zoë

Zoë is an AI data analyst who uses your data to answer questions for you. This section will describe some of her capabilities, and how to get best results.

## Just ask!

To get started using Zoë, just ask her a question. If you don't know what you can ask about, simply ask what data she can see, or what would be a great question to ask next. She will be even more helpful if you share your job title and more context about what you're trying to accomplish.

<figure><img src="../.gitbook/assets/zoe-welcome.png" alt=""><figcaption><p>Starting a new chat with Zoë</p></figcaption></figure>

When you're asking for data, you can be specific (e.g. "Show me sales YTD compared to the prior YTD, broken out by product type") or general (e.g. "I don't really know what I want to see, but tell me about channel and campaign performance"). Zoë can handle both type of questions, and will ask you follow up questions if she isn't able to make reasonable assumptions about what you intend from your question.

By pressing the Microphone icon, Zoë will listen through the web browser to capture your prompt through realtime voice transcription. The Lightning icon opens a panel for selecting a Workflow to run. The Plus icon supports adding file or query attachments to the message, like images, CSVs, and PDFs (limit 5). A dropdown on the right side of the user input supports changing the LLM model that will be used for the new conversation. Press "Enter" or click the Up Arrow button to submit the message.


## Querying

Zoë searches across the governed measures and dimensions to use existing fields and know when to create new ones to answer your data questions with compelling summaries and insightful visualizations. She was built on an agentic architecture that gives her ability to plan approaches to problems, to use tools to answer questions on your behalf, and memory to get better over time: all in service of helping you understand complex data. At times she may misunderstand what you are asking about, but you can see exactly what steps she is taking to respond, the reasoning behind her thinking, and the data she queries.

<figure><img src="../.gitbook/assets/querying.png" alt="Ask Zoe for a bar chart"><figcaption><p>Asking Zoë for a bar chart</p></figcaption></figure>

The left sidebar displays the Chat history, sorted by recent activity, and a button to create a new chat. In the upper left of the main content area, there's a button to collapse the left sidebar, a button to create a new chat, and the 3-Dot options menu that supports link sharing and "Save as Workflow" options.

<figure><img src="../.gitbook/assets/chat-drawer.png" alt="Clicking into the Query drawer"><figcaption><p>Clicking into the Query drawer</p></figcaption></figure>

Every chart that Zoë creates on your behalf can be clicked into, inspected and explored via the drawer, and added back to the conversation with follow up questions or tasks. The Magnifying glass icon represents that a component will open in the drawer when clicked. The query drawer header contains the label description of the query, a toggle between data and code, and an icon to close the drawer. The drawer content itself provides a form for exploring the query options available from this starting point. You can either click the buttons in the drawer or ask Zoë to change the question's chart type, fields, filters & sorts, limits, etc.


## Dynamic Fields

In addition to creating queries on your existing measures and dimensions, Zoë can (for Develop and above roles, and when the feature is turned on) create Dynamic Fields, which are measures and dimensions that are assigned to the person who created them, instead of the global data model. Those Dynamic Fields can be "promoted" into the global data model, but _Zoë cannot promote them_. You must do that in the UI.

We, very intentionally, have not given Zoë the ability to automatically modify the global cognitive layer, to ensure your end users are always getting a consistent and governed experience.


## Interactive Tool Calls

<figure><img src="../.gitbook/assets/v2_rich_tool_calls.gif" alt="Opening the search fields accordion"><figcaption><p>Opening the search fields accordion</p></figcaption></figure>

Like chart tiles, every tool call that Zoë dispatches on your behalf while analyzing the data can be clicked into, inspected, and explored via the drawer. Click on rows of text in the chat thread with the Magnifying glass icon to see that tool call's details opened in the drawer. Some examples of tools that Zoë uses in chat:

- Search across data model fields, memories, and external sources
- Generate and run SQL queries, or compile SQL from semantic model code
- Build interactive charts and accurate text summaries from data
- Write and run Python scripts for complex data analysis tasks
- Search across workspace dashboards and create new ones


## Citations

When users understand the data, they can trust the data: any numbers or query values that Zoë references in text summaries will be cited by a serially indexed element at the end of the paragraph. By interacting with the citation, users can understand the data lineage: where and how the value was calculated.

<figure><img src="../.gitbook/assets/v2_citations.gif" alt="Interacting with citations"><figcaption><p>Interacting with citations</p></figcaption></figure>


## Switching Agent Models

Use the LLM model dropdown menu in the lower right of the Chat input to pick the right-sized large language model for your current task. You can even change the model mid-conversation, which is particularly useful when following up to Proactive Agent runs with a faster model after letting a slower, more contemplative model build the initial report.

<figure><img src="../.gitbook/assets/v2_switching_models.gif" alt="Switching agent models mid-conversation"><figcaption><p>Switching agent models mid-conversation</p></figcaption></figure>


## Streaming

Zoë leverages streaming, so that incremental updates from the LLM model are shown to the user as soon as they are available. Tool calls can take up to several minutes to finish, while streaming text is available so quickly it looks like Zoë is using your keyboard directly. Feel free to start other chats simultaneously, navigate around the app, or refresh the page while your conversation is loading: whenever you return, the most recent updates will be streamed into the chat.

The figure from the previous section shows how each message submitted by the user is pinned to the top of the screen while Zoë is responding, with automatically scrolling to follow the response as it streams onto the page. By scrolling up and away from the recent updates, the user can dismiss this automatic scroll behavior. While the conversation is running, click the "follow live updates" pill when it appears to restore the automatic scroll behavior.


## Code Interpreter

Zoë also has the ability to write and evaluate Python code. This process occurs in a sandbox environment where she can write any code she needs on top of the governed results pulled from the data model. This gives Zoë a huge amount of flexibility to answer complex questions that involve merging results of separate queries, plugging in assumptions to scenarios,  building custom visualizations, and doing advanced clustering, correlation, regression, and forecast analysis.

<figure><img src="../.gitbook/assets/code-interpreter.png" alt="Running a forecast in Python"><figcaption>Running a forecast in Python</figcaption></figure>


## Edit and Retry Messages

If Zoë has finished responding but the answer did not meet your expectations, use the Edit button under user messages to modify the prompt before running again, or the Retry button under assistant messages to re-run the response with the same prompt.

<figure><img src="../.gitbook/assets/v2_retry.gif" alt="Retry a response to re-run the last user message"><figcaption>Retry a response to re-run the last user message</figcaption></figure>

At any point while Zoë is responding, click the Pause button in the lower right of the Chat input to cause Zoë to quickly exit out of the current task and allow submission of a new user message.


## Dashboards

Zoë can create new dashboards and add plots to those dashboards or add plots to existing dashboards. She can also search your dashboards for terms so you can answer questions like "What dashboards do we have for revenue and plan?"


## Slack & Teams

Zoë integrates with both Slack and Microsoft Teams. You can ask questions, and she will respond to them in either interface.

### Slack

To set up the Slack integration, you can install it from the "Slack Integration" tab of the Workspace Settings menu.

To make Zoë receive a message you must tag `@Zenlytic` in every message you want Zoë to see. Unfortunately, Zoë does not automatically see messages that are added to a thread without that tag.

Additionally, you can schedule dashboards for delivery in Slack, through the scheduled reports functionality in the dashboard options or the admin panel.

### Teams

To set up the Teams integration, contact Zenlytic support, following [these instructions](microsoft_teams_bot.md)

Zoë is available in DMs and in channels, but not in group DMs.

