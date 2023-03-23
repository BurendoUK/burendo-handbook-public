---
sidebar_position: 5
---

# Continuous Integration 

## Means...

* Committing to a shared main branch at least daily
* Each such commit causes an automated build and tests
* When the build fails, it’s usually back to green within ten minute

## Because...

* Integration is primarily about communication
* Integration allows developers to tell other developers about the changes they have made
* Frequent communication allows people to know quickly as changes develop

## How...

* Build should be done automatically on an integration machine. This avoids issues with environmental differences on developers machines
* It’s not a bad thing for the mainline build to break, however, it’s vital it’s fixed fast as everyone else is blocked until it’s returned to a stable state. Gated check-ins can be a useful aid to this

