from elephant import Elephant


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
