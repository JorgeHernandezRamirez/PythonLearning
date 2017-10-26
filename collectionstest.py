import collections
import unittest

from dto.species import Species

"""
defaultdict
OrderedDict
Counter
deque
namedtuple
enum.Enum
"""
class CollectionsTest(unittest.TestCase):

    def test_debeAnadirListaValoresADict(self):
        midictionario = {1: [1, 2, 3]}
        self.assertEqual([1, 2, 3], midictionario.get(1))
        midictionario[1].append(4)
        self.assertEqual([1, 2, 3, 4], midictionario.get(1))

    def test_debeAccederALosValoresDelDiccionario(self):
        diccionarioPersona = {"id": "1", "nombre": "Jorge"}
        self.assertEqual("Jorge", diccionarioPersona["nombre"])
        self.assertEqual("Jorge", diccionarioPersona.get("nombre"))
        self.assertEqual(None, diccionarioPersona.get("apellidos"))
        self.assertEqual("Hernández", diccionarioPersona.get("apellidos", "Hernández"))
        diccionarioPersona["apellidos"] = "Hernández"
        self.assertEqual("Hernández", diccionarioPersona.get("apellidos"))
        diccionarioPersona.setdefault("calle", "María Tubau")
        self.assertEqual("María Tubau", diccionarioPersona.get("calle"))

    def test_debeLanzarExcepcionSiAccedoConDosVariablesAlDiccionario(self):
        midiccionario = {}
        midiccionario["key1"] = {}
        midiccionario["key1"]["key2"] = "valor1"
        self.assertEqual(midiccionario["key1"]["key2"], "valor1")
        with self.assertRaises(KeyError):
            midiccionario["key12"]["key12"] = "valor1"

    def test_debeAnadirListaValoresADefaultDict(self):
        midefaultdict = collections.defaultdict(list)
        self.appendToDefaultDict(midefaultdict, 1, 1)
        self.appendToDefaultDict(midefaultdict, 1, 2)
        self.appendToDefaultDict(midefaultdict, 1, 3)
        self.assertEqual([1, 2, 3], midefaultdict.get(1))

    def test_debeAsignarCorrectamenteNKeysEnElDefaultDict(self):
        tree = lambda: collections.defaultdict(tree)
        midiccionario = tree()
        midiccionario["key1"]["key2"] = "valor1"
        self.assertEqual(midiccionario["key1"]["key2"], "valor1")

    def test_debeObtenerElementosEnOrdenEnUnaLista(self):
        self.imprimirDict(collections.OrderedDict([("Red", 198), ("Green", 170), ("Blue", 160)])) #Orden predecible
        self.imprimirDict(collections.OrderedDict({"Red" : 198, "Green" : 170, "Blue" : 160})) #Orden predecible
        self.imprimirDict({"Red" : 198, "Green" : 170, "Blue" : 160}) #Orden impredecible

    def test_debeDevolverElNumeroDeVecesQueAparecenLasPersonas(self):
        #Esto es como hacer un groupby
        mitupla = (("Jorge", 1), ("Jose", 2), ("Ana", 3), ("Jorge", 1))
        micounter = collections.Counter(key for key, value in mitupla)
        self.assertEqual({"Jorge": 2, "Jose": 1, "Ana": 1}, micounter)

    def test_debeContarElNumeroLineasDistintasEnUnFichero(self):
        #Esto es como hacer un groupby
        with open("counterfile.txt") as file:
            self.assertEqual({"Jorge\n": 2, "Jose\n": 1, "Ana\n": 1}, collections.Counter(file))

    def test_debeComportarseComoUnaPila(self):
        mipila = collections.deque()
        mipila.append(1)
        mipila.append(2)
        self.assertEqual(2, len(mipila))
        self.assertEqual(2, mipila.pop())
        self.assertEqual(1, mipila.pop())

    def test_debeComportarseComoUnaCola(self):
        micola = collections.deque()
        micola.append(1)
        micola.append(2)
        self.assertEqual(2, len(micola))
        self.assertEqual(1, micola.popleft())
        self.assertEqual(2, micola.popleft())

    def test_debeExtenderUnObjectoDeQueue(self):
        mideque = collections.deque([1, 2, 3, 4, 5])
        mideque.extendleft([0])
        mideque.extend([6, 7, 8])
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8], list(mideque))

    def test_debeTestearElObjetoNamedTupled(self):
        Persona = collections.namedtuple("Persona", "id nombre apellidos")
        personaJorge = Persona(id = 1, nombre = "Jorge", apellidos = "Hernandez Ramirez")
        self.assertEqual(1, personaJorge.id)
        self.assertEqual("Jorge", personaJorge.nombre)
        with self.assertRaises(AttributeError):
            personaJorge.id = 2;
        self.assertEquals(collections.OrderedDict([('id', 1), ('nombre', 'Jorge'), ('apellidos', 'Hernandez Ramirez')]),
                          personaJorge._asdict())

    def test_debeTestearElObjetoEnum(self):
        specieTiger = Species.tiger
        self.assertEqual(4, specieTiger.value)

    def imprimirDict(self, diccionario):
        for key, value in diccionario.items():
            print(key, value)

    def appendToDefaultDict(self, midefautdict, key, value):
        midefautdict[key].append(value)

if __name__ == "__main__":
    unittest.main()