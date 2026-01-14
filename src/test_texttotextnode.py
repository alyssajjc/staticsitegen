import unittest
from src.split_nodes import text_to_textnodes
from src.textnode import TextNode, TextType


class TestTextToNode(unittest.TestCase):
    def test_basic_text(self):
        nodes = text_to_textnodes("This is a basic text")
        self.assertEqual(nodes, [TextNode("This is a basic text", TextType.TEXT)])

    def test_text_with_italics(self):
        nodes = text_to_textnodes("This is a _italics_ text")
        self.assertEqual(nodes, [TextNode("This is a ", TextType.TEXT), TextNode("italics", TextType.ITALIC), TextNode(" text", TextType.TEXT)])

    def test_text_with_bold(self):
        nodes = text_to_textnodes("This is a **bold** text")
        self.assertEqual(nodes, [TextNode("This is a ", TextType.TEXT), TextNode("bold", TextType.BOLD), TextNode(" text", TextType.TEXT)])

    def test_text_with_links(self):
        nodes = text_to_textnodes("This is a [link](https://www.google.com) text")
        self.assertEqual(nodes, [TextNode("This is a ", TextType.TEXT), TextNode("link", TextType.LINK, "https://www.google.com"), TextNode(" text", TextType.TEXT)])

    def test_text_with_images(self):
        nodes = text_to_textnodes("This is a ![image](https://www.google.com/image.png) text")
        self.assertEqual(nodes, [TextNode("This is a ", TextType.TEXT), TextNode("image", TextType.IMAGE, "https://www.google.com/image.png"), TextNode(" text", TextType.TEXT)])

    def test_text_with_code(self):
        nodes = text_to_textnodes("This is a `code` text")
        self.assertEqual(nodes, [TextNode("This is a ", TextType.TEXT), TextNode("code", TextType.CODE), TextNode(" text", TextType.TEXT)])

    def test_text_with_multiple_delimiters(self):
        nodes = text_to_textnodes("This is a **bold** `code` text")
        self.assertEqual(nodes, [TextNode("This is a ", TextType.TEXT), TextNode("bold", TextType.BOLD), TextNode(" ", TextType.TEXT), TextNode("code", TextType.CODE), TextNode(" text", TextType.TEXT)])

    def test_text_with_all_delimiters(self):
        nodes = text_to_textnodes("This is a **bold** _italics_ `code` text")
        self.assertEqual(nodes, [TextNode("This is a ", TextType.TEXT), TextNode("bold", TextType.BOLD), TextNode(" ", TextType.TEXT), TextNode("italics", TextType.ITALIC), TextNode(" ", TextType.TEXT), TextNode("code", TextType.CODE), TextNode(" text", TextType.TEXT)])

    def test_empty_string(self):
        nodes = text_to_textnodes("")
        self.assertEqual(nodes, [])

    def test_text_with_code_and_image(self):
        nodes = text_to_textnodes("This is a `code` ![image](https://www.google.com/image.png) text")
        self.assertEqual(nodes, [TextNode("This is a ", TextType.TEXT), TextNode("code", TextType.CODE), TextNode(" ", TextType.TEXT), TextNode("image", TextType.IMAGE, "https://www.google.com/image.png"), TextNode(" text", TextType.TEXT)])

    def test_text_with_link_and_image(self):
        nodes = text_to_textnodes("This is a [link](https://www.google.com) ![image](https://www.google.com/image.png) text")
        self.assertEqual(nodes, [TextNode("This is a ", TextType.TEXT), TextNode("link", TextType.LINK, "https://www.google.com"), TextNode(" ", TextType.TEXT), TextNode("image", TextType.IMAGE, "https://www.google.com/image.png"), TextNode(" text", TextType.TEXT)])

    def test_text_with_all_delimiters_and_links(self):
        nodes = text_to_textnodes("This is a **bold** _italics_ `code` [link](https://www.google.com) ![image](https://www.google.com/image.png) text")
        self.assertEqual(nodes, [TextNode("This is a ", TextType.TEXT), TextNode("bold", TextType.BOLD), TextNode(" ", TextType.TEXT), TextNode("italics", TextType.ITALIC), TextNode(" ", TextType.TEXT), TextNode("code", TextType.CODE), TextNode(" ", TextType.TEXT), TextNode("link", TextType.LINK, "https://www.google.com"), TextNode(" ", TextType.TEXT), TextNode("image", TextType.IMAGE, "https://www.google.com/image.png"), TextNode(" text", TextType.TEXT)])

    def test_multiple_links_with_bold(self):
        nodes = text_to_textnodes("**This is a **[link1](https://www.google.com) and [link2](https://www.youtube.com) text")
        self.assertEqual(nodes, [TextNode("This is a ", TextType.BOLD), TextNode("link1", TextType.LINK, "https://www.google.com"), TextNode(" and ", TextType.TEXT), TextNode("link2", TextType.LINK, "https://www.youtube.com"), TextNode(" text", TextType.TEXT)])


if __name__ == '__main__':
    unittest.main()
