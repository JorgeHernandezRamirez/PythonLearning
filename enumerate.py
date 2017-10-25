import unittest

class EnumerateTest(unittest.TestCase):

    def test_shouldReturnTupleCounterValueUsingEnumerate(self):
        self.assertEquals([(0, 1),(1, 2), (2, 3)], list(enumerate([1, 2, 3])))

    def test_shouldLoopAndEnumerate(self):
        for count, value in enumerate(range(5)):
            self.assertEqual(count, value)

if __name__ == "__main__":
    unittest.main()
