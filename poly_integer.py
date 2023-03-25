from math_helper import MathHelper
from poly import SingleVarPoly


IntegerMath = MathHelper(
    value_type=int,
    zero=0,
    one=1,
)


class IntegerPoly:
    const = lambda c: SingleVarPoly.constant(IntegerMath, c)
    zero = const(0)
    one = const(1)
    two = const(2)
    x = SingleVarPoly.degree_one_var(IntegerMath, "x")

    @staticmethod
    def from_list(lst):
        return SingleVarPoly(IntegerMath, lst, "x")


IntegerPolyMath = MathHelper(
    value_type=SingleVarPoly,
    zero=IntegerPoly.zero,
    one=IntegerPoly.one,
)


if __name__ == "__main__":
    from commutative_ring import verify_ring_properties
    from lib.test_helpers import assert_equal, assert_str, run_test

    IP = IntegerPoly.from_list

    @run_test
    def check_IntegerPoly_basics():
        assert IP([1, 0, 2]) + IP([2, 4, 7, 8]) == IP([3, 4, 9, 8])
        assert 201 + 8742 == 8943

        assert IP([1, 2]) * IP([1, 3]) == IP([1, 5, 6])
        assert 21 * 31 == 651

        assert IP([7, 8]) * IP([1, 6]) == IP([7, 50, 48])
        assert 87 * 61 == 48 * 100 + 50 * 10 + 7

    @run_test
    def check_IntegerPoly_is_ring():
        samples = [
            IP([]),
            IP([42, 39, 2]),
            IP([-8, 0, 0, 0, 5]),
            IP([103, 8256523499]),
        ]

        verify_ring_properties(IntegerPolyMath, samples)

    zero = IntegerPoly.zero
    one = IntegerPoly.one
    two = IntegerPoly.two
    x = IntegerPoly.x
    three = two + one

    @run_test
    def check_SingleVarPoly_basics():
        assert_str(zero, "0")
        assert_str(one, "1")
        assert_str(two, "2")
        assert_str(three, "3")
        assert_str(x, "x")
        assert_str(IP([1, 2, 3, 4]), "(4)*x**3+(3)*x**2+(2)*x+1")

    p = (x + one) * (x + three) * (x + one) + two
    assert_equal(p.type_string, "SingleVarPoly.int")

    @run_test
    def check_eval():
        assert_str(p, "x**3+(5)*x**2+(7)*x+5")

        assert p.eval(10) == 1575
        assert p.eval(100) == 1050705

    @run_test
    def check_exponentiation():
        q = p.raised_to_exponent(3)
        assert_str(
            q,
            "x**9+(15)*x**8+(96)*x**7+(350)*x**6+(822)*x**5+(1320)*x**4+(1468)*x**3+(1110)*x**2+(525)*x+125",
        )
