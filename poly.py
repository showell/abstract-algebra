from lib.type_enforcers import (
    enforce_list_types,
    enforce_type,
)
import polynomial_algorithms


def enforce_math_type(math):
    assert hasattr(math, "add")
    assert hasattr(math, "additive_inverse")
    assert hasattr(math, "multiply")
    assert hasattr(math, "one")
    assert hasattr(math, "power")
    assert hasattr(math, "type_string")
    assert hasattr(math, "value_type")
    assert hasattr(math, "zero")
    assert callable(math.add)
    assert callable(math.additive_inverse)
    assert callable(math.multiply)
    assert callable(math.power)
    enforce_type(math.zero, math.value_type)
    enforce_type(math.one, math.value_type)
    enforce_type(math.type_string, str)


class SingleVarPoly:
    def __init__(self, math, lst, var_name):
        enforce_math_type(math)
        enforce_list_types(lst, math.value_type)
        if len(lst) > 1 and var_name is not None:
            enforce_type(var_name, str)
        self.lst = lst
        self.math = math
        self.var_name = var_name
        assert hasattr(math, "type_string")
        enforce_type(math.type_string, str)
        self.type_string = f"SingleVarPoly.{math.type_string}"
        self.simplify()

    def __add__(self, other):
        self.enforce_partner_type(other)
        return self.add_with(other)

    def __eq__(self, other):
        self.enforce_partner_type(other)
        return self.lst == other.lst

    def __mul__(self, other):
        self.enforce_partner_type(other)
        return self.multiply_with(other)

    def __neg__(self):
        return self.additive_inverse()

    def __pow__(self, exponent):
        return self.raised_to_exponent(exponent)

    def __str__(self):
        return self.polynomial_string()

    def additive_inverse(self):
        lst = self.lst
        additive_inverse = self.math.additive_inverse
        return self.new([additive_inverse(elem) for elem in lst])

    def add_with(self, other):
        if other.is_zero():
            return self

        zero = self.math.zero
        lst1 = self.lst
        lst2 = other.lst
        add = self.math.add

        lst = polynomial_algorithms.add(lst1, lst2, add=add, zero=zero)

        var_name = self.var_name or other.var_name
        return SingleVarPoly(self.math, lst, var_name)

    def enforce_partner_type(self, other):
        assert type(other) == SingleVarPoly
        assert type(other.math) == type(self.math)
        assert type(self) == type(other)
        if self.var_name is not None and other.var_name is not None:
            assert self.var_name == other.var_name

    def eval(self, x):
        add = self.math.add
        mul = self.math.multiply
        zero = self.math.zero
        power = lambda degree: self.math.power(x, degree)
        lst = self.lst
        return polynomial_algorithms.eval(lst, zero=zero, add=add, mul=mul, power=power)

    def is_one(self):
        return len(self.lst) == 1 and self.lst[0] == self.math.one

    def is_zero(self):
        return len(self.lst) == 0

    def multiply_with(self, other):
        if other.is_zero():
            return other

        if other.is_one():
            return self

        zero = self.math.zero
        add = self.math.add
        mul = self.math.multiply
        lst1 = self.lst
        lst2 = other.lst

        lst = polynomial_algorithms.multiply(lst1, lst2, add=add, mul=mul, zero=zero)
        var_name = self.var_name or other.var_name
        return SingleVarPoly(self.math, lst, var_name)

    def new(self, lst):
        return SingleVarPoly(self.math, lst, self.var_name)

    def one(self):
        return self.new([self.math.one])

    def polynomial_string(self):
        var_name = self.var_name
        zero = self.math.zero
        one = self.math.one
        lst = self.lst
        return polynomial_algorithms.stringify(
            lst, var_name=var_name, zero=zero, one=one
        )

    def raised_to_exponent(self, exponent):
        enforce_type(exponent, int)
        if exponent < 0:
            raise ValueError("we do not support negative exponents")

        if exponent == 0:
            return self.one()
        if exponent == 1:
            return self
        return self * self.raised_to_exponent(exponent - 1)

    def simplify(self):
        lst = self.lst
        zero = self.math.zero
        while lst and lst[-1] == zero:
            lst = lst[:-1]
        self.lst = lst

    @staticmethod
    def constant(math, c):
        enforce_type(c, math.value_type)
        return SingleVarPoly(math, [c], None)

    @staticmethod
    def degree_one_var(math, var_name):
        enforce_type(var_name, str)
        return SingleVarPoly(math, [math.zero, math.one], var_name)
