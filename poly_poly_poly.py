from poly import SingleVarPoly
from poly_integer import IntegerPoly
from poly_poly import PolyPoly
from lib.abstract_math import AbstractMath


PolyPolyMath = AbstractMath(
    value_type=SingleVarPoly,
    zero=PolyPoly.zero,
    one=PolyPoly.one,
)


class PolyPolyPoly:
    const = lambda c: SingleVarPoly.constant(PolyPolyMath, c)
    zero = const(PolyPoly.zero)
    one = const(PolyPoly.one)
    q = SingleVarPoly.degree_one_var(PolyPolyMath, "q")

    @staticmethod
    def from_list(lst):
        return SingleVarPoly(PolyPolyMath, lst, "q")


if __name__ == "__main__":
    from commutative_ring import verify_axioms
    from lib.test_helpers import assert_str, run_test

    IP = IntegerPoly.from_list
    PP = PolyPoly.from_list
    PPP = PolyPolyPoly.from_list

    ip_a = IP([1, 2])
    ip_b = IP([3, 4])
    ip_c = ip_a * ip_b

    assert_str(ip_a, "(2)*x+1")
    assert_str(ip_b, "(4)*x+3")
    assert_str(ip_c, "(8)*x**2+(10)*x+3")

    pp_a = PP([ip_a, ip_c])
    pp_b = PP([ip_b, ip_a])
    pp_c = pp_a * pp_b

    assert_str(
        pp_c,
        "((16)*x**3+(28)*x**2+(16)*x+3)*p**2+((32)*x**3+(68)*x**2+(46)*x+10)*p+(8)*x**2+(10)*x+3",
    )

    ppp_a = PPP([pp_a, pp_c])

    assert_str(
        ppp_a,
        "(((16)*x**3+(28)*x**2+(16)*x+3)*p**2+((32)*x**3+(68)*x**2+(46)*x+10)*p+(8)*x**2+(10)*x+3)*q+((8)*x**2+(10)*x+3)*p+(2)*x+1",
    )

    # Now start evaluating.
    pp_d = ppp_a.eval(pp_c)
    assert_str(
        pp_d,
        "((256)*x**6+(896)*x**5+(1296)*x**4+(992)*x**3+(424)*x**2+(96)*x+9)*p**4+((1024)*x**6+(3968)*x**5+(6304)*x**4+(5264)*x**3+(2440)*x**2+(596)*x+60)*p**3+((1024)*x**6+(4608)*x**5+(8336)*x**4+(7808)*x**3+(4012)*x**2+(1076)*x+118)*p**2+((512)*x**5+(1728)*x**4+(2288)*x**3+(1496)*x**2+(486)*x+63)*p+(64)*x**4+(160)*x**3+(148)*x**2+(62)*x+10",
    )

    ip_d = pp_d.eval(ip_a)
    assert_str(
        ip_d,
        "(4096)*x**10+(30720)*x**9+(103680)*x**8+(207616)*x**7+(273472)*x**6+(247808)*x**5+(156544)*x**4+(68112)*x**3+(19548)*x**2+(3346)*x+260",
    )

    big_int = ip_d.eval(1000000000)
    assert (
        big_int
        == 4096000030720000103680000207616000273472000247808000156544000068112000019548000003346000000260
    )

    @run_test
    def verify_ring_axioms():
        # This takes a while!!!
        samples = [
            PPP([pp_a, pp_d, pp_c]),
            PPP([pp_c, pp_a]),
            PPP([pp_a, pp_d]),
            PPP([pp_b]),
        ]

        verify_axioms(samples, zero=PolyPolyPoly.zero, one=PolyPolyPoly.one)
