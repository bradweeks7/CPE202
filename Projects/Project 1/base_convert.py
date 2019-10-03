#
#Name:                  Bradley Weeks
#Student ID:            014520268
#Date (last modified):  09/30/19
#
# Project 1
# Section 04
# Purpose of File: Converts any integer input from base 10 into any base system from 2 to 16
#

# int int -> string
def convert(num, b):
    """Recursive function that returns a string representing num in the base b"""
    convertString = "0123456789ABCDEF"
    if num < b:
        return convertString[num]
    else:
        return convert(num//b,b) + convertString[num%b]
