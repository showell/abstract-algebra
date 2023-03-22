"""
Technically, we are talking about commutative rings with
a multiplicative identity element (which we call "one").
"""


def verify_commutative(samples, combine):
    for a in samples:
        for b in samples:
            assert combine(a, b) == combine(b, a)


def verify_monoid(samples, *, identity, combine):
    for a in samples:
        assert combine(identity, a) == a
        for b in samples:
            for c in samples:
                assert combine(combine(a, b), c) == combine(a, combine(b, c))


def verify_commutative_monoid(samples, *, identity, combine):
    verify_commutative(samples + [identity], combine)
    verify_monoid(samples, identity=identity, combine=combine)


def verify_distributive_property(samples, *, zero, one):
    for a in samples:
        for b in samples:
            for c in samples:
                assert a * (b + c) == a * b + a * c


def verify_semiring(samples, *, zero, one):
    add = lambda a, b: a + b
    mul = lambda a, b: a * b
    verify_commutative_monoid(samples, identity=zero, combine=add)
    verify_commutative_monoid(samples, identity=one, combine=mul)
    verify_distributive_property(samples, zero=zero, one=one)


def verify_additive_inverses(samples, zero):
    for a in samples:
        assert a + (-a) == zero
        assert (-a) + a == zero


def ensure_samples_are_useful(samples):
    assert len(samples) >= 2

    # Make sure our samples are different from each
    # other (and that the equality operation actually
    # has meaning).
    for i in range(len(samples)):
        for j in range(i + 1, len(samples)):
            assert samples[i] != samples[j]


def verify_axioms(samples, *, zero, one):
    ensure_samples_are_useful(samples)
    verify_semiring(samples, zero=zero, one=one)
    verify_additive_inverses(samples, zero)


if __name__ == "__main__":
    from fractions import Fraction
    from lib.test_helpers import run_test

    @run_test
    def check_integers_are_ring():
        samples = [-7, 42, 13, 9, 4567, 14]
        verify_axioms(samples, zero=0, one=1)

    @run_test
    def check_fractions_are_ring():
        samples = [Fraction(1, 3), Fraction(-2, 7), Fraction(43, 13)]
        verify_axioms(samples, zero=Fraction(0), one=Fraction(1))
