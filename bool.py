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


def verify_semiring(samples, *, zero, one):
    # compare this to verify_axioms in commutative_ring.py
    assert zero * zero == zero
    assert zero * one == zero
    assert one * zero == zero
    assert one * one == one

    assert zero + zero == zero
    assert one + zero == one
    assert zero + one == one

    # This looks like overkill for Bool, but we want
    # to verify the distributive properties across all
    # possible 3-tuples of T and F.
    for a in samples:
        assert zero + a == a
        assert a + zero == a
        assert one * a == a
        assert a * one == a

        for b in samples:
            assert a * b == b * a
            assert a + b == b + a

            for c in samples:
                assert a * (b + c) == a * b + a * c
                assert (a + b) + c == a + (b + c)
                assert (a * b) * c == (a * b) * c


if __name__ == "__main__":
    from lib.test_helpers import run_test

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

    @run_test
    def Bool_is_semi_ring():
        verify_semiring([T, F], zero=F, one=T)

    @run_test
    def exponentiation():
        assert T**47 == T
        assert F**942 == F
        assert F**0 == T
        assert F**1 == F
        assert T**0 == T
        assert T**1 == T
