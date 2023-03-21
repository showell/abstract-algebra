from mod5 import Mod5
from poly import SingleVarPoly


class Mod5Math:
    add = lambda a, b: a + b
    additive_inverse = lambda a: -a
    multiply_by_constant = lambda a, b: a * b
    power = lambda m, exp: m**exp
    value_type = Mod5

    zero = Mod5(0)
    one = Mod5(1)
    two = Mod5(2)
    three = Mod5(3)
    four = Mod5(4)


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
    from commutative_ring import verify_axioms
    from lib.test_helpers import assert_str, run_test

    zero = Mod5Math.zero
    one = Mod5Math.one
    two = Mod5Math.two
    three = Mod5Math.three
    four = Mod5Math.four

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
        verify_axioms(poly_samples, zero=p_zero, one=p_one)
