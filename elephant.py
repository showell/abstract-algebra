from lib.type_enforcers import enforce_same_types, enforce_type


class Elephant:
    """
    An Elephant object remembers how it was created.
    """

    def __init__(self, val, history):
        self.val = val
        self.history = history

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


if __name__ == "__main__":
    from lib.test_helpers import run_test

    @run_test
    def basics():
        four = Elephant.make(4)
        five = Elephant.make(5)

        nine = Elephant.add(four, five)
        assert nine.val == 9
        assert nine.history == "(4 + 5)"

        twenty = Elephant.multiply(four, five)
        assert twenty.val == 20
        assert twenty.history == "(4 * 5)"

        sixty_four = Elephant.power(four, 3)
        assert sixty_four.val == 64
        assert sixty_four.history == "(4)**3"

        minus_four = Elephant.additive_inverse(four)
        assert minus_four.val == -4
        assert minus_four.history == "(-4)"
