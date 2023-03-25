from elephant import Elephant
from math_elephant import ElephantIntegerMath
from commutative_ring import verify_ring_properties
from lib.test_helpers import run_test


@run_test
def elephant_integers_form_a_ring():
    samples = [
        Elephant.make(4),
        Elephant.make(555),
        Elephant.make(-13),
        Elephant.make(37),
    ]
    verify_ring_properties(ElephantIntegerMath, samples)
