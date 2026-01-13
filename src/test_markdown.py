import unittest
from block import markdown_to_blocks, block_to_block_type, BlockType


class MarkdownToBlocks(unittest.TestCase):
    def test_simple_markdown(self):
        blocks = markdown_to_blocks("This is a test\n\nThis is another test")
        self.assertListEqual(blocks, ["This is a test", "This is another test"])

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_whitespace(self):
        md = """

   First block with leading spaces

Second block

Third block line 1
Third block line 2   

"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "First block with leading spaces",
                "Second block",
                "Third block line 1\nThird block line 2",
            ],
        )

    def test_markdown_to_blocks_extra_lines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type(self):
        self.assertEqual(block_to_block_type("This is a test"), BlockType.PARAGRAPH)

    def test_block_to_block_type_code(self):
        self.assertEqual(block_to_block_type("```\nprint('Hello World')\n```"), BlockType.CODE)

    def test_block_to_block_type_heading(self):
        self.assertEqual(block_to_block_type("# This is a heading"), BlockType.HEADING)

    def test_block_to_block_type_heading2(self):
        self.assertEqual(block_to_block_type("## This is a heading"), BlockType.HEADING)

    def test_block_to_block_type_heading3(self):
        self.assertEqual(block_to_block_type("### This is a heading"), BlockType.HEADING)

    def test_block_to_block_type_heading4(self):
        self.assertEqual(block_to_block_type("#### This is a heading\nAnd continued"), BlockType.HEADING)

    def test_block_to_block_type_heading5(self):
        self.assertEqual(block_to_block_type("##### This is a heading\nAnd continued"), BlockType.HEADING)

    def test_block_to_block_type_heading6(self):
        self.assertEqual(block_to_block_type("###### This is a heading\nAnd continued"), BlockType.HEADING)

    def test_block_to_block_type_heading_invalid(self):
        self.assertEqual(block_to_block_type("####### This is not a heading"), BlockType.PARAGRAPH)

    def test_block_to_block_type_quote(self):
        self.assertEqual(block_to_block_type("> This is a quote"), BlockType.QUOTE)

    def test_block_to_block_type_multiline_quote(self):
        self.assertEqual(block_to_block_type("> This is a quote\n> And continued"), BlockType.QUOTE)

    def test_block_to_block_type_code_missing_end(self):
        self.assertEqual(block_to_block_type("```python\nprint('Hello World"), BlockType.PARAGRAPH)

    def test_block_to_block_type_unordered_list(self):
        self.assertEqual(block_to_block_type("- This is a list"), BlockType.UNORDERED_LIST)

    def test_block_to_block_type_ordered_list(self):
        self.assertEqual(block_to_block_type("1. This is a list"), BlockType.ORDERED_LIST)

    def test_block_to_block_type_ordered_list_of_three(self):
        self.assertEqual(block_to_block_type("1. This is a list\n2. And another item\n3. And the last one"), BlockType.ORDERED_LIST)

    def test_block_to_block_type_unordered_list_of_three(self):
        self.assertEqual(block_to_block_type("- This is a list\n- And another item\n- And the last one"), BlockType.UNORDERED_LIST)

    def test_block_to_block_type_mixed_list(self):
        self.assertEqual(block_to_block_type("1. This is a list\n- And another item"), BlockType.PARAGRAPH)

if __name__ == '__main__':
    unittest.main()
