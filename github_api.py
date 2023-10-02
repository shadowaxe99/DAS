import requests
from src.config import GITHUB_API_URL

def fetch_repository_code(repo_url):
    """
    Fetches the code from a GitHub repository.

    Parameters:
    - repo_url (str): The URL of the GitHub repository.

    Returns:
    - dict: A dictionary containing the repository's code.
    """
    # Extract the owner and repo name from the URL
    owner, repo = repo_url.split('/')[-2:]

    # Construct the API URL
    api_url = f"{GITHUB_API_URL}/repos/{owner}/{repo}/git/trees/master?recursive=1"

    # Send a GET request to the GitHub API
    response = requests.get(api_url)

    # Raise an exception if the request was unsuccessful
    response.raise_for_status()

    # Return the repository's code
    return response.json()
}