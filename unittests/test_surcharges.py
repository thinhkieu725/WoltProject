import unittest
from util.surcharges import calculate


class TestSurcharges(unittest.TestCase):

    def test_1(self):
        result = calculate(700, 15)
        self.assertEqual(result, 970)

    def test_2(self):
        result = calculate(1260, 3)
        self.assertEqual(result, 0)

    def test_3(self):
        result = calculate(10000000000000000, 12364132704402347)
        self.assertEqual(result, 618206635220117270)

    def test_4(self):
        result = calculate(10, 1)
        self.assertEqual(result, 990)

    def test_5(self):
        result = calculate(25000, 7)
        self.assertEqual(result, 150)

    def test_6(self):
        result = calculate(1000, 4)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
