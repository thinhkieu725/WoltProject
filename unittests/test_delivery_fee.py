import unittest
from util.delivery_fee import calculate


class TestDeliveryFee(unittest.TestCase):

    def test_1(self):
        result = calculate(790, 2235, 4, "2024-01-15T13:00:00Z")
        self.assertEqual(result, 710)

    def test_2(self):
        result = calculate(100000000000, 30000, 12304512348572310, "2024-02-02T18:00:00Z")
        self.assertEqual(result, 0)

    def test_3(self):
        result = calculate(10, 200, 1, "2022-10-06T11:00:00Z")
        self.assertEqual(result, 1190)

    def test_4(self):
        result = calculate(1000, 1000, 4, "2024-01-15T13:00:00Z")
        self.assertEqual(result, 200)

    def test_5(self):
        result = calculate(20000, 3000, 13, "2024-01-26T15:00:00Z")
        self.assertEqual(result, 0)

    def test_6(self):
        result = calculate(700, 800, 4, "2024-01-26T18:59:59Z")
        self.assertEqual(result, 600)


if __name__ == '__main__':
    unittest.main()
