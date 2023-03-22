import requests
import os
from datetime import datetime
from pandoc import convert_text
from github import Github

# Step 1: Search for Confluence pages with the specific label
domain = os.environ["CONFLUENCE_DOMAIN"]
confluence_auth_token = os.environ["CONFLUENCE_AUTH_TOKEN"]
confluence_api_url = f"https://{domain}.atlassian.net/wiki/rest/api/content/search"
label = "export_to_github"
query = f'cql=type=page and label="{label}"'
headers = {"Authorization": f"Basic {confluence_auth_token}"}
response = requests.get(confluence_api_url, headers=headers, params=query)
pages = response.json()["results"]
github_token = os.environ["GITHUB_TOKEN"]

# Step 2: Iterate through the filtered list of pages
for page in pages:
    page_id = page["id"]
    page_title = page["title"]

    # Access Confluence content
    content_url = f"https://{domain}.atlassian.net/wiki/rest/api/content/{page_id}?expand=space"
    content_response = requests.get(content_url, headers=headers)
    content_data = content_response.json()
    confluence_content = content_data["body"]["storage"]["value"]
    space_name = content_data["space"]["name"]

    # Convert Confluence content to Markdown
    markdown_content = convert_text(confluence_content, 'markdown', format='confluence_storage')

    # Create or update Markdown files in GitHub
    github_token = os.environ["GITHUB_TOKEN"]
    repo_name = os.environ["GITHUB_REPOSITORY"]
    file_path = f"docs/{space_name}/{page_title}.md"
    commit_message = f"Updated {page_title} from Confluence"

    github_instance = Github(github_token)
    repo = github_instance.get_repo(repo_name)

    base_branch = repo.get_branch("main")
    branch_name = f"{page_title}_{datetime.now().strftime('%Y%m%d%H%M%S')}"
    repo.create_git_ref(ref=f"refs/heads/{branch_name}", sha=base_branch.commit.sha)

    try:
        contents = repo.get_contents(file_path, ref=branch_name)
        repo.update_file(contents.path, commit_message, markdown_content, contents.sha, branch=branch_name)
    except Exception:
        repo.create_file(file_path, commit_message, markdown_content, branch=branch_name)
