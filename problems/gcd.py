"""Greatest common divisor"""
import unittest


def gcd(a: int, b: int) -> int:
    """
    Returns the greatest common divisor amongst two numbers
    """
    if a > b:
        smaller = b
        larger = a
    else:
        smaller = a
        larger = b

    while larger > smaller:
        remainder = larger % smaller
        if remainder == 0:
            return smaller
        larger = smaller
        smaller = remainder

    return None


class GcdTest(unittest.TestCase):
    def test2416(self):
        self.assertEqual(8, gcd(24, 16))


if __name__ == '__main__':
    unittest.main()
