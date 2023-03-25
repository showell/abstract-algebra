from poly import SingleVarPoly
from poly_poly import PolyPoly
from math_helper import MathHelper


PolyPolyMath = MathHelper(
    value_type=SingleVarPoly,
    zero=PolyPoly.zero,
    one=PolyPoly.one,
)
