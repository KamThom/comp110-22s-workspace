"""Some tests for the useful functions."""
__author__ = "730514879"

from dictionary import invert, count, favorite_color 
import pytest


def test_norm_invert() -> None:
    """Tests normal functions of invert."""
    assert invert({"a": "1", "b": "2"}) == {"1": "a", "2": "b"}


with pytest.raises(KeyError):
    my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
    invert(my_dictionary)


def test_words_invert() -> None:
    """Tests invert function with actual words."""
    assert invert({"apple": "1", "bear": "2"}) == {"1": "apple", "2": "bear"}


def test_norm_favorite_color() -> None:
    """Tests normal functions of favorite_color."""
    assert favorite_color({"a": "2", "b": "2", "c": "4"}) == "2"


def test_multiples_favorite_color() -> None:
    """Tests if there are > 1 multiple."""
    assert favorite_color({"a": "2", "b": "2", "c": "4", "d": "4", "e": "6", "f": "2"}) == "2"


def test_tie_favorite_color() -> None:
    """Tests tie breaker functionality."""
    assert favorite_color({"a": "2", "b": "2", "c": "4", "d": "4", "e": "4", "f": "2"}) == "2"


def test_act_colors_favorite_color() -> None:
    """Tests with words."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == "blue"


def test_norm_count() -> None:
    """Tests normal peram of count."""
    assert count(["a", "b", "b", "c", "a", "r", "g", "c"]) == {'a': 2, 'b': 2, 'c': 2, 'r': 1, 'g': 1}


def test_words_count() -> None:
    """Tests words in count."""
    assert count(["apple", "bird", "dog", "dog", "cat", "apple"]) == {'apple': 2, 'bird': 1, 'dog': 2, 'cat': 1}


def test_Uppercase_count() -> None:
    """Test to make sure uppercase is counted as seprate."""
    assert count(["a", "b", "b", "c", "a", "r", "g", "A"]) == {'a': 2, 'b': 2, 'c': 1, 'r': 1, 'g': 1, 'A': 1}