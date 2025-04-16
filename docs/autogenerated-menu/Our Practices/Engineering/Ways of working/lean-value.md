---
title: Lean Value
sidebar_position: 2
---
# Lean Value

In this article we show the concept of `value-add` within Lean Manufacturing and how it helps us to classify and prioritise our development roadmap by introducing the concept of classifying each of our day-to-day activities into the following definitions:

*   Value Add
    
*   Non-Value Add
    
*   Waste
    

## Classifications

In the very simplest of terms it's about understanding what the customer WANTS & NEEDS.

![Classifying Activities](/img/Our%20Practices/lean-value.png)

### Value Add

Value-Add activities can be defined as those that a **customer is willing to pay for**.

If we were to look at a standard e-commerce site then we could identify the following as some of the value-add.

1.  Content Management System
    
2.  Product Search Page
    
3.  Product Details Page
    
4.  Checkout Process
    
5.  Package Tracker
    
6.  Chatbot
    
7.  1-click purchasing
    
8.  Sales dashboard
    
9.  Branding
    
10.  Stuff
    

It's quite easy to see how each of the examples above is something that a client would be interested in. They all demonstrate clear value to the customer.

### Non-Value Add

Non-Value add activities can be defined as those that a **customer is NOT willing to pay for**.

If we were to look at a standard e-commerce site then we could identify the following as some of the non-value add.

1.  User Registration
    
2.  Login Page
    
3.  Forgotten Password
    
4.  Cookie Popup
    
5.  Database Creation Script
    
6.  WAF/CDN
    
7.  Training
    
8.  Project Management ( Sorry PMO! :D )
    
9.  Sprint Planning
    
10.  Code Reviews
    
11.  Accessibility
    

Now we've moved into different territory. All of the activities above will be necessary for the project to be completed successfully, but these are not the things the customer have come to us to do. No customer has ever asked for a Forgotten Password or for code to be Peer Reviewed, but we all know that both would be necessary. There may also be activities that they have willingly accepted (such as Accessibility or PMO updates) but again, these do not meet the core activities of the site, which is about selling.

### Waste

Waste are actually Non-Value Add activities, but are actively detremental to the project.

If we were to look at a standard e-commercy site then we could identify the following as some waste.

1.  Communication Delays
    
2.  Tickets sitting idle in queues
    
3.  Moving goalposts
    
4.  Bugs
    
5.  Design Flaws
    
6.  Technical Debt
    
7.  Acting with a Lack of Knowledge
    
8.  Working on the wrong priorities
    

It should be easy to see how each of the issues are waste.

## What do we do?

Given that we understand that what these classifications exist, how should we handle them?

### Value-Add

This is where we should be spending our time and effort, as it is justified by the customer's willingness to pay for us. If we spend the majority of our time doing Value-Add then the end result should be a delighted customer.

### Non-Value Add

We can cascade through the following stages and exit at the earliest one.

1.  Is this (or has it become) Waste?
    
2.  Can we minimise doing this? (e.g. Buy don't Build)
    
3.  Is there a "Standard and Repeatable" pattern/process to follow?
    
4.  Should we create a Standard and Repeatable pattern/process?
    

If we've passed through all those steps then this is an ad-hoc piece of value-add work, which should be completed in a timely fashion. Note that failure to address it in a timely fashion will introduce Waste, such as Technical Debt and longer Backlog Grooming sessions.

### Waste

Simple. Identify and eliminate them.

In practice this could be harder to achieve. A customer who keeps changing their mind or doesn't respond to emails quickly will need effective management. Bugs may be recurring because of faulty software or a failure to learn lessons from the past.

Therefore we need to be constantly on the lookout for Waste, and address it as it occurs. We should also be challenging all Non-Value Add activities to understand when they will become Waste. (Do we still need this meeting? Are we spending too much effort on Peer Reviews?)

## Summary

Look at each activity we undertake and the software it produces and learn to classify them as Value-Add, Non-Value-Add and Waste, as it helps us understand and address them.