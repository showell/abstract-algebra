from commutative_ring import verify_ring_properties
from lib.test_helpers import assert_equal, run_test
from math_helper import MathHelper
from number_list import NumberList


@run_test
def verify_basics():
    assert NumberList([1, 0, 2]) + NumberList([2, 4, 7, 8]) == NumberList([3, 4, 9, 8])
    assert 201 + 8742 == 8943

    assert NumberList([1, 2]) * NumberList([1, 3]) == NumberList([1, 5, 6])
    assert 21 * 31 == 651

    assert NumberList([7, 8]) * NumberList([1, 6]) == NumberList([7, 50, 48])
    assert 87 * 61 == 48 * 100 + 50 * 10 + 7


@run_test
def verify_equality_check():
    assert NumberList([5, 2]) == NumberList([5, 2])
    assert NumberList([5]) != NumberList([5, 2])


@run_test
def number_list_is_a_ring():
    samples = [
        NumberList([]),
        NumberList([42, 39, 2]),
        NumberList([-8, 0, 0, 0, 5]),
        NumberList([103, 8256523499]),
    ]
    math = MathHelper(
        value_type=NumberList,
        zero=NumberList([]),
        one=NumberList([1]),
    )
    verify_ring_properties(math, samples)


@run_test
def exponentiation():
    x = NumberList([5, 7, -21])
    assert_equal(x**3, x * x * x)
