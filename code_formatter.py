from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from src.config import DEFAULT_FONT_SIZE, DEFAULT_FONT_STYLE


def format_code(code, language):
    """
    Formats the code using syntax highlighting.

    Parameters:
    - code (str): The code to be formatted.
    - language (str): The programming language of the code.

    Returns:
    - str: The formatted code.
    """
    lexer = get_lexer_by_name(language)
    formatter = HtmlFormatter(linenos=True, cssclass='source', style=DEFAULT_FONT_STYLE)
    formatted_code = highlight(code, lexer, formatter)
    return formatted_code
