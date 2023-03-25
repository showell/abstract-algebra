"""
Most of our classes in this project implement data structures
related to commutative rings.

Here we provide an interesting counterexample. A class that
performs simple boolean logic without NOT (i.e. negation) forms
only a semiring. (Note that rings require an additive inverse.)
"""


class Bool:
    def __init__(self, b):
        assert b in [False, True]
        self.b = b

    def __add__(self, other):
        return Bool(self.b or other.b)

    def __eq__(self, other):
        return self.b == other.b

    def __mul__(self, other):
        return Bool(self.b and other.b)

    def __pow__(self, exponent):
        if exponent == 0:
            return Bool(True)
        return self

    def __str__(self):
        return str(self.b)
