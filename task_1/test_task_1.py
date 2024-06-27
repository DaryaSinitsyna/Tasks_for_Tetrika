from task_1 import strict


def test_strict_decorator_with_valid_inputs():
    @strict
    def sum_two(a: int, b: int) -> int:
        return a + b

    assert sum_two(1, 2) == 3
    assert sum_two(-5, 10) == 5


def test_strict_decorator_with_invalid_inputs():
    @strict
    def sum_two(a: int, b: int) -> int:
        return a + b

    try:
        sum_two(1, 2.4)
    except TypeError:
        pass
    else:
        assert False


def test_strict_decorator_with_multiple_arguments():
    @strict
    def func_with_multiple_arguments(a: int, b: int, c: str) -> str:
        return f"{a} + {b} = {c}"

    assert func_with_multiple_arguments(1, 2, "3") == "1 + 2 = 3"


def test_strict_decorator_with_named_arguments():
    @strict
    def func_with_named_arguments(a: int, b: int, c: str) -> str:
        return f"{a} + {b} = {c}"

    assert func_with_named_arguments(a=1, b=2, c="3") == "1 + 2 = 3"
    assert func_with_named_arguments(1, 2, c="3") == "1 + 2 = 3"

    try:
        func_with_named_arguments(a=1, b=2, c=3)
    except TypeError:
        pass
    else:
        assert False
