# coding=utf8

"""
Challenge:  the Pythonic card deck class

The class CardDeck below represents a pack
of cards.

Find out how to use magic methods so that the
following three standard functions work:

    >>> import random
    >>> deck = CardDeck()
    >>> len(deck)
    52
    >>> print(deck[0])
    2♠
    >>> print(deck[-1])
    A♣
    >>> random.choice(deck) in list(deck)
    True
    >>> random.shuffle(deck)

Tip:
If you have lines in the docstring (this string) that look like interactive
Python sessions, you can use the doctest module to run and test this code.

Try: python3 -m doctest -v magic_methods.py

See: https://docs.python.org/3/library/doctest.html


Credit to Luciano Ramalho and his excellent book Fluent Python, from which
I stole this example.
"""



class CardDeck:
    ranks = [str(n) for n in range(2, 11)] + ['J', 'Q', 'K', 'A']
    suits = '♠♡♢♣'

    def __init__(self):
        self._cards = [
            rank + suit
            for suit in self.suits
            for rank in self.ranks
        ]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, key):
        return self._cards[key]

    def __setitem__(self, key, value):
        self._cards[key] = value

"""
Bonus exercise: Polynomial class

Create a class that represents polynomials.  You may need to stretch your memory back to high school maths!

A polynomial loks like

    2(xx) - x + 7

And its essential features are the coefficients of each power of x

in this example, power-2=2, power-1=-1, power-0=7

Credit to Moshe Goldstein
"""

from itertools import zip_longest

class Polynomial:
    def __init__(self, coefficients=()):
        self._coefficients = list(coefficients)

    def __str__(self):
        if not self._coefficients:
            return '0'
        if len(self._coefficients) == 1:
            return str(self._coefficients[0])
        l = [str(self._coefficients[0])] + ['{0}x^{1}'.format(p, i+1) for i, p in enumerate(self._coefficients[1:])]
        return ' + '.join(l)

    def __add__(self, poly):
        coefficient_sums = [
            x+y
            for x,y in zip_longest(self._coefficients, poly.coefficients, fillvalue=0)
        ]
        return Polynomial(coefficients=coefficient_sums)

    def __sub__(self, poly):
        coefficient_differences = [
            x-y
            for x,y in zip_longest(self._coefficients, poly.coefficients, fillvalue=0)
        ]
        return Polynomial(coefficients=coefficient_differences)

    def __len__(self):
        return len(self._coefficients)

    def __iter__(self):
        return iter(self._coefficients)

    def __repr__(self):
        return str(self)

    def __mul__(self, poly):
        self_degree = len(self) - 1 if len(self) != 0 else 0
        poly_degree = len(poly) - 1 if len(poly) != 0 else 0
        multiply_coefficients = [0.0] * (self_degree + poly_degree + 1)
        for i, p in enumerate(self):
            for j, q in enumerate(poly):
                multiply_coefficients[i+j] += p * q
        return Polynomial(coefficients=multiply_coefficients)

    @property
    def coefficients(self):
        return self._coefficients

    def value(self, x):
        return self._coefficients[x]

    def derivative(self):
        derivative_coefficients = list()
        if not self._coefficients:
            derivative_coefficients += [0.0]
        derivative_coefficients += [
            p*i
            for i, p in enumerate(self._coefficients) if i > 0
        ]
        return Polynomial(coefficients=derivative_coefficients)
