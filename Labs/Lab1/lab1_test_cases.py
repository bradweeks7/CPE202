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


    def test_max_list_iter_EmptyList(self):
        """tests max_list_iter function for its empty list return
        """
        t_list = []
        self.assertEqual(max_list_iter(t_list), None)

    def test_max_list_iter_Maxis0(self):
        '''Tests to see if a 0 max will stil work'''
        t_list = [0,0,0,0,0,0,0]
        self.assertEqual(max_list_iter(t_list), 0)

    def test_reverse_rec_NoneTest(self):
        """tests the reverse_rec function
           if the int list == None, it should raise a ValueError
        """
        t_list = None
        with self.assertRaises(ValueError):
            reverse_rec(t_list)

    def test_reverse_rec_EmptyTest(self):
        """test the reverse_rec function
           if the int list is empty, it should return the empty list
        """
        t_list = []
        self.assertEqual(reverse_rec(t_list), t_list)

    def test_reverse_rec_Functionality_1(self):
        """test to see if reverse_rec actually works as intended"""
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])


    def test_reverse_rec_Functionality_2(self):
        """lager list test for reverse_rec to test, the more the better"""
        self.assertEqual(reverse_rec([1,2,3,4,5,6,7,8,9]), [9,8,7,6,5,4,3,2,1])


    def test_reverse_rec_Functionality_3(self):
        """still not convinced reverse_rec is working, switching up number order"""
        self.assertEqual(reverse_rec([10,15,9,2,300,81,72,0,0,0,0,100000,3,1]), [1,3,100000,0,0,0,0,72,81,300,2,9,15,10])




    def test_bin_search_Functionality(self):
        """test to check if the bin_search function actually works"""
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, low, high, list_val), 4)

    #some error in bin_search function
    def test_bin_search_Functionality_oddnumber(self):
        '''bin_serch looks for a midpoint, checking to see if it can deal with an odd-numbered set'''
        list_val = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
        low = 0
        high = 20
        self.assertEqual(bin_search(5, low, high, list_val), 5)

    def test_bin_search_Empty(self):
        """Edge case test for a list if given"""
        t_list = None
        with self.assertRaises(ValueError):
            bin_search(0, 10, 20, t_list)

    def test_bin_search_gap(self):
        '''Tests for a target where a gap is in a sequential array'''
        t_list = [1,2,3,4,6,7,8,9,10,11]
        high = 10
        low = 0
        self.assertEqual(bin_search(5, low, high, t_list), None)

    def test_bin_search_empty(self):
        '''Tests for an empty list'''
        t_list = []
        high = 10
        low = 0
        self.assertEqual(bin_search(5, low, high, t_list), None)


    def test_bin_search_2(self):
        '''Another test of the bin_search function'''
        t_list = [0,1,2,3,4,5,6,7,8,9,10]
        low = 0
        high = 10
        self.assertEqual(bin_search(2,low,high,t_list), 2)

    def test_bin_search_TargetNotFound(self):
        """Tests to see if correct return value for a target not found in list"""
        t_list = [0,1,2,3,4,5,6,7,8,9,10]
        low = 0
        high = 10
        self.assertEqual(bin_search(11,low,high,t_list),None)

    def test_bin_search_SingleItemList(self):
        '''Tests to see if a single-item array will be functional'''
        t_list = [1]
        low = 0
        high = 0
        self.assertEqual(bin_search(1,low,high,t_list), 0)

    def test_bin_search_extreme_values(self):
        '''Guaruntees max and min valued indexes in an array for a bin search will be returned correctly'''
        t_list = [0,1,2,3,4,5,6,7,8,9,10]
        low = 0
        high = 10
        self.assertEqual(bin_search(0,low,high,t_list),0)
        self.assertEqual(bin_search(10,low,high,t_list),10)


    def test_bin_search_1st_element(self):
        '''Searches for a value at the lowest point in the list that isn't there'''
        t_list = [2,4,6,8,10,12]
        low = 0
        high = 6
        self.assertEqual(bin_search(1,low,high,t_list), None)


    def test_bin_search(self):
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(4, low, high, list_val), 4)

    def test_bin_search(self):
        list_val = [0, 2, 4, 6, 8, 10, 12, 14, 16]
        low = 0
        high = 8
        self.assertEqual(bin_search(1,low,high,list_val), None)




if __name__ == "__main__":
        unittest.main()
