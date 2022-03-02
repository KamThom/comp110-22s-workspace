def only_evens(nums: list[int]) -> list:
    evn_lst = [] 
    sub = 1
    i = 0

    while i < len(nums):
        chck = nums.pop(len(nums) - sub)
        zro = chck % 2
        
        if zro == 0:
            evn_lst.append(chck)
            nums.append(chck)
            i += 1
            sub += 1
        else:
            nums.append(chck)
            i += 1
            sub += 1

    i = 1
    for var in evn_lst:
        evn_lst = [var] + evn_lst
        evn_lst.pop(len(evn_lst) - 1)

    return evn_lst

# from sandbox.testex05 import only_evens
# only_evens([2, 4, 3, 5, 8, 9])