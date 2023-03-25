from mod5 import Mod5
from lib.test_helpers import run_test

zero = Mod5(0)
one = Mod5(1)
two = Mod5(2)
three = Mod5(3)
four = Mod5(4)


@run_test
def verify_exponentiation():
    for m in [zero, one, two, three, four]:
        assert m**0 == one
        assert m**1 == m

        product = one
        for exp in range(30):
            assert m**exp == product
            product *= m
