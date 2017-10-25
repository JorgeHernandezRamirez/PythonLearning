import unittest

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

if __name__ == "__main__":
    unittest.main()