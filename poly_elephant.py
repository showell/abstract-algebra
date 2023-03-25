from elephant import Elephant, ElephantIntegerMath
from poly import SingleVarPoly


class ElephantIntegerPoly:
    const = lambda c: SingleVarPoly.constant(
        ElephantIntegerMath,
        Elephant.make(c),
    )
    zero = const(0)
    one = const(1)
    x = SingleVarPoly.degree_one_var(ElephantIntegerMath, "x")

    @staticmethod
    def from_list(lst):
        return SingleVarPoly(ElephantIntegerMath, lst, "x")


if __name__ == "__main__":
    from commutative_ring import verify_ring_properties
    from lib.test_helpers import assert_equal, assert_str, run_test
    from math_helper import MathHelper

    @run_test
    def test_basics():
        x = ElephantIntegerPoly.x
        assert_equal(x.type_string, "SingleVarPoly.Elephant")

        two = ElephantIntegerPoly.const(2)
        three = ElephantIntegerPoly.const(3)
        p = (x + two) * (x + three)
        assert_str(p, "x**2+(5)*x+6")
        n = p.eval(Elephant.make(4))
        assert n.val == 42
        assert_str(
            n.history,
            "(((0 + ((2 * 3) * (4)**0)) + (((2 * 1) + (1 * 3)) * (4)**1)) + ((1 * 1) * (4)**2))",
        )

    @run_test
    def test_axioms():
        x = ElephantIntegerPoly.x
        one = ElephantIntegerPoly.one
        two = ElephantIntegerPoly.const(2)
        three = ElephantIntegerPoly.const(3)
        samples = [
            (x + two) ** 3,
            (x + one),
            three,
            two * three,
        ]

        math = MathHelper(
            value_type=SingleVarPoly,
            zero=ElephantIntegerPoly.zero,
            one=ElephantIntegerPoly.one,
        )
        verify_ring_properties(math, samples)
