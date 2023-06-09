"""
Technically, we are talking about commutative rings with
a multiplicative identity element (which we call "one").
"""


def verify_commutative(samples, combine):
    # https://en.wikipedia.org/wiki/Commutative_property
    for a in samples:
        for b in samples:
            assert combine(a, b) == combine(b, a)


def verify_monoid(samples, *, identity, combine):
    # https://en.wikipedia.org/wiki/Monoid
    for a in samples:
        assert combine(identity, a) == a
        for b in samples:
            for c in samples:
                assert combine(combine(a, b), c) == combine(a, combine(b, c))


def verify_commutative_monoid(samples, *, identity, combine):
    verify_commutative(samples + [identity], combine)
    verify_monoid(samples, identity=identity, combine=combine)


def verify_distributive_property(math, samples):
    # https://en.wikipedia.org/wiki/Distributive_property
    add = math.add
    mul = math.multiply
    for a in samples:
        for b in samples:
            for c in samples:
                assert mul(a, add(b, c)) == add(mul(a, b), mul(a, c))


def verify_semiring(math, samples):
    # https://en.wikipedia.org/wiki/Semiring
    verify_commutative_monoid(samples, identity=math.zero, combine=math.add)
    verify_commutative_monoid(samples, identity=math.one, combine=math.multiply)
    verify_distributive_property(math, samples)


def verify_additive_inverses(math, samples):
    # https://en.wikipedia.org/wiki/Additive_inverse
    for a in samples:
        assert math.add(a, math.additive_inverse(a)) == math.zero
        assert math.add(math.additive_inverse(a), a) == math.zero


def ensure_samples_are_useful(samples):
    assert len(samples) >= 2

    # Make sure our samples are different from each
    # other (and that the equality operation actually
    # has meaning).
    for i in range(len(samples)):
        for j in range(i + 1, len(samples)):
            assert samples[i] != samples[j]


def verify_ring_properties(math, samples):
    # https://en.wikipedia.org/wiki/Commutative_ring
    ensure_samples_are_useful(samples)
    verify_semiring(math, samples)
    verify_additive_inverses(math, samples)
