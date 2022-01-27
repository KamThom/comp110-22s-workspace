"""EX02 - Basic Wordle-like Game"""
__author__ = "730514879"
# python -m exercises.ex02_one_shot_wordle
# Rocinante


cor_ans = str("python")
cor_len = len(cor_ans)
sub = cor_len
var = str()
yellow = cor_len
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


guess = str(input(f"What is your {cor_len}-letter guess? "))

while len(guess) != cor_len:
    guess = str(input((f"That was not {cor_len} letters! Try again: ")))
    # this loops the given question untikl the parameters are met

while yellow >= 1:
    color = 0  # this reset the color variable to that a new white box can be added after eaxh itteration
    yellow_check = cor_len  # resets the variable so that it alwayse starts at the end of the correct word
    add = cor_len
    gue_char = guess[len(guess) - sub]  # this goes through and itterates down the guessed word to read each character withen
    gue_num = [len(guess) - sub]  # this assigns a number to each of the itterations
    
    while yellow_check >= 1:  # this while loop itterates through the correct answer and checks it against one guess character at a time
        yellow_char = cor_ans[len(cor_ans) - add] 
        yellow_num = [len(cor_ans) - add]

        if yellow_char == gue_char and yellow_num == gue_num:  # if the guess character = correct charcter and are in same place, put green. immediatly exit while loop
            var += GREEN_BOX
            add -= 1
            yellow_check -= 1 
            color = 0
            break

        elif yellow_char == gue_char and yellow_num != gue_num:  # if the guess character = correct charcter but not in same place, put yellow. immediatly exit while loop
            var += YELLOW_BOX
            add -= 1
            yellow_check -= 1
            color = 0
            break

        else:  # if characters do not match make color = 1 and exit this while loop
            color = 1
            add -= 1
            yellow_check -= 1

    ###

    if color == 1:  # if the characters do not match, then color = 1 and if color = 1 then a white box will be added
        var += WHITE_BOX
        # this is outside the other loop so that it does not add cor_len white boxes at every itteration
    yellow -= 1   # sets yellow down one to eventually match the last character in correct word
    sub -= 1  # itterates down the guessed word
    yellow_check = cor_len  # resets ellow check again just to be sure

###

print(var)

if guess == cor_ans:  # if guess == answer then do this. all at end of while loops for simplicity
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")