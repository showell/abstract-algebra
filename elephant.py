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
