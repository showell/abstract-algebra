from math_pair import PairMath
from poly import SingleVarPoly


class PairPoly:
    const = lambda c: SingleVarPoly.constant(PairMath, c)
    zero = const(PairMath.zero)
    one = const(PairMath.one)
    t = SingleVarPoly.degree_one_var(PairMath, "t")
