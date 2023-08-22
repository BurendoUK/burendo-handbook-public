---
title: The Engineers Playbook - Handling Incidents
description: 
slug: handling-incidents
authors: cavery
tags: [sre, engineering, incident, management]
image: images/2023-08-20-Engineers-playbook-handling-incidents/post-header.png
---

Depending on your working environment, you may experience incidents differently from someone else. Every organisation has their way of dealing with incidents, how they triage them and what paperwork is required (hopefully not literally).

Despite the differences, there's one thing in common, it's usually the responsibility of engineers & DevOps to get back to business as usual as quickly as possible.

<!--truncate-->

In my time as a Consultant Engineer, I've experienced various ways in which teams are built, route-to-lives operate and how incidents are found, reported and dealt with. In all of these various teams, I've had to deal with incidents, ie. something has unfortunately gone offline or users have suffered a degradation of the service they expect.

Incidents happen - Don't think for a moment that 'firefighting' doesn't happen in the likes of Google and Amazon. Heck, Amazon created the Well-Architected Framework after a disaster!

I want to offer up my thought process for dealing with incidents, from the perspective of the engineers and DevOps. As much as I'd not wish for an incident to happen to you, I know at some point it unfortunately will.

I believe this playbook will bring order to the chaos. Don't take it gospelly if you don't wish to, build upon it so it suits your needs, but whatever you do, don't create an unwieldy monster. Keep it sharp, consistent and useful.

## Elect an owner

As often in the chaos, various people are 'pulled in' to offer their expertise and insight. They could be members from within your team or wider depending on the incident.

Ultimately it doesn't matter who is there from the beginning, but in my experience the moment an incident is raised, it should be owned. Some incident management software requires owners to be specified, for the sake of the paperwork, this owner doesn't need to be an engineer.

When I'm saying an owner, I'm meaning the engineer leading the charge to handle the incident. Electing an owner doesn't have to be the individual with the most context in any particular area, but someone able to adapt their calendar and other obligations to resolve the most pressing matter.

> Too many cooks spoil the broth

I love the quote 'Too many cooks spoil the broth', it sums up nicely that everyone is operating on an agenda of their own based on their experiences and knowledge, but ultimately that could be to the detriment of the goal. Gordon Ramsey elects a head chef to make the calls and final decisions for a reason.

Electing an owner isn't about giving someone an ego boost, it's about having a spearhead individual who can be at the receiving end of the hypothetical funnel of all of the context surrounding the incident.

## Gather the facts

As the owner, you need to gather the facts relating to the incident, paint a picture of the system in your mind and understand the effects that have happened. With this knowledge, you'll be primed to assess the impact and mitigate the problem.

A take on the typical who, what, where and when won't leave much to be desired when approaching the fact collection methodically.

* What has or hasn't happened that shouldn't or should have? - Journey through the system
    
* What can you prove quickly? Using metrics, statuses and logs.
    
* What are the SLAs?
    
* What is the risk? To the business, to regulatory requirements or to security.
    
* When could the action happen again?
    
* When did it start? What was the condition of the system before this?
    
* Who is affected?
    
* ...
    

## Assess the impact

An issue may arise anywhere in a system, an incident could be raised for an effect caused as a byproduct. With the facts at hand, you are probably already narrowing your scope of investigation - but hold fire. If you narrow your view too much, you may lose sight of the root cause.

You must understand the system's chain of events and all available 'check points' - places where you can validate conditions and expected behaviour; to best equip yourself to identify the root cause.

In a micro-service architecture, one such checkpoint could be your service logs between every micro-service or a queue with messages waiting to process etc.

Here is an example to illustrate what I mean a little better.

<details data-node-type="hn-details-summary"><summary>Example</summary><div data-type="detailsContent"><strong>System</strong>: An image hosting website. <strong>Action</strong>: A user has uploaded an image in the correct format. <strong>Effect</strong>: A scheduled job which compresses new images to save storage space has encountered an error as it is unable the file as it is not an image.</div></details>

In the example, we can see that a bug in an 'upstream' service was the cause but the effect has been felt in a downstream process.

Let's use the example and assess the incident with a narrow scope:

* What journey was affected? The image compression journey.
    
* How many users were affected? Just the one, confirmed by monitoring and logs.
    
* How was the business affected and any known risks? Low risk as there is negligible cost implications.
    
* What SLA was affected? No SLA is expected in this process.
    

Given the example provided you may be assuming the scheduled compression job is to blame.

What if I told you that the file was originally an image but in transfer during upload bytes of data were lost resulting in file corruption? You can begin to understand why a narrow scope shouldn't be your immediate reaction and the effect is not always the cause.

Retracing the steps of the system to the point of issue is a much better approach, checking all information available to you to check the status of the system is operating as it 'should'.

Using the example, if we were to retrace the steps, we may not have concluded *yet* what the cause of the issue was, but using the 'check points' available to you, you will have an idea whether the system operated as intended or didn't and up to what part of the journey.

