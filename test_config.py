import unittest
from src.config import GITHUB_API_URL, DEFAULT_FONT_SIZE, DEFAULT_FONT_STYLE, PDF_OUTPUT_PATH, UI_TEXT_FIELD_ID, UI_MESSAGE_NAME, MAX_WAIT_TIME, MAC_OS_DEPLOYMENT_STANDARD

class TestConfig(unittest.TestCase):
    def test_github_api_url(self):
        self.assertEqual(GITHUB_API_URL, 'https://api.github.com/')

    def test_default_font_size(self):
        self.assertEqual(DEFAULT_FONT_SIZE, 12)

    def test_default_font_style(self):
        self.assertEqual(DEFAULT_FONT_STYLE, 'Courier')

    def test_pdf_output_path(self):
        self.assertEqual(PDF_OUTPUT_PATH, 'output.pdf')

    def test_ui_text_field_id(self):
        self.assertEqual(UI_TEXT_FIELD_ID, 'github_repo_url')

    def test_ui_message_name(self):
        self.assertEqual(UI_MESSAGE_NAME, 'status_message')

    def test_max_wait_time(self):
        self.assertEqual(MAX_WAIT_TIME, 180)

    def test_mac_os_deployment_standard(self):
        self.assertTrue(MAC_OS_DEPLOYMENT_STANDARD)


if __name__ == '__main__':
    unittest.main()
