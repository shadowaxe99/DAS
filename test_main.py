import unittest
from unittest.mock import patch, MagicMock
from src.main import convert_to_pdf


class TestMain(unittest.TestCase):
    @patch('src.main.fetch_repository_code')
    @patch('src.main.format_code')
    @patch('src.main.PDFGenerator')
    @patch('src.main.messagebox')
    def test_convert_to_pdf(self, mock_messagebox, mock_pdf_generator, mock_format_code, mock_fetch_repository_code):
        mock_fetch_repository_code.return_value = 'print("Hello, World!")'
        mock_format_code.return_value = '<span class="k">print</span><span class="p">(</span><span class="s">"Hello, World!"</span><span class="p">)</span>'
        mock_pdf_generator.return_value.generate_pdf.return_value = None
        mock_messagebox.showinfo = MagicMock()

        convert_to_pdf('https://github.com/username/repo')

        mock_fetch_repository_code.assert_called_once_with('https://github.com/username/repo')
        mock_format_code.assert_called_once_with('print("Hello, World!")')
        mock_pdf_generator.assert_called_once()
        mock_messagebox.showinfo.assert_called_once_with('Success', 'PDF generated successfully.')


if __name__ == '__main__':
    unittest.main()
