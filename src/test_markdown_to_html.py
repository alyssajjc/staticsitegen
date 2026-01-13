import unittest
from markdown_to_html import markdown_to_html_node


class MyTestCase(unittest.TestCase):
    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here
    
    This is another paragraph with _italic_ text and `code` here
    
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
    ```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_codeblock_variant(self):
        md = """
    ```
    line1
    line2
    
    line4
    ```
        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><pre><code>line1\nline2\n\nline4\n</code></pre></div>")

    def test_unordered_list(self):
        md = """
- list item 1
- list item 2
- list item 3
        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        print(html)
        self.assertEqual(html, "<div><ul><li>list item 1</li><li>list item 2</li><li>list item 3</li></ul></div>")

    def test_ordered_list(self):
        md = """
1. list item 1
2. list item 2
3. list item 3
        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        print(html)
        self.assertEqual(html, "<div><ol><li>list item 1</li><li>list item 2</li><li>list item 3</li></ol></div>")

    def test_headers(self):
        md = """
# header 1
## header 2
###### header 6

####### not a header
        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><h1>header 1</h1><h2>header 2</h2><h6>header 6</h6><p>####### not a header</p></div>")

    def test_quote_block(self):
        md = """
> quote goes here
> and here
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><blockquote>quote goes here and here</blockquote></div>")

    def test_empty_div(self):
        md = ""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div></div>")

if __name__ == '__main__':
    unittest.main()
