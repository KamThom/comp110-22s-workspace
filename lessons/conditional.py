"""Example conditional (if-else) statements"""

SECRET: int = 3

print("I'm thinking of a number between 1 and 5, what is it?")
guess: int = int(input("What is your guess? "))

if guess == SECRET:
    print("You guessed correctly!!!")
    print("Have a wonderful day! :)")
else:
    print("Sorry, you guessed incorrectly :(")
    if guess > SECRET:
        print("Your guess was to high")
    else:
        print("Your guess was to low")


print("Game over.")
