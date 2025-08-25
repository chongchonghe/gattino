import unittest
import src.parser as parser


class TestParser(unittest.TestCase):
    def test_extract_first_code_block(self):
        text = "Some text\n```\ncode block\n```\nmore text"
        result = parser.extract_first_code_block(text)
        self.assertEqual(result, "code block")

    def test_extract_first_code_block_with_no_blocks(self):
        text = "Some text without code blocks"
        result = parser.extract_first_code_block(text)
        self.assertEqual(result, "")

    def test_extract_first_code_block_with_bash(self):
        text = "Some text\n```bash\ncode block\n```\nmore text"
        result = parser.extract_first_code_block(text)
        self.assertEqual(result, "code block")

    def test_extract_multiline_command(self):
        text = "```\ncd /tmp\nls -la\necho done\n```"
        result = parser.extract_first_code_block(text)
        self.assertEqual(result, "cd /tmp\nls -la\necho done")

    def test_extract_preserves_internal_formatting(self):
        text = "```\nfor file in *.txt; do\n    echo $file\ndone\n```"
        result = parser.extract_first_code_block(text)
        expected = "for file in *.txt; do\n    echo $file\ndone"
        self.assertEqual(result, expected)

    def test_extract_strips_outer_whitespace_only(self):
        text = "```\n\n  ls -la  \n\n```"
        result = parser.extract_first_code_block(text)
        self.assertEqual(result, "ls -la")

    def test_extract_handles_empty_code_block(self):
        text = "```\n\n```"
        result = parser.extract_first_code_block(text)
        self.assertEqual(result, "")


if __name__ == '__main__':
    unittest.main()
