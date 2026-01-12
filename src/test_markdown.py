import unittest
from block import markdown_to_blocks


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


if __name__ == '__main__':
    unittest.main()
