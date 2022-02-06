"""functions of love"""


def love(name: str) -> str:
    """given a name as a parameter, returns a loving string"""
    return f"i love you, {name}!"


def spread_love(to: str, n: int) -> str:
    """Generates a string that repeats the message n number of times"""

    love_note = ""
    num = 0

    while num < n:
        love_note += love(to) + "\n"
        num += 1
        
    return love_note