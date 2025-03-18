---
Title: Our Learnings
sidebar_position: 2
---

# Our Learnings
As we create these Labs we learn how best to teach the content, any issues with it and ways to improve in the future.
We want to be transparent about our learnings, so that anyone looking to build a 'lab' can stand on our shoulders and build forward.

## Recognising where we can help further

In a recent run through the [WordPress via AWS Console](https://github.com/BurendoUK/burendo-aws-labs/tree/main/Labs/wordpress-via-console) lab, many individuals hadn't used SSH before. People using MacOS were using the terminal and executing the commands against their host machine. We could create a bitesize information video on what is SSH, how it is used and how to connect to server using it.

Alternatively, we could roll an AMI for these events which has AWS SSM agent on, so that the guests doesn't use SSH and can follow a simpler connection journey.

Investing in the material prior the event will be worth it. We have the ability to re-run these sessions for guests & potential clients in the future. Ensuring hiccups are resolved makes for a better experience and greater value delivered.
> It is difficult for engineers to gauge what is suitable for beginners. We should encourage non-engineers within Burendo to beta test our material before running it.
> Guests to these events often use Windows. We must better accommodate Windows when preparing our material. We should use an AWS WorkSpace to understand the process for a Windows user.

## Reducing the differences between operating systems

When developing the [WordPress via Infrastructure as Code](https://github.com/BurendoUK/burendo-aws-labs/tree/main/Labs/wordpress-via-iac) lab, we attempted to reduce the differences in instructions across operating systems - to make it easier to teach but also to debug.
As a result, we've developed a CLI 'toolbox' Docker container - aptly named the [Lab container](https://github.com/BurendoUK/burendo-aws-labs/blob/main/Labs/LABS-CONTAINER.md). This container has installed all the tools someone would require to conduct any of the labs we create.

## Distribution

The first lab we delivered was done so via a Word document. This isn't a great medium because it can't be contributed to easily.
We've since created the [burendo-aws-labs](https://github.com/BurendoUK/burendo-aws-labs) repo to host all the labs we've created for AWS and supporting materials, in addition we've made it possible to view the lab content directly from this handbook.
