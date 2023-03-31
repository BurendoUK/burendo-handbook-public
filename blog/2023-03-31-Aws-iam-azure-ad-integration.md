---
title: Azure AD and AWS IAM Identity Centre Integration
description: How to integrate Azure AD and IAM Identity Centre
slug: cloud-burendo-handbook
authors: bbayes
tags: [burendo-handbook, cloud]
---

# AWS IAM and Azure AD Integration

When it comes to User Management and authentication into multiple systems, it's good practice to have a single source of truth, and this applies even for authentication into public clouds. In this blog post we will cover how to integrate Azure AD and AWS IAM Identity Centre, so that you can have a central mechanism of managing users.

## Pre-requisites

In order to try this out, you will need:

1. An Azure AD subscription, you can sign-up for a free account [here](https://azure.microsoft.com/en-gb/free/)
2. AWS IAM Identity Centre enabled subscription, you can read more about what AWS IAM Idenitty Centre is [here](https://aws.amazon.com/iam/identity-center/)

## Enabling the Integration in Azure

### Adding the Enterprise Application

### Configuring Azure AD SSO

### Configuring AWS IAM Identity Centre SSO

## Wrap-up and Improvements

We have seen in this blog how relatively straight-forward this process is, and how we can make the most of Azure's ability to integrate with AWS and make your operations team lives a lot easier, not to mention reducing the security risk by having a centralised user management system.

If we wanted to take this process one step fruther, and automate the integration, we could look to use an Infrastructure-as-Code (IaC) agnostic tool such as Terraform to deploy the integration.

## Useful Links

1. https://azure.microsoft.com/en-us/products/active-directory
1. https://aws.amazon.com/iam/identity-center/
