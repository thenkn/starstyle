"""
Tests for LNNS module
"""
import unittest
from lnns import add_line_numbers, style_with_stars, lnns


class TestLNNS(unittest.TestCase):
    
    def test_add_line_numbers(self):
        """Test adding line numbers to text."""
        text = "Hello\nWorld"
        expected = "1. Hello\n2. World"
        self.assertEqual(add_line_numbers(text), expected)
    
    def test_add_line_numbers_single_line(self):
        """Test adding line numbers to single line."""
        text = "Hello"
        expected = "1. Hello"
        self.assertEqual(add_line_numbers(text), expected)
    
    def test_style_with_stars(self):
        """Test styling text with stars."""
        text = "Hello"
        result = style_with_stars(text)
        self.assertIn("*", result)
        self.assertIn("Hello", result)
        lines = result.split('\n')
        self.assertEqual(len(lines), 3)  # border, text, border
    
    def test_lnns_both(self):
        """Test LNNS with both line numbers and stars."""
        text = "Hello"
        result = lnns(text, add_numbers=True, add_stars=True)
        self.assertIn("1. Hello", result)
        self.assertIn("*", result)
    
    def test_lnns_numbers_only(self):
        """Test LNNS with only line numbers."""
        text = "Hello\nWorld"
        result = lnns(text, add_numbers=True, add_stars=False)
        self.assertEqual(result, "1. Hello\n2. World")
        self.assertNotIn("*", result)
    
    def test_lnns_stars_only(self):
        """Test LNNS with only stars."""
        text = "Hello"
        result = lnns(text, add_numbers=False, add_stars=True)
        self.assertIn("*", result)
        self.assertIn("Hello", result)
        self.assertNotIn("1.", result)


if __name__ == '__main__':
    unittest.main()
