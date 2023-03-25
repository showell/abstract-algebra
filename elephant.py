from lib.type_enforcers import enforce_same_types, enforce_type


class Elephant:
    """
    An Elephant object remembers how it was created.

    NOTE that we have no magic related to __add__ or __mul__
    in Elephant itself, but we do assume that the values it
    operate over support + and *.
    """

    def __init__(self, val, history):
        self.val = val
        self.history = history

    def __eq__(self, other):
        return self.val == other.val

    def __str__(self):
        return str(self.val)

    @staticmethod
    def add(elephant1, elephant2):
        enforce_type(elephant1, Elephant)
        enforce_type(elephant2, Elephant)
        enforce_same_types(elephant1.val, elephant2.val)

        val = elephant1.val + elephant2.val
        history = f"({elephant1.history} + {elephant2.history})"
        return Elephant(val, history)

    @staticmethod
    def additive_inverse(elephant):
        enforce_type(elephant, Elephant)

        val = -elephant.val
        history = f"(-{elephant.history})"
        return Elephant(val, history)

    @staticmethod
    def make(val):
        return Elephant(val, str(val))

    @staticmethod
    def multiply(elephant1, elephant2):
        enforce_type(elephant1, Elephant)
        enforce_type(elephant2, Elephant)
        enforce_same_types(elephant1.val, elephant2.val)

        val = elephant1.val * elephant2.val
        history = f"({elephant1.history} * {elephant2.history})"
        return Elephant(val, history)

    @staticmethod
    def power(elephant, exp):
        enforce_type(elephant, Elephant)
        enforce_type(exp, int)

        val = elephant.val**exp
        history = f"({elephant.history})**{exp}"
        return Elephant(val, history)


class ElephantMath:
    def __init__(self, *, zero, one):
        self.value_type = Elephant
        self.zero = zero
        self.one = one
        self.add = Elephant.add
        self.additive_inverse = Elephant.additive_inverse
        self.multiply = Elephant.multiply
        self.power = Elephant.power
        self.type_string = "Elephant"


ElephantIntegerMath = ElephantMath(
    zero=Elephant.make(0),
    one=Elephant.make(1),
)


if __name__ == "__main__":
    from commutative_ring import verify_ring_properties
    from lib.test_helpers import assert_str, run_test

    @run_test
    def basics():
        four = Elephant.make(4)
        five = Elephant.make(5)

        nine = Elephant.add(four, five)
        assert nine.val == 9
        assert nine.history == "(4 + 5)"
        assert_str(nine, "9")

        twenty = Elephant.multiply(four, five)
        assert twenty.val == 20
        assert twenty.history == "(4 * 5)"
        assert_str(twenty, "20")

        sixty_four = Elephant.power(four, 3)
        assert sixty_four.val == 64
        assert sixty_four.history == "(4)**3"

        minus_four = Elephant.additive_inverse(four)
        assert minus_four.val == -4
        assert minus_four.history == "(-4)"

        twenty_four = Elephant.add(twenty, four)
        assert twenty_four.val == 24
        assert twenty_four.history == "((4 * 5) + 4)"

    @run_test
    def elephant_integers_form_a_ring():
        samples = [
            Elephant.make(4),
            Elephant.make(555),
            Elephant.make(-13),
            Elephant.make(37),
        ]
        verify_ring_properties(ElephantIntegerMath, samples)
