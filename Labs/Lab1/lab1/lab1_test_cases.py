import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter_NoneTest(self):
        """tests the max_list_iter function
           if the int list == None, it should raise a ValueError
        """
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max_list_iter_Functionality(self):
        """tests the max_list_iter function to see if it actually gets the right answer"""
        #creating list and a max value that is should be equal to
        t_list = [1,2,3,4,5,6,7,8,9,10]
        self.assertEqual(max_list_iter(t_list), 10)

    def test_mas_list_iter_EmptyList(self):
        """tests max_list_iter function for its empty list return
        """
        t_list = []
        self.assertEqual(max_list_iter(t_list), None)

    def test_reverse_rec_NoneTest(self):
        """tests the reverse_rec function
           if the int list == None, it should raise a ValueError
        """
        t_list = None
        with self.assertRaises(ValueError):
            reverse_rec(None)


    def test_reverse_rec_EmptyTest(self):
        """test the reverse_rec function
           if the int list is empty, it should return the empty list
        """
        t_list = []
        self.assertEqual(reverse_rec(t_list), t_list)

    def test_reverse_rec_Functionality(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])

    """def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )
    """
if __name__ == "__main__":
        unittest.main()
