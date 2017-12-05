import unittest

class PositionTest(unittest.TestCase):

    def test_fail(self):
        self.assertEqual(1,2)
        #self.assertTrue(False)
    def test_pass(self):
        n=5
        self.assertequal(5,0)

if __name__=="__main__":
    unittest.main()