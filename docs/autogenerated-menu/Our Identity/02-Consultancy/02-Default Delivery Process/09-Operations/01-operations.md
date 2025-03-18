---
title: Operations
---
# Operations: Running and Managing Production Systems
## Introduction
This section covers operating the software produced during the build phase, ensuring that it runs reliably, securely, and cost-effectively in production.

These are recommended defaults, but teams can adapt them based on their specific needs (see What this is — and is not).

## Delivery Process Overview

#### Inputs
* Software running in production.

#### Outputs
* Reliable, observable, and scalable services.

### External Resources
In addition to this guidance, teams should validate their systems using external frameworks like:
* **AWS or Azure Well-Architected Frameworks** for architecture and operations best practices.
* **OWASP Security Best Practices** for identifying and mitigating vulnerabilities.
* **FinOps Foundation Guidelines** for managing cloud costs effectively.

## Preparing for Live Operations
Before a system goes live, ensure all operational aspects are planned and tested. Consider:

### Replacing an existing system?
* How can functionality be redesigned to be simpler and leaner rather than just replicating the old system?
* What data migration is needed?
* Will there be dual running or a hard switchover? Can it be rolled back if needed?
* How will users be migrated or onboarded? Will there be an outage?
* How will you monitor user impact (e.g., observability, analytics, feedback mechanisms)?
### Meeting non-functional requirements?
* Capture these as Service Level Objectives (SLOs).
* Ensure performance, security, and scalability needs are well understood and validated.
### Technology constraints?
* Are there existing systems or agreements that must be adhered to?
* If alternative technologies are proposed, negotiate and justify these recommendations.

## Designing and Building for Operability
Live operations should be a first-class concern when designing systems. Choose technologies and architectures that:

* Minimise complexity while maintaining flexibility.
* Enhance observability with structured logging, metrics, and tracing.
* Support required performance, scalability, and reliability.
* Automate maintenance tasks to minimise manual effort.

### Key Design Principles
#### Prefer serverless managed services where practical.
* Offloads operational overhead to the cloud provider, enabling teams to focus on delivering business value.
#### Split systems into well-defined components.
* Not too big or too small—each service should have a clear purpose and well-defined interfaces.
* Designed to allow independent development, deployment, and operation.
#### Deploy a steel thread / walking skeleton early.
* Getting something live early ensures operability is baked into the design.

### Observability
A production system should be observable, not just monitored. Implement:

* **Metrics** that matter to users (SLOs).
* **Clear dashboards** for critical service indicators.
* **Automated alerts** based on meaningful thresholds.
* **Structured logs** that are easily queryable.
* **Distributed tracing** to track requests across services.
[See: Observability and Monitoring Guide]

### Security
Security should be an integral part of operations, not an afterthought. Follow Secure Engineering best practices:

* Secure the software supply chain (e.g., dependency scanning, build pipeline security).
* Ensure strong authentication and authorisation (e.g., least privilege access, zero-trust security).
* Guard against OWASP Top 10 vulnerabilities through code review, automated scanning, and penetration testing.
* Regularly verify infrastructure security with automated tools.

[See: Secure Engineering Guide]

### Performance and Scalability
Operational performance should be validated continuously:

* Design with performance in mind.
* Address performance during elaboration, implementation, and validation.
* Perform regular load tests.
* Simulate traffic spikes and ensure the system scales effectively.

[See: Load Testing Guide]

### Reliability and Incident Readiness
Building reliable systems means designing for failure recovery:

* Automate recovery mechanisms.
* Self-healing instances and failover should be tested regularly.
* Practice failure scenarios.
* Use chaos engineering and Game Days to validate incident responses.

[See: Incident Management Guide]

### Cost Awareness in Operations (FinOps)
Effective operations include cost-conscious engineering:

* Track cloud spending with real-time monitoring.
* Implement auto-scaling to balance performance vs. cost.
* Shut down non-production environments when not needed.
* Select cost-effective compute and storage options based on actual usage.
* Teams should use FinOps principles to ensure cost transparency and optimisation.

[See: FinOps Best Practices Guide]

### Preparing for Live Support
Having a clear support process ensures a smooth handover to operations.

#### Define a Support Model
* Document Service Level Agreements (SLAs) that align with SLOs.
* Establish incident severity levels (e.g., P1-P3 based on impact).
* Agree on communication protocols for each severity level.
* Define operational responsibility (e.g., DevOps team, dedicated support team).
* Determine user support workflows for issue triaging and escalation.

#### On-Call and Out-of-Hours Support
* Determine on-call needs and compensation agreements.
* Set up alerting tools (e.g., PagerDuty, Pingdom) for immediate response.
* Ensure clear escalation paths for high-severity incidents.

[See: Support and On-Call Guide]

## Incident Management
When an incident occurs, follow a structured diagnosis and resolution process:

1. Detection & Communication:
* Monitor dashboards and alerts for early issue detection.
* Use Slack or another live channel for real-time coordination.
* Quickly determine the severity level (P1-P3).

2. Diagnosis & Resolution:
* Form hypotheses about root causes.
* Run safe, minimal tests to confirm the issue.
* Implement a fix or mitigation plan with support lead approval.

3. Post-Incident Review & Continuous Improvement:
* Conduct a Post-Incident Review (PIR) to document causes and improvements.
* Feed learnings into the delivery backlog to prevent recurrence.
* Rehearse incident handling through Game Days and chaos engineering.

[See: Incident Management and Postmortems Guide]

## Bringing It All Together
Effective operations is not just about keeping systems running but actively improving them. It requires a combination of thoughtful design, strong observability, security best practices, cost-conscious operations, and a proactive incident response.

By integrating operability concerns early, teams ensure systems are not just functional but sustainable and resilient.

Teams should continuously iterate on their support models, failure recovery, and cost management strategies to enhance service reliability while balancing performance and cost.

By following this approach, organisations can create scalable, maintainable, and secure production environments—while ensuring they are prepared for both routine operations and unexpected failures.

## Next Steps
This document provides an overview of production operations. For detailed guidance on specific tools and techniques, refer to the following:

* Observability & Monitoring Guide
* Secure Engineering Best Practices
* Load Testing Guide
* Incident Management & Postmortems
* Support and On-Call Guide
* FinOps Best Practices
