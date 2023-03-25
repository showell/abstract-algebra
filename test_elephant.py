from elephant import Elephant
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
