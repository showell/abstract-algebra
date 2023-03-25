def add(lst1, lst2, *, add, zero):
    if len(lst1) < len(lst2):
        (lst2, lst1) = (lst1, lst2)

    lst = lst1[:]
    for i, x in enumerate(lst2):
        if x != zero:
            if lst[i] == zero:
                lst[i] = x
            else:
                lst[i] = add(lst[i], x)
    return lst


def eval(lst, *, zero, add, mul, power):
    result = zero
    for degree, coeff in enumerate(lst):
        if coeff != zero:
            term = mul(coeff, power(degree))
            result = add(result, term)
    return result


def multiply(lst1, lst2, *, add, mul, zero):
    lst = [zero] * (len(lst1) + len(lst2) - 1)
    for i, x in enumerate(lst1):
        for j, y in enumerate(lst2):
            xy = mul(x, y)
            if xy != zero:
                lst[i + j] = add(lst[i + j], xy)
    return lst


def stringify(lst, *, var_name, zero, one):
    if len(lst) == 0:
        return str(zero)

    def monomial(coeff, i):
        if i == 0:
            return str(coeff)
        elif i == 1:
            if coeff == one:
                return var_name
            else:
                return f"({coeff})*{var_name}"
        else:
            if coeff == one:
                return f"{var_name}**{i}"
            else:
                return f"({coeff})*{var_name}**{i}"

    terms = [
        monomial(coeff, degree) for degree, coeff in enumerate(lst) if coeff != zero
    ]
    return "+".join(reversed(terms))
