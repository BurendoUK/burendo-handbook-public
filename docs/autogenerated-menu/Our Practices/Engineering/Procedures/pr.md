---
title: Internal PR Process
sidebar_position: 2
---

# Internal PR Process

Our internal PR process is simple, test and Slack driven.  All repositories have two gates to merge, testing and an approval.  

## As a raiser

The general format is, if they exist, tests will run when a PR is raised.  Once passed the PR should be posted in the appropriate Slack channel for review and approval.

When working on ticketed items, please include the ticket name in your PR and each commit message when possible, e.g.

title: `[EP-32] Add Peer Review process to Handbook`

Commit message: `git commit -m "[EP-32] Adding Peer Review process to Handbook"`

This should make it easier to associate tickets with code commits, and also make it easier to see when changes were made and why.

Once someone has begun to review your PR, you should expect to see emoji's on your post.  The table below describes each one.

### Feedback

If questions are raised, it is on you to respond in a timely fashion.  Refer to tickets or documentation when required, commit code suggestions or make the appropriate changes.  Once done inform the reviewer of any answers/changes and await further feedback or approval.

### Merges

It is preferred that the reviewer will get the PR to a state where either feedback is required, or a merge can go ahead, by marking it appropriately.  It is the responsibility of the person raising the PR to merge it, unless requested otherwise.

## As a reviewer

In Slack the reviewer should mark the Slack post with the relative emoji as seen in the table below:

| emoji | meaning |
|:-----:|:-------:|
| :eyes: | Reviewing |
| :question: | Question |
| :white_check_mark: | Approved |
| :x: | Blocked (GIVE A REASON) |
| ![merged](images/merge.png) | Merged |

### Questions :question:

When reviewing it is important to remain within the spirit of the PR.  This simply means, review what has been changed, not what has been changed previously or what you want to see changed in the future.

We currently have no preferred way of formatting code, so as long as it is readable and tests are passing, we should be happy until this changes.

When questions are raised, be sure to check any appropriate tickets quoted along side the PR, as you may find the answers you are looking for.

### _*Use code suggestions!*_ 

Simple changes such as spelling or grammar, can be applied by the reviewer in a code suggestion.  Take this as far as you see fit, as no one expects large blocks of code to be written, but helping each other out with minor fixes should be our default.

### Blocking :x:

Only block when the merge will be catastrophic, e.g. the exposure of secrets.  The :x: emoji in Slack, should be accompanied with an explanation in a Slack comment, a comment within the PR and a block action in the PR.  Be aware that if you are the blocker, only you can unblock the PR again.  Blocking without explanation, is not helpful to anyone.
