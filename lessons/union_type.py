"""Union Type Examples."""

from typing import Union 


def log(info: Union[int, str]) -> None:
    if isinstance(info, str):
        print(f"str: {info}")
    else:
        print(f"int: {info}")


log("Hello world")
log(110)