# Задание по программированию: Задача по созданию модульного теста функции factorize
import unittest
from math import gcd


def factorize(n):
    """
    Factorize positive integer and return its factors.
    :type x: int,>=0
    :rtype: tuple[N],N>0
    """
    if type(n) != int:
        raise TypeError
    if n < 0:
        raise ValueError
    if n <= 1:
        return (n,)
    factors = ()

    def get_factor(n):
        x_fixed = 2
        cycle_size = 2
        x = 2
        factor = 1

        while factor == 1:
            for _ in range(cycle_size):
                if factor > 1:
                    break
                x = (x * x + 1) % n
                factor = gcd(x - x_fixed, n)

            cycle_size *= 2
            x_fixed = x

        return factor

    while n > 1:
        next = get_factor(n)
        factors += (next,)
        n //= next

    return tuple(sorted(factors))


class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        self.cases = ("string", 1.5)
        for b in self.cases:
            with self.subTest(case=b):
                self.assertRaises(TypeError, factorize, b)

    def test_negative(self):
        self.cases = (-1, -10, -100)
        for b in self.cases:
            with self.subTest(case=b):
                self.assertRaises(ValueError, factorize, b)

    def test_zero_and_one_cases(self):
        self.cases = (0, 1)
        for b in self.cases:
            with self.subTest(cases=b):
                self.assertEqual(factorize(b), (b,))

    def test_simple_numbers(self):
        self.cases = (3, 13, 29)
        for b in self.cases:
            with self.subTest(cases=b):
                self.assertEqual(factorize(b), (b,))

    def test_two_simple_multipliers(self):
        self.cases = (6, 26, 121)
        expected = [(2, 3), (2, 13), (11, 11)]
        for b, a in enumerate(self.cases, expected):
            with self.subTest(cases=b):
                self.assertEqual(factorize(b), a)

    def test_many_multipliers(self):
        self.cases = (1001, 9699690)
        expected = [(7, 11, 13), (2, 3, 5, 7, 11, 13, 17, 19)]
        for b, a in enumerate(self.cases, expected):
            with self.subTest(cases=b):
                self.assertEqual(factorize(b), a)


if __name__ == "__main__":
    unittest.main()