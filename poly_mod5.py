from mod5 import Mod5
from math_mod5 import Mod5Math
from poly import SingleVarPoly


class Mod5Poly:
    const = lambda c: SingleVarPoly.constant(Mod5Math, Mod5(c))
    zero = const(0)
    one = const(1)
    two = const(2)
    three = const(3)
    four = const(4)
    m = SingleVarPoly.degree_one_var(Mod5Math, "m")

    @staticmethod
    def from_list(lst):
        return SingleVarPoly(Mod5Math, lst, "m")
