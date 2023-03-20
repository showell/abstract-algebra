from mod5 import Mod5
from single_poly import SingleVarPoly

class Mod5Math:
    add = lambda a, b: a + b
    additive_inverse = lambda a: -a
    multiply_by_constant = lambda a, b: a * b
    power = lambda m, exp: m**exp
    value_type = Mod5

    zero = Mod5(0)
    one = Mod5(1)


def Mod5Poly(lst):
    return SingleVarPoly(lst, Mod5Math, "x")


if __name__ == "__main__":
    from commutative_ring import verify_axioms
    from lib.test_helpers import assert_str, run_test

    zero = Mod5Math.zero
    one = Mod5Math.one
    two = Mod5(2)
    three = Mod5(3)
    four = Mod5(4)

    p_zero = Mod5Poly([])
    p_one = Mod5Poly([one])
    p_two = Mod5Poly([two])
    p_three = Mod5Poly([three])
    p_four = Mod5Poly([four])
    p_x = Mod5Poly([zero, one])

    @run_test
    def polynomial_math_works_over_mod5():
        q = (p_x + p_four) * (p_x + p_three)
        assert_str(q, "x**2+(2)*x+2")
        assert q.eval(four) == one

    @run_test
    def mod5_polys_conform_to_axioms():
        poly_samples = [
            Mod5Poly([one, zero, three]),
            Mod5Poly([three, one, four, two]),
            Mod5Poly([two]),
            (p_x * p_two) + p_one,
            (p_x + p_three).raised_to_exponent(15),
        ]
        verify_axioms(poly_samples, zero=p_zero, one=p_one)
