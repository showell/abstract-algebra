from pair import Pair
from poly import SingleVarPoly
from lib.abstract_math import AbstractMath


PairMath = AbstractMath(
    value_type=Pair,
    zero=Pair(0, 0),
    one=Pair(1, 1),
)


class PairPoly:
    const = lambda c: SingleVarPoly.constant(PairMath, c)
    zero = const(PairMath.zero)
    one = const(PairMath.one)
    t = SingleVarPoly.degree_one_var(PairMath, "t")


if __name__ == "__main__":
    from commutative_ring import verify_ring_properties
    from lib.test_helpers import assert_equal, assert_str, run_test

    @run_test
    def show_basics():
        c1 = PairPoly.const(Pair(1, 14))
        c2 = PairPoly.const(Pair(41, 7))

        t = PairPoly.t
        assert_equal(t.type_string, "SingleVarPoly.Pair")

        p = (t + c1) * (t + c2)
        assert_str(p, "t**2+((42, 21))*t+(41, 98)")

        assert_equal(
            p.eval(Pair(1000000, 10000)),
            Pair(1000042000041, 100210098),
        )

    @run_test
    def check_is_ring():
        c1 = PairPoly.const(Pair(111, -214))
        c2 = PairPoly.const(Pair(421, 77))
        t = PairPoly.t

        samples = [
            t + c1,
            c1 * c2,
            c2**4,
            (t + c1) ** 3,
        ]

        verify_ring_properties(samples, zero=PairPoly.zero, one=PairPoly.one)
