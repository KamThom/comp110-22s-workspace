"""6-guess Worlde...but with functions"""
__author__ = "730514879"
# python -m sandbox.testex03
# # from sandbox.testex03 import contains_char
# from sandbox.testex03 import emojified
# emojified("python", "woohoo")
# from sandbox.testex03 import input_guess
# from sandbox.testex03 import main
# python -m exercises.ex03_wordle


def main():
    """The entrypoint of the program and main game loop."""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    
    turns = 1
    answer = "codes"
    ans_len = len(answer)

    def contains_char(answer: str, guess_char: str):
        """iterate through answer"""
        assert len(guess_char) == 1

        cor_len = len(answer)
        num = cor_len
        ans_char = answer[len(answer) - num]
        search_len = cor_len

        while search_len > 0:
            ans_char = answer[len(answer) - num]
            ans_num = [len(answer) - num]

            if guess_char == ans_char:
                return True, ans_num

            search_len -= 1
            num -= 1

        return False

    def emojified(guess: str, answer: str):
        """checks each answer char to each guess char for match and emoji supplement"""
        assert len(guess) == len(answer)

        guess_len = len(guess)
        i = guess_len
        sub = guess_len
        sec_code = ""

        while i > 0:  # picks out the guess char and guess char_num

            gue_char = guess[len(guess) - sub]
            gue_num = len(guess) - sub
            gue_num = str(gue_num)
            contains_char(answer, gue_char)
            finder = str(contains_char(answer, gue_char))
            # will return (p,0) + (T,0) if guess == python and answer == piddle

            if contains_char(answer, gue_char):
                ans_num = finder[len(finder) - 3]

                if ans_num == gue_num:
                    sec_code += GREEN_BOX
                    # print(gue_num, ans_num, "1", gue_char, i)
                    
                elif ans_num != gue_num and True:
                    sec_code += YELLOW_BOX
                    # print(gue_num, ans_num, "2", gue_char, i)

            else:
                sec_code += WHITE_BOX
                # print(gue_num, "3")

            i -= 1
            sub -= 1

        return sec_code

    def input_guess(exp_len: int) -> str:
        """prompt user to give guess with x length"""

        guess = str(input(f"Enter a {exp_len} character word: "))

        while len(guess) != exp_len:
            guess = str(input(f"That wasn't {exp_len} chars! Try again:"))

        return guess
    
    while turns <= ans_len:
        exp_len = len(answer)
        print(f"=== Turn {turns}/{exp_len} ===")
    
        guess = input_guess(exp_len)
        code = emojified(guess, answer)
        print(code)

        if guess == answer:
            return print(f"You won in {turns}/{ans_len} turns!")

        turns += 1
    return print(f"X/{ans_len} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
