def test(samples, f, g, type1, type2):
    # print(f"We can use {type2} to compute {type1}")
    for a in samples:
        assert type(a) == type1
        assert type(f(a)) == type2
        assert type(g(f(a))) == type1
        assert g(f(a)) == a

        for b in samples:
            assert g(f(a) + f(b)) == g(f(a + b))
            assert g(f(a) * f(b)) == g(f(a * b))


if __name__ == "__main__":
    from fractions import Fraction
    from mod5 import Mod5
    from number_list import NumberList

    # Fraction can compute int

    samples = [-7, 42, 13, 9, 4567, 14]
    f = lambda integer: Fraction(integer)
    g = lambda fraction: int(fraction)

    test(samples, f, g, int, Fraction)

    # int can compute mod5
    samples = [Mod5(0), Mod5(1), Mod5(2), Mod5(3), Mod5(4)]
    f = lambda m: m.n
    g = lambda n: Mod5(n % 5)

    test(samples, f, g, Mod5, int)

    # NumberList can compute int in a trivial way
    samples = [-7, 42, 13, 9, 4567, 14]
    f = lambda n: NumberList([n])
    g = lambda nl: nl.lst[0]

    test(samples, f, g, int, NumberList)

    # NumberList can compute int in a more interesting way
    samples = [-732, 42, 13, 9, 4567, 142340862349551239912346999234654190]

    def get_digits(n):
        if n < 0:
            return [-digit for digit in get_digits(-n)]
        if n == 0:
            return []
        return [n % 10] + get_digits(n // 10)

    assert get_digits(1234) == [4, 3, 2, 1]

    def number_from_digit_list(lst):
        return sum(c * 10**i for i, c in enumerate(lst))

    f = lambda n: NumberList(get_digits(n))
    g = lambda nl: number_from_digit_list(nl.lst)

    test(samples, f, g, int, NumberList)
