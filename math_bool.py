from math_helper import MathHelper
from bool import Bool


def NOT_DEFINED():
    raise AssertionError("We don't allow boolean negation")


BoolMath = MathHelper(
    value_type=Bool,
    zero=Bool(False),
    one=Bool(True),
)

BoolMath.additive_inverse = NOT_DEFINED


if __name__ == "__main__":
    from lib.test_helpers import run_test
    from commutative_ring import verify_semiring

    F = Bool(False)
    T = Bool(True)

    @run_test
    def Bool_is_semi_ring():
        verify_semiring(BoolMath, [T, F])
