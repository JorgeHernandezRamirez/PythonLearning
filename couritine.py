import unittest

class CachingTest(unittest.TestCase):

    def test_debeCalcularElFibonacciDeUnNumero2VecesUtilizandoCustomCache(self):
        search = self.grep('coroutine')
        next(search) #Aquí es cuenta se imprime Buscando el patrón coroutine
        search.send("I love you") #No imprime nada
        search.send("Don't you love me?") #No imprime nada
        search.send("I love coroutines instead!") #Imprime I love coroutines instead!

    def grep(self, pattern):
        print("Buscando el patrón ", pattern)
        while True:
            line = (yield)
            if pattern in line:
                print(pattern)

if __name__ == "__main__":
    unittest.main()