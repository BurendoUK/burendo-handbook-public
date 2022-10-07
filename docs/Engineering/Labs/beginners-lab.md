---
sidebar_position: 2
---

# Beginners Labs
We want to encourage, educate and engage with budding engineers - one way to do this is to run beginners labs.
These sessions aren't limited just for beginners - we can use the pre-made sessions to educate and up skill our clients engineers.

Labs by their nature should be hands on, they are less about talking theoretically about how something can be done or demonstrating something that was created.
They are designed to educate people on a small section of knowledge at a time. They should be self contained and completing any should create a finished product - therefore not requiring a chain of labs to achieve something.

## Labs we've created
All the labs we've created for AWS are available in the [burendo-aws-labs](https://github.com/BurendoUK/burendo-aws-labs) repo.

## Learnings along the way
Some learnings came from our first beginners lab. We should look to improve the experience and value ahead of the next one.

### AWS Accounts
We liased with AWS to create some 'test' accounts for the event. This would have allowed the guests to use these accounts without fear of costing themselves anything if they used any resources out of free tier OR forgot to destroy resources.
Unfortunately these accounts weren't activated and weren't available to use at the time of the event.

At Burendo, we should be prepared for anything. We should be able to supply our guests with an AWS account from us - where we can resolve any issues directly.

### Difficult material
Although a full walk through was written for the beginners lab, many struggled at advanced points such as SSH. People on Mac were using the terminal and executing the commands against their host machine.
We could create a bitesize information video on what is SSH, how it is used and how to connect to server using it.

Alternatively, we can roll an AMI for these events which has AWS SSM agent on, so that the guests doesn't use SSH and can follow a simpler connection journey.

Investing in the material prior the event will be worth it. We have the ability to re-run these sessions for guests & potential clients in the future. Ensuring hiccups are resolved makes for a better experience and greater value delivered.
> It is difficult for engineers to gauge what is suitable for beginners. We should encourage non-engineers within Burendo to beta test our material before running it.
> Guests to these events often use Windows. We must better accommodate Windows in when preparing our material. We should use an AWS WorkSpace to understand the process for a Windows user.

### Distribution
The Beginners lab material that was delivered, was delivered via a WordPress website (which was to demonstrate what we'd be creating). This has since been destroyed. 
The material is available as a Word document which mightn't be the greatest form to deliver if we want to manage this via version control. We should create material as mark down, in a repository of its own. So that it can have supporting resources such as terraform.
