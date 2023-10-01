```python
import unittest
from src.pdf_generator import PDFGenerator

class TestPDFGenerator(unittest.TestCase):

    def setUp(self):
        self.pdf_generator = PDFGenerator()

    def test_generate_pdf(self):
        # Mock repository data
        repo_data = {
            'name': 'test_repo',
            'owner': 'test_owner',
            'code': 'print("Hello, World!")',
            'language': 'Python'
        }

        # Generate PDF
        pdf_file = self.pdf_generator.generate_pdf(repo_data)

        # Check if PDF file is created
        self.assertIsNotNone(pdf_file)

        # Check if PDF file has correct name
        self.assertEqual(pdf_file, 'test_repo.pdf')

    def test_add_table_of_contents(self):
        # Mock directory structure
        directory_structure = {
            'src': ['main.py', 'utils.py'],
            'tests': ['test_main.py', 'test_utils.py']
        }

        # Add table of contents
        self.pdf_generator.add_table_of_contents(directory_structure)

        # Check if table of contents is added
        self.assertTrue(self.pdf_generator.has_table_of_contents)

    def test_add_page_numbers(self):
        # Add page numbers
        self.pdf_generator.add_page_numbers()

        # Check if page numbers are added
        self.assertTrue(self.pdf_generator.has_page_numbers)

    def test_add_footer(self):
        # Mock repository data
        repo_data = {
            'name': 'test_repo',
            'owner': 'test_owner'
        }

        # Add footer
        self.pdf_generator.add_footer(repo_data)

        # Check if footer is added
        self.assertTrue(self.pdf_generator.has_footer)

if __name__ == '__main__':
    unittest.main()
```