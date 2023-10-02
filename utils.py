import os
import requests

def validate_github_url(url):
    """
    Validates the provided GitHub URL.

    Parameters:
    - url (str): The URL to validate.

    Returns:
    - bool: True if the URL is a valid GitHub URL, False otherwise.
    """
    if 'github.com' not in url:
        return False
    return True


def fetch_repository(url):
    """
    Fetches the code from the provided GitHub repository URL.

    Parameters:
    - url (str): The URL of the GitHub repository.

    Returns:
    - str: The code of the repository.
    """
    if not validate_github_url(url):
        raise ValueError('Invalid GitHub URL.')

    response = requests.get(url)
    response.raise_for_status()

    return response.text


def create_directory(path):
    """
    Creates a directory at the provided path.

    Parameters:
    - path (str): The path of the directory to create.
    """
    if not os.path.exists(path):
        os.makedirs(path)


def write_to_file(path, content):
    """
    Writes the provided content to a file at the provided path.

    Parameters:
    - path (str): The path of the file to write.
    - content (str): The content to write to the file.
    """
    with open(path, 'w') as file:
        file.write(content)
}