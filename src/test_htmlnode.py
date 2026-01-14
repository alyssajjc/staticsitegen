import unittest
from src.htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(tag="div", props={"class": "test"})
        self.assertEqual(node.props_to_html(), " class=\"test\"")
        node2 = HTMLNode(tag="div", props={"class": "test", "id": "test-id"})
        self.assertEqual(node2.props_to_html(), " class=\"test\" id=\"test-id\"")
        node3 = HTMLNode(tag="div")
        self.assertEqual(node3.props_to_html(), "")
        node4 = HTMLNode(tag="div", value="test", children=["test", "test2"], props={"class": "test"})
        self.assertEqual(node4.props_to_html(), " class=\"test\"")

    def test_repr(self):
        node = HTMLNode(tag="div", value="test", children=["test", "test2"], props={"class": "test"})
        self.assertEqual(repr(node), "Tag: div, Value: test, Children: ['test', 'test2'], Props: {'class': 'test'}")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        node2 = LeafNode("p", None)
        self.assertRaises(ValueError, node2.to_html)
        node3 = LeafNode("p", "Hello, world!", props={"class": "test"})
        self.assertEqual(node3.to_html(), "<p class=\"test\">Hello, world!</p>")
        node4 = LeafNode("p", None, props={"class": "test"})
        self.assertRaises(ValueError, node4.to_html)

    def test_leaf_repr(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(repr(node), "Tag: p, Value: Hello, world!, Props: None")
        node2 = LeafNode("p", "test", props={"class": "test"})
        self.assertEqual(repr(node2), "Tag: p, Value: test, Props: {'class': 'test'}")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_no_children(self):
        parent_node = ParentNode("div", [])
        self.assertEqual(parent_node.to_html(), "<div></div>")

    def test_to_html_with_no_tag(self):
        node = ParentNode(None, "test")
        self.assertRaises(ValueError, node.to_html)

    def test_to_html_grandparent_with_multiple_grandchildren(self):
        grandchild_node1 = LeafNode("b", "grandchild1")
        grandchild_node2 = LeafNode("b", "grandchild2")
        grandchild_node3 = LeafNode("b", "grandchild3")
        child_node = ParentNode("span", [grandchild_node1, grandchild_node2, grandchild_node3])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild1</b><b>grandchild2</b><b>grandchild3</b></span></div>",
        )

    def test_to_html_grandparent_with_two_children(self):
        grandchild_node1 = LeafNode("b", "grandchild1")
        child_node1 = ParentNode("span", [grandchild_node1])
        child_node2 = LeafNode("span", "child2")
        parent_node = ParentNode("div", [child_node1, child_node2])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild1</b></span><span>child2</span></div>")

if __name__ == "__main__":
    unittest.main()