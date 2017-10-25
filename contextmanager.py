import unittest
from contextlib import contextmanager

class MiCustomManager:

    def __init__(self, estado):
        self.estado = estado

    def __enter__(self):
        print("Entrando en el contexto")
        return self.estado

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Saliendo del contexto")
        return True; #Al devolver un True siempre salimos del contexto correctamente. Haya o no haya excepcion

@contextmanager
def openfile(filepath):
    file = open(filepath, "r")
    yield file
    file.close()

class ContextManagerTest(unittest.TestCase):

    def test_debeLlamarAUnCustomContextManagerComoClase(self):
        with MiCustomManager("miestado") as estado:
            self.assertEqual("miestado", estado)

    def test_debeLanzarUnaExcecionLlamarAUnCustomContextManager(self):
        with MiCustomManager("miestado") as estado:
            raise Exception("Mi Excepcion")

    def test_debeLlamarAUnContextManagerComoGeneratorYDecorator(self):
        with openfile("file.txt") as mifichero:
            self.assertEqual("Contenido", mifichero.read())

if __name__ == "__main__":
    unittest.main()