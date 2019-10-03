import unittest
from  base_convert import *

class TestBaseConvert(unittest.TestCase):

    def test_base2(self):
        self.assertEqual(convert(45,2),"101101")
        self.assertEqual(convert(1,2), "1")
        self.assertEqual(convert(3, 2), "11")
        self.assertEqual(convert(15, 2), "1111")
        self.assertEqual(convert(4, 2), "100")
        self.assertEqual(convert(8, 2), "1000")



    def test_base4(self):
        self.assertEqual(convert(30,4),"132")

    def test_base16(self):
        self.assertEqual(convert(316,16),"13C")

if __name__ == "__main__":
        unittest.main()