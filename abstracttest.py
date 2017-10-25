import unittest
from abc import ABCMeta, abstractmethod
import logging

logging.basicConfig( level=logging.DEBUG, format='[%(levelname)s] - %(threadName)-10s : %(message)s')

class Vehicle(metaclass=ABCMeta):

    def __init__(self, wheelsNumber):
        self.wheelsNumber = wheelsNumber;

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def __init__(self, wheelsNumber):
        super(Car, self).__init__(wheelsNumber)

    def start(self):
        logging.info('Arrancando el coche de %s ruedas', self.wheelsNumber)

    def stop(self):
        logging.info('Parando el coche de %s ruedas', self.wheelsNumber)

class AbstractTest(unittest.TestCase):

    def test_debeLanzarExcepcionCuandoSeInstanciaClaseAbstracta(self):
        with self.assertRaises(TypeError):
            Vehicle(2)

    def test_debeCrearElObjetoCarQueExtiendeDeClaseAbstracta(self):
        self.assertIsNotNone(Car(4))
        self.assertEquals(4, Car(4).wheelsNumber)
        Car(4).start()

if __name__ == "__main__":
    unittest.main()
