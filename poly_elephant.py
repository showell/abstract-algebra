from elephant import Elephant
from math_elephant import ElephantIntegerMath
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
