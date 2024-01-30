import unittest
from util.input_validation import check


class TestInputValidation(unittest.TestCase):

    def test_valid_input(self):
        result = check(790, 2235, 4, "2024-01-15T13:00:00Z")
        self.assertEqual(result, (None, ""))

    def test_large_numbers(self):
        result = check(22356700000, 7000000000, 41623789405,
                       "2024-01-31T13:00:00Z")
        self.assertEqual(result, (None, ""))

    def test_lack_param_1(self):
        result = check(None, 2235, 4, "2024-01-15T13:00:00Z")
        self.assertEqual(result,
                         (422, "One or more required parameters are missing."))

    def test_lack_param_2(self):
        result = check(790, None, 4, "2024-01-15T13:00:00Z")
        self.assertEqual(result,
                         (422, "One or more required parameters are missing."))

    def test_lack_param_3(self):
        result = check(790, 2235, None, "2024-01-15T13:00:00Z")
        self.assertEqual(result,
                         (422, "One or more required parameters are missing."))

    def test_lack_param_4(self):
        result = check(790, 2235, 4, None)
        self.assertEqual(result,
                         (422, "One or more required parameters are missing."))

    def test_wrong_type_1(self):
        result = check("a", 2235, 4, "2024-01-15T13:00:00Z")
        self.assertEqual(result, (422, "The cart value must be an integer."))

    def test_wrong_type_2(self):
        result = check(790, "b", "c", "2024-01-15T13:00:00Z")
        self.assertEqual(result,
                         (422, "The delivery distance must be an integer."))

    def test_wrong_type_3(self):
        result = check(790, 2235, "c", "2024-01-15T13:00:00Z")
        self.assertEqual(result,
                         (422, "The number of items must be an integer."))

    def test_wrong_type_4(self):
        result = check(790, 2235, 4, 10122023)
        self.assertEqual(result, (422, "The time parameter must be a string."))

    def test_wrong_format_1(self):
        result = check(-120, 2235, 4, "2024-01-15T13:00:00Z")
        self.assertEqual(result, (422, "The cart value must not be negative."))

    def test_wrong_format_2(self):
        result = check(790, 0, 4, "2024-01-15T13:00:00Z")
        self.assertEqual(result, (
        422, "The delivery distance must be greater than 0."))

    def test_wrong_format_3(self):
        result = check(790, 2235, -2, "2024-01-15T13:00:00Z")
        self.assertEqual(result,
                         (422, "The number of items must be greater than 0."))

    def test_wrong_format_4(self):
        result = check(790, 2235, 4, "2024-01-15T13::00:00Z")
        self.assertEqual(result, (422, "The time must be in ISO 8601 format."))

    def test_wrong_format_5(self):
        result = check(790, 2235, 4, "2024-01-33T13:00:00Z")
        self.assertEqual(result, (422, "The time must be in ISO 8601 format."))

    def test_wrong_format_6(self):
        result = check(790, 2235, 4, "2024-01-33T13:0:00Z")
        self.assertEqual(result, (422, "The time must be in ISO 8601 format."))


if __name__ == '__main__':
    unittest.main()
