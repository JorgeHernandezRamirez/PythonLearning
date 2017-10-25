import unittest

class ObjectIntrospectionTest(unittest.TestCase):

    def test_debeRealizarLaIntrospeccionConDir(self):
        self.assertEqual(['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'],
                         dir([1, 2, 3]))

    def test_debeDevolverElTipoDeLosElementos(self):
        self.assertEqual(type([]), list)
        self.assertEqual(type({}), dict)
        self.assertEqual(type(()), tuple)
        self.assertEqual(type({0}), set)
        self.assertEqual(type(""), str)
        self.assertEqual(type(1), int)

    def test_debeSerDistintosLasSiguientesReferencias(self):
        self.assertNotEqual(id(1), id(2))
        self.assertNotEqual(id(""), id("1"))
        lista = [1, 2, 3]
        self.assertNotEqual(id(lista), id([1, 2, 3]))

    def test_debeSerIgualLasSiguientesReferencias(self):
        self.assertEqual(id(1), id(1))
        self.assertEqual(id(""), id(""))
        lista = [1, 2, 3]
        listaAux = lista
        self.assertEqual(id(lista), id(listaAux))

if __name__ == "__main__":
    unittest.main()
