from poly import SingleVarPoly
from poly_integer import IntegerPoly


class IntegerPolyMath:
    add = lambda a, b: a + b
    additive_inverse = lambda a: -a
    multiply_by_constant = lambda a, b: a * b
    power = lambda poly, exp: poly.raised_to_exponent(exp)
    value_type = SingleVarPoly
    zero = IntegerPoly.zero
    one = IntegerPoly.one


class PolyPoly:
    zero = SingleVarPoly.constant(IntegerPoly.zero, IntegerPolyMath, "p")
    one = SingleVarPoly.constant(IntegerPoly.one, IntegerPolyMath, "p")

    @staticmethod
    def from_list(lst):
        return SingleVarPoly(lst, IntegerPolyMath, "p")


if __name__ == "__main__":
    from commutative_ring import verify_axioms
    from lib.test_helpers import assert_str, run_test

    PP = PolyPoly.from_list

    zero = IntegerPoly.zero
    one = IntegerPoly.one
    two = IntegerPoly.two
    x = IntegerPoly.x
    three = two + one

    @run_test
    def check_PolyPoly_basics():
        assert PP([one, two]) + PP([two]) == PP([three, two])
        assert PP([one, one]) * PP([one, one]) == PP([one, two, one])

        pp = PP([one, two, x])
        assert_str(pp, "(x)*p**2+(2)*p+1")
        assert_str(pp.eval(x + one), "x**3+(2)*x**2+(3)*x+3")
        assert_str(pp.eval(x * x * x + three), "x**7+(6)*x**4+(2)*x**3+(9)*x+7")

        assert_str(pp * pp, "(x**2)*p**4+((4)*x)*p**3+((2)*x+4)*p**2+(4)*p+1")

    p = (x + one) * (x + three) * (x + one) + two
    q = p.raised_to_exponent(3)

    @run_test
    def check_PolyPoly_is_ring():
        samples = [
            PP([one, two, three]),
            PP([p, q, x, p, q, x]),
            PP([x + one, x + two, p + three]),
        ]

        verify_axioms(samples, zero=PolyPoly.zero, one=PolyPoly.one)
