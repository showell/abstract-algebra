from poly import SingleVarPoly
from poly_integer import IntegerPoly
from math_poly_integer import IntegerPolyMath


class PolyPoly:
    const = lambda c: SingleVarPoly.constant(IntegerPolyMath, c)
    zero = const(IntegerPoly.zero)
    one = const(IntegerPoly.one)
    p = SingleVarPoly.degree_one_var(IntegerPolyMath, "p")

    @staticmethod
    def from_list(lst):
        return SingleVarPoly(IntegerPolyMath, lst, "p")
