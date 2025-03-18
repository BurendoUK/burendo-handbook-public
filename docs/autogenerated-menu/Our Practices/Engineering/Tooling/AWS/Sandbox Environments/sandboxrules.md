---
Title: AWS Sandbox Environments
sidebar_position: 1
---

# AWS Sandbox Environments

The AWS Cloud Sandbox is meant to provide a real, open AWS environment for you to learn by doing, innovating and having fun along the way. We allow a variety of tools and services within AWS, so you have as many choices as possible when working through your certification training, innovating or just exploring!

## Available Services*

*All services available but limited to `eu-west-1`.

We will review new services as and when they are made available for suitability for the sandboxes. 

## Offered Service Limitations

We try to minimise the limitations of our sandboxes to provide the most comprehensive experience possible. Unfortunately, there are some limits to what we can provide. Refer to the list below for specific limits we enforce on our AWS Sandbox. You will be alerted when you do not have access.

### All Services

* No Purchasing or Billing Permissions
* Cannot modify Account settings
* Organizations
* Lightsail 

### S3 Bucket Limits

Can only be launched in `eu-west-1`.

### EC2 Limits

**ONLY** these Instance Types are allowed:

* t2.micro to t2.medium
* t3.micro to t3.medium
* Max Volume Size of 50GB
* Max Volume IOPS of 150
* No Elastic GPU

### EMR Limits

* **ONLY** m4.large instance type

### IAM Limits

* Cannot modify cloud_user or admin role
* Cannot use or set up SSO

Additional checks enforced via Abuse Checks (bottom of page)

### RDS Limits

ONLY these Instance types are allowed:

* db.t2.micro to db.t2.medium
* db.t3.micro to db.t3.medium
* Cannot use Provisioned IOPS
* Max Storage size of 50GB

### Redshift

* ONLY dc1.large or dc2.large Instance types
* Max Cluster Node count of 3

### Comprehend

* No Custom Classifiers
* No Custom Entity Recognizers
* No Custom Endpoints

### AWS Sandbox Abuse

The AWS Sandboxes are provided for fun, learning and innovative purposes. We actively monitor the sandboxes for abusive, prohibited, or otherwise un-awesome behavior. We do not provide the specifics of how or what we look for to prevent workarounds. The purpose of this abuse detection is to ensure compliance with our [Terms of Use](https://example.com "Terms of Use") which can be found in this handbook.

A few examples of abuse are listed below. This list is not comprehensive, so if you have any questions on your activity we invite you to contact [Support Team](http://example.com "Support Team") team prior to starting the activity. 

* Incorrect instance type
* Ten or more instances created at a time
* Attempting to use resources for Bitcoin mining
* Excessive network traffic
* DDoS or port scanning external hosts
* Keep ECS tasks to a minimum (5 max)
