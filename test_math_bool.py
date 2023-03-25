from bool import Bool
from math_bool import BoolMath
from lib.test_helpers import run_test
from commutative_ring import verify_semiring


@run_test
def Bool_is_semi_ring():
    F = Bool(False)
    T = Bool(True)

    verify_semiring(BoolMath, [T, F])
