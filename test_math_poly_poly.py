from commutative_ring import verify_ring_properties
from lib.test_helpers import run_test
from poly_integer import IntegerPoly
from poly_poly import PolyPoly
from math_poly_poly import PolyPolyMath

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
