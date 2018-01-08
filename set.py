import unittest

from collections import Counter


class SetTest(unittest.TestCase):

    def test_debeContener1ElementoLaLista(self):
        listaElementos = set([1, 1, 1])
        self.assertEqual(1, len(listaElementos))
        self.assertEqual(1, len({1, 1, 1}))

    def test_debeDevolverLosElementosComunes(self):
        listaElementosComunes = set([1, 2, 3]).intersection([1, 2])
        self.assertEqual({1, 2}, listaElementosComunes)
        self.assertEqual([1, 2], list(listaElementosComunes))

    def test_debeDevolverLosElementosNoComunes(self):
        listaElementosComunes = set([1, 2, 3]).difference([1, 2])
        self.assertEqual({3}, listaElementosComunes)

    def test_debeIterarSobreLaLista(self):
        iteradorLista = iter({1, 2, 3})
        self.assertEqual(1, next(iteradorLista))
        self.assertEqual(2, next(iteradorLista))
        self.assertEqual(3, next(iteradorLista))
        self.assertRaises(StopIteration, next, iteradorLista) #Primera forma de capturar una excepción
        with self.assertRaises(StopIteration): #Segunda forma de capturar una excepcion
            next(iteradorLista)

    def test_debeDevolverUnaSublista(self):
        self.assertEqual([], [1, 2, 3, 4][:0])
        self.assertEqual([1], [1, 2, 3, 4][:1])
        self.assertEqual([1, 2], [1, 2, 3, 4][:2])
        self.assertEqual([1, 2, 3], [1, 2, 3, 4][:3])
        self.assertEqual([1, 2, 3, 4], [1, 2, 3, 4][:4])
        self.assertEqual([1, 2, 3, 4], [1, 2, 3, 4][:5])

    def test_prueba(self):
        self.assertEqual(duplicate_count("abcde"), 0)
        self.assertEqual(duplicate_count("abcdea"), 1)
        self.assertEqual(duplicate_count("indivisibility"), 1)
        self.assertEqual(duplicate_count("aabbcde"), 2)
        self.assertEqual(duplicate_count("Indivisibilities"), 2)
        self.assertEqual(duplicate_count("ABBA"), 2)

    def test_prueba(self):
        print(self.arithmetic_sequence_elements(1, 2, 5))

    def arithmetic_sequence_elements(self, a, r, n):
        return ", ".join(list(map(lambda x: str(a + r * x), range(n))))


def duplicate_count(text):
    characterlist = list(iter(text.lower()))
    lista = {k: v for k, v in Counter(characterlist).items() if v > 1}
    return len(lista)


if __name__ == "__main__":
    unittest.main()