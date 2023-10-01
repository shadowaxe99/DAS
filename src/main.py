```python
import sys
from PyQt5.QtWidgets import QApplication
from src.user_interface import MainWindow
from src.github_api import GitHubAPI
from src.code_formatter import CodeFormatter
from src.pdf_generator import PDFGenerator
from src.config import Config
from src.utils import Utils

class Main:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = MainWindow()
        self.github_api = GitHubAPI()
        self.code_formatter = CodeFormatter()
        self.pdf_generator = PDFGenerator()
        self.config = Config()
        self.utils = Utils()

    def run(self):
        self.window.show()
        self.window.repo_link_input.textChanged.connect(self.handle_input_change)
        sys.exit(self.app.exec_())

    def handle_input_change(self, text):
        if self.utils.validate_github_url(text):
            repo_code = self.github_api.fetch_code(text)
            formatted_code = self.code_formatter.format_code(repo_code)
            pdf_path = self.pdf_generator.generate_pdf(formatted_code)
            self.window.show_message(f"PDF generated at {pdf_path}")
        else:
            self.window.show_message("Invalid GitHub URL")

if __name__ == "__main__":
    main = Main()
    main.run()
```