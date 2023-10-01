```python
from fpdf import FPDF
from src.config import Config

class PDFGenerator:
    def __init__(self):
        self.pdf = FPDF()

    def set_header(self, repo_name, owner):
        self.pdf.set_font('Arial', 'B', 12)
        self.pdf.cell(0, 10, f'Repository: {repo_name} | Owner: {owner}', 0, 1, 'C')

    def set_footer(self):
        self.pdf.set_y(-15)
        self.pdf.set_font('Arial', 'I', 8)
        self.pdf.cell(0, 10, 'Page %s' % self.pdf.page_no(), 0, 0, 'C')

    def add_toc(self, directory_structure):
        self.pdf.add_page()
        self.pdf.set_font('Arial', 'B', 12)
        self.pdf.cell(0, 10, 'Table of Contents', 0, 1, 'C')
        self.pdf.set_font('Arial', '', 12)
        for dir in directory_structure:
            self.pdf.cell(0, 10, dir, 0, 1, 'L')

    def add_code(self, code):
        self.pdf.add_page()
        self.pdf.set_font('Courier', '', 10)
        self.pdf.multi_cell(0, 10, code)

    def generate_pdf(self, repo_name, owner, directory_structure, code):
        self.set_header(repo_name, owner)
        self.add_toc(directory_structure)
        self.add_code(code)
        self.set_footer()
        self.pdf.output(Config.PDF_OUTPUT_PATH, 'F')
```