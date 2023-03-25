class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Pair(self.a + other.a, self.b + other.b)

    def __eq__(self, other):
        return (self.a, self.b) == (other.a, other.b)

    def __mul__(self, other):
        return Pair(self.a * other.a, self.b * other.b)

    def __neg__(self):
        return Pair(-self.a, -self.b)

    def __pow__(self, exp):
        return Pair(self.a**exp, self.b**exp)

    def __str__(self):
        return str((self.a, self.b))


if __name__ == "__main__":
    from lib.test_helpers import run_test

    @run_test
    def verify_exponentiation():
        zero = Pair(0, 0)
        one = Pair(1, 1)
        x = Pair(5, -3)
        y = Pair(152, 4)
        z = Pair(-9, 7)
        for pair in [zero, one, x, y, z]:
            product = one
            for exp in range(30):
                assert pair**exp == product
                product *= pair
