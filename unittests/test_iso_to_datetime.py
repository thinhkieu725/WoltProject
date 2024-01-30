import unittest
from datetime import datetime
from util.iso_to_datetime import convert


class TestDistanceFee(unittest.TestCase):

    def test_1(self):
        result = convert("2024-01-31T23:59:59Z")
        test_datetime_1 = datetime(2024, 1, 31, 23, 59, 59)
        self.assertEqual(result, test_datetime_1)

    def test_2(self):
        result = convert("1961-02-19T06:30:55Z")
        test_datetime_2 = datetime(1961, 2, 19, 6, 30, 55)
        self.assertEqual(result, test_datetime_2)

    def test_3(self):
        result = convert("2023-05-30T07:01:23Z")
        test_datetime_3 = datetime(2023, 5, 30, 7, 1, 23)
        self.assertEqual(result, test_datetime_3)


if __name__ == '__main__':
    unittest.main()
