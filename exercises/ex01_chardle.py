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
            # they are set as str becasue i got an error in gradescope wanting them to be a str but this did not help
            a = str(word[0])
            b = str(word[1])
            c = str(word[2])
            d = str(word[3])
            e = str(word[4])

            if a == char:
                a = str([len(word) - 5])
                # the '-#' is to give the location of that varible in ascending order by aking the max len and subtracting
                print(str(char) + " found at index " + str(a)[1:-1])
                # the [1:-1] makes it so the "list" is printed without brackets. It just removes the first and last characters of a lsit

            if b == char:
                b = str([len(word) - 4])
                print(str(char) + " found at index " + str(b)[1:-1])

            if c == char:
                c = str([len(word) - 3])
                print(str(char) + " found at index " + str(c)[1:-1])

            if d == char:
                d = str([len(word) - 2])
                print(str(char) + " found at index " + str(d)[1:-1])

            if e == char:
                e = str([len(word) - 1])
                print(str(char) + " found at index " + str(e)[1:-1])

            if char == char and word.count(char) == 1:
                # if all character in word == char, this last if exits the if statement and prints the desired message
                # word.count gives me the number of instances of char in word very simply
                print(str(word.count(char)) + " instance of " + str(char) + " found in " + str(word)) 

            if char == char and word.count(char) > 1:
                # this new if statement is used if more than one instance is found giveing plurality to instances 
                print(str(word.count(char)) + " instances of " + str(char) + " found in " + str(word))
    
        else:
            # next three else statements are self explnitory 
            print("no instances of " + char + " found in " + word)
    else:
        print("Error: Character must be a single character.")
        exit()
else:
    print("Error: Word must contain 5 characters")
    exit()
    

# exercises.ex01_chardle