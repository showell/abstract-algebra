from mod5 import Mod5
from math_mod5 import Mod5Math
from poly import SingleVarPoly


class Mod5Poly:
    const = lambda c: SingleVarPoly.constant(Mod5Math, Mod5(c))
    zero = const(0)
    one = const(1)
    two = const(2)
    three = const(3)
    four = const(4)
    m = SingleVarPoly.degree_one_var(Mod5Math, "m")

    @staticmethod
    def from_list(lst):
        return SingleVarPoly(Mod5Math, lst, "m")


if __name__ == "__main__":
    from commutative_ring import verify_ring_properties
    from lib.test_helpers import assert_equal, assert_str, run_test
    from math_helper import MathHelper

    zero = Mod5Math.zero
    one = Mod5Math.one
    two = Mod5(2)
    three = Mod5(3)
    four = Mod5(4)

    p_zero = Mod5Poly.zero
    p_one = Mod5Poly.one
    p_two = Mod5Poly.two
    p_three = Mod5Poly.three
    p_four = Mod5Poly.four
    p_m = Mod5Poly.m

    @run_test
    def polynomial_math_works_over_mod5():
        q = (p_m + p_four) * (p_m + p_three)
        assert_str(q, "m**2+(2)*m+2")
        assert q.eval(four) == one
        assert_equal(q.type_string, "SingleVarPoly.Mod5")

    @run_test
    def mod5_polys_conform_to_axioms():
        poly_samples = [
            Mod5Poly.from_list([one, zero, three]),
            Mod5Poly.from_list([three, one, four, two]),
            Mod5Poly.from_list([one, four, two, three, three]),
            Mod5Poly.from_list([two]),
            (p_m * p_two) + p_one,
            (p_m + p_three).raised_to_exponent(15),
        ]
        math = MathHelper(
            value_type=SingleVarPoly,
            zero=p_zero,
            one=p_one,
        )

        verify_ring_properties(math, poly_samples)
