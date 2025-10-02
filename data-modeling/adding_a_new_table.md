# Adding a New Table

## 1. Go to the data model editor

Using the left-hand navigation, go to the data model editor.

![add-new-table-data-model-editor](../assets/5_data_modeling/add-new-table-data-model-editor.png)

## 2. Click the "Add new table" button 

Tables can be added by clicking the **"Add new table"** button in the Data Model Editor.

Clicking the button will bring up the Add New Table modal. 

![add-new-table-modal](../assets/5_data_modeling/add-new-table-modal.png)

## 3. Add a table from data warehouse or upload a CSV

The default tab is "Data Warehouse", which lets you select tables from existing database connections.

Alternatively, file upload is supported for CSVs. Only one table can be selected at a time, and only CSVs can be uploaded. CSV headers
must only use alphanumeric characters, spaces, and underscores.

![add-new-table-file-upload](../assets/5_data_modeling/add-new-table-file-upload.png)

## 4. Configure table metadata

After selecting a table or CSV to upload, table metadata like name, column data types, default date, and primary key can be configured.

![add-new-table-preview](../assets/5_data_modeling/add-new-table-preview-data.png)

## 5. Associate table with topic

If the table doesn't join to any existing topics in the data model, add it to a new topic.

![add-new-table-add-joins](../assets/5_data_modeling/add-new-table-new-topic.png)

If the table does join to an existing topic, add it to an existing topic. Additional joins can also be set up later.

![add-new-table-add-joins](../assets/5_data_modeling/add-new-table-existing-topic.png)

## 6. Add table

After associating the table with a topic, the table is added to the data model.

![add-new-table-success](../assets/5_data_modeling/add-new-table-success.png)