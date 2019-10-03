
# array -> integer
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

# array -> array
def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""

   if int_list is None:
       raise ValueError
   if len(int_list) == 1 or len(int_list) == 0:
       return int_list
   #append last item in list to the next last item to the next last item to the... until finished
   else:
       return int_list[-1:] + reverse_rec(int_list[:-1])


# integer integer integer integer_array -> integer_index
def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """

   #Check if the list even has a target
   if int_list == []:
       return None

   #Send None, raise an error
   if int_list == None:
      raise ValueError

   #midpoint of the bin array
   mid = (high+low)//2

   #target was not in the list
   if high <= low and int_list[high] != target:
      return None

   if int_list[mid] == target:
      return mid

   # if elecment is smaller than mid, then it will only be in the smaller half of int_list
   elif int_list[mid] > target:
      return bin_search(target, low, mid-1, int_list)

   # Else element must be in the righthand array
   elif int_list[mid] < target:
      return bin_search(target, mid+1, high, int_list)
