
def repeat(word, rpt) -> str:
    num = len(word)
    char = word[len(word) - num]
    z = ""
    i = 0

    while i < len(word):
        a = char * rpt
        z += a 
        i += 1
        num -= 1
    
    return z


# from sandbox.random import repeat
# repeat("tar", 3)