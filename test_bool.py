from bool import Bool
from lib.test_helpers import run_test

F = Bool(False)
T = Bool(True)


@run_test
def truth_tables():
    assert F + F == F
    assert F + T == T
    assert T + F == T
    assert T + T == T

    assert F * F == F
    assert F * T == F
    assert T * F == F
    assert T * T == T

    assert T == T
    assert F == F
    assert F != T


@run_test
def exponentiation():
    assert T * T == T**2
    assert F * F == F**2

    assert T * T * T == T**3
    assert F * F * F == F**3

    assert T**47 == T
    assert F**942 == F
    assert F**0 == T
    assert F**1 == F
    assert T**0 == T
    assert T**1 == T
