def arr_get(lst, i):
    return lst[i] if i < len(lst) else 0


class NumberList:
    def __init__(self, lst):
        self.lst = lst
        self.simplify()

    def __add__(self, other):
        return NumberList.add(self, other)

    def __eq__(self, other):
        return NumberList.equal(self, other)

    def __mul__(self, other):
        return NumberList.mul(self, other)

    def __neg__(self):
        return NumberList.negate(self)

    def simplify(self):
        self.lst = NumberList.simplify_list(self.lst)

    @staticmethod
    def add(number_list1, number_list2):
        lst1 = number_list1.lst
        lst2 = number_list2.lst
        # do the analog of elementary school arithmetic
        new_size = max(len(lst1), len(lst2))
        return NumberList(
            [arr_get(lst1, i) + arr_get(lst2, i) for i in range(new_size)]
        )

    @staticmethod
    def equal(number_list1, number_list2):
        return number_list2.lst == number_list2.lst

    @staticmethod
    def mul(number_list1, number_list2):
        lst1 = number_list1.lst
        lst2 = number_list2.lst
        # do the analog of elementary school arithmetic
        result = NumberList([])
        for i, elem in enumerate(lst1):
            result += NumberList.mul_by_constant(elem, [0] * i + lst2)
        return result

    @staticmethod
    def mul_by_constant(c, lst):
        return NumberList([c * elem for elem in lst])

    @staticmethod
    def negate(number_list):
        lst = number_list.lst
        return NumberList([-elem for elem in lst])

    @staticmethod
    def simplify_list(lst):
        while lst and lst[-1] == 0:
            lst = lst[:-1]
        return lst


if __name__ == "__main__":
    assert NumberList([1, 0, 2]) + NumberList([2, 4, 7, 8]) == NumberList([3, 4, 9, 8])
    assert 201 + 8742 == 8943

    assert NumberList([1, 2]) * NumberList([1, 3]) == NumberList([1, 5, 6])
    assert 21 * 31 == 651

    assert NumberList([7, 8]) * NumberList([1, 6]) == NumberList([7, 50, 48])
    assert 87 * 61 == 48 * 100 + 50 * 10 + 7

    import commutative_ring

    samples = [
        NumberList([]),
        NumberList([42, 39, 2]),
        NumberList([-8, 0, 0, 0, 5]),
        NumberList([103, 8256523499]),
    ]
    zero = NumberList([])
    one = NumberList([1])
    commutative_ring.test(samples, zero=zero, one=one)
