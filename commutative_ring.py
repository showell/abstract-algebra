"""
Technically, we are talking about commutative rings with
a multiplicative identity element (which we call "one").
"""


def test(samples, *, zero, one):
    assert zero * zero == zero
    assert zero * one == zero
    assert one * zero == zero
    assert one * one == one

    assert zero + zero == zero
    assert one + zero == one
    assert zero + one == one

    for a in samples:
        assert zero + a == a
        assert a + zero == a
        assert one * a == a
        assert a * one == a
        assert a + (-a) == zero
        assert (-a) + a == zero

        for b in samples:
            assert a * b == b * a
            assert a + b == b + a

            for c in samples:
                assert a * (b + c) == a * b + a * c
                assert (a + b) + c == a + (b + c)
                assert (a * b) * c == (a * b) * c


if __name__ == "__main__":
    samples = [-7, 42, 13, 9, 4567, 14]
    test(samples, zero=0, one=1)

    from fractions import Fraction

    samples = [Fraction(1, 3), Fraction(-2, 7), Fraction(43, 13)]
    test(samples, zero=Fraction(0), one=Fraction(1))
