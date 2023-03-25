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


if __name__ == "__main__":
    from commutative_ring import verify_ring_properties
    from lib.test_helpers import run_test

    @run_test
    def elephant_integers_form_a_ring():
        samples = [
            Elephant.make(4),
            Elephant.make(555),
            Elephant.make(-13),
            Elephant.make(37),
        ]
        verify_ring_properties(ElephantIntegerMath, samples)
