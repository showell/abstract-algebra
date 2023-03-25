from mod5 import Mod5
from math_mod5 import Mod5Math
from commutative_ring import verify_ring_properties
from lib.test_helpers import run_test

zero = Mod5(0)
one = Mod5(1)
two = Mod5(2)
three = Mod5(3)
four = Mod5(4)


@run_test
def mod5_is_a_ring():
    samples = [
        zero,
        one,
        two,
        three,
        four,
    ]

    verify_ring_properties(Mod5Math, samples)
