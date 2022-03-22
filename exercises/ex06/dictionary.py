"""Practice with some useable functions."""
__author__ = "730514879"


def invert(book: dict[str, str], ) -> dict[str, str]:
    """Inverts a dict of keys, vals so that vals = keys and vice versa."""
    # from exercises.ex06.dictionary import invert
    # invert({"a":"1", "b":"2"})
    koob: dict[str, str] = {}

    for key in book:  # takes in each val of book and appends the val to the key (vs key to val) to koob
        if book[key] not in koob:
            koob[book[key]] = key  # this does the flip only iff the val is not already in koob
        else:
            raise KeyError
    return koob


def favorite_color(color: dict[str, str]) -> str:
    """Outputs the var with the highest frequency."""
    # from exercises.ex06.dictionary import favorite_color
    # favorite_color({"a":"2", "b":"2", "c":"4", "d":"4", "e":"6", "f":"2", "g":"3", "h":"4"})
    reg = []
    repeat = []
    
    for key in color:  # for each key in the dict, it appends to reg if it occurs once and repeat if > 1
        if color[key] not in reg:  # if the val is not in the reg list add it to it otherwise add it to the repeat lst
            reg.append(color[key])
        else:
            repeat.append(color[key]) 

    most: dict[str, int] = {}

    for val in repeat:  # takes in the repeat lst and assigns a value to the frequency of occurence for each key
        if val in most:
            most[val] += 1
        else:
            most[val] = 1
    
    i = 0
    big = ""
    for val in most:  # takes in the dict and turns it back into a str that contains only the largest val
        if i < most[val]:  # if the val is bigger, make the str the corresponidng key 
            i = most[val]
            big = val

    return big


def count(tbc: list[str]) -> dict[str, int]:
    """Creates a counter for the frequency of each var in a lst."""
    # from exercises.ex06.dictionary import count
    # count(("a, b, b, c, a, r, g, c"))
    score: dict[str, int] = {}

    for val in tbc:  # takes in the repeat lst and assigns a value to the frequency of occurence for each key
        if val in score:
            score[val] += 1
        else:
            score[val] = 1

    return score