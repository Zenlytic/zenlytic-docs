---
layout:
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# Embedding Overview

Embedded analytics is the process of taking content you've created in Zenlytic, and making it available to users via an iframe in a separate application. There are two ways to embed Zenlytic content in your application.

### Private Embedding

* This type of embedding is most useful for internal applications within a company (e.g. embedding a Zenlytic dashboard or chat interface in Notion or Confluence where you have company documentation)
* Private embedding is an iframe with the embedded url of the content you want to embed. All users must have a Zenlytic account of their own with a username and password.
* Users must log into their Zenlytic account in the iframe before seeing content. If the user is not logged in, they will see a login screen inside of the iframe.

### Signed Embedding

* This type of embedding is best for external applications (e.g. embedding a Zenlytic dashboard on usage of your SaaS platform into an admin panel for your own users and scoping user's access to content to only their data within your system).
* Signed embedding lets you provide a seamless authentication experience for your end customers. In this method, you use Zenlytic API credentials to hit an endpoint, which returns a signed URL for the embedded content you've selected to display to the user.
* You can apply permissions for the signed url using row-based and column-based [access grants](../data-modeling/access_grants.md) that are added to the signed url when you request it. The signed URL is placed in the iframe, which is displayed in your application.
