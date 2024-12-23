import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

import unittest
from main import get_excessive_letter  # Теперь Python сможет найти main.py в папке src.

class TestGetExcessiveLetter(unittest.TestCase):
    def test_basic_case(self):
        self.assertEqual(get_excessive_letter("abc", "abca"), "a")
    
    def test_extra_letter_at_start(self):
        self.assertEqual(get_excessive_letter("abc", "dabc"), "d")
    
    def test_extra_letter_at_middle(self):
        self.assertEqual(get_excessive_letter("abc", "abdc"), "d")
    
    def test_extra_letter_at_end(self):
        self.assertEqual(get_excessive_letter("abc", "abcd"), "d")
    
    def test_unsorted_input(self):
        self.assertEqual(get_excessive_letter("bca", "bcad"), "d")
    
    def test_empty_shorter_string(self):
        self.assertEqual(get_excessive_letter("", "x"), "x")
    
    def test_duplicate_letters(self):
        self.assertEqual(get_excessive_letter("aabb", "aabbb"), "b")
    
    def test_large_case(self):
        shorter = "a" * 1000
        longer = "a" * 999 + "b"
        self.assertEqual(get_excessive_letter(shorter, longer), "b")

if __name__ == "__main__":
    unittest.main()