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


if __name__ == "__main__":
    from fractions import Fraction
    from bool import Bool
    from mod5 import Mod5
    from number_list import NumberList
    from poly import SingleVarPoly
    from poly_integer import IntegerPoly
    from lib.test_helpers import run_test

    def get_digits(n):
        if n < 0:
            return [-digit for digit in get_digits(-n)]
        if n == 0:
            return []
        return [n % 10] + get_digits(n // 10)

    def number_from_digit_list(lst):
        return sum(c * 10**i for i, c in enumerate(lst))

    @run_test
    def fractions_can_compute_int():
        samples = [-7, 42, 13, 9, 4567, 14]
        f = lambda integer: Fraction(integer)
        g = lambda fraction: int(fraction)

        verify_mappability(samples, f, g, int, Fraction)

    @run_test
    def ints_can_compute_mod5():
        samples = [Mod5(0), Mod5(1), Mod5(2), Mod5(3), Mod5(4)]
        f = lambda m: m.n
        g = lambda n: Mod5(n % 5)

        verify_mappability(samples, f, g, Mod5, int)

    @run_test
    def ints_can_compute_simple_bool_logic():
        """
        Note that our Bool class is very limited, and it does
        not have any concept of negation.  However, it has
        addition (OR) and multiplication (AND) operators that
        form a semiring, so we should be able to map this to
        integer arithmetic.

        Here we use "homomorphism" in a slightly casual sense
        of the word.
        """
        T = Bool(True)
        F = Bool(False)

        samples = [T, F]
        f = lambda b: 1 if b.b else 0
        g = lambda n: Bool(n >= 1)

        assert f(T) + f(T) + f(T) == 3
        assert g(3) == T

        assert (f(T) + f(T)) * (f(T) + f(T)) * (f(T) + f(T)) == 8
        assert g(8) == T

        assert f(F) * f(T) * f(T) == 0
        assert g(0) == F

        verify_mappability(samples, f, g, Bool, int)

    @run_test
    def NumberList_can_trivally_compute_int():
        samples = [-7, 42, 13, 9, 4567, 14]
        f = lambda n: NumberList([n])
        g = lambda nl: nl.list()[0]

        verify_mappability(samples, f, g, int, NumberList)

    @run_test
    def NumberList_can_simulate_decimal_digit_math():
        # NumberList can compute int in a more interesting way
        samples = [-732, 42, 13, 9, 4567, 142340862349551239912346999234654190]

        assert get_digits(1234) == [4, 3, 2, 1]
        assert number_from_digit_list([5, 6, 7]) == 765

        f = lambda n: NumberList(get_digits(n))
        g = lambda nl: number_from_digit_list(nl.list())

        verify_mappability(samples, f, g, int, NumberList)

    @run_test
    def NumberList_and_IntegerPoly_are_isomorphic():
        """
        IntegerPoly is a more interesting class than NumberList,
        because IntegerPoly has the notion of variables, and you can
        actually plug in variables to evaluate the polynomials.

        On the other hand, the two classes behave identically with
        respect to addition and multiplication, so they are isomorphic
        over those operations.

        In fact, we could have built IntegerPoly on top of NumberList.
        In this project I didn't follow that strategy, but if you look
        at the code, there are striking similarities between the two
        data types, and this is no coincidence.

        Likewise, we could easily re-implement NumberList to just be
        a simple wrapper around IntegerPoly.
        """
        samples_a = [
            IntegerPoly.from_list([0, 1, 3]),
            IntegerPoly.from_list([-47]),
            IntegerPoly.from_list([43, 0, 0, 0, 0, 27]),
        ]
        type_a = SingleVarPoly

        samples_b = [
            NumberList([43, 97, 2]),
            NumberList([0, 123497862373]),
            NumberList([5, -37, -38]),
        ]
        type_b = NumberList

        a_to_b = lambda ip: NumberList(ip.lst)
        b_to_a = lambda nl: IntegerPoly.from_list(nl.list())

        verify_isomorphism(
            samples_a=samples_a,
            type_a=type_a,
            samples_b=samples_b,
            type_b=type_b,
            a_to_b=a_to_b,
            b_to_a=b_to_a,
        )
