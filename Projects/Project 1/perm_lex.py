#
#Name:                  Bradley Weeks
#Student ID:            014520268
#Date (last modified):  10/01/19
#
# Project 1
# Section 04
# Purpose: For some alphabetical input string, return lexicographic list of all permutations of said input recursively
#

# string -> list
def perm_gen_lex(a_string):

    #list of all permutations
    perm_list = []
    perm_dict = {}


    if len(a_string) == 0:
        return []
    if len(a_string) == 1:
        return [a_string]

    '''
    #get all permutations for a length of n-1
    permutations = perm_gen_lex(a_string[1:])
    first_letter=a_string[0]
    '''


    for current_character_index in range(len(a_string)):
        current_char = a_string[current_character_index]
        current_perm = ''

        #use index instead of literal string bc an input with more than
        # 1 of the same letter is difficult to return correct index
        for characters_index in range(len(a_string)):
            # This statement is to ensure that even if there is a duplicate in the input, it will preserve order
            if current_character_index != characters_index:
                current_perm += a_string[characters_index]

        permutations = perm_gen_lex(current_perm)
        # for each generated permutation
        for permutation in permutations:
            # if a previous doesn't exist in a dictionary permutation
            if permutation not in perm_dict:
                # add the permutation to the dictionary and the list
                perm_dict[permutation] = permutations
                perm_list.append(current_char+permutation)

    return perm_list