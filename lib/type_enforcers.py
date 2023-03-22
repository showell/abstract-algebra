def enforce_list_types(lst, _type):
    assert type(lst) == list
    for elem in lst:
        assert type(elem) == _type


def enforce_same_types(x, y):
    assert type(x) == type(y)


def enforce_subtype(x, _type):
    assert isinstance(x, _type)


def enforce_type(x, _type):
    assert type(x) == _type
