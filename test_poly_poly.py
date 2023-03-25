from lib.test_helpers import assert_equal, assert_str, run_test
from poly_integer import IntegerPoly
from poly_poly import PolyPoly

PP = PolyPoly.from_list

zero = IntegerPoly.zero
one = IntegerPoly.one
two = IntegerPoly.two
x = IntegerPoly.x
three = two + one


@run_test
def check_PolyPoly_basics():
    assert PP([one, two]) + PP([two]) == PP([three, two])
    assert PP([one, one]) * PP([one, one]) == PP([one, two, one])

    pp = PP([one, two, x])
    assert_str(pp, "(x)*p**2+(2)*p+1")
    assert_str(pp.eval(x + one), "x**3+(2)*x**2+(3)*x+3")
    assert_str(pp.eval(x * x * x + three), "x**7+(6)*x**4+(2)*x**3+(9)*x+7")

    assert_str(pp * pp, "(x**2)*p**4+((4)*x)*p**3+((2)*x+4)*p**2+(4)*p+1")

    assert_equal(pp.type_string, "SingleVarPoly.SingleVarPoly.int")


@run_test
def check_eval():
    pp = PolyPoly.p * PolyPoly.p
    assert_str(pp, "p**2")
    p = pp.eval(x + one)
    assert_str(p, "x**2+(2)*x+1")
    assert p.eval(100) == 10201
