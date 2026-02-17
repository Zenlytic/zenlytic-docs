# Attachments

Zoë supports attachments to provide additional context for your questions. You can attach files like CSVs, images, and PDFs, or attach queries from your data model to help Zoë understand your needs and provide more relevant answers.

## Attachments Dropdown

Click the Plus icon in the chat input to open the attachments dropdown menu. This menu provides two options for adding context to your message:

- **Upload a file**: Attach CSVs, images, PDFs, and other file types (limit 5 files per message, 25mb each)
- **Run a query**: Attach results from raw SQL or an existing query in your data model

<figure><img src="../assets/3_zenlytic_ui/attachments-dropdown.png" alt=""><figcaption><p>Opening the attachments dropdown menu</p></figcaption></figure>

## File Attachments

Upload files directly to your conversation to give Zoë additional data and context. This is particularly useful when you have external data sources, spreadsheets, or documents that complement your data warehouse.

### CSV Example

Attach a CSV file to have Zoë analyze the data, create visualizations, and provide insights. Simply select your file from the upload dialog, and Zoë will process it as part of your conversation.

<figure><img src="../assets/3_zenlytic_ui/attachments-csv.png" alt=""><figcaption><p>Attaching a CSV file to the conversation</p></figcaption></figure>

Once attached, Zoë can read the file contents, understand the data structure, and perform analysis. Ask Zoë to build charts, calculate metrics, or identify trends in the uploaded data.

<figure><img src="../assets/3_zenlytic_ui/attachments-csv-response.png" alt=""><figcaption><p>Zoë analyzing CSV data with charts and insights</p></figcaption></figure>

## Query Attachments

Attach results from existing queries in your data model to provide Zoë with specific context about the data you want to discuss. This is useful when you want to reference a particular dataset or build on top of previous analysis, without making Zoë start from scratch. In Exploratory mode, instead of picking metrics and slices, the application supports writing or uploading raw SQL directly.

Select "Run a query" from the attachments dropdown to search for and attach metrics and slices to build a query from your workspace. Zoë will use the query results as context for understanding your question.

<figure><img src="../assets/3_zenlytic_ui/attachments-query.png" alt=""><figcaption><p>Attaching a query to the conversation</p></figcaption></figure>

### Query Attachments with Charts

After attaching a query, Zoë can analyze the results and create visualizations that highlight key insights. She can build on top of the existing data model, compare metrics, or identify patterns in the query results.

<figure><img src="../assets/3_zenlytic_ui/attachments-query-response.png" alt=""><figcaption><p>Zoë building charts from attached query data</p></figcaption></figure>

### Query Attachments with Citations

When Zoë references specific values from attached queries in her text summaries, she provides citations that link back to the source data. Click on any citation to see exactly where and how the value was calculated, ensuring transparency and trust in the analysis.

<figure><img src="../assets/3_zenlytic_ui/attachments-query-citations.png" alt=""><figcaption><p>Citations linking text summaries to query data sources</p></figcaption></figure>
