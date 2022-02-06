"""Function Definition Walkthrough"""


def my_max(a: int, b: int) -> int:  # returns largest areguement
    if a >= b:
        return a
    else:
        return b

print(my_max(11, 10))