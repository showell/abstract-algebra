class Elephant:
    """
    An Elephant object remembers how it was created.
    """
    def __init__(self, val, history):
        self.val = val
        self.history = history

    @staticmethod
    def add(elephant1, elephant2):
        val = elephant1.val + elephant2.val
        history = f"({elephant1.history} + {elephant2.history})"
        return Elephant(val, history)

    @staticmethod
    def multiply(elephant1, elephant2):
        val = elephant1.val * elephant2.val
        history = f"({elephant1.history} * {elephant2.history})"
        return Elephant(val, history)

    @staticmethod
    def make(val):
        return Elephant(val, str(val))

    @staticmethod
    def power(elephant, exp):
        val = elephant.val ** exp
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
