import sys
import os
import unittest

# Добавляем путь к директории src в sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from main import get_excessive_letter  # Импорт функции из main.py


class TestGetExcessiveLetter(unittest.TestCase):
    def test_basic_case(self):
        self.assertEqual(get_excessive_letter("abc", "abca"), "a")


if __name__ == "__main__":
    unittest.main()
