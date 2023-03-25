from math_helper import MathHelper
from poly import SingleVarPoly
from poly_integer import IntegerPoly


IntegerPolyMath = MathHelper(
    value_type=SingleVarPoly,
    zero=IntegerPoly.zero,
    one=IntegerPoly.one,
)
