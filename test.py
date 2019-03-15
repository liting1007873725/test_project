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
    #class
    def tearDown(self):
        pass
if __name__=="__main__":
    unittest.main()
