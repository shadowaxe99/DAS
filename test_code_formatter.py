import unittest
from src.code_formatter import format_code

class TestCodeFormatter(unittest.TestCase):
    def test_format_code(self):
        code = 'def hello():\n    print("Hello, World!")'
        language = 'python'
        expected_result = '<span class="k">def</span> <span class="nf">hello</span><span class="p">():</span>\n    <span class="k">print</span><span class="p">(</span><span class="s">"Hello, World!"</span><span class="p">)</span>'
        result = format_code(code, language)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
