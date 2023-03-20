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


if __name__ == "__main__":
    from commutative_ring import verify_axioms
    from lib.test_helpers import run_test

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
