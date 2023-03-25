from poly import SingleVarPoly
from poly_poly import PolyPoly
from math_poly_poly import PolyPolyMath


class PolyPolyPoly:
    const = lambda c: SingleVarPoly.constant(PolyPolyMath, c)
    zero = const(PolyPoly.zero)
    one = const(PolyPoly.one)
    q = SingleVarPoly.degree_one_var(PolyPolyMath, "q")

    @staticmethod
    def from_list(lst):
        return SingleVarPoly(PolyPolyMath, lst, "q")
