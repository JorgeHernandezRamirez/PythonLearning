import unittest


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

    def test_debeUtilizarElMetodoUpdateParaActualizarUnDict(self):
        midictionario = {"a": 1, "b": 2}
        midictionario.update({"a": 2})
        self.assertEqual({"a": 2, "b": 2}, midictionario)

if __name__ == "__main__":
    unittest.main()