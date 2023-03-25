from commutative_ring import verify_monoid, verify_ring_properties
from fractions import Fraction
from math_helper import MathHelper
from lib.test_helpers import run_test


@run_test
def check_integers_are_ring():
    integer_math = MathHelper(
        value_type=int,
        zero=0,
        one=1,
    )
    samples = [-7, 42, 13, 9, 4567, 14]
    verify_ring_properties(integer_math, samples)


@run_test
def check_fractions_are_ring():
    fraction_math = MathHelper(
        value_type=Fraction,
        zero=Fraction(0),
        one=Fraction(1),
    )
    samples = [Fraction(1, 3), Fraction(-2, 7), Fraction(43, 13)]
    verify_ring_properties(fraction_math, samples)


@run_test
def verify_python_lists_form_a_monoid():
    samples = [
        [1, 2, 3],
        [99, 42, -7],
        ["whatever"],
    ]
    concat = lambda lst1, lst2: lst1 + lst2
    verify_monoid(samples, identity=[], combine=concat)
