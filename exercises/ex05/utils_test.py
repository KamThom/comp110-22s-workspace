"""Testing utility functions."""
__author__ = "730514879"

from utils import only_evens, sub, concat
# python -m pytest exercises/ex05/utils_test.py


def test_num_many_evens() -> None:
    """Tests all evens."""
    assert only_evens([2, 2, 2, 2, 2, 2]) == [2, 2, 2, 2, 2, 2]


def test_nums_many() -> None:
    """Tests with huge list."""
    assert only_evens([1, 5, 6, 2, 9, 6, 4, 3, 2, 3, 6]) == [6, 2, 6, 4, 2, 6]


def test_nums_larg() -> None:
    """Tests with double digit nums."""
    assert only_evens([23, 45, 26, 47, 84, 96, 45]) == [26, 84, 96]
# ________________________________________


def test_sub_base() -> None:
    """Tests just basic input."""
    assert sub([1, 2, 4, 5, 6, 9, 3], 1, 4) == [2, 4, 5]


def test_sub_neg_start() -> None:
    """Tests with a neg start peram."""
    assert sub([1, 2, 4, 5, 6, 9, 3], -1, 4) == [1, 2, 4, 5]


def test_sub_big_end() -> None:
    """Tests with an end num peram > the len og list."""
    assert sub([1, 2, 4, 5, 6, 9, 3], 1, 8) == [2, 4, 5, 6, 9, 3]


def test_sub_neg_end() -> None:
    """Tests if end peram is neg."""
    assert sub([1, 2, 4, 5, 6, 9, 3], 1, -4) == []


def test_sub_zro_lst() -> None:
    """Tests if one list has no nums."""
    assert sub([], 1, 4) == []


def test_sub_big_start() -> None:  
    """Tests if start peram is > list length.""" 
    assert sub([1, 2, 4, 5, 6, 9, 3], 10, 4) == []
# ________________________________________


def test_concat_base() -> None:
    """Tests normal peram."""
    assert concat([1, 2, 3, 4], [5, 6, 7, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_concat_zro_first() -> None:
    """Tests if one list is empty."""
    assert concat([], [5, 6, 7, 8, 9]) == [5, 6, 7, 8, 9]


def test_concat_zro_sec() -> None:
    """Tests if sec list is empty."""
    assert concat([1, 2, 3, 4], []) == [1, 2, 3, 4]


def test_concat_none() -> None:
    """Tests if both lists are empty."""
    assert concat([], []) == []


def test_concat_large_neg() -> None:
    """Tests if nums in list are double digit and negative."""
    assert concat([-12, -42, -36, 4], [32, -68, 46]) == [-12, -42, -36, 4, 32, -68, 46]