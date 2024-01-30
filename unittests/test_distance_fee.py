import unittest
from util.distance_fee import calculate


class TestDistanceFee(unittest.TestCase):

    def test_over_1000(self):
        result = calculate(2235)
        self.assertEqual(result, 500)

    def test_under_1000(self):
        result = calculate(700)
        self.assertEqual(result, 200)

    def test_under_500(self):
        result = calculate(352)
        self.assertEqual(result, 200)

    def test_1000(self):
        result = calculate(1000)
        self.assertEqual(result, 200)

    def test_1500(self):
        result = calculate(1500)
        self.assertEqual(result, 300)

    def test_large_number(self):
        result = calculate(90000000000)
        self.assertEqual(result, 18000000000)


if __name__ == '__main__':
    unittest.main()
