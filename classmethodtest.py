import unittest

class ClassMethod:

    def foo(self, x):
        return (self, x)

    @classmethod
    def classfoo(clazz, x):
        return (clazz, x)

    @staticmethod
    def staticfoo(x):
        return (x)

class MiClase:

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "value=" + str(self.value);

class ClassMethodTest(unittest.TestCase):

    def test_debeLlamarAlMetodoEstatico(self):
        instanceOfClassMethod = ClassMethod()
        self.assertEqual((1), ClassMethod.staticfoo(1))
        self.assertEqual((1), instanceOfClassMethod.staticfoo(1))
        self.assertEqual((instanceOfClassMethod, 1), instanceOfClassMethod.foo(1))
        self.assertEqual((type(instanceOfClassMethod), 1), instanceOfClassMethod.classfoo(1))

    def test_debeDevolverCorrectamenteElStr(self):
        self.assertEqual("value=1", MiClase(1).__str__())

if __name__ == "__main__":
    unittest.main()