class Mod5:
    def __init__(self, n):
        assert n in [0, 1, 2, 3, 4]
        self.n = n

    def __add__(self, other):
        return Mod5((self.n + other.n) % 5)

    def __eq__(self, other):
        return self.n == other.n

    def __mul__(self, other):
        return Mod5((self.n * other.n) % 5)

    def __neg__(self):
        if self.n == 0:
            return self
        return Mod5(5 - self.n)

    def __pow__(self, exp):
        return self.raised_to_exponent(exp)

    def __str__(self):
        return str(self.n)

    def raised_to_exponent(self, exponent):
        if exponent == 0:
            return Mod5(1)
        if exponent == 1:
            return self
        return self * self.raised_to_exponent(exponent - 1)


class Mod5Math:
    add = lambda a, b: a + b
    additive_inverse = lambda a: -a
    multiply_by_constant = lambda a, b: a * b
    power = lambda m, exp: m**exp
    value_type = Mod5

    zero = Mod5(0)
    one = Mod5(1)


def Mod5Poly(lst):
    return SingleVarPoly(lst, Mod5Math, "x")


if __name__ == "__main__":
    from commutative_ring import verify_axioms
    from single_poly import SingleVarPoly
    from lib.test_helpers import assert_str, run_test

    zero = Mod5(0)
    one = Mod5(1)
    two = Mod5(2)
    three = Mod5(3)
    four = Mod5(4)

    @run_test
    def mod5_is_a_ring():
        samples = [
            zero,
            one,
            two,
            three,
            four,
        ]

        verify_axioms(samples, zero=zero, one=one)

    p_zero = Mod5Poly([])
    p_one = Mod5Poly([one])
    p_two = Mod5Poly([two])
    p_three = Mod5Poly([three])
    p_four = Mod5Poly([four])
    p_x = Mod5Poly([zero, one])

    @run_test
    def polynomial_math_works_over_mod5():
        q = (p_x + p_four) * (p_x + p_three)
        assert_str(q, "x**2+(2)*x+2")
        assert q.eval(four) == one

    @run_test
    def mod5_polys_conform_to_axioms():
        poly_samples = [
            Mod5Poly([one, zero, three]),
            Mod5Poly([three, one, four, two]),
            Mod5Poly([two]),
            (p_x * p_two) + p_one,
            (p_x + p_three).raised_to_exponent(15),
        ]
        verify_axioms(poly_samples, zero=p_zero, one=p_one)
