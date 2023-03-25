def arr_get(lst, i):
    return lst[i] if i < len(lst) else 0


class BasicNumberList:
    def __init__(self, lst):
        self.lst = lst
        self.simplify()

    def raised_to_exponent(self, exponent):
        if exponent < 0:
            raise ValueError("we do not support negative exponents")

        if exponent == 0:
            return BasicNumberList([1])
        if exponent == 1:
            return self
        return BasicNumberList.mul(self, self.raised_to_exponent(exponent - 1))

    def simplify(self):
        self.lst = BasicNumberList.simplify_list(self.lst)

    @staticmethod
    def add(basic_number_list1, basic_number_list2):
        lst1 = basic_number_list1.lst
        lst2 = basic_number_list2.lst
        # do the analog of elementary school arithmetic
        new_size = max(len(lst1), len(lst2))
        return BasicNumberList(
            [arr_get(lst1, i) + arr_get(lst2, i) for i in range(new_size)]
        )

    @staticmethod
    def equal(basic_number_list1, basic_number_list2):
        return basic_number_list1.lst == basic_number_list2.lst

    @staticmethod
    def mul(basic_number_list1, basic_number_list2):
        lst1 = basic_number_list1.lst
        lst2 = basic_number_list2.lst
        # do the analog of elementary school arithmetic
        result = BasicNumberList([])
        for i, elem in enumerate(lst1):
            sub_result = BasicNumberList.mul_by_constant(elem, [0] * i + lst2)
            result = BasicNumberList.add(result, sub_result)
        return result

    @staticmethod
    def mul_by_constant(c, lst):
        return BasicNumberList([c * elem for elem in lst])

    @staticmethod
    def negate(basic_number_list):
        lst = basic_number_list.lst
        return BasicNumberList([-elem for elem in lst])

    @staticmethod
    def simplify_list(lst):
        while lst and lst[-1] == 0:
            lst = lst[:-1]
        return lst


class NumberList:
    def __init__(self, lst):
        self.bnl = BasicNumberList(lst)

    def __add__(self, other):
        return NumberList(BasicNumberList.add(self.bnl, other.bnl).lst)

    def __eq__(self, other):
        return BasicNumberList.equal(self.bnl, other.bnl)

    def __mul__(self, other):
        return NumberList(BasicNumberList.mul(self.bnl, other.bnl).lst)

    def __neg__(self):
        return NumberList(BasicNumberList.negate(self.bnl).lst)

    def __pow__(self, n):
        return NumberList(self.bnl.raised_to_exponent(n).lst)

    def __str__(self):
        return str(self.bnl.lst)

    def list(self):
        return self.bnl.lst


if __name__ == "__main__":
    from commutative_ring import verify_ring_properties
    from lib.test_helpers import assert_equal, run_test
    from math_helper import MathHelper

    @run_test
    def verify_basics():
        assert NumberList([1, 0, 2]) + NumberList([2, 4, 7, 8]) == NumberList(
            [3, 4, 9, 8]
        )
        assert 201 + 8742 == 8943

        assert NumberList([1, 2]) * NumberList([1, 3]) == NumberList([1, 5, 6])
        assert 21 * 31 == 651

        assert NumberList([7, 8]) * NumberList([1, 6]) == NumberList([7, 50, 48])
        assert 87 * 61 == 48 * 100 + 50 * 10 + 7

    @run_test
    def verify_equality_check():
        assert NumberList([5, 2]) == NumberList([5, 2])
        assert NumberList([5]) != NumberList([5, 2])

    @run_test
    def number_list_is_a_ring():
        samples = [
            NumberList([]),
            NumberList([42, 39, 2]),
            NumberList([-8, 0, 0, 0, 5]),
            NumberList([103, 8256523499]),
        ]
        math = MathHelper(
            value_type=NumberList,
            zero=NumberList([]),
            one=NumberList([1]),
        )
        verify_ring_properties(math, samples)

    @run_test
    def exponentiation():
        x = NumberList([5, 7, -21])
        assert_equal(x**3, x * x * x)
