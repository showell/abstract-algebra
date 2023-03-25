def mod5(n):
    return n % 5


class Mod5:
    def __init__(self, n):
        assert n in [0, 1, 2, 3, 4]
        self.n = n

    def __add__(self, other):
        return Mod5(mod5(self.n + other.n))

    def __eq__(self, other):
        return self.n == other.n

    def __mul__(self, other):
        return Mod5(mod5(self.n * other.n))

    def __neg__(self):
        return Mod5(mod5(5 - self.n))

    def __pow__(self, exp):
        return self.raised_to_exponent(exp)

    def __str__(self):
        return str(self.n)

    def raised_to_exponent(self, exponent):
        if self.n == 0:
            return Mod5(0) if exponent >= 1 else Mod5(1)

        # Just to be cute, take advantage that all our
        # non-zero values are fourth roots of unity.
        # https://en.wikipedia.org/wiki/Root_of_unity_modulo_n
        exponent = exponent % 4

        if exponent == 0:
            return Mod5(1)
        elif exponent == 1:
            return self
        elif exponent == 2:
            return self * self
        elif exponent == 3:
            return self * self * self
