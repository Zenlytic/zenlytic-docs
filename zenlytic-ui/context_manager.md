# Context Manager

Use Context Manager to manage your semantic model files, review changes, and deploy updates to production.

![Context Manager overview](../assets/5_data_modeling/context-manager-overview.png)

## Open Context Manager

Open Context Manager from the workspace navigation or from chat.

![Open Context Manager entry points](../assets/5_data_modeling/context-manager-entry-points.png)

## Understand the tabs

Use the tabs to control model context and query-based learning:

- **Context:** Create and edit model files, view files, folders, and branches
- **Query history:** Let Zenlytic learn from prior queries to improve query accuracy and speed

![Context Manager tabs](../assets/5_data_modeling/context-manager-tabs.png)

## Manage files in the Context tab

Use the file tree to organize and maintain your data model:

- Create files and folders
- Rename files and folders
- Open view and model files in the editor
- Access file actions from the three-dot menu

From the three-dot menu, you can also:

- Show documentation for view and model files
- Open database preview for view files

![Context tab file tree](../assets/5_data_modeling/context-manager-file-tree.png)
![Three-dot menu actions](../assets/5_data_modeling/context-manager-file-menu.png)

## Add new model assets

Use the **Add** button to create new assets:

- **Add view**
- **Add model file**

When you add a view, choose one of these methods:

- Upload a CSV file
- Add from a database connection

Use an existing connection or create a new connection during setup.

![Add button options](../assets/5_data_modeling/context-manager-add-options.png)
![Add view modal](../assets/5_data_modeling/context-manager-add-view.png)

## Edit, validate, and review changes

Edit files directly in the text editor. Use the validation panel to review errors and warnings, then fix issues before deployment.

Open diff view to compare branch changes against production before you deploy.

![Editor with validation panel](../assets/5_data_modeling/context-manager-editor-validation.png)
![Diff view](../assets/5_data_modeling/context-manager-diff-view.png)

## Work with branches safely

Use the branch selector next to the Context Manager title to work on non-production branches.

Enable the workspace setting that blocks direct editing on the production branch when you want to enforce a branch-based workflow.

![Branch selector](../assets/5_data_modeling/context-manager-branch-selector.png)
![Disable production edits setting](../assets/5_data_modeling/context-manager-disable-production-edits.png)

## Deploy to production

After you commit changes on a development branch, use the action button to deploy to production.

Context Manager saves changes as you type, but you must resolve validation errors before deployment.

![Deploy action](../assets/5_data_modeling/context-manager-deploy.png)

