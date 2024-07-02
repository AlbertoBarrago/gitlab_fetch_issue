import os
import requests
from dotenv import load_dotenv

load_dotenv()

token_gitlab_pa = os.getenv('TOKEN_GITLAB_PA')
project_id = os.getenv('PROJECT_ID')


# TODO: Add filter and allow user to use multiple gitlab filters
def fetch_project_issues():
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {token_gitlab_pa}",  # Fixed
        "Content-Type": "application/json"
    }

    response = requests.get(
        f"https://gitlab.progettopa.it/api/v4/projects/{project_id}/issues?labels=Bug",
        headers=headers
    )

    response.raise_for_status()

    data_json = response.json()
    return data_json
