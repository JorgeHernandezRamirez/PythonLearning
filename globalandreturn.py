import unittest

class GlobalAndReturnTest(unittest.TestCase):

    def test_debeDevolverUnConjuntoDeVariablesDeFormaGlobal(self):
        self.devolverDosVariablesDeFormaGlobal()
        self.assertEqual(variable1, 1)
        self.assertEqual(variable2, 2)

    def test_debeDevolverUnConjuntoDeVariablesConUnaTupla(self):
        self.assertEquals((1, 2), self.devolverDosVariablesConUnaTupla())
        self.assertEquals((1, 2), self.devolverDosVariablesConUnaTuplaSinParentesis())
        variable1, variable2 = self.devolverDosVariablesConUnaTupla()
        self.assertEqual(variable1, 1)
        self.assertEqual(variable2, 2)

    def devolverDosVariablesConUnaTupla(self):
        return (1, 2)

    def devolverDosVariablesConUnaTuplaSinParentesis(self):
        return 1, 2

    def devolverDosVariablesDeFormaGlobal(self):
        global variable1
        global variable2
        variable1 = 1;
        variable2 = 2

if __name__ == "__main__":
    unittest.main()

