import unittest
from unittest.mock import patch

from utils import ask_number, check_number, count_symbols, count_vowels, create_name, divide


class TestCheckNumber(unittest.TestCase):
    def test_valid_number(self):
        self.assertEqual(5, check_number("5"))
        self.assertEqual(42, check_number(" 42 "))

    def test_boundary(self):
        self.assertEqual(1, check_number("1"))
        with self.assertRaises(ValueError):
            check_number("0")

    def test_invalid_number(self):
        for value in ["-3", "abc", "2.5", ""]:
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    check_number(value)

    def test_create_name(self):
        self.assertEqual("Маркіян", create_name("Маркіян"))
        with self.assertRaises(ValueError):
            create_name("")


class TestFunctions(unittest.TestCase):
    def test_count_symbols(self):
        self.assertEqual(3, count_symbols("abc"))
        self.assertEqual(0, count_symbols(""))

    def test_divide(self):
        self.assertEqual(2, divide(10, 5))

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)


class TestCountVowels(unittest.TestCase):
    def test_english(self):
        self.assertEqual(2, count_vowels("hello"))

    def test_uppercase(self):
        self.assertEqual(5, count_vowels("AEIOU"))

    def test_no_vowels(self):
        self.assertEqual(0, count_vowels("rhythm"))

    def test_empty_string(self):
        self.assertEqual(0, count_vowels(""))

    def test_digits(self):
        self.assertEqual(0, count_vowels("12345"))
        self.assertEqual(2, count_vowels("a1b2e3"))

    def test_ukrainian(self):
        self.assertEqual(3, count_vowels("Маркіян"))
        self.assertEqual(5, count_vowels("їжак є юла"))


class TestAskNumber(unittest.TestCase):
    @patch("builtins.input", return_value="5")
    def test_ask_number(self, mock_input):
        self.assertEqual(5, ask_number())
        mock_input.assert_called_once_with("Введіть додатне число: ")

    @patch("builtins.input", return_value="-1")
    def test_ask_number_invalid(self, mock_input):
        with self.assertRaises(ValueError):
            ask_number()
        mock_input.assert_called_once()


if __name__ == "__main__":
    unittest.main(verbosity=2)
