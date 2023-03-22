def verify_semiring(samples, *, zero, one):
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

        for b in samples:
            assert a * b == b * a
            assert a + b == b + a

            for c in samples:
                assert a * (b + c) == a * b + a * c
                assert (a + b) + c == a + (b + c)
                assert (a * b) * c == (a * b) * c
