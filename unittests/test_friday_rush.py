import unittest
from util.friday_rush import check


class TestDistanceFee(unittest.TestCase):

    def test_1(self):
        result = check("2024-02-02T16:54:22Z")
        self.assertEqual(result, True)

    def test_2(self):
        result = check("2023-01-13T18:59:02Z")
        self.assertEqual(result, True)

    def test_3(self):
        result = check("1995-01-20T17:00:22Z")
        self.assertEqual(result, True)

    def test_4(self):
        result = check("1995-01-19T17:00:22Z")
        self.assertEqual(result, False)

    def test_5(self):
        result = check("2004-06-19T16:54:22Z")
        self.assertEqual(result, False)

    def test_6(self):
        result = check("1969-07-05T22:11:05Z")
        self.assertEqual(result, False)

    def test_7(self):
        result = check("1992-10-31T18:10:22Z")
        self.assertEqual(result, False)

    def test_8(self):
        result = check("1995-01-20T19:00:00Z")
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
