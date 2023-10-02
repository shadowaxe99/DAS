import sys
from PyQt5.QtWidgets import QApplication
from src.user_interface import UserInterface
from src.github_api import fetch_repository_code
from src.code_formatter import format_code
from src.pdf_generator import PDFGenerator
from src.config import UI_TEXT_FIELD_ID, UI_MESSAGE_NAME


def convert_to_pdf(repo_url):
    """
    Converts the GitHub repository code to a PDF document.

    Parameters:
    - repo_url (str): The URL of the GitHub repository.
    """
    try:
        # Fetch the repository code
        code = fetch_repository_code(repo_url)

        # Format the code
        formatted_code = format_code(code)

        # Generate the PDF
        pdf_generator = PDFGenerator()
        pdf_generator.generate_pdf(formatted_code)

        # Show success message
        ui = UserInterface()
        ui.window.children[UI_TEXT_FIELD_ID].delete(0, 'end')
        ui.window.children[UI_MESSAGE_NAME].config(text='PDF generated successfully.')

    except Exception as e:
        # Show error message
        ui = UserInterface()
        ui.window.children[UI_MESSAGE_NAME].config(text=str(e))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = UserInterface()
    ui.run()
    sys.exit(app.exec_())
