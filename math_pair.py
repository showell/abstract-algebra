from math_helper import MathHelper
from pair import Pair


PairMath = MathHelper(
    value_type=Pair,
    zero=Pair(0, 0),
    one=Pair(1, 1),
)


if __name__ == "__main__":
    from commutative_ring import verify_ring_properties
    from lib.test_helpers import run_test

    @run_test
    def pair_is_a_ring():
        samples = [
            Pair(0, 5),
            Pair(777777, -2),
            Pair(43, -69),
            Pair(-2, 4),
        ]

        verify_ring_properties(PairMath, samples)
