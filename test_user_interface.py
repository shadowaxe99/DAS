import unittest
from unittest.mock import patch, MagicMock
from src.user_interface import UserInterface


class TestUserInterface(unittest.TestCase):
    def setUp(self):
        self.ui = UserInterface()

    @patch('src.user_interface.messagebox')
    @patch('src.user_interface.main.convert_to_pdf')
    def test_convert_to_pdf_valid_url(self, mock_convert_to_pdf, mock_messagebox):
        mock_convert_to_pdf.return_value = None
        mock_messagebox.showinfo = MagicMock()

        self.ui.repo_url_entry.insert(0, 'https://github.com/username/repo')
        self.ui.convert_to_pdf()

        mock_convert_to_pdf.assert_called_once_with('https://github.com/username/repo')
        mock_messagebox.showinfo.assert_called_once_with('Success', 'PDF generated successfully.')

    @patch('src.user_interface.messagebox')
    def test_convert_to_pdf_invalid_url(self, mock_messagebox):
        mock_messagebox.showerror = MagicMock()

        self.ui.repo_url_entry.insert(0, 'https://gitlab.com/username/repo')
        self.ui.convert_to_pdf()

        mock_messagebox.showerror.assert_called_once_with('Error', 'Invalid GitHub URL.')


if __name__ == '__main__':
    unittest.main()
