# Signed Embedding

Signed embedding provides a seamless and secure way to integrate Zenlytic content into your application using dynamically generated signed URLs. This method is especially suitable for scenarios where smooth experience and controlled access to analytics data are paramount. The signed URL ensures that each embedded analytics instance is secure, time-limited, and tailored to individual user permissions.

## **Use Cases**

Signed embedding is particularly useful in:

* External-facing applications where enhanced customization is crucial.
* Situations where access to analytics needs to be controlled on a per-session basis.
* Environments where analytics content needs to be securely shared to the user base of an application.

## **Implementation Guide**

{% hint style="info" %}
Signed URl Security

Protect this signed URL as you would an access token or password credentials - do not write it to disk, do not pass it to a third party, and only pass it through a secure HTTPS encrypted transport
{% endhint %}

### **Generating Signed URLs**

1. **API Request for a Signed URL**
   * Make a request to the API endpoint to obtain a signed URL.
   * Include necessary authentication credentials (client\_id and client\_secret you receive from your Zenlytic representative) and user-specific parameters in the request.
   * See details in [API Reference](signed_embedding.md#api-reference) below
2.  **Parameters for iframe**

    * Signed URL retrieved in the previous step
    * Pass the url to the iframe like in the examples below

    <pre class="language-html" data-overflow="wrap"><code class="lang-html">&#x3C;iframe src="&#x3C;MY_SIGNED_URL>" allow="microphone *; clipboard-write *" style="height:700px;width:100%;border:none;" title="Dashboard" description="Zenlytic Dashboard">&#x3C;/iframe>
    </code></pre>



    The `microphone` permission allows the Transcribe voice feature to work as expected. The `clipboard-write` permission allows the Copy to clipboard buttons under each message to work as expected. Please note, the presence of these permissions on the iframe will allow the native browser's "Ask for permission" popups to appear, they do not automatically give embedded users' consent to those actions.
3.  **To request a chat embedded url, you'd change the `target_url` to** `https://app.zenlytic.com/chat`

    <pre class="language-html" data-overflow="wrap"><code class="lang-html">&#x3C;iframe src="&#x3C;MY_SIGNED_URL>" allow="microphone *; clipboard-write *" style="height:700px;width:100%;border:none;" title="Dashboard" description="Zenlytic Dashboard">&#x3C;/iframe>
    </code></pre>


4. **Handling URL Expiry**

* Implement logic to handle the expiry of a signed URL, refreshing the url you receive from the endpoint.

## **API Reference**

### **Endpoint**

* **URL:** `https://api.zenlytic.com/api/v1/embed/signed_url`
* **Purpose:** To generate a signed URL for embedding analytics.

### **Request**

* **Method:** `POST`
* **Headers:** Include basic authentication header. You will need to base64 encode your credentials in the form `client_id:client_secret`, then pass under the `Authorization` header with the `Basic` prefix. Python code to create the header is given below:

{% code overflow="wrap" %}
```python
import base64

def create_basic_auth_header(client_id, client_secret):
    # Concatenate the client ID and client secret
    credentials = f"{client_id}:{client_secret}"
    
    # Encode the credentials using base64
    credentials_encoded = base64.b64encode(credentials.encode()).decode()
    
    # Create the Basic Auth header
    auth_header = f"Basic {credentials_encoded}"
    
    return auth_header

# Example usage
client_id = "your_client_id_here"
client_secret = "your_client_secret_here"
auth_header = create_basic_auth_header(client_id, client_secret)
print(auth_header)
```
{% endcode %}

## **Body Parameters**

### **Structure**

* `external_user_id`: (Required) The identifier of the user for whom the analytics is being embedded. This is the user's unique identifier in _your_ system.
* `target_url`: (Required) The complete url in your Zenlytic interface for the content you want to embed. For example, `https://app.zenlytic.com/dashboards/73b64533-c027-43b8-b8a8-6069534235413` or `https://app.zenlytic.com/chat`.
* `user_attributes`: (Optional) The user\_attributes to use when applying row and column level permissions for this user. If you have already requested for a given `external_user_id` then make another request with different `user_attributes` passed, the most recent user\_attributes will be used. The format of user attributes is:

{% code overflow="wrap" %}
```
{
  "department": "Marketing",
  "account_id": 1327789
}
```
{% endcode %}

* `extra_prompt_context`: (Optional) This is extra context added to Zoë to make your user's experience customized. You could say things like "Only speak to me in French" or "Always address me as Doctor." This is only visible to Zoë, not to the user.
* `chat_header_message`: (Optional) This is the welcome header that Zoë shows to the user. For example, you could have Zoë say "Welcome Paul," or send " " to not display this value.
* `chat_welcome_message`: (Optional) This is the initial message that Zoë shows to the user. For example, you could have Zoë say "How can I help you find your data today?"
* `chat_initial_prompts`: (Optional) This is an array of initial prompts to display in Zoë. This helps a user see example questions they can ask. For example, \["What were sales in 2023?", "How many customers joined in the last week?"]
* `first_name`: (Optional) The first name of the user in your system. Defaults to 'Embedded'.
* `last_name`: (Optional) The last name of the user in your system. Defaults to 'User'.
* `role_name`: (Optional) The role you want the user to assume in the application. Options are `embed` and `embedded_with_scheduling` Defaults to `embed`. See [user role details](../zenlytic-ui/user_roles.md) for more information

## **Example Body Parameters**

{% code overflow="wrap" %}
```json
{
    "external_user_id": "237645tgfghe6",
    "target_url": "https://app.zenlytic.com/chat",
    "user_attributes": {
        "account_id": 1327789
    },
    "extra_prompt_context": "Always address me in French",
    "chat_header_message": "Welcome Paul,",
    "chat_welcome_message": "How can I help you today?",
    "chat_initial_prompts": ["What are my sales in the last month?", "How many customers joined in the last week?"],
    "role_name": "embed"
}
```
{% endcode %}

### **Example Request**

{% code overflow="wrap" %}
```python
import requests

data = {
    "external_user_id": "237645tgfghe6",
    "target_url": "https://app.zenlytic.com/chat",
    "user_attributes": {
        "account_id": 1327789
    }
}
headers = {
    "Authorization": "Basic mdfiothisisanexampleqewnqjo3eiqjdfqi3oirfqqj301r0j2oqfioewiq3i=",
    "Content-Type": "application/json"
}
url = "https://api.zenlytic.com/api/v1/embed/signed_url"
requests.post(url, headers=headers, data=data)
```
{% endcode %}

### **Response**

* **Structure**
  * `signed_url`: The generated URL for embedding.
  * `expires_in`: Expiry in seconds from now.
*   **Example Response**

    \{% code overflow="wrap" %\}

    ```json
    {
        "signed_url": "https://app.zenlytic.com/embed/chat?userID=12345&userJWT=abc123",
        "expires_in": 86400
    }
    ```

    \{% endcode %\}

### **Error Handling**

* **Common Errors**
  * Authentication failures. This will occur if you do not pass the client\_id and client\_secret correctly, or if those credentials are invalidated.
  * Missing or invalid parameters.
  * Server-side errors in URL generation.

### **Customization**

To dynamically change the database chosen in the query, you can set the`zenlytic_connection_database` user attribute. See additional docs on the behavior of this attribute [here](../zenlytic-ui/user_attributes.md#zenlytic_connection_database).

To dynamically change the connection chosen in the query, you can set the `zenlytic_connection_name` user attribute. See additional docs on the behavior of this attribute [here](../zenlytic-ui/user_attributes.md#zenlytic_connection_name).

Note: You cannot set both of these properties at the same time.

## Embedded UI Settings

You can additionally set some other settings and system prompt context for Zoë in the Embedded settings page in the UI. These settings will apply to all of your tenants.

![embedded-ui-settings](../.gitbook/assets/embedded-ui-settings.png)

You can also change the name of Zoë to any name you would like using the Chat Agent Name setting.

## **Communication**

### Zenlytic Embedded iframe Events

Zenlytic provides an event system for embedded iframes to communicate with the parent application. Currently, we support one event: `questionRunFinished`. Additional events can be added upon request.

### Listening for Events

To handle events from the Zenlytic iframe, add an event listener to the window object. Here's an example of how to properly listen for and handle events:

{% code overflow="wrap" %}
```javascript
window.addEventListener('message', (message) => {
  if (message.origin !== 'https://app.zenlytic.com') {
    // Ignore messages not from Zenlytic
    return;
  }
  
  switch (message.data.type) {
    case 'questionRunFinished':
      console.log(`Question ${message.data.detail.id} finished running!`);
      // Handle the event here
      break;
    // Add cases for future events as they become available
  }
});
```
{% endcode %}

### Supported Events

`questionRunFinished`

This event is triggered when a question in the embedded iframe finishes running.

Event details include:

{% code overflow="wrap" %}
```
id: The ID of the question that finished
slices: An array of column IDs representing slices in the question
metrics: An array of column IDs representing metrics in the question
filters: An array of filters applied to the question
time_periods: The current and compare time periods for the question
row_limit: The row limit set for the question
sql: The SQL query used to generate the question result
compare_query: The SQL query used for comparison (if applicable)

```
{% endcode %}

### Security Note

Always verify that the origin of the message is `https://app.zenlytic.com` (or your custom domain, if you are an enterprise customer) before processing the event to ensure the message comes from Zenlytic.

For any questions or requests for additional events, please contact Zenlytic support.

### **Troubleshooting**

* **Invalid URL Errors:** Ensure all required parameters are correctly included in the API request.
* **Expired URL Access Attempts:** Implement automatic URL regeneration or user prompts for re-authentication.
* **Access Denied Errors:** Verify user permissions and roles to ensure they align with the access rights of the analytics content.
