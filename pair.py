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
