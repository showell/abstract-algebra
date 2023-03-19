def arr_get(lst, i, zero):
    return lst[i] if i < len(lst) else zero


def enforce_list_types(lst, _type):
    assert type(lst) == list
    for elem in lst:
        assert type(elem) == _type


def enforce_math_protocol(math):
    assert hasattr(math, "add")
    assert hasattr(math, "additive_inverse")
    assert hasattr(math, "multiply_by_constant")
    assert hasattr(math, "value_type")
    assert hasattr(math, "zero")
    assert callable(math.add)
    assert callable(math.additive_inverse)
    assert callable(math.multiply_by_constant)
    assert type(math.zero) == math.value_type


class ValueList:
    def __init__(self, lst, math):
        enforce_math_protocol(math)
        enforce_list_types(lst, math.value_type)
        self.lst = lst
        self.math = math
        self.simplify()

    def __add__(self, other):
        self.enforce_partner_type(other)
        return self.add_with(other)

    def __eq__(self, other):
        self.enforce_partner_type(other)
        return self.lst == other.lst

    def __mul__(self, other):
        self.enforce_partner_type(other)
        return self.multiply_with(other)

    def __neg__(self):
        return self.additive_inverse()

    def additive_inverse(self):
        lst = self.lst
        additive_inverse = self.math.additive_inverse
        return self.new([additive_inverse(elem) for elem in lst])

    def add_with(self, other):
        add = self.math.add
        zero = self.math.zero
        lst1 = self.lst
        lst2 = other.lst
        # do the analog of elementary school arithmetic
        new_size = max(len(lst1), len(lst2))
        return self.new(
            [
                add(arr_get(lst1, i, zero), arr_get(lst2, i, zero))
                for i in range(new_size)
            ]
        )

    def enforce_partner_type(self, other):
        assert type(other) == ValueList
        assert type(other.math) == type(self.math)

    def multiply_by_constant(self, c, lst):
        enforce_list_types(lst, self.math.value_type)
        mul = self.math.multiply_by_constant
        return self.new([mul(c, elem) for elem in lst])

    def multiply_with(self, other):
        """
        We are mostly simulating high school arithmetic, but it is probably
        more precise to say that we are creating a discrete convulution of
        our two lists over the non-zero values.

        https://en.wikipedia.org/wiki/Convolution#Discrete_convolution
        """
        zero = self.math.zero
        lst1 = self.lst
        lst2 = other.lst
        # do the analog of elementary school arithmetic
        result = self.new([])
        for i, elem in enumerate(lst1):
            result += self.multiply_by_constant(elem, [zero] * i + lst2)
        return result

    def new(self, lst):
        return ValueList(lst, self.math)

    def simplify(self):
        lst = self.lst
        zero = self.math.zero
        while lst and lst[-1] == zero:
            lst = lst[:-1]
        self.lst = lst


if __name__ == "__main__":

    class IntegerMath:
        add = lambda a, b: a + b
        additive_inverse = lambda a: -1 * a
        multiply_by_constant = lambda a, b: a * b
        value_type = int
        zero = 0

    def IntegerList(lst):
        return ValueList(lst, IntegerMath)

    assert IntegerList([1, 0, 2]) + IntegerList([2, 4, 7, 8]) == IntegerList(
        [3, 4, 9, 8]
    )
    assert 201 + 8742 == 8943

    assert IntegerList([1, 2]) * IntegerList([1, 3]) == IntegerList([1, 5, 6])
    assert 21 * 31 == 651

    assert IntegerList([7, 8]) * IntegerList([1, 6]) == IntegerList([7, 50, 48])
    assert 87 * 61 == 48 * 100 + 50 * 10 + 7

    import commutative_ring

    samples = [
        IntegerList([]),
        IntegerList([42, 39, 2]),
        IntegerList([-8, 0, 0, 0, 5]),
        IntegerList([103, 8256523499]),
    ]
    zero = IntegerList([])
    one = IntegerList([1])
    commutative_ring.test(samples, zero=zero, one=one)

    from number_list import NumberList

    class NumberListMath:
        add = lambda a, b: a + b
        additive_inverse = lambda a: -a
        multiply_by_constant = lambda c, num_list: NumberList(
            NumberList.mul_by_constant(c, num_list.lst)
        )
        value_type = NumberList
        zero = NumberList([])

    def NumberListList(lst):
        return ValueList(lst, NumberListMath)

    x = NumberList([42, 39, 2])
    y = NumberList([-8, 0, -5888, 0, 5])
    z = NumberList([103, 8256523499])

    samples = [
        NumberListList([x, y, z, x]),
        NumberListList([z]),
        NumberListList([y, z, y, z, x]),
        NumberListList([x, x, x, x, x, x, x, z, y]),
    ]

    zero = NumberListList([])
    one = NumberListList([NumberList([1])])

    commutative_ring.test(samples, zero=zero, one=one)
