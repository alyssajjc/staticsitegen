import unittest
from src.generate_webpage import extract_title


class MyTestCase(unittest.TestCase):
    def test_extract_title(self):
        self.assertEqual(extract_title("# Test"), "Test")

    def test_extract_title_no_heading(self):
        self.assertRaises(Exception, extract_title, "Test")

    def test_extract_title_multiline(self):
        self.assertEqual(extract_title("# Test\nTest"), "Test")

    def test_extract_title_multiple_headings(self):
        self.assertEqual(extract_title("# Test\n## Test"), "Test")

    def test_extract_title_bold_in_title(self):
        self.assertEqual(extract_title("# **Test**"), "**Test**")


if __name__ == '__main__':
    unittest.main()
