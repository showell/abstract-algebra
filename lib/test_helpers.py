def run_test(f):
    f()


def assert_equal(x, y):
    if x != y:
        raise AssertionError(f"{x} != {y}")


def assert_str(p, expected_str):
    if str(p) != expected_str:
        raise AssertionError(f"got {p} when expecting {expected_str}")
