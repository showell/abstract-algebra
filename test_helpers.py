def run_test(f):
    f()


def assert_str(p, expected_str):
    if str(p) != expected_str:
        raise AssertionError(f"got {p} when expecting {expected_str}")
