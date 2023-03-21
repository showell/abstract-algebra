from lib.type import enhanced_type


def verify_homomorphism(samples, f, g, type1, type2):
    for a in samples:
        assert enhanced_type(a) == type1
        assert enhanced_type(f(a)) == type2
        assert enhanced_type(g(f(a))) == type1
        assert g(f(a)) == a

        for exp in range(8):
            assert g(f(a) ** exp) == g(f(a**exp))

        for b in samples:
            assert g(f(a) + f(b)) == g(f(a + b))
            assert g(f(a) * f(b)) == g(f(a * b))


def verify_isomorphism(*, samples_a, type_a, samples_b, type_b, a_to_b, b_to_a):
    verify_homomorphism(samples_a, a_to_b, b_to_a, type_a, type_b)
    verify_homomorphism(samples_b, b_to_a, a_to_b, type_b, type_a)


if __name__ == "__main__":
    from fractions import Fraction
    from bool import Bool
    from mod5 import Mod5
    from number_list import NumberList
    from poly import SingleVarPoly
    from poly_integer import IntegerMath, IntegerPoly
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

        verify_homomorphism(samples, f, g, int, Fraction)

    @run_test
    def ints_can_compute_mod5():
        samples = [Mod5(0), Mod5(1), Mod5(2), Mod5(3), Mod5(4)]
        f = lambda m: m.n
        g = lambda n: Mod5(n % 5)

        verify_homomorphism(samples, f, g, Mod5, int)

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

        verify_homomorphism(samples, f, g, Bool, int)

    @run_test
    def NumberList_can_trivally_compute_int():
        samples = [-7, 42, 13, 9, 4567, 14]
        f = lambda n: NumberList([n])
        g = lambda nl: nl.list()[0]

        verify_homomorphism(samples, f, g, int, NumberList)

    @run_test
    def NumberList_can_simulate_decimal_digit_math():
        # NumberList can compute int in a more interesting way
        samples = [-732, 42, 13, 9, 4567, 142340862349551239912346999234654190]

        assert get_digits(1234) == [4, 3, 2, 1]
        assert number_from_digit_list([5, 6, 7]) == 765

        f = lambda n: NumberList(get_digits(n))
        g = lambda nl: number_from_digit_list(nl.list())

        verify_homomorphism(samples, f, g, int, NumberList)

    @run_test
    def NumberList_and_IntegerPoly_are_isomorphic():
        samples_a = [
            IntegerPoly.from_list([0, 1, 3]),
            IntegerPoly.from_list([-47]),
            IntegerPoly.from_list([43, 0, 0, 0, 0, 27]),
        ]
        type_a = (SingleVarPoly, IntegerMath)

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
