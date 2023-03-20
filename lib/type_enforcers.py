def enforce_list_types(lst, _type):
    assert type(lst) == list
    for elem in lst:
        assert type(elem) == _type


def enforce_math_protocol(math):
    assert hasattr(math, "add")
    assert hasattr(math, "additive_inverse")
    assert hasattr(math, "multiply_by_constant")
    assert hasattr(math, "power")
    assert hasattr(math, "value_type")
    assert hasattr(math, "one")
    assert hasattr(math, "zero")
    assert callable(math.add)
    assert callable(math.additive_inverse)
    assert callable(math.multiply_by_constant)
    assert callable(math.power)
    one = math.one
    zero = math.zero
    power = math.power
    add = math.add
    assert type(one) == math.value_type
    assert type(zero) == math.value_type
    assert power(zero, 0) == one
    assert power(one, 0) == one
    assert power(one, 1) == one
    assert power(one, 2) == one


def enforce_type(x, _type):
    assert type(x) == _type
