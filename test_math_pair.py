from pair import Pair
from math_pair import PairMath
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
