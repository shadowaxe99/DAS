import unittest
from unittest.mock import patch
from src.github_api import fetch_repository_code


class TestGitHubAPI(unittest.TestCase):
    @patch('src.github_api.requests.get')
    def test_fetch_repository_code(self, mock_get):
        repo_url = 'https://github.com/username/repo'
        expected_result = {
            'files': [
                {
                    'path': 'file1.py',
                    'content': 'print("Hello, World!")'
                },
                {
                    'path': 'file2.py',
                    'content': 'def add(a, b):\n    return a + b'
                }
            ]
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = expected_result

        result = fetch_repository_code(repo_url)

        mock_get.assert_called_once_with('https://api.github.com/repos/username/repo/git/trees/master?recursive=1')
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
