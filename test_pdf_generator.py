import unittest
from unittest.mock import patch
from src.pdf_generator import PDFGenerator


class TestPDFGenerator(unittest.TestCase):
    def setUp(self):
        self.pdf_generator = PDFGenerator()

    @patch('src.pdf_generator.FPDF')
    def test_generate_pdf(self, mock_fpdf):
        repo_name = 'my-repo'
        owner = 'my-username'
        directory_structure = ['src', 'tests']
        code = 'def hello():\n    print("Hello, World!")'

        self.pdf_generator.generate_pdf(repo_name, owner, directory_structure, code)

        mock_fpdf.assert_called_once()
        mock_fpdf.return_value.set_font.assert_called_once_with('Arial', 'B', 12)
        mock_fpdf.return_value.cell.assert_called_once_with(0, 10, 'Repository: my-repo | Owner: my-username', 0, 1, 'C')
        mock_fpdf.return_value.set_y.assert_called_once_with(-15)
        mock_fpdf.return_value.set_font.assert_called_with('Arial', 'I', 8)
        mock_fpdf.return_value.cell.assert_called_with(0, 10, 'Page %s' % mock_fpdf.return_value.page_no(), 0, 0, 'C')
        mock_fpdf.return_value.add_page.assert_called_once()
        mock_fpdf.return_value.set_font.assert_called_with('Arial', 'B', 12)
        mock_fpdf.return_value.cell.assert_called_with(0, 10, 'Table of Contents', 0, 1, 'C')
        mock_fpdf.return_value.set_font.assert_called_with('Arial', '', 12)
        mock_fpdf.return_value.cell.assert_called_with(0, 10, 'src', 0, 1, 'L')
        mock_fpdf.return_value.cell.assert_called_with(0, 10, 'tests', 0, 1, 'L')
        mock_fpdf.return_value.add_page.assert_called_once()
        mock_fpdf.return_value.set_font.assert_called_with('Courier', '', 10)
        mock_fpdf.return_value.multi_cell.assert_called_once_with(0, 10, code)
        mock_fpdf.return_value.output.assert_called_once_with('output.pdf', 'F')


if __name__ == '__main__':
    unittest.main()
