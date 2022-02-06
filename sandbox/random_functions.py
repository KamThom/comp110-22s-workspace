def mystery(n: int):
    i = 0

    while i < n:
        if i % 2 == 1:
            return "ooh"
        i += 1
    return "ahh"

    # >>> mystery(4)
    # 'ooh'
    #