evesso
======

Single Sign On application for EVE Online

Libraries used:
http://github.com/eve-val/evelink

Spec
====


Definitions
======
EVESSO - EVE Single Sign On, the application under discussion.
Staff - Any administrator or other person responsible for the upkeep of the system. Granted access to everything.
Group Owner - Any person tasked with running or administering a group
Group Member - Any person who is part of a group
User - Any person registered on the site

Requirements
=========
User Management
----------------------
- Must allow a user to register a new account
- Must require users to supply an API key upon account creation
- Must allow users to supply multiple API keys
- Must allow users to manage their account (change their passwords, change contact email address, request new password if they forget it etc)

Group Management
-----------------------
- Staff must be able to create and delete groups
- Staff must be able to add Group Owners to groups
- Group Owners must be able to set criteria for automatic group addition via the API
- Group Owners must be able to set criteria for automatic removal from the group via the API (in cases where users are added to the group manually, such as supercapital or leadership groups)
- Group Owners must be able to add or remove users manually
- API integration must be able to add users to groups based on:
   - Their corp or alliance
   - Their standings to the corp or alliance running the instance
   - Their in-game titles (nice-to-have)

3rd Party Integration
-------------------------
- Must provide some way of authenticating communication with third party applications, via some shared secret.
- Must expose an interface to allow an external application to supply a username and password and be returned the authenticated user's details and any groups of which they are a member
- Must expose an interface to allow the retrieval of information about a specific user or group (for instance, by Cerberus)
- Must provide a plugin architechture to allow third party plugins to access the authentication information

