"""
Fibonacci Sequence
"""
import functools
import unittest


def memoise(function):
    function.cache = dict()

    @functools.wraps(function)
    def _memoise(*args):
        if args not in function.cache:
            function.cache[args] = function(*args)
        return function.cache[args]
    return _memoise


@memoise
def fibonacci(nterms: int) -> int:
    """
    Returns the fibonacci number for nth term
    :param nterms: The n-th term till which fibonacci number would be computed
    :return: The Fibonacci number
    """
    return nterms if nterms < 2 else fibonacci(nterms - 1) + fibonacci(nterms - 2)


class TestFibonacci(unittest.TestCase):
    def testFibonacci(self):
        self.assertEqual(8, fibonacci(6))

    def testFibonacciLarge(self):
        self.assertEqual(12586269025, fibonacci(50))

if __name__ == '__main__':
    unittest.main()
