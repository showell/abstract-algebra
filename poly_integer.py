from math_helper import MathHelper
from poly import SingleVarPoly


IntegerMath = MathHelper(
    value_type=int,
    zero=0,
    one=1,
)


class IntegerPoly:
    const = lambda c: SingleVarPoly.constant(IntegerMath, c)
    zero = const(0)
    one = const(1)
    two = const(2)
    x = SingleVarPoly.degree_one_var(IntegerMath, "x")

    @staticmethod
    def from_list(lst):
        return SingleVarPoly(IntegerMath, lst, "x")
