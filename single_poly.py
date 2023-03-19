def arr_get(lst, i, zero):
    return lst[i] if i < len(lst) else zero


def enforce_list_types(lst, _type):
    assert type(lst) == list
    for elem in lst:
        assert type(elem) == _type


def enforce_type(x, _type):
    assert type(x) == _type


def enforce_math_protocol(math):
    assert hasattr(math, "add")
    assert hasattr(math, "additive_inverse")
    assert hasattr(math, "multiply_by_constant")
    assert hasattr(math, "power")
    assert hasattr(math, "value_type")
    assert hasattr(math, "one")
    assert hasattr(math, "zero")
    assert callable(math.add)
    assert callable(math.additive_inverse)
    assert callable(math.multiply_by_constant)
    assert callable(math.power)
    one = math.one
    zero = math.zero
    power = math.power
    add = math.add
    assert type(one) == math.value_type
    assert type(zero) == math.value_type
    assert power(zero, 0) == one
    assert power(one, 0) == one
    assert power(one, 1) == one
    assert power(one, 2) == one


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
    def base_values(math, var_name):
        enforce_math_protocol(math)
        enforce_type(var_name, str)
        make = lambda lst: SingleVarPoly(lst, math, var_name)
        zero = make([])
        one = make([math.one])
        x = make([math.zero, math.one])
        return zero, one, x

    @staticmethod
    def constant(c, math, var_name):
        enforce_math_protocol(math)
        enforce_type(var_name, str)
        enforce_type(c, math.value_type)
        return SingleVarPoly([c], math, var_name)


if __name__ == "__main__":
    import commutative_ring

    def assert_str(p, expected_str):
        if str(p) != expected_str:
            raise AssertionError(f"got {p} when expecting {expected_str}")

    class IntegerMath:
        add = lambda a, b: a + b
        additive_inverse = lambda a: -a
        multiply_by_constant = lambda a, b: a * b
        power = lambda n, p: n**p
        value_type = int
        zero = 0
        one = 1

    def IntegerPoly(lst):
        return SingleVarPoly(lst, IntegerMath, "x")

    assert IntegerPoly([1, 0, 2]) + IntegerPoly([2, 4, 7, 8]) == IntegerPoly(
        [3, 4, 9, 8]
    )
    assert 201 + 8742 == 8943

    assert IntegerPoly([1, 2]) * IntegerPoly([1, 3]) == IntegerPoly([1, 5, 6])
    assert 21 * 31 == 651

    assert IntegerPoly([7, 8]) * IntegerPoly([1, 6]) == IntegerPoly([7, 50, 48])
    assert 87 * 61 == 48 * 100 + 50 * 10 + 7

    samples = [
        IntegerPoly([]),
        IntegerPoly([42, 39, 2]),
        IntegerPoly([-8, 0, 0, 0, 5]),
        IntegerPoly([103, 8256523499]),
    ]

    zero, one, x = SingleVarPoly.base_values(IntegerMath, "x")
    commutative_ring.test(samples, zero=zero, one=one)

    two = SingleVarPoly.constant(2, IntegerMath, "x")
    three = two + one

    assert_str(zero, "0")
    assert_str(one, "1")
    assert_str(two, "2")
    assert_str(three, "3")
    assert_str(x, "x")
    assert_str(IntegerPoly([1, 2, 3, 4]), "(4)*x**3+(3)*x**2+(2)*x+1")

    p = (x + one) * (x + three) * (x + one) + two
    assert_str(p, "x**3+(5)*x**2+(7)*x+5")

    assert p.eval(10) == 1575
    assert p.eval(100) == 1050705

    q = p.raised_to_exponent(3)
    assert_str(
        q,
        "x**9+(15)*x**8+(96)*x**7+(350)*x**6+(822)*x**5+(1320)*x**4+(1468)*x**3+(1110)*x**2+(525)*x+125",
    )

    ip_zero = zero
    ip_one = one

    class IntegerPolyMath:
        add = lambda a, b: a + b
        additive_inverse = lambda a: -a
        multiply_by_constant = lambda a, b: a * b
        power = lambda poly, exp: poly.raised_to_exponent(exp)
        value_type = SingleVarPoly
        zero = ip_zero
        one = ip_one

    def PolyPoly(lst):
        return SingleVarPoly(lst, IntegerPolyMath, "p")

    assert PolyPoly([one, two]) + PolyPoly([two]) == PolyPoly([three, two])
    assert PolyPoly([one, one]) * PolyPoly([one, one]) == PolyPoly([one, two, one])

    pp = PolyPoly([one, two, x])
    assert_str(pp, "(x)*p**2+(2)*p+1")
    assert_str(pp * pp, "(x**2)*p**4+((4)*x)*p**3+((2)*x+4)*p**2+(4)*p+1")
    assert_str(pp.eval(x + one), "x**3+(2)*x**2+(3)*x+3")
    assert_str(pp.eval(x * x * x + three), "x**7+(6)*x**4+(2)*x**3+(9)*x+7")

    samples = [
        PolyPoly([one, two, three]),
        PolyPoly([p, q, x, p, q, x]),
        PolyPoly([x + one, x + two, p + three]),
    ]

    pp_zero = PolyPoly([])
    pp_one = PolyPoly([one])

    commutative_ring.test(samples, zero=pp_zero, one=pp_one)
