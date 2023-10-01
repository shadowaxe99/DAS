```python
import unittest
from src import code_formatter

class TestCodeFormatter(unittest.TestCase):

    def setUp(self):
        self.formatter = code_formatter.CodeFormatter()

    def test_format_code(self):
        test_code = "def hello_world():\n    print('Hello, world!')"
        expected_output = "1 def hello_world():\n2     print('Hello, world!')"
        self.assertEqual(self.formatter.format_code(test_code), expected_output)

    def test_syntax_highlighting(self):
        test_code = "def hello_world():\n    print('Hello, world!')"
        highlighted_code = self.formatter.syntax_highlighting(test_code)
        self.assertNotEqual(test_code, highlighted_code)

    def test_adjust_font_size(self):
        test_code = "def hello_world():\n    print('Hello, world!')"
        adjusted_code = self.formatter.adjust_font_size(test_code, 14)
        self.assertNotEqual(test_code, adjusted_code)

    def test_adjust_font_style(self):
        test_code = "def hello_world():\n    print('Hello, world!')"
        adjusted_code = self.formatter.adjust_font_style(test_code, 'Courier')
        self.assertNotEqual(test_code, adjusted_code)

if __name__ == '__main__':
    unittest.main()
```