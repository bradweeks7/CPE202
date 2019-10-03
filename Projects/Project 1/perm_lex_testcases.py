import unittest
import time
import perm_lex

class TestAssign1(unittest.TestCase):

    def test_perm_gen_lex_emptylist(self):
        '''An empty list should return an empty list'''
        self.assertEqual(perm_lex.perm_gen_lex(''), [])

    def test_perm_gen_lex_singleitem(self):
        '''Single-character item in list should be returned'''
        self.assertEqual(perm_lex.perm_gen_lex('a'),['a'])

    def test_perm_gen_lex_simple(self):
        '''simple permutation test'''
        self.assertEqual(perm_lex.perm_gen_lex('ab'), ['ab', 'ba'])

    def test_perm_gen_lex_big(self):
        '''more complicated permutation test'''
        self.assertEqual(perm_lex.perm_gen_lex('abcd'), ['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca', 'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba'])

    def test_perm_gen_lex_multiple_letters(self):
        '''Tests a list with more than one of the same letter'''
        self.assertEqual(perm_lex.perm_gen_lex('aab'), ['aab','aba','baa'])
        self.assertEqual(perm_lex.perm_gen_lex('aaab'), ['aaab','aaba','abaa','baaa'])
        self.assertEqual(perm_lex.perm_gen_lex('aabc'), ['aabc','aacb','abac','abca','acab','acba','baac','baca','bcaa','caab','caba','cbaa'])

'''start = time.time()'''



if __name__ == "__main__":

        start = time.time()
        alist = perm_lex.perm_gen_lex('aaabbbccc')
        end = time.time()
        print(end-start)
        print(alist)

        unittest.main()