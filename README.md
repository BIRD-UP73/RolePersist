# RolePersist
A very minimal Discord bot that makes use of persistent roles.
No databases or logging needed.

## What are persistent roles?
If a user leaves your discord server their roles are removed.
Currently Discord provides no way of adding these roles when a member rejoins your server.
This bot makes sure these roles are actually added.

## How does this work?
When a user joins your server, the bot checks for all roles that were added to that user and never removed.
These roles will be added to the user.

## How do I know the bot is working?
Check the audit log to see which roles were persisted.

## Will the bot work for all roles in my server?
No, it will only work for roles that are below the bot's top role.
The bot is not allowed to work with those roles.
So the higher you set the bot in your server, the more roles it will work on.
