import unittest

class ArgsAndKWardsTest(unittest.TestCase):

    def test_debeDevolverLaListaDeParametros(self):
        self.assertEqual(self.devolverListaParametros("1", "2", "3"), ["1", "2", "3"])

    def test_debeDevolverLaListaDeKeysParametros(self):
        self.assertEqual(self.devolverListaClaveParametros(nombre="Jorge"), ["nombre"])
        self.assertEqual(self.devolverListaClaveParametros(nombre="Jorge", apellidos="Hernandez Ramirez"), ["nombre", "apellidos"])

    def test_debeDevolverLaListaDeParametros(self):
        self.assertEqual(devolverVectorParametros("1", "2", "3"), ["1", "2", "3"])
        self.assertEqual(devolverVectorParametros(*("1", "2", "3")), ["1", "2", "3"])
        devolverVectorParametros(**{"parametro1": "1", "parametro2": "2", "parametro3": "3"})

    def test_debeDevolverElMismoIdQueSePasaComoKwargs(self):
        valorDevuelto = self.ejecutarFuncionCallback(id="1", callback=self.devolverMismoValor)
        self.assertEqual("1", valorDevuelto)

    def devolverListaParametros(self, *argv):
        listaParametrosADevolver = list()
        for parameter in argv:
            listaParametrosADevolver.append(parameter)
        return listaParametrosADevolver;

    def devolverListaClaveParametros(self, **kwargs):
        listaKeysADevolver = list()
        for key, value in kwargs.items():
            listaKeysADevolver.append(key)
        return listaKeysADevolver;

    def ejecutarFuncionCallback(self, **kwargs):
        return kwargs.get("callback")(kwargs.get("id"))

    def devolverMismoValor(self, texto):
        return texto

def devolverVectorParametros(parametro1, parametro2, parametro3):
    return [parametro1, parametro2, parametro3]

if __name__ == "__main__":
    unittest.main()


