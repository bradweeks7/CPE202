#
#Name:                  Bradley Weeks
#Student ID:            ---REDACTED---
#Date (last modified):  09/30/19
#
# Project 1
# Section 04
# Purpose: The goal of the game is to end up with EXACTLY 42 bears.
#

# int -> bool
def bears(n):

    if n == 0:
        return False

    if n == 42:
        return True

    # if this choice will not result in the goal
    elif n < 42:
        return False

    # other possibilities
    else:
        if (n % 2 == 0) and bears(n / 2):
            return True
        if (n % 3 == 0):
            if ((n % 10) * (n % 100) // 10) != 0:
                if bears(n - ((n % 10) * (n % 100) // 10)):
                    return True
        if (n % 4 == 0):
            if ((n % 10) * (n % 100) // 10) != 0:
                if bears(n - ((n % 10) * (n % 100) // 10)):
                    return True
        if (n % 5 == 0):
            if (n-42) != 0:
                if bears(n - 42):
                    return True

        return False
