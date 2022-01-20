"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730514879"

print("Enter a 5-character word: ", end=""),
word: str = str(input())
# end="" makes it so the input is added on after the print function
val = len(word)

if val == 5:
    print("Enter a single character: ", end=""),
    char: str = str(input())
    if len(char) == 1:
        print("Searching for " + str(char) + " in " + str(word))

        if char in word:
            # each variable is set to a character in the given word to be called later
            a = word[0]
            b = word[1]
            c = word[2]
            d = word[3]
            e = word[4]

            if a == char:
                a = [len(word) - 5]
                # the '-#' is to give the location of that varible in ascending order by aking the max len and subtracting
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
                # if all character in word == char, this last if exits the if statement and prints the desired message
                # word.count gives me the number of instances of char in word very simply
                print(str(word.count(char)) + " instances of " + str(char) + " found in " + str(word)) 
    
        else:
            # next three else statements are self explnitory 
            print("no instances of " + char + " found in " + word)
    else:
        print("Error: Character must be a single character.")
else:
    print("Error: Word must contain 5 characters")
    

# exercises.ex01_chardle