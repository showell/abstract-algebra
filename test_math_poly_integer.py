from commutative_ring import verify_ring_properties
from lib.test_helpers import run_test
from poly_integer import IntegerPoly
from math_poly_integer import IntegerPolyMath

IP = IntegerPoly.from_list


@run_test
def check_IntegerPoly_is_ring():
    samples = [
        IP([]),
        IP([42, 39, 2]),
        IP([-8, 0, 0, 0, 5]),
        IP([103, 8256523499]),
    ]

    verify_ring_properties(IntegerPolyMath, samples)
