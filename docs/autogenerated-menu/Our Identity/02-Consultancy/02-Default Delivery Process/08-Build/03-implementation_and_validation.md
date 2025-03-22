---
title: Implementation and Validation
---
# **Implementation and Validation**
## **Overview**
The **Implementation and Validation** phase is where teams transform **refined backlog items into production-ready software**. This is the phase where the majority of a team's time is spent, writing code, testing, validating, and deploying software. 

Our approach is designed to balance **technical excellence with pragmatism**, ensuring that software is delivered in a way that is both sustainable and effective. While specific processes may vary between teams, this section provides **recommended best practices** to guide day-to-day activities.

➡️ *[See "How to Structure an Agile Delivery Workflow"]*

## **Culture and Ways of Working**
The **effectiveness of a team is defined more by its culture than by rigid processes**. Delivery practices are important, but the way team members collaborate, communicate, and support each other is what truly drives success.

### **Defining a Team Culture**
A high-performing team is greater than the sum of its parts. A strong culture ensures alignment, encourages open discussion, and promotes shared ownership of both successes and challenges. To reinforce this, teams should define and document their **Working Agreement**; a set of ground rules that articulate how they will work together.  

<!-- There's an important definition missing here.  How this is done is a combination of leadership and operator skill/experience.  You can not run a team of junior operators like a team of highly experienced ones.  Also a combination of personalities and leadership skills can have a huge impact.  Good leaders are aware of these and create the right culture for the right team. -->
<!-- Calling out leadership as a core skill is important.  None of these things are achievable with weak or poor leadership.  How do we ensure this? -->

➡️ *[See "How to Define an Effective Team Working Agreement"]*

### **Core Principles for Effective Teams**
1. **Team First:** No individual is more important than the collective success of the team. Helping teammates when needed ensures smoother delivery.
2. **Visibility and Transparency:** All work should be visible. Personal backlogs should be avoided to maintain focus on the highest-priority work.
3. **Inclusive Decision Making:** Whether it’s product design, technology selection, or prioritisation, decisions should be made collaboratively.
4. **Pragmatic Excellence:** Teams should strive for technical quality while prioritising real customer needs and adjusting when new insights emerge.

➡️ *[See "Building a Culture of Continuous Improvement"]*

## **Workflow and Delivery Process**
The **workflow** defines how a backlog item moves from "ready for implementation" to "running in production". While teams can evolve their process over time, the following workflow provides a solid starting point.

### **Workflow Overview**
1. **Backlog Preparation** – The backlog is continuously refined, ensuring that items are ready for implementation.
2. **Implementation & Validation** – Code is written, reviewed, and tested before merging.
3. **User Acceptance Testing (UAT)** – Key stakeholders validate changes before release.
4. **Final Validation** – The last quality checks before moving to production.
5. **Deployment to Production** – Software is released and monitored for stability.

➡️ *[See "How to Structure an Effective Agile Workflow"]*

### **Handling Blocked Work**
Blocked items should be identified and resolved as quickly as possible. Teams should avoid using a separate "blocked" column, as this removes visibility of which stage the item is in. Instead, flag blocked items within their current state and ensure they are actively monitored.


## **Creating Fast Flow**
Delivering software efficiently requires removing unnecessary hand-offs, reducing wait time, and automating where possible. The following approaches help create a smooth, fast-moving delivery pipeline.

### **Automation**
Automation plays a critical role in ensuring fast, reliable delivery. Automated testing, infrastructure, and deployment pipelines allow teams to move quickly and reduce operational risks.

- **Automated Testing**: The majority of functional and non-functional tests should be automated.
- **Infrastructure as Code**: Infrastructure and deployments should be managed through declarative code to ensure repeatability.
- **Continuous Integration & Continuous Deployment (CI/CD)**: Every change should be automatically built, tested, and deployed. 

➡️ *[See "Automating Agile Delivery: Best Practices"]*

