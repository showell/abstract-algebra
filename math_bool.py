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
