---
title: Repository templates
sidebar_position: 2
---

# Repository templates

## What

We will standardise the creation of repositories.  This will bring consistency and tools directly to each repository we create, adjusted depening on what purpose the repository serves e.g. Infrastructure, application, containers etc.  As our preferred tool for repository mangement is GitHub, the templating will initially focus here.


## How

These templates are held within our GitHub [Org](https://www.github.com/BurendoUK), and used exclusivley to create reopsitories using a standardised pattern for creation and deployment (Pipeline), and a standardised tool for repository state (Terraform).

[Standard Repo](https://github.com/BurendoUK/burendo-repo-template)  
[Terraform Repo](https://github.com/BurendoUK/burendo-repo-template-terraform)  
[Container Repo](https://github.com/BurendoUK/burendo-repo-template-container)

## Content

Each repository template should hold standardised licensing, githooks, actions, README and any code based templating we wish to include, again depending on repository functionality.

## Terraform

Below is an example terraform template file for repository management.  These repositories are created and managed in the [Burendo GitHub Config repo](https://github.com/BurendoUK/burendo-github-config):

```hcl
resource "github_repository" "example" {
  name             = "example"
  description      = "example"
  visibility       = "public"
  auto_init        = false

  allow_merge_commit     = false
  delete_branch_on_merge = true
  has_issues             = true
  topics                 = local.common_topics

  lifecycle {
    prevent_destroy = true
  }

  template {
    owner = var.github_org
    repository = "burendo-repo-template"
  }
}

resource "github_team_repository" "example_burendo" {
  repository = github_repository.example.name
  team_id    = github_team.burendo.id
  permission = "push"
}

resource "github_team_repository" "example_admin" {
  repository = github_repository.example.name
  team_id    = github_team.engineering.id
  permission = "admin"
}

resource "github_branch_protection" "example_main" {
  pattern        = github_repository.example.default_branch
  repository_id     = github_repository.example.name
  enforce_admins = false

  required_status_checks {
    strict = true
  }

  required_pull_request_reviews {
    dismiss_stale_reviews      = true
    require_code_owner_reviews = true
  }
}

resource "github_issue_label" "example" {
  for_each   = { for common_label in local.common_labels : common_label.name => common_label }
  color      = each.value.colour
  name       = each.value.name
  repository = github_repository.example.name
}

resource "github_actions_secret" "example_terraform_version" {
  repository      = github_repository.example.name
  secret_name     = "TERRAFORM_VERSION"
  plaintext_value = var.terraform_version
}
```
## Git hooks

What are git hooks? See [here](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks)

Example of reasoning behind using git hooks.

A pre-commit is designed to catch any secret/private content being accidently commited to public repositories. These include AWS Account IDs, Access key IDs, IP addresses, email addresses etc... This can been adjusted to ignore lines beginning Subproject commit to avoid triggering its own pre-commit check ("40 character random (e.g. AWS secret access key, PAT)"). 


Below is an example `pre-commit` git hook.  Burendo Git hooks are managed in the [Burendo Githooks Repo](https://github.com/BurendoUK/burendo-githooks):

```bash
#!/bin/bash
#set -x
declare -a patterns=(
    "\b[A-Z0-9]{20}\b"
    "\b[A-Za-z0-9\/+=]{40}\b"
    "\b[0-9]{12}\b"
    "\b[a-z0-9]{32}\b"
    "PRIVATE KEY-----"
    "\b.[a-z]{2}-[a-z]{4,9}-[0-9]{1}.\b"
)

declare -a descriptions=(
    "AWS access key ID"
    "40 character random (e.g. AWS secret access key, PAT)"
    "AWS account number"
    "16 byte hex (e.g. S3 bucket name)"
    "Private key (e.g. rsa private key, openssh private key)"
    "Regions embedded as part of resource descriptions"
)

declare -a email_patterns=(
    "\b[A-Za-z0-9._%+-]{1,}@[A-Za-z0-9]{1,}.[A-Za-z0-9]{1,4}.[A-Za-z0-9]{1,4}\b"
)

declare -a email_descriptions=(
    "Email addresses"
)

declare -a ip_patterns=(
    "\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"
)

declare -a ip_descriptions=(
    "IP address"
)

declare -a allowed_tags=(
    "@given"
    "@when"
    "@then"
)

if [ -d ".gitsecret" ]; then
    git secret hide
fi


match=0
for i in "${!patterns[@]}"
do
    git diff-index -p -M --cached HEAD -- | grep -v "Subproject commit" | grep -v "mxfile host" |
    grep '^+[^+]' | grep -Eq "${patterns[$i]}" &&
    echo "Blocking commit: ${descriptions[$i]} detected in patch" &&
    echo "This part of your change triggered this issue:" &&
    git diff-index -p -M --cached HEAD -- | grep -v "Subproject commit" | grep -v "mxfile host" |
    grep '^+[^+]' | grep -E "${patterns[$i]}" &&
    ((match++))
done

for i in "${!email_patterns[@]}"
do
    git diff-index -p -M --cached HEAD -- | grep -v "snyk/snyk@"| grep -v "create-release@latest"| grep -v "checkout@master"| grep -v "Publish-Docker-Github-Action@master"| grep -v "docker@master"|
    grep -Eq -v "${allowed_tags[$i]}" | grep '^+[^+]' | grep -Eq "${email_patterns[$i]}" &&
    echo "Blocking commit: ${email_descriptions[$i]} detected in patch" &&
    echo "This part of your change triggered this issue:" &&
    git diff-index -p -M --cached HEAD -- | grep -v "snyk/snyk@"| grep -v "create-release@latest"| grep -v "checkout@master"| grep -v "Publish-Docker-Github-Action@master"| grep -v "docker@master"|
    grep -Eq -v "${allowed_tags[$i]}" | grep '^+[^+]' | grep -E "${email_patterns[$i]}" &&
    ((match++))
done

for i in "${!ip_patterns[@]}"
do
    git diff-index -p -M --cached HEAD -- | grep -v "169.254.169.254" | grep -v "0.0.0.0" | grep -v "127.0.0.1" |
    grep '^+[^+]' | grep -Eq "${ip_patterns[$i]}" &&
    echo "Blocking commit: ${ip_descriptions[$i]} detected in patch" &&
    echo "This part of your change triggered this issue:" &&
    git diff-index -p -M --cached HEAD -- | grep -v "169.254.169.254" | grep -v "0.0.0.0" | grep -v "127.0.0.1" |
    grep '^+[^+]' | grep -E "${ip_patterns[$i]}" &&
    ((match++))
done

if (( match > 0 )); then
    echo "If the above are false positives then you can use the --no-verify flag to skip checks"
    echo "git commit --no-verify"
    exit 1
fi
```
