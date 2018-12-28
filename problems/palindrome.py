"""String Palidrome"""
import unittest


def palindrome(string: str) -> bool:
    return string[:] == string[::-1]


class PalindromeTest(unittest.TestCase):
    def testPalindromeString(self):
        self.assertTrue(palindrome('madam'))

    def testNonPalindrome(self):
        self.assertFalse(palindrome('adam'))

    def testEmptyString(self):
        self.assertTrue(palindrome(''))

    def testNoneString(self):
        with self.assertRaises(TypeError):
            palindrome(None)

if __name__ == '__main__':
    unittest.main()
