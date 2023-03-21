from bool import Bool
from poly import SingleVarPoly


def NOT_DEFINED():
    raise AssertionError("We don't allow boolean negation")


class BoolMath:
    add = lambda a, b: a + b
    additive_inverse = NOT_DEFINED
    multiply_by_constant = lambda a, b: a * b
    power = lambda n, p: n**p
    value_type = Bool
    zero = Bool(False)
    one = Bool(True)


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


if __name__ == "__main__":
    from lib.test_helpers import assert_str, run_test

    @run_test
    def show_relation_to_ints():
        F = Bool(False)
        T = Bool(True)

        x = BoolPoly.from_ints({0, 2, 4, 6})
        y = BoolPoly.from_ints({3})
        z = BoolPoly.from_ints({4})

        b = BoolPoly.p
        assert x == b**0 + b**2 + b**4 + b**6
        assert y == b**3
        assert z == b**4

        p = x * y * z
        assert_str(p, "p**13+p**11+p**9+p**7")
        assert BoolPoly.to_ints(p) == [7, 9, 11, 13]
        assert 7 == 0 + 3 + 4
        assert 9 == 2 + 3 + 4
        assert 11 == 4 + 3 + 4
        assert 13 == 6 + 3 + 4

        q = x + y + z
        assert_str(q, "p**6+p**4+p**3+p**2+True")
        assert BoolPoly.to_ints(q) == [0, 2, 3, 4, 6]

        # Evaluating boolean polynomials is kind of silly, since
        # we are only really looking at the "constant" coefficient.
        assert p.eval(F) == F
        assert p.eval(T) == T

        assert q.eval(F) == T
        assert q.eval(T) == T
