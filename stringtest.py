import unittest


class StringTest(unittest.TestCase):

    def test_debeEjecutarCorrectamenteLosMetodosJoinYSplit(self):
        self.assertEqual(["1", "2", "3"], "1,2,3".split(","))
        self.assertEqual("1,2,3", ",".join(["1", "2", "3"]))

if __name__ == "__main__":
    unittest.main()
