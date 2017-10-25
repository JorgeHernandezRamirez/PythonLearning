import unittest

class ComprehensionsTest(unittest.TestCase):

    def test_debeSerIgualElConjuntoDeListas(self):
        self.assertEqual([0, 1, 2], [x for x in range(3)])
        self.assertEqual([1, 2], [x for x in range(3) if x > 0])
        self.assertEqual([1, 4], [x * x for x in range(3) if x > 0])

    def test_debeSerIgualElConjuntoDeConjuntos(self):
        self.assertEqual({0, 1, 2}, {x for x in range(3)})
        self.assertEqual({1, 2}, {x for x in range(3) if x > 0})
        self.assertEqual({1, 4}, {x * x for x in range(3) if x > 0})

    def test_debeSerIgualElConjuntoDeDict(self):
        self.assertEqual({0: 0, 1: 2, 2: 4},{x: x * 2 for x in range(3)})
        self.assertEqual({1: 2, 2: 4}, {x: x * 2 for x in range(3) if x > 0})
        midictionary = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
        midictionaryFrequency = {
            k.lower(): midictionary.get(k.lower(), 0) + midictionary.get(k.upper(), 0) #Si no lo encuentra es cero
            for k in midictionary.keys()
        }
        self.assertEqual({'a': 17, 'z': 3, 'b': 34}, midictionaryFrequency)


if __name__ == "__main__":
    unittest.main()