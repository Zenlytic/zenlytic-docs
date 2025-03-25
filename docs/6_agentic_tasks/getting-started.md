---
sidebar_position: 1
---

# Getting Started

Tasks allow us to build and run entire conversations with Zoe, and then enable others in the organization to re-run those conversations easily. With this feature, Zoe is more programmable and reusable for solving workflow-specific Tasks than ever before.

Tasks can be used to automate repetitive data processes, iterate on better Zoe prompts, and much more. Some examples include:  

- Building narrative-based weekly business reviews that can be re-run periodically
- Automating a tedious manual process of reconciling CSVs against database data
- Demonstrating chains of thought and other Zoe prompting techniques to new users
- Saving exceptional conversational outputs from Zoe so that the reasoning steps can be reproduced and refined
- Getting lists of products or customers and then having Zoe produce personalized long form promotional content for each one

## Navigating to Tasks

1. To view your tasks and create new ones, from the left-hand navigational sidebar, click on ⚡Tasks

![navigate-to-tasks](../assets/agentic-tasks/navigate-to-tasks-one.png)

2. To run Tasks from chat, click the ⚡ *Lightning* icon button in the chat input:

![run-tasks-from-chat](../assets/agentic-tasks/run-tasks-from-chat.png)

## Running Tasks

After clicking on the ⚡ *Lightning* icon button, the following modal will appear. Search tasks by name, creator, and creation date. Click a Task name and press “Submit” to run it. If a Task requires user input before it can run, click the "Next" button to provide the required input values first. More on inputs in the [Requiring User Inputs](/docs/agentic_tasks/inputs) section.

![tasks-modal](../assets/agentic-tasks/tasks-modal.png)

While the Task runs, the chat input for the Task's conversation will display "Task in progress…” Feel free to navigate away from the Task's conversation to other chats or browser tabs while the Task is running. Tasks were designed with workflows that take a long time to complete in mind; the Task's conversation will update with responses whenever they are available.

![running-task](../assets/agentic-tasks/running-task.png)

## Continuing the Task Conversation

That’s it! After the Task is completed, the chat input will become available again and we can send follow up messages to continue our analysis with Zoe from wherever the Task completed.

![task-followup](../assets/agentic-tasks/task-followup.png)

## Viewing Tasks

By navigating to https://app.zenlytic.com/tasks or clicking the *Tasks* option in the left-hand navigational sidebar, you will see a list of Tasks that have been created in your workspace. The three-dot menu reveals options to run, duplicate, or delete a Task. When you click on a Task name or highlighted row, you will be navigated to the Task Builder.

![tasks](../assets/agentic-tasks/tasks.png)

## Creating Tasks

In the upper right-hand side of the screen, you can create new Tasks by pressing *New Task*. This button will then navigate you to your new Task in the Task Builder.

![create-task](../assets/agentic-tasks/create-task.png)

## Editing Tasks

By default, the newly created Task will be titled “New Task" and contain no messages. We can click the Task title and type to change the title. The new name will be saved with an outside click or "Enter" keypress. 

Tasks allow us to define an entire "script" of messages that will be added to a conversation and run in sequence. Let’s click on  the *Add Message* button in the *Step Builder* tab to get started.

![new-task](../assets/agentic-tasks/new-task.png)

After adding the first message to the Task, check the preview on the right to see how that message will be added to the conversation when run. Because we haven't added any message content yet, the Task preview is showing placeholder text.

![new-message](../assets/agentic-tasks/new-message.png)

Click the textarea labeled “Write a message…” to edit the first message in the Task. Type the new prompt, then click outside the textarea or hit *Enter on your keyboard* to save the changes. Once saved, the text content of the message in the *Step Builder* tab on the left-hand side should correspond with the text content of the first user message in the Task conversation preview on the right-hand side.

Click on the *Play* button in the upper right-hand section to preview a Run of our single-message Task.

![first-message](../assets/agentic-tasks/first-message.png)

When running, the Task messages will temporarily be unavailable to edit. The Task run can be cancelled at any time by pressing the *Pause* button in the upper right-hand section. The current Task message being run will be distinguished by a pulsing black outline. The respective message in the Task conversation preview will read “Zoe is generating a response…” until it is available.

![message-running](../assets/agentic-tasks/message-running.png)

When the Task conversation preview has completed its run, we can inspect its output, run it again, or we can modify the Task before running again. The *Trash* icon button will remove the message from the Task. The *Upload* icon button will allow you to attach files to the Task message. 

![message-done](../assets/agentic-tasks/message-done.png)

## Building more advanced Tasks

In the following example,  three additional messages have been added to the Task we previously ran, and this is represented by the Task conversation preview on the right-hand side by three placeholder responses following each message that hasn't been run yet. 

![complex-task-partial](../assets/agentic-tasks/complex-task-partial.png)

When  the Play button is clicked in the upper right header, the Task starts running from the beginning, and responses are generated for the newly added messages. The image below shows the updated, completed Task.

![complex-task-completed](../assets/agentic-tasks/complex-task-completed.png)

## Run from Here

When writing new Tasks, you may find yourself making small changes to messages and often re-running the conversation preview. In the previous section, the last Task message prompted Zoe to generate a "concise executive summary". If we wanted to run the Task again, but this time generating a "comprehensive final report", We can modify the text of the message we want to change, and then use the *Run from Here* button to run the Task from that point. The most recent run of the conversation preview will be re-used for all messages from before the new starting point.

When making changes to the Task messages, you may find yourself using a combination of running from the start and running from a point as you hone into the perfect message prompts.

![run-from-here](../assets/agentic-tasks/run-from-here.png)

## File Attachments

Files can be added to Task messages by pressing the *File Upload* icon button in the message card. When the Task has `file attachment` type Inputs available, the Upload icon button will appear as a Plus icon and open a detail menu including the option to attach an uploaded file or require one from the user. Once a file attachment or input is selected, the conversation preview on the right side will add the attachment above the text content. The Upload/Plus icon button within the message card will change to a Chip and indicate that a File is attached or an Input is required.

![file-message](../assets/agentic-tasks/file-message.png)

## Create Task from an existing Conversation

From an existing chat, we can click the “Save as Workflow” button in the three-dot dropdown menu to create a new workflow from the outline of an existing chat. It will be saved in the Workflows tab, and you can navigate to it in the future by hovering over the left-hand navigation side bar and clicking on 'Workflows'. You can also run the new workflow immediately by clicking the Lightning icon button in the Chat inputbox and selecting the latest workflow.

![save-as-task](../assets/agentic-tasks/save-as-task.png)

