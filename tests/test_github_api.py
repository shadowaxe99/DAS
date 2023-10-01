```python
import unittest
from unittest.mock import patch
from src import github_api

class TestGitHubAPI(unittest.TestCase):

    @patch('src.github_api.requests.get')
    def test_fetch_repo(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'content': 'test_content'}

        response = github_api.fetch_repo('https://github.com/user/repo')

        self.assertEqual(response, 'test_content')
        mock_get.assert_called_once_with('https://github.com/user/repo')

    @patch('src.github_api.requests.get')
    def test_fetch_repo_failure(self, mock_get):
        mock_get.return_value.status_code = 404

        response = github_api.fetch_repo('https://github.com/user/repo')

        self.assertIsNone(response)
        mock_get.assert_called_once_with('https://github.com/user/repo')

if __name__ == '__main__':
    unittest.main()
```