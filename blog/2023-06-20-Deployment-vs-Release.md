---
title: Understanding Deployment and Release
description: An analysis of methods that will help improve your deployments and releases.
slug: understanding-deployment-and-release
authors: cscottthomas
tags: [deployment, release, feature-flags, engineering]
---

# Understanding Deployment and Release

Two terms you'll no doubt have come across frequently are "deployment" and "release". While they are sometimes used interchangeably, they are _not_ the same. In this blog, I will attempt to explain the definitions, differences, and interactions of these two often confused terms and how they each form a crucial part of the [SDLC](/Our%20Practices/Engineering/Procedures/sdlc). Then look how anyone can take steps towards Continuous Deployment, and explore Feature Flags as a method to enable this.

![He's not a Deployment, I am!](/img/blogs/2023-06-20-Deployment-vs-Release/not-fred.gif)
<!--truncate-->
Deployment, an operational activity, involves installing and manipulating the configuration of an environment. Ideally this is an internal activity with frequent occurrence. Release, however, is a strategic process concerning the planning and timing of delivery to users, impacting end-users directly, and can happen (less) frequently following the cadence of the organisation. The Deployment takes us to a state we wish to be in, and the release makes it available for use by end-users.
  
## So what's a deployment?

To break it down, deployment is the act of putting of the thing you made (artefact, container, microservice, infrastructure, serverless function etc), in the place you want it to go e.g., An environment built to run and support interactions with your deployable thing. This isn't always as easy as it sounds, and each deployable will have it's own challenges and so will the environments you are working with.

The purpose of a deployment is to validate performance under real-world conditions, deliver value by rolling out new features and updates, streamline and automate updates to minimise disruptions, and facilitate rollbacks to maintain system stability. This can be done in multiple ways, from manual (in...dev...right) to fully automated (hurray!). It could involve a few steps, or it could be a complex pipeline involving multiple stages, jobs, teams, and even geographical zones. Whether the most simple, or the most complex, it's always worth remembering that every deployment needs good testing, version control, and rollback capabilities.  
  
## What about releases? 

A release is where functionality e.g., a new feature or an upgraded version of an API, is made available to its users. This is all around _when_ the new functionality is presented to the users. The timing and execution of a release is the most important consideration, commonly balancing the needs of the business e.g., getting new feature out that generates revenue, and the expectations of the users e.g., uptime.  It serves to evolve the product, meet user expectations, measure user response for future development refinement, and mitigate risk by controlling the timing and manner of delivery.
  
### Deployment types
The common expectation is a successful deployment is followed immediately by a release, and while this can happen, you might want to deploy a new version without releasing it to your users. There are many ways this can be done, remembering this can be dependant on what you are deploying and the underlying infrastructure of your environment(s):

#### Rolling Deployment

Where the new version is gradually deployed across all instances. As the new version is being deployed, the old versions continue to operate, reducing the chances of system downtime.

#### Blue-Green Deployment

Here two environments (Blue and Green) are maintained. The Blue environment has the live production application, while the Green environment is used for the new version. Once the new version is ready and tested in the Green environment, the routing is switched, and the Green environment becomes live production.

#### Canary Deployment

With canary a new version is initially released to a small subset of servers or users. If everything works well, the new version is progressively rolled out to the rest of the servers or users.

#### A/B Testing

While similar to a Canary deployment, in A/B testing the performance of both versions is compared in order to decide whether the new version is beneficial or not.

### Feature Flags (or Feature Toggles)

Feature flags allow developers to control the visibility and functionality of a specific feature in a live environment. This means they can turn features on or off, enable them for specific user groups, or roll them out progressively. This deployment strategy enables teams to test new features in the production environment without affecting the entire user base. If an issue arises with the new feature, it can be toggled off immediately, reducing the impact on users. Feature flags provide a safety net and offer flexibility for both deployments and releases.

Deployment and release practices often hit plenty of common challenges that can impact their success, especially those practices that have grown organically over time rather than through explicit direction and planning. Recognising these obstacles is the first step towards mitigating them and enhancing the efficiency of these processes. 
For example, deploying a new version could be a rigid and laborious process. Changes, often require a significant amount of effort to implement, especially when dependencies or configurations are separated from the artefact, managed by different teams or third parties. 
Then we have the human error factor, brought on by manual deployment processes. The lack of automation can lead to mistakes in configuration, incorrect file transfers, or forgotten/overlooked steps, resulting in failed deployments and service disruptions. This underscores the mantra in modern development: automate everything!
In deployment models where changes accumulate behind infrequent release events, coordinating all necessary stakeholders from developers and testers, operations ans support, to marketing and leadership - it becomes an overly complex, challenging and unrepeatable process. This usually creates a lack of trust across the teams involved, but an issue that can be alleviated through good practices and open communication.
Finally, when users discover issues or bugs that slipped past testing, experience unexpected downtime during deployments, or suffer from reduced performance. All these factors can lead to user dissatisfaction. This can create churn in your product and cause a loss of trust within your customer.
Considering all these challenges, it's clear that each of them individually, or even combined (argh!), can considerably impact a product's progress and success. Taking time to discover and understand your bottlenecks, and taking steps to address them by communication, restoring and building trust, and leveraging modern practices and tools to tackle these issues is not just tech debt, but an essential strategy in creating the most value for your organisation.
  
## Feature Flags

Feature flags, are a simple yet powerful enabler that allow teams to make changes without exposing those changes to the user. This allows teams to deploy whenever they choose, and take steps towards continuous deployment, as any changes, new features or even incomplete features are protected from the user behind the feature flags.

Feature flags work by wrapping a feature or a portion of code in a conditional statement. When a feature is 'flagged,' its execution depends on the condition defined by the flag. This condition could be anything – a configuration setting, user attributes, or system parameters. This conditional logic allows developers to toggle features on or off without having to deploy or rollback code.

Essentially they provide a safety net, enabling teams to deploy code more frequently with less risk. Features can be merged into the main codebase but remain disabled in production until ready for release. This way, feature flags decouple deployment from release, facilitating easier code integration, reducing deployment risk, and allowing for more controlled release management.  All these things lead to improving the outcomes we discussed earlier, improving communication and trust via modern practices.

Using Feature flags can give you great benefits that were not possible before without them.  For example, switches that you can turn on or off to control different parts of your app or website, allowing you to try out new things and make changes in a safe, controlled way. Or if you have a new feature, that you don't want to show to everyone all at once. You can show it to a small group of users first, sort of like a sneak peek. This is like testing the waters before jumping in, reducing the chances of something going wrong for everyone.  They can also help you see what works best. You could even go so far as to have two versions of a feature and use a feature flag to show version A to one group of users and version B to another group. This is known as A/B testing, and it can give you some really useful information about what your users prefer.
Feature flags can also make the user experience smoother. We've all experienced downtime when suddenly a product or service is unavailable or stops working when new is being added. With feature flags, new features can be added without interrupting what users are doing.
For multiple teams working in the same codebase, feature flags can also make things easier, allowing developers to work on, and deploy, new features separately without impacting those around then. If something goes wrong with a new feature, they can simply turn off the feature flag, rather than go through a long winded roll-back or panic around bug fixes.

Now, feature flags can offer great flexibility in managing deployments and releases, it's important to always consider a few good practices to get the most out of them and avoid potential pitfalls, 
Firstly, practice restraint! Their sole function should be for controlling feature rollouts, not as a crutch to enable discrepancies in system behaviour. Overuse can clutter your codebase and complicate application behaviour.  Flags shouldn't be long-lived and once features are fully available, they should be removed.
Always avoid scenarios where feature flags are nested or are dependant on one another. This just adds to complexity, and goes against the principle that flags should be independent around a single feature.  This brings us back to jeopardising any trust we've been building. 

 ### Clean up. Clean up. Clean up!

As I mentioned earlier, after a feature flag has fulfilled its purpose, remove it! Failure to do so will contribute to technical debt, making your product increasingly difficult to maintain and evolve over time.
Lastly, don't forget to keep an eye the impact of your feature flags. Measuring this not only helps you understand how well a feature is performing but can also provide insights into user behaviour. Observability tools can greatly assist in this, giving you a detailed view of your feature flags in action.

Feature flags, while powerful, should be used at the right time, for the right reasons. Their overuse can lead to overly complex config and technical debt. However, using them correctly feature flags can be an invaluable tool in your delivery processes, enabling teams to manage deployments and releases faster, more effectively and responsively.

The use of feature flags in deployment and release processes enables more flexible, controlled, and data-driven delivery. By understanding and decoupling deployment from release through feature flags, anyone can enable teams to integrate, test, and release more efficiently and with less risk, whilst building trust and communication across the organisation.

The growing popularity in the use of practices like feature flags reflects a broader shift in delivery towards organisations that prioritise adaptability, continuous improvement, and user-centric design. As those organisations continue to innovate and advance using these principles, they will continue to guide the evolution of delivery through the right application of deployment and release strategies like these.
