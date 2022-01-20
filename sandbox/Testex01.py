"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730514879"

print("Enter a 5-character word: ", end=""),
word: str = str(input())

val = len(word)

if val == 5:
    print("Enter a single character: ", end=""),
    char: str = str(input())

    if len(char) == 1:
        print("Searching for " + str(char) + " in " + str(word))

        if char in word:
            a = word[0]
            b = word[1]
            c = word[2]
            d = word[3]
            e = word[4]
            ext = word[4]

            if a == char:
                a = [len(word) - 5]
                print(str(char) + " found at index " + str(a))
            if b == char:
                b = [len(word) - 4]
                print(str(char) + " found at index " + str(b))
            if c == char:
                c = [len(word) - 3]
                print(str(char) + " found at index " + str(c))
            if d == char:
                d = [len(word) - 2]
                print(str(char) + " found at index " + str(d))
            if e == char:
                e = [len(word) - 1]
                print(str(char) + " found at index " + str(e))
            if char == char:
                print(str(word.count(char)) + " instances of " + str(char) + " found in " + str(word)) 
        else:
            print("no instances of " + char + " found in " + word)
    else:
        print("Error: Character must be a single character.")
else:
    print("Error: Word must contain 5 characters")
    

# exercises.ex01_chardle