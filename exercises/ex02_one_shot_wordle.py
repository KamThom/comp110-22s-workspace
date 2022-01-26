"""EX02 - Basic Wordle-like Game"""
__author__ = "730514879"
# python -m exercises.ex02_one_shot_wordle
# Rocinante


cor_ans = str("python")
cor_len = len(cor_ans)
len_chng = cor_len
sub = cor_len
var = str()
box_color = str()
yell = str()
yellow = cor_len
less = cor_len
white = 0
color = 0
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


guess = str(input(f"What is your {cor_len}-letter guess? "))

while len(guess) != cor_len:
    guess = str(input((f"That was not {cor_len} letters! Try again: ")))

while yellow >= 1:
    color = 0
    yellow_check = cor_len
    add = cor_len
    gue_char = guess[len(guess) - sub]
    gue_num = [len(guess) - sub]
    
    while yellow_check >= 1:
        yellow_char = cor_ans[len(cor_ans) - add]
        yellow_num = [len(cor_ans) - add]

        if yellow_char == gue_char and yellow_num == gue_num:
            var += GREEN_BOX
            add -= 1
            yellow_check -= 1 
            color = 0
            break

        elif yellow_char == gue_char and yellow_num != gue_num:
            var += YELLOW_BOX
            add -= 1
            yellow_check -= 1
            color = 0
            break

        else:
            color = 1
            add -= 1
            yellow_check -= 1

    ###

    if color == 1:
        var += WHITE_BOX

    yellow -= 1
    sub -= 1
    yellow_check = cor_len

###

print(var)

if guess == cor_ans:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")