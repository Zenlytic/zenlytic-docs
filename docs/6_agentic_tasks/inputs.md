---
sidebar_position: 2
---

# Requiring User Inputs

Inputs are used to collect information from the user before the Task begins. Consider the following example, where Zoe is taking a look at products in a week over week analysis. With inputs, it's possible to make this Task run differently depending on the user's input.

![pre-input-task](../assets/agentic-tasks/pre-input-task.png)

Let's click the "Inputs" tab within the left panel and create a new input named "period". Input names must be unique, not empty, and a single word without whitespace. Inputs are like variables that will be replaced with the information the user provides when the Task is run. The types of inputs currently supported are `text`, `select`, and `file attachment`. In the following image, I've added a text input with a description entry that helps the Task runner understand what kind of value they should provide.

![inputs-tab](../assets/agentic-tasks/inputs-tab.png)

Now that our Input has been created, we have to modify the Task messages to use the Input instead of the existing hard-coded value. In the message editor, access `text` and `select` inputs with the "braces" syntax: `{{ input_name }}` . Inputs can automatically be created or inserted from a valid text selection.  An autocomplete menu will also appear after typing `{{` when there are available inputs. In the Task preview on the right, a dashed variable chip will represent the input value that will be provided by the Task runner.

![input-used](../assets/agentic-tasks/input-used.png)

In the following image, I've created another input and added it to the first Task message. The file attachment input is shown in the bottom right of the card and can be changed or removed by clicking the chip. In the Task preview on the right, a dashed region above the user message represents the input file that will be uploaded by the Task runner. 

![all-inputs-used](../assets/agentic-tasks/all-inputs-used.png)

Now, when the Task is run, the user will first be presented with a modal to provide input values. Once the values are provided, and "Run" button is pressed, the conversation preview will show the "filled in" values of the inputs. 

![input-values-modal](../assets/agentic-tasks/input-values-modal.png)

That's it! Inputs are an important tool in crafting Task workflows for your organization that are highly flexible and can incorporate data from outside the data model such as CSVs. 