import sys
import os
import unittest
from main import get_excessive_letter


sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../src")
    )
)


class TestGetExcessiveLetter(unittest.TestCase):
    def test_basic_case(self):
        self.assertEqual(get_excessive_letter("abc", "abca"), "a")


if __name__ == "__main__":
    unittest.main()
