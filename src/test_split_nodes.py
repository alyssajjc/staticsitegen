import unittest
from src.split_nodes import split_nodes_delimiter, split_nodes_link, split_nodes_image
from src.textnode import TextNode, TextType


class TestDelimiter(unittest.TestCase):
    def test_inline_code(self):
        node1 = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is another `text` node", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node1, node2], "`", TextType.CODE)
        res1 = TextNode("This is another ", TextType.TEXT)
        res2 = TextNode("text", TextType.CODE)
        res3 = TextNode(" node", TextType.TEXT)
        self.assertEqual(new_nodes, [node1, res1, res2, res3])

    def test_start_of_line_code(self):
        node1 = TextNode("`This` is a text node", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node1], "`", TextType.CODE)
        res1 = TextNode("This", TextType.CODE)
        res2 = TextNode(" is a text node", TextType.TEXT)
        self.assertEqual(new_nodes, [res1, res2])

    def test_multiple_delimiters(self):
        node1 = TextNode("`code1` and `code2`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node1], "`", TextType.CODE)
        res1 = TextNode("code1", TextType.CODE)
        res2 = TextNode(" and ", TextType.TEXT)
        res3 = TextNode("code2", TextType.CODE)
        self.assertEqual(new_nodes, [res1, res2, res3])

    def test_inline_bold(self):
        node1 = TextNode("This is a **bold** text node", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node1], "**", TextType.BOLD)
        res1 = TextNode("This is a ", TextType.TEXT)
        res2 = TextNode("bold", TextType.BOLD)
        res3 = TextNode(" text node", TextType.TEXT)
        self.assertEqual(new_nodes, [res1, res2, res3])

    def test_multiple_bold(self):
        node1 = TextNode("This is a **bold** text **node**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node1], "**", TextType.BOLD)
        res1 = TextNode("This is a ", TextType.TEXT)
        res2 = TextNode("bold", TextType.BOLD)
        res3 = TextNode(" text ", TextType.TEXT)
        res4 = TextNode("node", TextType.BOLD)
        self.assertEqual(new_nodes, [res1, res2, res3, res4])

    def test_inline_italic(self):
        node1 = TextNode("This is an _italic_ text node", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node1], "_", TextType.ITALIC)
        res1 = TextNode("This is an ", TextType.TEXT)
        res2 = TextNode("italic", TextType.ITALIC)
        res3 = TextNode(" text node", TextType.TEXT)
        self.assertEqual(new_nodes, [res1, res2, res3])

    def test_split_link(self):
        node1 = TextNode("[This is a link](https://www.google.com)", TextType.TEXT)
        new_nodes = split_nodes_link([node1])
        res1 = TextNode("This is a link", TextType.LINK, "https://www.google.com")
        self.assertEqual(new_nodes, [res1])

    def test_inline_link(self):
        node1 = TextNode("This is a [link](https://www.google.com) text node", TextType.TEXT)
        new_nodes = split_nodes_link([node1])
        res1 = TextNode("This is a ", TextType.TEXT)
        res2 = TextNode("link", TextType.LINK, "https://www.google.com")
        res3 = TextNode(" text node", TextType.TEXT)
        self.assertEqual(new_nodes, [res1, res2, res3])

    def test_multiple_links(self):
        node1 = TextNode("This is a [link1](https://www.google.com) and [link2](https://www.youtube.com) text node", TextType.TEXT)
        new_nodes = split_nodes_link([node1])
        res1 = TextNode("This is a ", TextType.TEXT)
        res2 = TextNode("link1", TextType.LINK, "https://www.google.com")
        res3 = TextNode(" and ", TextType.TEXT)
        res4 = TextNode("link2", TextType.LINK, "https://www.youtube.com")
        res5 = TextNode(" text node", TextType.TEXT)
        self.assertEqual(new_nodes, [res1, res2, res3, res4, res5])

    def test_no_links(self):
        node1 = TextNode("This is a text node", TextType.TEXT)
        new_nodes = split_nodes_link([node1])
        self.assertEqual(new_nodes, [node1])

    def test_nontext_node(self):
        node1 = TextNode("This is not a text node", TextType.BOLD)
        new_nodes = split_nodes_link([node1])
        self.assertEqual(new_nodes, [node1])

    def test_identical_links(self):
        node1 = TextNode("Go [here](url) and again [here](url)", TextType.TEXT)
        new_nodes =  split_nodes_link([node1])
        res1 = TextNode("Go ", TextType.TEXT)
        res2 = TextNode("here", TextType.LINK, "url")
        res3 = TextNode(" and again ", TextType.TEXT)
        res4 = TextNode("here", TextType.LINK, "url")
        self.assertEqual(new_nodes, [res1, res2, res3, res4])

    def test_inline_image(self):
        node1 = TextNode("Sample: ![This is an image](https://www.google.com/image.png)", TextType.TEXT)
        new_nodes = split_nodes_image([node1])
        res0 = TextNode("Sample: ", TextType.TEXT)
        res1 = TextNode("This is an image", TextType.IMAGE, "https://www.google.com/image.png")
        self.assertEqual(new_nodes, [res0, res1])

    def test_multiple_images(self):
        node1 = TextNode("Sample: ![This is an image](https://www.google.com/image.png) and ![Another image](https://www.google.com/image2.png)", TextType.TEXT)
        new_nodes = split_nodes_image([node1])
        res0 = TextNode("Sample: ", TextType.TEXT)
        res1 = TextNode("This is an image", TextType.IMAGE, "https://www.google.com/image.png")
        res2 = TextNode(" and ", TextType.TEXT)
        res3 = TextNode("Another image", TextType.IMAGE, "https://www.google.com/image2.png")
        self.assertEqual(new_nodes, [res0, res1, res2, res3])

    def test_no_images(self):
        node1 = TextNode("Sample: This is a text node", TextType.TEXT)
        new_nodes = split_nodes_image([node1])
        self.assertEqual(new_nodes, [node1])

    def test_nontext_node_image(self):
        node1 = TextNode("Sample: ![This is not an image](https://www.google.com/image.png)", TextType.BOLD)
        new_nodes = split_nodes_image([node1])
        self.assertEqual(new_nodes, [node1])

    def test_identical_images(self):
        node1 = TextNode("Sample: ![This is an image](https://www.google.com/image.png) and ![This is an image](https://www.google.com/image.png)", TextType.TEXT)
        new_nodes = split_nodes_image([node1])
        res0 = TextNode("Sample: ", TextType.TEXT)
        res1 = TextNode("This is an image", TextType.IMAGE, "https://www.google.com/image.png")
        res2 = TextNode(" and ", TextType.TEXT)
        res3 = TextNode("This is an image", TextType.IMAGE, "https://www.google.com/image.png")
        self.assertEqual(new_nodes, [res0, res1, res2, res3])

if __name__ == '__main__':
    unittest.main()
