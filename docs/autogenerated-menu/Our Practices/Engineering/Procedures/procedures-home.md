---
title: Procedures
sidebar_position: 1
---

# Procedures Home

## Code Review & Pull Requests

A pull request is the main and only way that code should reach a production environment.

### Developer Process

A developer contributing code will take the following steps before it is merged into the master branch:
* The developer will create a branch from the master branch on their local machine
* They will then create commits with code changes, constantly pushing changes to their branch changes to GitHub.
* While they are still developing or after they have completed developing their changes, they will open a pull request.
* Once the pull request has been opened, the developer will wait for all tests to pass and fix any bugs.
* The developer will assign reviewers who will review the code and ensure that it is as good as it should be and fulfils its purpose.
* Once reviewer approval has been marked on the pull request, the developer can then merge the pull request, which will then be passed onto the CI/CD pipeline.

### Automated Tests & Tasks

We will be running automated tests against all PRs to ensure that they will not cause issues when merged into production. These generally consist of a mixture of the following types of tests:

* Unit Tests
* Code Style tests
* Performance testing
* Deployment and testing on PR environment
* Lighthouse testing
* Third party dependency testing
* Preview environment deployment
* Static Code Analysis

Please see the [tooling](../Tooling/tool-home.md "Tooling") section for more information on the tools that we use to test our code.

### Coding Standards

Coding standards ensure that all developers working on a project are following the same set of specified guidelines to produce concise, maintainable code. The benefits of this include:

* Enhanced efficiency
* Reduced risk of project failure
* Minimise complexity
* Easy to maintain

We aim to write code that can be easily understood and that is consistent across all commits and projects. Ensuring consistency has a positive impact on the quality of the project, and one should ensure that it is maintained while coding. Also, it should be taken care that the guidelines are homogeneously followed across different levels of the system and do not contradict each other. The finished codebase should look like it has been written by a single developer, in a single session.

We automate coding standards wherever possible to ensure the least hassle for engineers. For more information about the tools and guidelines we apply, please read our coding standards documentation for specific areas:

* Frontend Engineering
* Backend Engineering

### Further Reading

* [Importance of Code Quality and Coding Standard in Software](https://www.multidots.com/importance-of-code-quality-and-coding-standard-in-software-development/)
