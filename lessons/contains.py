"""example of a function that searches through a list"""


def main() -> None:
    print(contains("kevin", ["kanye", "pete"]))


def contains(needle: str, haystack: list[str]) -> bool:

    for item in haystack:

        if item == needle:
            return True
    
    return False


if __name__ == "__main__":
    main()  
else:
    print(__name__)