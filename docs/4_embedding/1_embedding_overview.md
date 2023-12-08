---
sidebar_position: 1
---

# Embedded Analytics


Embedded analytics is the process of taking content you've created in Zenlytic, and making it available to users via an iframe in a separate application. There are two ways to embed Zenlytic content in your application.

* [Private Embedding](./2_private_embedding.md)
    * Private embedding is an iframe with the embedded url of the content you want to embed. The authentication is done by logging into Zenlytic with a username and password for a user with a Zenlytic account. 
    * Users must log into their Zenlytic account in the iframe before seeing content. 
    * This type of embedding is most useful for internal applications within a company (e.g. embedding a Zenlytic dashboard or chat interface in Notion or Confluence where you have company documentation)

* [Signed Embedding](./3_signed_embedding.md)
    * Signed embedding lets you provide a seamless authentication experience for your end customers. In this method, you use Zenlytic API credentials to hit an endpoint which gives you a signed URL for the embedded content you want to display to the user. 
    * This URL is scoped to just the permissions you request using row-based and column-based [access grants](../4_data_modeling/8_access_grants.md) that are added to the token's context when you request it. The signed URL is placed in the iframe, which is displayed in your application.
    *  This form of embedding is best for external applications (e.g. embedding a Zenlytic dashboard on usage of your SaaS platform into an admin panel for your own users and scoping user's access to content to only their data within your system).  

