from bool import Bool
from math_bool import BoolMath
from poly import SingleVarPoly


class BoolPoly:
    const = lambda c: SingleVarPoly.constant(BoolMath, Bool(c))
    zero = const(False)
    one = const(True)
    p = SingleVarPoly.degree_one_var(BoolMath, "p")

    @staticmethod
    def from_list(lst):
        return SingleVarPoly(BoolMath, lst, "p")

    @staticmethod
    def from_ints(ints):
        assert type(ints) == set
        F = Bool(False)
        T = Bool(True)

        lst = [T if n in ints else F for n in range(max(ints) + 1)]

        return BoolPoly.from_list(lst)

    @staticmethod
    def to_ints(bp):
        T = Bool(True)
        nums = [i for i, b in enumerate(bp.lst) if b == T]
        return sorted(nums)
