def verify_mappability(samples, f, g, type1, type2):
    # https://en.wikipedia.org/wiki/Surjective_function
    # https://en.wikipedia.org/wiki/Injective_function
    """
    We are using a somewhat informal notion of mappability here,
    which is essentially just saying that two different Python
    types have a natural mapping between them.

    We require both types to natively support the * and +
    operators, whether they are just built-in concepts (as for
    Python integers) or they are implemented with magic
    dunder methods like __add__ and __mul__.

    If we have samples of type type1, then we expect our f
    function to map values of type type1 to "similar" values
    of type type2. Note that we do NOT require this mapping to
    be either surjective (onto) or injective (one-to-one).

    Likewise the g function maps values back from type2 to type1.

    We are verifying only that type2 is powerful enough to simulate
    type1 math.  In other words, we decide whether you can take two
    values from type1, then use f to map them over to type2 values,
    and then do the +/* operation under type2, and then finally
    use g to get back a value of type1, and find that the result is
    the same as if you had done the same operation completely in
    type1.

    Under this scheme, g is a homomorphism from type2 to type1,
    but f may not necessarily be one. (Another caveat is that g
    may only make sense for a subset of type2 values, although
    I think most, if not all, of the examples here are
    complete.)

    Unless we are dealing with small, finite sets, this function
    does not exhaust all possible values, so you shouldn't
    consider this function to provide a proof. It is useful
    in that it will quickly find counterexamples if you choose
    your sample values carefully.
    """
    for a in samples:
        assert type(a) == type1
        assert type(f(a)) == type2
        assert type(g(f(a))) == type1
        assert g(f(a)) == a

        for exp in range(8):
            assert g(f(a) ** exp) == a**exp

        for b in samples:
            # show that we can compute values in type2
            assert g(f(a) + f(b)) == a + b
            assert g(f(a) * f(b)) == a * b

            # https://en.wikipedia.org/wiki/Homomorphism
            # show g is a homomorpism, at least for the image of
            # our samples over f
            x = f(a)
            y = f(b)
            assert g(x + y) == g(x) + g(y)
            assert g(x * y) == g(x) * g(y)


def verify_isomorphism(*, samples_a, type_a, samples_b, type_b, a_to_b, b_to_a):
    # https://en.wikipedia.org/wiki/Isomorphism
    """
    In math, the term "isomorphism" if a fancy and more precise way of
    saying that two different things are really equivalent things, for all
    practical purposes.  In other words, two things may look different on a
    superficial level, but they have the same underlying structure.

    In order to show that two different Python data types are isomorphic
    (at least over the basic operations of addition and multiplication),
    it is sufficient to prove that there is a pair of functions that map
    between the two types in such a way that you can choose either type
    to do the actual multiplication/addition computations, and then the
    other type essentially gets the result for free.  (You apply a forward
    mapping to the inputs, then the treat the other Python type as a black
    box, and then you apply the reverse mapping to the output.)
    """
    verify_mappability(samples_a, a_to_b, b_to_a, type_a, type_b)
    verify_mappability(samples_b, b_to_a, a_to_b, type_b, type_a)
