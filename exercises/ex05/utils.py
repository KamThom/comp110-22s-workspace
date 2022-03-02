"""Utility functions."""
__author__ = "730514879"


def only_evens(nums: list[int]) -> list[int]:
    """Finds all of the even nums in a list."""
    evn_lst = [] 
    sub = 1
    i = 0

    while i < len(nums):  # thsi section takes in all of the nums in the list and then checks if they are even
        chck = nums.pop(len(nums) - sub)
        zro = chck % 2  # returns 0 if even
        
        if zro == 0:
            evn_lst.append(chck)
            nums.append(chck)
            i += 1
            sub += 1
        else:
            nums.append(chck)
            i += 1
            sub += 1

    for var in evn_lst:  # this takes that list of even nums and flips is around so its forward
        evn_lst = [var] + evn_lst
        evn_lst.pop(len(evn_lst) - 1)

    return evn_lst


def sub(lst: list[int], start: int, end: int) -> list[int]:
    """Makes a smaller list from a bigger list given peramaters."""
    length = []

    if len(lst) == 0 or start > len(lst) or end <= 0:
        return []

    if start < 0:
        start = 0

    if end > len(lst):
        end = len(lst)
    
    while start <= end - 1:  # this creates a list of nums between the given start and end perams
        length.append(start)
        start += 1
    
    sub_lst = [lst[i] for i in length]  # this takes the list of nums previously made and gives the value of the num at that point in the OG list
    return sub_lst


def concat(first: list[int], sec: list[int]) -> list[int]:
    """Adds two lists together."""
    i = 0
    fl = []
    fl.append(i)
    sl = []
    sl.append(i)
    addit = []

    while len(fl) < len(first):  
        i += 1
        fl.append(i)
# these two while loops makes an indicie counter for the len of the two lists 
    i = 0
    while len(sl) < len(sec):
        i += 1
        sl.append(i)
    
    if len(first) > 0: 
        for index in fl:
            addit.append(first[index])
# if the len of the OG lists ar > 0, these for loops will add the numbers in those lists to the new list 
    if len(sec) > 0:
        for index in sl:
            addit.append(sec[index])

    return addit
       