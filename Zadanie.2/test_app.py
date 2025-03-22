import unittest
from app import is_valid_email, calculate_area, process_list, convert_date_format, is_palindrome


class TestAppFunctions(unittest.TestCase):
    def test_is_valid_email(self):
        self.assertTrue(is_valid_email("test@example.com"))
        self.assertTrue(is_valid_email("user.name+tag+sorting@example.com"))
        self.assertFalse(is_valid_email("invalid-email"))
        self.assertFalse(is_valid_email("@missingusername.com"))

    def test_calculate_area(self):
        self.assertAlmostEqual(calculate_area("circle", radius=3), 28.27431)
        self.assertEqual(calculate_area("square", side=4), 16)
        self.assertEqual(calculate_area("rectangle", width=3, height=5), 15)
        with self.assertRaises(ValueError):
            calculate_area("triangle", base=3, height=4)

    def test_process_list(self):
        self.assertEqual(process_list([1, 2, 3, 4, 5], "filter_even"), [2, 4])
        self.assertEqual(process_list([5, 3, 1, 4, 2], "sort"), [1, 2, 3, 4, 5])
        with self.assertRaises(ValueError):
            process_list([1, 2, 3], "unknown_operation")

    def test_convert_date_format(self):
        self.assertEqual(convert_date_format("15-03-2025", "%d-%m-%Y", "%Y/%m/%d"), "2025/03/15")
        with self.assertRaises(ValueError):
            convert_date_format("2025-03-15", "%d-%m-%Y", "%Y/%m/%d")

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("Ala"))
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(is_palindrome("Hello"))


if __name__ == "__main__":
    unittest.main()
