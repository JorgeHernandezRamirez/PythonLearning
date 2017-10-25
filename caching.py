import unittest
from functools import lru_cache

class CustomCache:

    def __init__(self, function):
        self.function = function
        self.cache = {}

    def __call__(self, *args, **kwargs):
        if args not in self.cache:
            self.cache[args] = self.function(*args, **kwargs)
        return self.cache[args]

@lru_cache(maxsize=32)
def fibonacci(number):
    print("Calculando el fibonacci de number")
    if number < 2:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)

@CustomCache
def fibonacciCustomCache(number):
    print("Calculando el fibonacci de number")
    if number < 2:
        return number
    return fibonacciCustomCache(number - 1) + fibonacciCustomCache(number - 2)

class CachingTest(unittest.TestCase):

    def test_debeCalcularElFibonacciDeUnNumero2Veces(self):
        self.assertEqual(3, fibonacci(4))
        self.assertEqual(3, fibonacci(4))

    def test_debeCalcularElFibonacciDeUnNumero2VecesUtilizandoCustomCache(self):
        self.assertEqual(3, fibonacciCustomCache(4))
        self.assertEqual(3, fibonacciCustomCache(4))

if __name__ == "__main__":
    unittest.main()