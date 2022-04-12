"""Dictionary related utility functions."""

__author__ = "730514879"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Return the rows of a csv."""
    result: list[dict[str, str]] = []

    file_handle = open(filename, "r", encoding="utf8")

    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)

    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Make a list of all values in a column."""
    result: list[str] = []

    for row in table:
        item: str = row[column]
        result.append(item)

    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row table to column table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]

    for column in first_row:
        result[column] = column_values(row_table, column) 

    return result


def head(tab: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Produce a new column-basedtable with only the first `N` rows of data for each column."""
    result: dict[str, list[str]] = {}

    for item in tab:
        store = []
        key = item

        for i in tab[item][:N]:
            store.append(i)
        
        result[key] = store
    
    return result 


def select(ntable: dict[str, list[str]], nnames: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}

    for item in nnames:
        for i in ntable:
            if i == item:
                result[item] = ntable[i]
        
    return result


def concat(one: dict[str, list[str]], two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}

    for item in one:
        result[item] = one[item]

    for i in two:
        if i in result:
            result[i] += two[i]
        else:
            result[i] = two[i]
    
    return result


def count(many: list[str]) -> dict[str, int]:
    """Produce a dict where each key is a unique value in the given list and each value associated is the _count_ of the number of times that value appeared in the input list."""
    result: dict[str, int] = {}

    for item in many:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    
    return result


def add(check: dict[str, int]) -> int:
    result: int = 0

    for i in check:
        if i == '5':
            result += check[i]
        elif i == '6':
            result += check[i]
        elif i == '7':
            result += check[i]
        elif i == '7-12 months':
            result += check[i]
        elif i == '2-6 months':
            result += check[i]
        elif i == '1-2 years':
            result += check[i]
        elif i == '> 2 years':
            result += check[i]
    
    return result