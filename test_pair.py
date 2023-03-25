from pair import Pair
from lib.test_helpers import run_test


@run_test
def verify_exponentiation():
    zero = Pair(0, 0)
    one = Pair(1, 1)
    x = Pair(5, -3)
    y = Pair(152, 4)
    z = Pair(-9, 7)
    for pair in [zero, one, x, y, z]:
        product = one
        for exp in range(30):
            assert pair**exp == product
            product *= pair
