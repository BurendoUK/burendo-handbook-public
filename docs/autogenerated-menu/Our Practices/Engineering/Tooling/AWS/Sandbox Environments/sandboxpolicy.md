---
title: AWS Sandbox Policy & Best Practices
sidebar_position: 1
---

# AWS Sandbox Policy & Best Practices

Sandbox environments are more permissive than say a development or test environment and given we are at an early stage we need to protect critical assets of our organisation by introducing a clearly defined usage policy for sandbox accounts which should be in an agreement with developers, stakeholders, security, and compliance teams if we have them.

* **Data classification:** Specify which classes of data are allowed in the sandbox accounts. Many organisations prohibit the use of customer data (names, email addresses, phone numbers, payment information, and so on) in sandbox environments.

* **Network connectivity:** Specify whether networks in the sandbox environment are allowed to connect to networks in other or shared services environments. Typically, these environments are isolated. You can set up guardrails to alert the appropriate groups when peering connections,

* **Access control:** Specify who has access to sandbox AWS accounts. Accounts can either be dedicated to a single developer or shared by a small team. Using individual accounts simplifies cost reporting and makes it much easier to identify resource owners. Shared accounts are simpler to centrally monitor and manage. Your usage policy should also specify that a cross account Identity and Access Management (IAM) role must be implemented in each sandbox account to give security and compliance teams the access required to monitor resources and activity in the account.

* **Tagging policy:** Even in a sandbox account, tagging your resources is critical. Tagging helps your identity who created resources, who is responsible for them, and how costs should be allocated. Your policy should specify which tag keys should be applied to all resources in sandbox environments.

* **Resource lifecycle policy:** Specify how long resources can persist in a sandbox account. That’s a good way to prevent them from becoming shadow development or even production environments. Organisations often implement lifecycle policies to shut down resources after a specified number of days.
 
* **Implement guardrails:** To prevent unwanted actions, apply appropriate guardrails to our sandbox accounts. When we design and implement guardrails, be sure to reference the sandbox usage policy. When we implement preventative and detective measures in our multi-account sandbox environment, you can use AWS Control Tower to manage the implementation of guardrails.

## AWS services for security guardrails
 
You can use several AWS security services to protect your sandbox environment from security threats. For example, Amazon Macie is useful for detecting personally identifiable information (PII) type data and other sensitive data types in your Amazon Simple Storage Service (Amazon S3) storage. That’s why it’s important to classify which type of data is suitable for your sandbox environment in your sandbox usage policy. Using Macie to detect PII data will help you maintain your data classification policy. You might also want to use Amazon GuardDuty for threat monitoring, Amazon Inspector for vulnerability assessment, and Amazon Detective for identifying the root cause of security issues.
 
You can also use the following services to create custom guardrails:
 
## AWS Config
 
As a preventative control, you can use AWS Config to implement managed and custom rules to manage resource configurations across your AWS account. Config makes it possible to evaluate the configuration of your AWS resources to evaluate appropriate settings. For example, you can implement a managed rule to monitor that all S3 buckets have server-side encryption enabled. If an S3 bucket in your sandbox environment does not have server-side encryption enabled, AWS Config detects and flags the noncompliant resource. You can optionally include an auto-remediation using AWS Systems Manager to resolve the rule. For more information, see the Amazon S3 bucket compliance using the AWS Config auto remediation feature blog post. AWS Config conformance packs can also help you implement best practices and custom controls across your sandbox environments.
 
## AWS CloudTrail and Amazon EventBridge
 
You can use AWS CloudTrail as an auditing tool to continuously monitor API calls in your AWS environment. You can use Amazon EventBridge to create rules that trigger on the information captured by CloudTrail. For example, you can set up an EventBridge rule to trigger when CloudTrail records an API call to create a VPC peering connection. The EventBridge rule can use Amazon Simple Notification Service (Amazon SNS) as a target to notify your development team of the new peering which can then post into a Slack channel, thus setting up detective controls for your sandbox environment.
 
## AWS Organizations
 
Service control policies (SCPs) are management feature of AWS Organizations that allow you to manage permissions across your organization. You should implement SCPs as a security guardrail to prevent unwanted actions.
 
Sandbox accounts should be grouped into a “Sandbox” organizational unit in Organizations so that SCP’s can easily be applied across all sandbox accounts. See Best Practices for Organizational Units with AWS Organizations for more assistance on establishing an OU structure.
 
Here are some example SCPs to consider implementing in our sandbox environment:

* Deny access to AWS based on requested Region.
* Restrict Amazon Virtual Private Cloud (VPC)internet access and network connectivity.
* Require Amazon Elastic Cloud Compute (EC2)instances to use a specific type (for example, any instance not launching t2.micro is denied).
* Prevent users from changing AWS Config rules.
* Prevent users from ordering a Snowmobile container.
* You can allow access only to the services that you want your developers to use rather than denying access to specific services.
 
## Tracking and managing costs
 
Given their exploratory nature, it is critical to implement budget controls on your sandbox accounts. Budget controls allow you to view and manage the amount of spend on AWS accounts in your organization.
 
Here are two best practices for limiting spending on your sandbox accounts:

You can plan how much you want to spend on a service (cost) or how much you want to use on one or more services (usage). You can also set up optional notifications to warn you if you exceed, or are about to exceed, your allotted amount for cost or usage budgets.
 
## Use cost allocation tags

When you tag your AWS resources, it’s much easier to organize, categorize, and track your AWS costs. Cost allocation tags are useful for tracking expenditure on exploratory workloads in your sandbox account.
 
## AWS Cost Explorer
 
For inspection of your cost and usage, consult AWS Cost Explorer in the AWS Management Console. It displays your past usage and cost, forecasts expected spend, and provides recommendations for ways to optimize costs. AWS Cost Explorer is useful for tracking costs across your sandbox accounts.
Resource lifecycle management
 
If you do not implement lifecycle management policies and spending limits, your sandbox environment can easily become an undocumented and unsupportable production environment. A defined lifecycle policy allows you to control costs, prevent unauthorized use of sandbox environments, and set expectations for sandbox account users.
 
For example, you might want EC2 instances to be shut down or S3 buckets to be deleted after a fixed number of days. You might also want the environment to reset to a baseline set of resources on a periodic basis. Your approach to automating these policies will vary, depending on how resources are created.
 
If you use AWS CloudFormation stacks to create resources in the sandbox environment, see the approach described in the scheduling automatic deletion of AWS CloudFormation stacks blog post.
If you are using the console or API operations to create resources, you should implement AWS Lambda functions to determine when resources were created and when they should be deleted. There are a few ways to do this. One way is to set a tag key-value pair for when resources should be deleted and then implement a Lambda function to delete them. Another way is to use AWS Config (for services that it supports) to find when resources were created to determine if they should be deleted.
 
If you want to reset your sandbox environments to a baseline set of resources (for example, a baseline VPC, required IAM roles, configuration S3 buckets, and so on) on a periodic basis you can build your own automation, or utilise open-source tools that are built for this purpose.
 