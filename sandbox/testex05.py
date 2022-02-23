def sub(lst: list[int], start: int, end: int) -> list:
    length = []

    if len(lst) == 0 or start > len(lst) or end <= 0:
        return []

    if start < 0:
        start = 0

    if end > len(lst):
        end = len(lst)
    
    # If the length of the list is 0, start > len of the list or end <= 0, return the empty list.
    while start <= end - 1:
        length.append(start)
        start += 1
    
    sub_lst = [lst[i] for i in length]
    return sub_lst

        
# sub([1, 2, 4, 5, 6, 9, 3], 1, 4)
# 1, 2, 4, 5, 6, 9, 3
# len(lst) = 7
# start = 1 (2)
# end = 4 (5)
# return [2, 4, 5]