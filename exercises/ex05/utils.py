"""Utility functions."""
__author__ = "730514879"

# from exercises.ex05.utils import only_evens
# only_evens([2,3,2,5,3,6,8])
# from exercises.ex05.utils import sub
# sub([1, 2, 4, 5, 6, 2, 3], 1, 4)


def only_evens(nums: list[int]) -> list:
    evn_lst = [] 
    sub = 1
    i = 0

    while i < len(nums):
        chck = nums.pop(len(nums) - sub)
        zro = chck % 2
        # print(chck)
        
        if zro == 0:
            evn_lst.append(chck)
            nums.append(chck)
            i += 1
            sub += 1
        else:
            nums.append(chck)
            i += 1
            sub += 1

    return evn_lst


def sub(lst: list[int], start: int, end: int) -> list:
    length = []

    if len(lst) == 0 or start > len(lst) or end <= 0:
        return []

    if start < 0:
        start = 0

    if end > len(lst):
        end = len(lst)
    
    while start <= end - 1:
        length.append(start)
        start += 1
    
    sub_lst = [lst[i] for i in length]
    return sub_lst


def concat(first: list[int], sec: list[int]) -> list:
    i = 0
    fl = []
    fl.append(i)
    sl = []
    sl.append(i)
    addit = []

    while len(fl) < len(first):
        i += 1
        fl.append(i)
    
    i = 0
    while len(sl) < len(sec):
        i += 1
        sl.append(i)
    
    if len(first) > 0:
        for index in fl:
            addit.append(first[index])
    
    if len(sec) > 0:
        for index in sl:
            addit.append(sec[index])

    return addit
       