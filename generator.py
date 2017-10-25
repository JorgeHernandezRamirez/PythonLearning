import unittest

class GeneratorTest(unittest.TestCase):

    def test_shouldIterateFromGeneratorFunction(self):
        generator = self.getIteratorNumericValues();
        self.assertEqual(next(generator), 0)
        self.assertEqual(next(generator), 1)
        self.assertEqual(next(generator), 2)
        self.assertEqual(next(generator), 3)
        self.assertEqual(next(generator), 4)
        self.assertRaises(StopIteration, next, generator)

    def test_shouldIterateFromGeneratorFunctionLoop(self):
        counter = 0
        for value in self.getIteratorNumericValues():
            self.assertEqual(value, counter)
            counter = counter + 1

    def test_shouldIterateString(self):
        iterator = iter("Jorge")
        self.assertEqual(next(iterator), "J")
        self.assertEqual(next(iterator), "o")
        self.assertEqual(next(iterator), "r")
        self.assertEqual(next(iterator), "g")
        self.assertEqual(next(iterator), "e")

    def test_shouldIterateList(self):
        iterator = iter(list(["1", "2"]))
        self.assertEqual(next(iterator), "1")
        self.assertEqual(next(iterator), "2")


    def getIteratorNumericValues(self):
        for value in range(5):
            yield value

if __name__ == "__main__":
    unittest.main()