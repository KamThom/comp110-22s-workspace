"""Practice with some useable functions."""
__author__ = "730514879"


def invert(book: dict[str, str], ) -> dict[str, str]:
    # from exercises.ex06.dictionary import invert
    # invert({"a":"1", "b":"2"})
    koob: dict[str, str] = {}

    for key in book:
        if book[key] not in koob:
            koob[book[key]] = key
        else:
            raise KeyError
    return koob


def favorite_color(color: dict[str, str]) -> str:
    # from exercises.ex06.dictionary import favorite_color
    # favorite_color({"a":"2", "b":"2", "c":"4", "d":"4", "e":"6", "f":"2", "g":"3", "h":"4"})
    reg: list = []
    repeat: list = []
    
    for key in color:
        if color[key] not in reg:
            reg.append(color[key])
        else:
            repeat.append(color[key])

    most = {}

    for val in repeat:
        if val in most:
            most[val] += 1
        else:
            most[val] = 1
    
    i = 0
    big = ""
    for val in most:
        if i < most[val]:
            i = most[val]
            big = val

    return big


def count(tbc: list[str]) -> dict[str, int]:
    # from exercises.ex06.dictionary import count
    # count(("a", "b", "b", "c", "a", "r", "g", "c"))
    score: dict[str, int] = {}

    for val in tbc:
        if val in score:
            score[val] += 1
        else:
            score[val] = 1

    return score