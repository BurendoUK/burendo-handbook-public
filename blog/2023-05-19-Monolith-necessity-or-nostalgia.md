---
title: Monoliths in the 21st Century - Necessity or Nostalgia?
description: A summary of my thoughts, from the DTX panel.
slug: monolith-necessity-or-nostalgia
authors: cavery
tags: [engineering, Cloud, AWS]
---

# Monoliths in the 21st Century
_Approximately 5 minutes reading time._

Allow me to set the scene, on Wed 17th May at the [DTX expo](https://dtxevents.io/manchester/en/page/dtx-manchester), I was a panel member discussing the place and presence of monolithic applications within systems, now and going forward.
There was a lot of interesting points raised by the other panel members and myself, regarding the huge momentum shift towards serverless micro-services and whether or not monoliths should be sentenced to /dev/null.

Allow me to cover a few of the headline points and express my opinion, in words, as to why I feel we are looking at the original question slightly incorrectly.

## What is a monolith?

Within the tech industry there are many acronyms and terms banded around with the assumption that the receiving audience knows what it means. Monolith is one such term where everyone 'kind of' knows what it means but it can look and feel slightly differently to everyone.

Previously, when everyone practiced waterfall, monolithic applications were often the result of the engineering team's efforts. Now, they aren't too much different. Monoliths often have a single codebase, where all functionality, dependencies and modules are stored. Additionally, the modules are interdependent and therefore can't be deployed independently.

So thinking back to that time, or if you are like me and were still in nappies, think back to the tales your parents told you of the software in that era.

The software of that time was revolutionary, when spreadsheet software was pioneering the way everyone did, well, everything. Each year in order to gain the newest version, you'd have to purchase that version outright,
and install it whole. This was the 'traditional' monolith - everything that was required came in one package.

Fast forward to the 21st century and the world has changed, produced some fantastic movies in the process (Fast & Furious Tokyo Drift, bby!) and morphed the definition of a monolith slightly.
We no longer build everything to be a 'desktop' application, we build for the web first (exceptions apply). Which means that our users only need a browser to be able to use our product or service.
As such, the definition of a monolith, is now a designation of the applications and services which are the sum total or a large part of a wider system, for that web product or service.

For me, I would classify a monolith as any application which has more than a single responsibility, where a responsibility is the smallest unit of a task.
What do I mean by the term 'smallest unit of a task'? Take for example an API. For each API endpoint, that does something slightly different, I would class that as a task. It is the smallest unit of value available (note: not the same as a unit test).
Monolithic API applications have, and will always exist. However, they also make for great candidates for micro-services which I'll touch on shortly.

## Every 'monolith' isn't a monolith

Now that we are working with a common understanding of the historical thought of what a monolith is. Over my years in the industry, what people class as a monolith is everything from 0 to it being a micro-service.
I disagree that everything up-to full fledged micro-service applications, are monoliths. There is a middle ground.

Think of Monolith <-> Micro-service as a linear scale of application depth and complexity. You can say that, additional names or stages are missing from that linear scale.
However naming anything on a scale would require it to have defined conditions as to when it is 'something' - not something I want to do right now.
For the sake of this blog, let's imagine that the linear scale looks like this (no definition supplied - your warranty may vary):

Monolith <-> Macro-service <-> Micro-service

## What are the differences?

Monoliths differ greatly compared to macro or microservices. Monoliths are typically deployed as a single unit, where as microservices are independently deployed and there could be hundreds of units.

When it comes to scalability, you must scale the entire monolithic application in order meet your needs, even if only a small subset of functionality is receiving high demand. As you've probably guessed, this is wasteful for resources.
Microservices in contrast are already, loosely coupled and designed to be independently scalable. Allowing for much quicker responsive scaling.

As mentioned prior, it is often the case that monolithic applications are held in a single codebase. A microservice approach would house each part of functionality in separate codebase.

## What place do they have in the 21st Century?

To define where a monolith truly belongs would not be the right thing to do. Your system, the problem you are trying to solve and the way you work are all factors in the equation and will always be (slightly) different to everyone else.
Therefore there is no hard and fast rule of 'Monoliths should only be created for X problem'.

However some problem cases lean more towards building an application in a monolithic nature than a micro-service nature.
You may want to ask yourself the following, "For the problem I am trying to solve...":

- What are the various different stages or tasks it must do?
- What are the SLAs on completion of those tasks?
- How resilient to failure should it be?
- Could any of its tasks be done in parallel?
- Are the tasks event driven in nature or simply timed / batch events?
- What is the team size, skills and knowledge?

These high-level questions are not meant to determine whether the result should be monolithic or micro-service, but they do indicate which direction to lean.
If you lean toward the micro-service side but your application doesn't fit the definition of a micro-service, it would be classified as a macro-service.
It's a step in the right direction!

## I have a monolith, what can I do?

You may already have a monolith(s) in your system. If it works perfectly fine, tests pass and it achieves the value you want it to do - that is perfectly fine! (For now)
You should not be in a hurry to move to the latest technological trends, you need to evaluate every trend for it's pros vs. cons and consider the cost and effort required in order to achieve those.

You should reflect on your monolith and ask yourself these questions:

- Are you able to maintain your application easily? (Adding new features, fixing bugs)
- Does your application scale easily?
- Are you able to quickly deliver new value to your customers?

If any of your answers is no, it might be time to consider giving the application some attention.
The journey a monolith must take to become a micro-service is difficult to define, your problem and obstacles will be different to anyone elses.

You could consider the following, when determining the journey ahead:

- Splitting the monolith into a modulated monolith
- Look to reduce the scope of what the monolith is to achieve
- Consequently, make smaller applications / services for the scope you've moved out of the monolith
- Re-build the application from the ground up in a micro-service approach

## I only use micro-services, I don't ever need a monolith

That statement may well be the case. The problem being solved can be done so purely by micro-services alone. It is still important however, to understand when and where micro-services meet their limits.

Micro-services are fantastic but do come with their cons. It is always important to continually re-evaluate your system, how it is built and whether it continues to be fit for purpose for the value trying to be achieved.
As you may have read recently, Amazon Prime Video recently re-evaluated their services and infrastructure and recognised that there was both performance and cost improvements to be made, despite using micro-services and serverless infrastructure.
You can read more about that on the [Prime Video Tech Blog](https://www.primevideotech.com/video-streaming/scaling-up-the-prime-video-audio-video-monitoring-service-and-reducing-costs-by-90).

Both a blessing and a curse as you build a distributed system, is that you build a 'spiders' web of loosely coupled, inter-connected services that resolve a task at a time. 
Often these tasks are part of chain of events, once one task has completed, the task service picks it up where it was left off and continues. Like a conveyer belt.
In order to facilitate this, infrastructure such as object storage or a database is used to safely 'facilitate' the next step, as micro-services are built ephemeral in nature.
All of this incurs network calls, storage read and writes and ultimately service capacity limitations - in the form of quotas, maximum throughput or latency.

Some of these issues may never impact your system, as the problem you are aiming to solve doesn't introduce them.

As the Prime Video team recognised, by consolidating already 'small' tasks together, they can reduce the affects highlighted above.
They may have moved away from being 'fully' micro-services, but by no means have they created a monolith like we know from history. They've moved ever so slightly left on the scale, towards a macro-service to reduce the effect of the cons. of micro-service and serverless architecture.
They have retained many pros that micro-services offered them originally, as they could remain 'serverless'.

## A Monolith can be Serverless

One common misconception is that a monolithic application can only be deployed on infrastructure classified as 'serverful'. That is, you deploy it to a traditional server and must maintain that server or fleet and are unable
to benefit from the many advantages Serverless infrastructure offers. This isn't the case.

There is no obstacle preventing a monolithic application from being containerized and hosted on a serverless container service like [AWS ECS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html).
If your application exceeds the size limit to benefit from on-demand Serverless infrastructure like [AWS Lambda](https://aws.amazon.com/lambda/), you won't be able to take advantage of the additional benefits Lambda provides.

This is where micro-services really shine, they are super small in their size as they've been built to complete a single unit or task of work. They are one of many applications, that make up a sum total of a service, system or product.

Ultimately you must consider the pros vs. cons of the infrastructure and what it can offer you, against what value you are trying to achieve.

## Monoliths are here to stay

Hopefully the points highlighted here, which were covered (some briefly) in the panel discussion on Wednesday, offer food for thought when you think about the architectural structure of both your application and infrastructure.
Additional, you should be able to form an opinion, based on my opinion that there is a linear scale between monolith <-> micro-service and we should stop thinking of them being so clean cut.

My opinion, monoliths are a necessity, or a necessary evil. Their shape may be much different from that of the early '90s applications but we've all still got work to do. They require modernisation as much as possible in the form of modularisation, separation of concerns and shrinking the overall scope and size. These efforts will move the applications more towards the centre line of the linear scale and begin to reduce the impact of the cons and even gain some pros usually enjoyed by micro-services.

I would always advocate to consider micro-services and Serverless first and foremost.
