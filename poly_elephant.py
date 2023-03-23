from elephant import Elephant
from poly import SingleVarPoly
from lib.abstract_math import AbstractMath


class ElephantMath(AbstractMath):
    def __init__(self, *, zero, one):
        self.value_type = Elephant
        self.zero = zero
        self.one = one
        self.add = Elephant.add
        self.additive_inverse = Elephant.additive_inverse
        self.multiply = Elephant.multiply
        self.power = Elephant.power


ElephantIntegerMath = ElephantMath(
    zero=Elephant.make(0),
    one=Elephant.make(1),
)


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
    from commutative_ring import verify_axioms
    from lib.test_helpers import assert_str, run_test

    @run_test
    def test_basics():
        x = ElephantIntegerPoly.x
        two = ElephantIntegerPoly.const(2)
        three = ElephantIntegerPoly.const(3)
        p = (x + two) * (x + three)
        assert_str(p, "x**2+(5)*x+6")
        n = p.eval(Elephant.make(4))
        assert n.val == 42
        assert (
            n.history
            == "(((0 + ((0 + (((0 + 0) + 2) * ((0 + 0) + 3))) * (4)**0)) + (((0 + (((0 + 0) + 2) * (0 + 1))) + ((0 + 1) * ((0 + 0) + 3))) * (4)**1)) + ((0 + ((0 + 1) * (0 + 1))) * (4)**2))"
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

        verify_axioms(
            samples,
            zero=ElephantIntegerPoly.zero,
            one=ElephantIntegerPoly.one,
        )
