---
sidebar_position: 2
---

# Our Learnings
As we create these Labs we learn how best to teach the content, any issues with it and ways to improve in the future.
We want to be transparent about our learnings, so that anyone looking to build a 'lab' can stand on our shoulders and build forward.

## AWS Accounts
We liaised with AWS to create some 'test' accounts for the event. This would have allowed the guests to use these accounts without fear of costing themselves anything if they used any resources out of free tier OR forgot to destroy resources.
Unfortunately these weren't available to use at the time of the event.

At Burendo, we should be prepared for anything. We should be able to supply our guests with an AWS account from us - where we can resolve any issues directly.

This facilitates the freedom of learning without having to have the additional knowledge of how to clean up afterwards. That can come in time for an individuals learning journey.

## Recognising where we can help further

In a recent run through the [WordPress via AWS Console](https://handbook.burendo.com/Engineering/Labs/wordpress-via-console/) lab, many individuals hadn't used SSH before. People using MacOS were using the terminal and executing the commands against their host machine. We could create a bitesize information video on what is SSH, how it is used and how to connect to server using it.

Alternatively, we could roll an AMI for these events which has AWS SSM agent on, so that the guests doesn't use SSH and can follow a simpler connection journey.

Investing in the material prior the event will be worth it. We have the ability to re-run these sessions for guests & potential clients in the future. Ensuring hiccups are resolved makes for a better experience and greater value delivered.
> It is difficult for engineers to gauge what is suitable for beginners. We should encourage non-engineers within Burendo to beta test our material before running it.
> Guests to these events often use Windows. We must better accommodate Windows when preparing our material. We should use an AWS WorkSpace to understand the process for a Windows user.

## Distribution

The first lab we delivered was done so via a Word document. This isn't a great medium because it can't be contributed to easily.
We've since created the [burendo-aws-labs](https://github.com/BurendoUK/burendo-aws-labs) repo to host all the labs we've created and supporting materials, in addition we've made it possible to view the lab content directly from this handbook.
