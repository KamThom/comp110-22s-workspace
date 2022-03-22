"""CSV file utility functions."""
from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """return the rows of a csv"""
    result: list[dict[str, str]] = []

    file_handle = open(filename, "r", encoding="utf8")

    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)

    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Make a list of all values in a column"""
    result: list[str] = []

    for row in table:
        item: str = row[column]
        result.append(item)

    return result


def coulmnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row table to column table"""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]

    for column in first_row:
        result[column] = column_values(row_table, column) 

    return result
    
