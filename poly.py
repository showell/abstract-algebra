from lib.type_enforcers import (
    enforce_list_types,
    enforce_math_protocol,
    enforce_type,
)


def arr_get(lst, i, zero):
    return lst[i] if i < len(lst) else zero


class SingleVarPoly:
    def __init__(self, lst, math, var_name):
        enforce_math_protocol(math)
        enforce_list_types(lst, math.value_type)
        enforce_type(var_name, str)
        self.lst = lst
        self.math = math
        self.var_name = var_name
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

    def __str__(self):
        return self.polynomial_string()

    def additive_inverse(self):
        lst = self.lst
        additive_inverse = self.math.additive_inverse
        return self.new([additive_inverse(elem) for elem in lst])

    def add_with(self, other):
        zero = self.math.zero
        lst1 = self.lst
        lst2 = other.lst
        # do the analog of elementary school arithmetic
        new_size = max(len(lst1), len(lst2))
        return self.new(
            [arr_get(lst1, i, zero) + arr_get(lst2, i, zero) for i in range(new_size)]
        )

    def enforce_partner_type(self, other):
        assert type(other) == SingleVarPoly
        assert type(other.math) == type(self.math)
        assert self.var_name == other.var_name

    def eval(self, x):
        add = self.math.add
        mul = self.math.multiply_by_constant
        power = lambda degree: self.math.power(x, degree)

        result = self.math.zero
        for degree, coeff in enumerate(self.lst):
            term = mul(coeff, power(degree))
            result = add(result, term)
        return result

    def multiply_by_constant(self, c, lst):
        enforce_list_types(lst, self.math.value_type)
        mul = self.math.multiply_by_constant
        return self.new([mul(c, elem) for elem in lst])

    def multiply_with(self, other):
        """
        We are mostly simulating high school arithmetic, but it is probably
        more precise to say that we are creating a discrete convulution of
        our two lists over the non-zero values.

        https://en.wikipedia.org/wiki/Convolution#Discrete_convolution
        """
        zero = self.math.zero
        lst1 = self.lst
        lst2 = other.lst
        # do the analog of elementary school arithmetic
        result = self.new([])
        for i, elem in enumerate(lst1):
            result += self.multiply_by_constant(elem, [zero] * i + lst2)
        return result

    def new(self, lst):
        return SingleVarPoly(lst, self.math, self.var_name)

    def one(self):
        return self.new([self.math.one])

    def polynomial_string(self):
        var_name = self.var_name
        zero = self.math.zero
        one = self.math.one

        if len(self.lst) == 0:
            return str(zero)

        def monomial(coeff, i):
            if i == 0:
                return str(coeff)
            elif i == 1:
                if coeff == one:
                    return var_name
                else:
                    return f"({coeff})*{var_name}"
            else:
                if coeff == one:
                    return f"{var_name}**{i}"
                else:
                    return f"({coeff})*{var_name}**{i}"

        terms = [
            monomial(coeff, degree)
            for degree, coeff in enumerate(self.lst)
            if coeff != zero
        ]
        return "+".join(reversed(terms))

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
    def constant(c, math, var_name):
        enforce_math_protocol(math)
        enforce_type(var_name, str)
        enforce_type(c, math.value_type)
        return SingleVarPoly([c], math, var_name)
