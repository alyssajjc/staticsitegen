import unittest
from src.extract_links import extract_markdown_links, extract_markdown_images


class MyTestCase(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches) # add assertion here

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://www.google.com)"
        )
        self.assertListEqual([("link", "https://www.google.com")], matches)

    def test_extract_markdown_links_no_match(self):
        matches = extract_markdown_links(
            "This is text with a link"
        )
        self.assertListEqual([], matches)

    def test_extract_markdown_images_no_match(self):
        matches = extract_markdown_images(
            "This is text with an image"
        )
        self.assertListEqual([], matches)

    def test_extract_markdown_links_multiple(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://www.google.com) and another [link](https://www.youtube.com)"
        )
        self.assertListEqual([("link", "https://www.google.com"), ("link", "https://www.youtube.com")], matches)

    def test_extract_markdown_images_multiple(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png"), ("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

if __name__ == '__main__':
    unittest.main()
