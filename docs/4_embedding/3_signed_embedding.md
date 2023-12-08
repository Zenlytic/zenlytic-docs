---
sidebar_position: 3
---

# Signed Embedding


Signed embedding provides a seamless and secure way to integrate Zenlytic content into your application using dynamically generated signed URLs. This method is especially suitable for scenarios where smooth experience and controlled access to analytics data are paramount. The signed URL ensures that each embedded analytics instance is secure, time-limited, and tailored to individual user permissions.

### **Use Cases**

Signed embedding is particularly useful in:

- External-facing applications where enhanced customization is crucial.
- Situations where access to analytics needs to be controlled on a per-session basis.
- Environments where analytics content needs to be securely shared to the user base of an application.

### **Implementation Guide**

:::tip Signed URl Security

Protect this signed URL as you would an access token or password credentials - do not write it to disk, do not pass it to a third party, and only pass it through a secure HTTPS encrypted transport

:::

**Generating Signed URLs**

1. **API Request for a Signed URL**
   - Make a request to the API endpoint to obtain a signed URL. 
   - Include necessary authentication credentials (client_id and client_secret you receive from your Zenlytic representative) and user-specific parameters in the request.
   - See details in [API Reference](./3_signed_embedding.md#api-reference) below

2. **Parameters for iframe**
   - Signed URL retrieved in the previous step
   - Pass the url to the iframe like in the examples below

   Pass the url to the iframe:
   ```
   <iframe src="<MY_SIGNED_URL>" style="height:700px;width:100%;border:none;" title="Dashboard" description="Zenlytic Dashboard"></iframe>
   ```

   Likewise for a chat session in iframe. To request a chat embedded url, you'd just pass `target_url`: `https://app.zenlytic.com/chat`
   ```
   <iframe src="<MY_SIGNED_URL>" style="height:700px;width:100%;border:none;" title="Dashboard" description="Zenlytic Dashboard"></iframe>
   ```

3. **Handling URL Expiry**
   - Implement logic to handle the expiry of a signed URL, refreshing the url you receive from the endpoint.

### **API Reference**

**Endpoint**
- **URL:** `https://api.zenlytic.com/api/v1/embed/signed_url`
- **Purpose:** To generate a signed URL for embedding analytics.

**Request**
- **Method:** `POST`
- **Headers:** Include basic authentication header. You will need to base64 encode your credentials in the form `client_id:client_secret`, then pass under the `Authorization` header with the `Basic ` prefix. Python code to create the header is given below:

```
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


**Body Parameters:**
- **Structure**
  - `external_user_id`: (Required) The identifier of the user for whom the analytics is being embedded. This is the user's unique identifier in *your* system.
  - `target_url`: (Required) The complete url in your Zenlytic interface for the content you want to embed. For example, `https://app.zenlytic.com/dashboards/73b64533-c027-43b8-b8a8-6069534235413` or `https://app.zenlytic.com/chat`.
  - `user_attributes`: (Optional) The user_attributes to use when applying row and column level permissions for this user. If you have already requested for a given `external_user_id` then make another request with different `user_attributes` passed, the most recent user_attributes will be used. The format of user attributes is:
  ```
  {
    "department": "Marketing",
    "account_id": 1327789
  }
  ```
  - `first_name`: (Optional) The first name of the user in your system. Defaults to 'Embedded'.
  - `last_name`: (Optional) The last name of the user in your system. Defaults to 'User'.

- **Example Body Parameters**
```json
{
    "external_user_id": "237645tgfghe6",
    "target_url": "https://app.zenlytic.com/chat",
    "user_attributes": {
        "account_id": 1327789
    }
}
```

- **Example Request**
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

**Response**
- **Structure:**
  - `signed_url`: The generated URL for embedding.
  - `expires_in`: Expiry in seconds from now.

- **Example Response:**
  ```json
  {
      "signed_url": "https://app.zenlytic.com/embed/chat?userID=12345&userJWT=abc123",
      "expires_in": 86400
  }
  ```

**Error Handling**
- **Common Errors:**
  - Authentication failures. This will occur if you do not pass the client_id and client_secret correctly, or if those credentials are invalidated.
  - Missing or invalid parameters.
  - Server-side errors in URL generation.


### **Troubleshooting**

- **Invalid URL Errors:** Ensure all required parameters are correctly included in the API request.
- **Expired URL Access Attempts:** Implement automatic URL regeneration or user prompts for re-authentication.
- **Access Denied Errors:** Verify user permissions and roles to ensure they align with the access rights of the analytics content.

