"""magic eight ball of truth"""

from random import randint 

input("Ask a yes or no question: ")

response: int = randint(0,3)

if response == 0:
    print("Most likely")

else:
    if response == 1:
        print("Hopeful")
    else:
        if response == 2:
            print("Doubtful")
        else:
            print("unlikely")