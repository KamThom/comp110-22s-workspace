"""Testing utility functions."""
__author__ = "730514879"

from exercises.ex05.utils import only_evens, sub, concat
# python -m pytest exercises/ex05/utils_test.py


def test_num_many_evens() -> None:
    assert only_evens([2, 2, 2, 2, 2, 2]) == [2, 2, 2, 2, 2, 2]


def test_nums_many() -> None:
    assert only_evens([1, 5, 6, 2, 9, 6, 4, 3, 2, 3, 6]) == [6, 2, 4, 6, 2, 6]


def test_nums_larg() -> None:
    assert only_evens([23, 45, 26, 47, 84, 96, 45]) == [96, 84, 26]
# ________________________________________


def test_sub_base() -> None:
    assert sub([1, 2, 4, 5, 6, 9, 3], 1, 4) == [2, 4, 5]


def test_sub_neg_start() -> None:
    assert sub([1, 2, 4, 5, 6, 9, 3], -1, 4) == [1, 2, 4, 5]


def test_sub_big_end() -> None:
    assert sub([1, 2, 4, 5, 6, 9, 3], 1, 8) == [2, 4, 5, 6, 9, 3]


def test_sub_neg_end() -> None:
    assert sub([1, 2, 4, 5, 6, 9, 3], 1, -4) == []


def test_sub_zro_lst() -> None:
    assert sub([], 1, 4) == []


def test_sub_big_start() -> None:   
    assert sub([1, 2, 4, 5, 6, 9, 3], 10, 4) == []
# ________________________________________


def test_concat_base() -> None:
    assert concat([1, 2, 3, 4], [5, 6, 7, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_concat_zro_first() -> None:
    assert concat([], [5, 6, 7, 8, 9]) == [5, 6, 7, 8, 9]


def test_concat_zro_sec() -> None:
    assert concat([1, 2, 3, 4], []) == [1, 2, 3, 4]


def test_concat_none() -> None:
    assert concat([], []) == []


def test_concat_large_neg() -> None:
    assert concat([-12, -42, -36, 4], [32, -68, 46]) == [-12, -42, -36, 4, 32, -68, 46]