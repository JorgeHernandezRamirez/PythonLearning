import unittest

class TernaryOperationsTest(unittest.TestCase):

    def test_debeDevolverTrueLasSiguientesOperaciones(self):
        self.assertTrue(True if 1 == 1 else False)
        self.assertTrue((True, False)[False])
        self.assertTrue((True, False)[0])

    def test_debeDevolverFalseLasSiguientesOperaciones(self):
        self.assertFalse(True if 1 != 1 else False)
        self.assertFalse((True, False)[True])
        self.assertFalse((True, False)[1])

if __name__ == "__main__":
    unittest.main()