Issues come from a wide range of causes, so unfortunately there isn't a concise enough decision tree to find the cause for you.  
However, you can ask the following questions at every step you retrace to further shrink the scope.

With the facts you've gathered earlier, ask yourself the following:

* What journey is affected? Preliminary scope setting - Don't get too fixated though.
    
* What high-level 'state' was the system in before and after the issues started? ie. Available vs. Offline
    
* What metrics are abnormal? What (if any) alerts were fired? ie. Error rate increased.
    
* Under what conditions would lead to the high-level state change and metrics becoming abnormal?
    

As the owner, you might want to lean on other teams with context to areas outside of your knowledge or understanding, to best grasp the answers to such questions.

Communication is key and even better when done often!

### Also, have you checked

* A recent release - Check your CI / CD, release calendar etc.
    
* Configuration properties - Check recent commits for config in code changes. Does your environment config match?
    
* Connectivity - DNS, Network routing, ACLs
    
* Availability - A system was unavailable at the time, and dependent services had no failure tolerance
    

Once you've identified the issue, even at a high level, you can begin to mitigate it.

## Mitigate the problem

There, unfortunately, isn't a magic wand here, your system is unique to you (and your company) and therefore only you (and them together) will be able to fully comprehend the problem to resolve it.

However, in my experience of dealing with incidents, these guidelines have worked well in the past to keep everyone informed, work the problem and resolve the issue swiftly.

* Who do you need to notify (stakeholders, users)?
    
* Is the problem getting worse? ie. Continually happening or one-off.
    
    * Can you stop the system temporarily to reduce the impact? 'Stop the bleed'
        
    * Can you disable a subset of functionality so that the whole system isn't compromised?
        
* Is a fix required to resume normal service behaviour?
    
    * **Suggestion**: Fix forward if it can be repaired in hours, and roll back if in days.
        
* Can a privileged user manually correct behaviour? (Breakcase scenario)
    

If you've correctly assessed the situation and can begin processing the requirements to resolve the issue, you'll be out of the woods in no time.

## Retrospective view

> Escape the forest so that you can see the wood from the trees.

Once you've gotten past the issue, and mitigations have been completed to return the system to working order and correct any missteps, it is important to realise it isn't over. Luckily the chaos and pressure are behind you.

Just as retrospectives hold value at the end of agile sprints, I believe they hold value when looking back at incidents. They offer a no-blame, honest and open forum to highlight the multiple areas of improvement to the system, testing and release structure.

Anybody can organise a retrospective for incidents - but I believe it is best for the elected owner mentioned prior, to be available and in attendance. That valuable full-picture context will pay its dues here. Schedule this as soon as reasonably possible.

* Monitoring and alerting - Was it comprehensive enough for this incident? What about other teams?
    
* Testing - Are there any missing scenarios (automated) that could have identified this?
    
* Release process - Could it be better controlled or simplified? Could you implement A/B releases & testing?
    
* Application fault tolerance - Retries, DLQ.
    
* Architecture or application self-healing - Could your system automatically recover?
    
* Synchronous vs. Asynchronous - Is something synchronous that doesn't need to be?
    

Whatever you identify, you should categorise with a strong bias towards the highest priority. By that, I mean prioritising long-term improvements higher than future feature work. If your system can fail, for any known situation, you risk monetary, reputation and time losses.

### Fail with grace

> Everything fails all the time - Werner Vogels

The philosophy of 'graceful degradation', which I aptly rephrase to 'fail with grace', is to build architecturally sound applications with redundancy and graceful degradation of service that minimises the likelihood of complete system failure.

In essence, maintaining the minimum functionality that can be supported in a system in the event of a failure while also ensuring recovery from such is cumbersome.

Even in your existing system, you can begin building applications and architecture to fail with grace today - it doesn't have to have been a decision at the inception of the system.

## TL;DR From incident inception to resolution

* **Elect an owner quickly** - Too many cooks spoil the broth. Someone with a technical understanding to orchestrate the actions and remediations.
    
* **Gather the facts, methodically** - What hasn't happened that should? What can we prove quickly (metrics or errors)? What are the SLAs?
    
* **Assess the impact** - Which journeys on the system are affected? How many users? What is the risk? What teams need engaging for a 'context champion'?
    
* **Mitigate the problem** - Who do you need to escalate or notify (users)? How can you stop the 'bleed' right now? Is a fix required to get back to normal service behaviour?
    
* **Retro & build for 'fail with grace'** - Your highest priority should be re-assessing the problem, how could you improve resiliency? Build systems to 'fail with grace'.
    

## Read further

[10 Lessons from 10 Years of Amazon Web Services](https://www.allthingsdistributed.com/2016/03/10-lessons-from-10-years-of-aws.html) - Werner Vogels

[Google SRE - Incident Response](https://sre.google/workbook/incident-response/)

[Principles of Chaos Engineering](https://principlesofchaos.org/)
