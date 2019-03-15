#coding=utf-8
def add(a,b):
    return a+b
import unittest
class AddTest(unittest.TestCase):
    def setUp(self):
        pass
    def test_add(self):
        self.assertEqual(add(3,4),7)

    def test_add1(self):
        self.assertEqual(add(13,4),17)
    def test_add2(self):
        self.assertEqual(add(113,4),117)
    def test_add3(self):
        self.assertEqual(add(123,4),127)
    def test_add4(self):
        self.assertEqual(add(123,4),127)
    #class
    def tearDown(self):
        pass
if __name__=="__main__":
    unittest.main()
