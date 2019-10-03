import unittest
from location import *

class TestLab1(unittest.TestCase):

    #the following test_repr iterations are testing different parts of the Location class
    def test_repr_1(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")

    def test_repr_2(self):
        loc = Location("Canada", 0.0, 0.0)
        self.assertEqual(repr(loc),"Location('Canada', 0.0, 0.0)")

    # Add more tests!

if __name__ == "__main__":
        unittest.main()