### **Feature Flags**
Feature flags allow teams to deploy continuously without fully releasing a feature. By hiding incomplete functionality behind flags, new code can be shipped safely without impacting users. This decouples deployment from release, giving teams flexibility to validate features in production before rolling them out widely.

➡️ *[See "Using Feature Flags to Enable Continuous Delivery"]*



## **Code Development and Quality**
Delivering high-quality software means adopting disciplined coding, testing, and review practices. These ensure that software is reliable, maintainable, and meets both functional and non-functional requirements.

### **Trunk-Based Development**
Our preferred branching stratey is trunk-based development with short-lived feature branches. This approach ensures that the main branch is always in a deployable state and prevents long-lived branches from diverging significantly.

- **Feature branches** should be short-lived (1–2 days maximum).
- **Code reviews should be mandatory** before merging changes.
- **Squash merging is recommended** to keep the commit history clean.

➡️ *[See "Trunk-Based Development: Best Practices"]*

### **Code Reviews**
Code reviews are an essential part of maintaining high-quality code and knowledge sharing. Every change should be reviewed by at least one other team member before being merged. Reviews should focus on clarity, maintainability, and adherence to team conventions.

➡️ *[See "How to Conduct Effective Code Reviews"]*

### **Pairing**
Pair programming and other forms of collaborative development can significantly improve code quality, team learning, and consistency. While not every task requires pairing, teams should adopt it wherever it adds value.

➡️ *[See "Pair Programming: When and How to Use It"]*



## **Testing Strategy**
Testing should be integrated into the development process, not a separate phase. The recommended approach is "shift-left testing", ensuring that quality is built into the software as early as possible.

### **Automated Tests**
Testing should be structured using the testing pyramid:
- **Unit tests** provide fast, targeted validation of business logic.
- **Integration tests** ensure components interact correctly.
- **End-to-end tests** verify system-wide functionality but should be kept lean to avoid maintenance overhead.

➡️ *[See "Building a Scalable Test Automation Strategy"]*

### **Exploratory Testing**
In addition to automated tests, targeted exploratory testing should be performed before merging changes. This ensures that unexpected issues are caught early and that the software behaves as intended in real-world scenarios.

➡️ *[See "How to Structure Effective Exploratory Testing"]*



## **User Acceptance Testing (UAT)**
User Acceptance Testing ensures that the software meets business and user expectations before release. UAT should be conducted by Product Owners or Subject Matter Experts (SMEs) who can validate functionality from a user perspective.

Rather than finding bugs, UAT should focus on validating business value and usability. 

➡️ *[See "Structuring UAT for Agile Teams"]*



## **Deployment and CI/CD**
Teams should automate deployments wherever possible, ensuring that software can be released quickly and safely.

- **CI/CD pipelines should be fully automated**, triggered by changes to the main branch.
- **Deployments should be small and frequent**, reducing risk.
- **Rollback strategies should favour "fix-forward"**, allowing teams to deploy a fix rather than rolling back.

➡️ *[See "Building an Effective CI/CD Pipeline"]*



## **Technical Debt and Continuous Improvement**
Technical debt should be managed proactively, not left to accumulate. Teams should identify and address technical debt as part of normal delivery, rather than deferring it indefinitely.

- **Small improvements** should be made continuously, rather than through large refactoring efforts.
- **Technical backlog items** should be prioritised alongside feature work.
- **A culture of learning and improvement** should be encouraged.

➡️ *[See "Managing Technical Debt in Agile Teams"]*



## **Key Takeaways**
- **Effective delivery** is about culture as much as process. Teams should define and reinforce their ways of working.
- **A structured workflow** ensures smooth delivery, from backlog preparation to deployment.
- **Automation and CI/CD** reduce friction, allowing for frequent, reliable releases.
- **Testing** should be integrated into development, ensuring quality at every step.
- **Continuous improvement** is essential, balancing feature delivery with managing technical debt.
