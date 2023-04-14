---
title: Event Driven Architecture with Azure Logic Apps
description: How to create a simple event driven service using Azure's Logic Apps
slug: event-driven-architecture-azure-logic-apps
authors: bbayes
tags: [Cloud, Azure, Logic Apps, Serverless, Event Driven Architecture]
---

In this blog post we will explore how easy it is to create an event driven architecture using Azure's Logic Apps. We will create supporting services such including Azure Service Bus which will act as the event trigger for the Logic App to run, and Twilio, which will allow us to send an SMS message. If you want to find out more about what Logic Apps are, then keep reading, if you just want to get into the example, [feel free](#creating-a-notification-service-using-logic-apps).

<!--truncate-->

### Pre-requisites

In order to try this out, you will need:

1. An Azure AD subscription, you can sign-up for a free account [here](https://azure.microsoft.com/en-gb/free/);
2. A Twilio account, which you can sign up for free [here](https://www.twilio.com/try-twilio);
3. A basic understanding of [JSON](https://www.w3schools.com/whatis/whatis_json.asp).

## What are Logic Apps?

Before going into what we'll be doing, it's probably worth understanding what Logic Apps are: Logic Apps are a Microsoft low-code serverless technology that allow you to build workflows inside of a visual designer, and connectors enable you implement integrations with third-parties. If you have any familiarity with [AWS Step Functions](https://aws.amazon.com/step-functions/), then you'll feel at home here. Logic Apps have many triggers, including events and timers, we will cover off what we mean by an 'event' below.

### What is an Event to a Logic App?

An event in a Logic App are defined using triggers, and this is what starts the execution of a Logic App; different types of triggers can include:

1. Azure services such as a Service Bus that will we will be creating here;
2. Software-as-a-Service (SaaS) applications;
3. Custom APIs.

### What are Logic App Connectors?
 Connectors are pre-built pieces of logic that act as steps in your Logic App workflow, for example sending data to an external system; Connectors will often need configuring i.e. providing some kind of authentication for the system they are integrating with. You can read more about Connectors [here](https://learn.microsoft.com/en-us/azure/connectors/introduction).

 ## Creating a Notification Service using Logic Apps
