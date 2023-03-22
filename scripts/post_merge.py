import os
import requests
import re
from datetime import datetime
from github import Github

def update_confluence_labels():
    # Set up the GitHub and Confluence API
    domain = os.environ["CONFLUENCE_DOMAIN"]
    github_token = os.environ["GITHUB_TOKEN"]
    confluence_auth_token = os.environ["CONFLUENCE_AUTH_TOKEN"]

    github_instance = Github(github_token)
    repo = github_instance.get_repo(os.environ["GITHUB_REPOSITORY"])
    pr_number = os.environ["INPUT_PR_NUMBER"]
    pull_request = repo.get_pull(int(pr_number))

    merged_branch_name = pull_request.head.ref

    # Extract Confluence page IDs from the merged branch name
    page_ids = re.findall(r'\d+', merged_branch_name)

    # Update Confluence labels
    headers = {"Authorization": f"Basic {confluence_auth_token}"}
    date_label = datetime.now().strftime("exported_%Y%m%d")

    for page_id in page_ids:
        # Remove the 'export_to_github' label
        confluence_api_url = f"https://{domain}.atlassian.net/wiki/rest/api/content/{page_id}/label"
        response = requests.get(confluence_api_url, headers=headers)
        labels = response.json()["results"]

        for label in labels:
            if label["name"] == "export_to_github":
                label_id = label["id"]
                delete_url = f"https://{domain}.atlassian.net/wiki/rest/api/content/{page_id}/label"

        # Add the 'exported_<date>' label
        new_label_data = {"prefix": "global", "name": date_label}
        add_label_url = f"https://{domain}.atlassian.net/wiki/rest/api/content/{page_id}/label"
        requests.post(add_label_url, headers=headers, json=new_label_data)

if __name__ == "__main__":
    update_confluence_labels()
