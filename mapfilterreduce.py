import unittest
from functools import reduce

class MapFilterReduceTest(unittest.TestCase):

    def test_shouldReturnSquaredElements(self):
        squaredElements = list(map(lambda x: x * x, [1, 2, 3]))
        self.assertEqual(squaredElements, [1, 4, 9]);

    def test_shouldFilterPositiveElements(self):
        filteredElements = list(filter(lambda x: x > 0, [-1, 1, -2]))
        self.assertEqual(filteredElements, [1]);

    def test_shouldGetAllSumOfAllElements(self):
        self.assertEqual(6, reduce(lambda x, y: x + y, [1, 2, 3]))

if __name__ == "__main__":
    unittest.main()
