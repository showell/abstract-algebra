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

    @staticmethod
    def from_list(lst):
        return SingleVarPoly(BoolMath, lst, "p")


if __name__ == "__main__":
    from lib.test_helpers import assert_str, run_test

    @run_test
    def show():
        F = Bool(False)
        T = Bool(True)

        x = BoolPoly.from_list([T, F, T, F, T, F, T])
        y = BoolPoly.from_list([F, F, F, T])
        z = BoolPoly.from_list([F, F, F, F, T])
        p = x * y * z
        assert_str(p, "p**13+p**11+p**9+p**7")

        assert p.eval(F) == F
        assert p.eval(T) == T
