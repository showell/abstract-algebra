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


if __name__ == "__main__":
    from lib.test_helpers import run_test
    from commutative_ring import verify_semiring

    F = Bool(False)
    T = Bool(True)

    @run_test
    def truth_tables():
        assert F + F == F
        assert F + T == T
        assert T + F == T
        assert T + T == T

        assert F * F == F
        assert F * T == F
        assert T * F == F
        assert T * T == T

        assert T == T
        assert F == F
        assert F != T

    @run_test
    def Bool_is_semi_ring():
        verify_semiring([T, F], zero=F, one=T)

    @run_test
    def exponentiation():
        assert T * T == T**2
        assert F * F == F**2

        assert T * T * T == T**3
        assert F * F * F == F**3

        assert T**47 == T
        assert F**942 == F
        assert F**0 == T
        assert F**1 == F
        assert T**0 == T
        assert T**1 == T
