def search(book: list[str], key: str) -> list[str]:
    record = []

    for i in book:
        x = i[len(i) - 1]
        if x == key:
            record.append(i)
        
    return record


# search(["apple", "bear", "gog", "ape"], ("e"))


def search2(objects: list[str], letter: str) -> list[str]:
    filtered: list[str] = []
    for word in objects:
        if word[len(word) - 1] == letter:
            filtered.append(word)
    return filtered


print(search2(['apple', 'banana', 'orange'], 'e'))