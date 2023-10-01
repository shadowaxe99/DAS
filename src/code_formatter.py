```python
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from src.config import DEFAULT_FONT_SIZE, DEFAULT_FONT_STYLE

class CodeFormatter:
    def __init__(self):
        self.font_size = DEFAULT_FONT_SIZE
        self.font_style = DEFAULT_FONT_STYLE

    def set_font_size(self, size):
        self.font_size = size

    def set_font_style(self, style):
        self.font_style = style

    def format_code(self, code, language):
        lexer = get_lexer_by_name(language)
        formatter = HtmlFormatter(linenos=True, cssclass="source", style=self.font_style)
        formatted_code = highlight(code, lexer, formatter)
        return formatted_code
```