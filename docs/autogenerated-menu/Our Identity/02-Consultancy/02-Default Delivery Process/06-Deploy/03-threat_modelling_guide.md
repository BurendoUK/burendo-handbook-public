---
title: Threat Modelling Guide
---
# Threat Modelling Guide  

## Introduction  

Security is best addressed proactively rather than reactively. Threat modelling is a structured approach to identifying and mitigating potential security risks early in the software development lifecycle. By understanding possible attack vectors, security flaws, and system vulnerabilities, teams can design more resilient systems and avoid costly security issues later.  

Threat modelling should be a collaborative exercise involving engineers, product managers, security specialists, and other stakeholders. It is not just a security compliance task—it is a way to build better, more secure software by design.  

## What is Threat Modelling?  

Threat modelling is the process of systematically identifying and assessing security threats to an application, system, or service. It helps answer key security questions:  

- **What are we building?** Understanding the architecture, data flows, and system components.  
- **What can go wrong?** Identifying threats and attack vectors that could compromise security.  
- **What are we doing about it?** Mitigating threats through security controls, best practices, and design changes.  
- **Did we do a good job?** Validating that security risks have been properly addressed and tracked.  

Threat modelling is an ongoing practice, not a one-time activity. It should be revisited as systems evolve, new threats emerge, and architectures change.  

## When Should You Do Threat Modelling?  

Threat modelling is most effective when integrated early in development but should also be revisited throughout the software lifecycle. Key times to conduct or update threat models include:  

- **During initial system design** – Before development starts, to ensure security is considered from the beginning.  
- **When introducing new features** – To assess potential security risks related to new functionality.  
- **When integrating with third-party services** – To evaluate potential supply chain risks and external attack vectors.  
- **After a security incident** – To identify weaknesses and improve defences based on real-world attacks.  
- **As part of regular security reviews** – To proactively identify emerging risks and validate existing controls.  

## How to Perform Threat Modelling  

Threat modelling typically follows a structured process to ensure a comprehensive analysis of potential security threats. While different methodologies exist, a common approach includes the following steps:  

### **1. Define the System and Assets**  

Before identifying threats, you must understand what you’re protecting. Start by mapping out:  

- **System components** – Servers, databases, APIs, cloud infrastructure, third-party integrations.  
- **Data flows** – How data moves between components, including sensitive data processing.  
- **Entry points** – Where users, systems, or attackers can interact with your application.  
- **Actors and roles** – Who or what interacts with the system, including users, admins, and external services.  

This is best represented visually, using **Data Flow Diagrams (DFDs)** to illustrate interactions between components.  

### **2. Identify Potential Threats**  

Once you have a clear system overview, the next step is to identify potential threats. The **STRIDE framework** is a widely used approach to categorising threats:  

| **Threat** | **Description** | **Example** |  
|-----------|---------------|------------|  
| **Spoofing** | Impersonating another user or system | An attacker gains access by using stolen credentials |  
| **Tampering** | Modifying data or code to alter behaviour | A malicious user injects scripts to manipulate database entries |  
| **Repudiation** | Denying having performed an action | A user denies making a fraudulent transaction, and there is no audit log |  
| **Information Disclosure** | Exposing sensitive data | An API leaks customer information due to misconfigured permissions |  
| **Denial of Service (DoS)** | Overloading a system to disrupt availability | Attackers flood an API with requests, causing outages |  
| **Elevation of Privilege** | Gaining unauthorized higher-level access | A low-privileged user exploits a flaw to gain admin rights |  

By evaluating each component and data flow through the lens of STRIDE, teams can systematically identify potential attack vectors.  

### **3. Assess the Risk of Each Threat**  

Not all threats carry the same level of risk. Once identified, assess each threat based on:  

- **Likelihood** – How likely is it that this threat could be exploited?  
- **Impact** – What would be the consequences if the threat were exploited?  
- **Existing controls** – Are there already security measures in place to mitigate this threat?  

One practical way to prioritise risks is by using a **Risk Rating Matrix** (e.g., Low, Medium, High, Critical) to determine which threats require immediate attention.  

### **4. Mitigate Identified Threats**  

For each significant threat, determine appropriate security controls and mitigations. These may include:  

- **Authentication & Authorization** – Implement strong authentication (e.g., MFA, OAuth) and role-based access controls (RBAC).  
- **Data Protection** – Encrypt sensitive data in transit (TLS 1.2+) and at rest (AES-256).  
- **Input Validation & Sanitization** – Prevent SQL injection, XSS, and other common attacks.  
- **Logging & Monitoring** – Detect and respond to suspicious activity in real time.  
- **Rate Limiting & DoS Protections** – Protect against automated attacks using WAFs and API rate limiting.  
- **Secure Defaults** – Enforce least privilege access and use secure configurations.  

Each mitigation should be assigned an **owner** and tracked to ensure implementation.  

### **5. Validate and Review**  

Threat models should be living documents that evolve as the system changes. Regularly review and validate them by:  

- **Running security tests** – Automated security scans, penetration testing, and fuzzing.  
- **Simulating attacks** – Conducting **red team exercises** or **chaos engineering** to test defences.  
- **Updating threat models** – When introducing new features, integrations, or major architectural changes.  

## Threat Modelling in Agile and DevOps  

Traditional threat modelling has often been seen as a heavyweight process, but it can be adapted for **Agile and DevOps environments** by:  

- **Performing "Just-in-Time" threat modelling** – Quickly assessing risks during sprint planning or feature elaboration.  
- **Automating security scans** – Integrating SAST (Static Application Security Testing) and DAST (Dynamic Application Security Testing) into CI/CD pipelines.  
- **Using lightweight models** – Instead of complex diagrams, focus on key risks and mitigations using a collaborative whiteboard approach.  
- **Embedding security champions** – Having designated security-focused engineers within development teams.  

## Bringing It All Together  

Threat modelling is an essential security practice that enables teams to proactively identify and mitigate risks before they become real-world security incidents. By following a structured approach—mapping system components, identifying threats, assessing risks, implementing controls, and validating security measures—teams can build more resilient, secure applications.  

Threat modelling is not a one-time task but an ongoing practice that should evolve with the system. Integrating it into Agile and DevOps workflows ensures security becomes a natural part of development rather than an afterthought.  

By fostering a culture where security is a shared responsibility, teams can deliver software that not only meets functional needs but also stands strong against modern cyber threats.  
