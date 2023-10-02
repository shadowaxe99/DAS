import unittest
import os
from unittest.mock import patch
from src.utils import validate_github_url, fetch_repository, create_directory, write_to_file


class TestUtils(unittest.TestCase):
    def test_validate_github_url_valid(self):
        url = 'https://github.com/username/repo'
        result = validate_github_url(url)
        self.assertTrue(result)

    def test_validate_github_url_invalid(self):
        url = 'https://gitlab.com/username/repo'
        result = validate_github_url(url)
        self.assertFalse(result)

    @patch('src.utils.requests.get')
    def test_fetch_repository(self, mock_get):
        url = 'https://github.com/username/repo'
        expected_result = 'print("Hello, World!")'
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = expected_result

        result = fetch_repository(url)

        mock_get.assert_called_once_with(url)
        self.assertEqual(result, expected_result)

    def test_create_directory(self):
        path = 'test_directory'
        create_directory(path)
        self.assertTrue(os.path.exists(path))
        os.rmdir(path)

    def test_write_to_file(self):
        path = 'test_file.txt'
        content = 'Hello, World!'
        write_to_file(path, content)
        with open(path, 'r') as file:
            result = file.read()
        self.assertEqual(result, content)
        os.remove(path)


if __name__ == '__main__':
    unittest.main()
