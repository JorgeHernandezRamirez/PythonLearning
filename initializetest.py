import unittest
from collections import Counter


class ClassToInitialize(object):
    def __init__(self, id, name):
        self.__dict__.update({k: v for k, v in locals().items() if k != 'self'})

class ClassToInitializeArgs(object):
    def __init__(self, **kargs):
        self.__dict__.update({k: v for k, v in kargs.items() if k != 'self'})

def metodo(*args):
    for value in args:
        print(value)

class InitializeTest(unittest.TestCase):

    def test_debeInicializarLaInstanciaCorrectamente(self):
        instancia = ClassToInitialize(id = "1", name = "Jorge")
        self.assertEqual("1", instancia.id)
        self.assertEqual("Jorge", instancia.name)

    def test_debeInicializarLaInstanciaCorrectamenteArgs(self):
        instancia = ClassToInitializeArgs(id = "1", name = "Jorge")
        self.assertEqual("1", instancia.id)
        self.assertEqual("Jorge", instancia.name)

if __name__ == "__main__":
    unittest.main()