
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""

   if int_list == None:
       raise ValueError

   # An empty list should return None
   if len(int_list) == 0:
       return None

   for number in range(len(int_list)):
       maximum = 0
       new_max = int_list[number]

       if new_max > maximum:
           maximum = new_max

   return maximum


def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   pass

def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   pass
