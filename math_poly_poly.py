from poly import SingleVarPoly
from poly_poly import PolyPoly
from math_helper import MathHelper


PolyPolyMath = MathHelper(
    value_type=SingleVarPoly,
    zero=PolyPoly.zero,
    one=PolyPoly.one,
)


if __name__ == "__main__":
    from commutative_ring import verify_ring_properties
    from lib.test_helpers import run_test
    from poly_integer import IntegerPoly

    PP = PolyPoly.from_list

    zero = IntegerPoly.zero
    one = IntegerPoly.one
    two = IntegerPoly.two
    x = IntegerPoly.x
    three = two + one

    @run_test
    def check_PolyPoly_is_ring():
        p = (x + one) * (x + three) * (x + one) + two
        q = p.raised_to_exponent(3)

        samples = [
            PP([one, two, three]),
            PP([p, q, x, p, q, x]),
            PP([x + one, x + two, p + three]),
        ]

        verify_ring_properties(PolyPolyMath, samples)
