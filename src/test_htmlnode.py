import unittest
from htmlnode import HTMLNode

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