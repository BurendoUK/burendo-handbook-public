---
sidebar_position: 1
---

# Integrating Azure AD Single Sign-On with AWS IAM Identity Center

In today's rapidly evolving technological landscape, organizations are looking for ways to streamline their IT infrastructure, reduce costs, and improve security. One of the ways to achieve this is by integrating Azure Active Directory (AD) Single Sign-On (SSO) with Amazon Web Services (AWS) Identity and Access Management (IAM) Identity Center.

## What is Azure AD SSO?

Azure AD SSO is a cloud-based identity and access management solution provided by Microsoft. It enables users to log in to multiple applications using a single set of credentials, thereby reducing the burden of remembering multiple usernames and passwords. Azure AD SSO integrates with many popular third-party applications, including AWS, to provide a seamless user experience.

## What is AWS IAM Identity Center?  

AWS IAM Identity Center is Amazon's centralized identity and access management solution for cloud resources. It enables administrators to manage the identities of their users, control their access to AWS resources, and enforce security policies. The AWS IAM Identity Center integrates with Azure AD SSO to provide a seamless and secure sign-on experience for users.

## How to Integrate Azure AD SSO with AWS IAM Identity Center?

Integrating Azure AD SSO with AWS IAM Identity Center involves several steps, including:

- Setting up an AWS IAM Identity Provider: In the AWS IAM console, go to Identity Providers and select Microsoft Azure AD. Fill in the required information, including the tenant domain and the client ID, which can be obtained from the Azure AD portal.

- Setting up Azure AD SSO: In the Azure AD portal, go to the Application Proxy section and add the AWS IAM Identity Provider as an application. Configure the settings as required and assign users or groups to the application.

- Configuring AWS IAM Roles: In the AWS IAM console, go to Roles and create a new role for Azure AD SSO. Assign the appropriate permissions and policies to the role.

- Testing the Integration: Log in to the Azure AD portal and access the AWS IAM Identity Provider. You should be able to access the AWS IAM console without having to enter separate credentials.

## Summary:

Integrating Azure AD SSO with AWS IAM Identity Center provides organizations with a seamless and secure way to manage the identities of their users. By eliminating the need for multiple usernames and passwords, this integration streamlines the login process and reduces the risk of security breaches. Whether you're a large multinational corporation or a small startup, integrating Azure AD SSO with AWS IAM Identity Center is an important step towards achieving a more secure, efficient, and cost-effective IT infrastructure.
