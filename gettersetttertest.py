import unittest

# Como en JAVA
# _property es privado y tenemos getter y setter
# El problema que tiene es que no llamamos a instancia.property
class ValorPositivoPrimerCaso:

    def __init__(self, value):
        self.set_value(value)

    def get_value(self):
        return self._value;

    def set_value(self, value):
        if value < 0:
            raise Exception("El valor no puede ser negativo")
        self._value = value;

# Lo mismo que antes pero habilitamos la posibilidad de acceder a través de
# instancia.value
class ValorPositivoSegundoCaso:

    def __init__(self, value):
        self._value = value

    def get_value(self):
        return self._value;

    def set_value(self, value):
        if value < 0:
            raise Exception("El valor no puede ser negativo")
        self._value = value;

    value = property(get_value, set_value)

# Lo mismo que el segundo pero con anotaciones @property
class ValorPositivoTercerCaso:

    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value;

    @value.setter
    def value(self, value):
        if value < 0:
            raise Exception("El valor no puede ser negativo")
        self._value = value;


class GetterSetterTest(unittest.TestCase):

    def test_debeTestearElPrimerCaso(self):
        primerCaso = ValorPositivoPrimerCaso(1)
        self.assertEqual(1, primerCaso.get_value())
        self.assertEqual(1, primerCaso._value) #Acceso al atributo privado
        with self.assertRaises(Exception):
            primerCaso.set_value(-1)

    def test_debeTestearElSegundoCaso(self):
        segundoCaso = ValorPositivoSegundoCaso(1)
        self.assertEqual(1, segundoCaso.get_value())
        self.assertEqual(1, segundoCaso._value) #Acceso al atributo privado
        self.assertEqual(1, segundoCaso.value)  # Acceso al atributo privado
        with self.assertRaises(Exception):
            segundoCaso.set_value(-1)
        with self.assertRaises(Exception):
            segundoCaso.value = -1
        segundoCaso._value = -1
        self.assertEqual(-1, segundoCaso.value)

    def test_debeTestearElTercerCaso(self):
        tercerCaso = ValorPositivoTercerCaso(1)
        self.assertEqual(1, tercerCaso.value)
        self.assertEqual(1, tercerCaso._value) #Acceso al atributo privado
        with self.assertRaises(Exception):
            tercerCaso.value = -1
        tercerCaso._value = -1
        self.assertEqual(-1, tercerCaso.value)

if __name__ == "__main__":
    unittest.main()