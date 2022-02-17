"""examples of list based actions"""

from random import randint

rolls: list[int] = list()

while len(rolls) == 0 or rolls[len(rolls) - 1] != 1:
    rolls.append(randint(1, 6))

print(rolls)

rolls.pop(len(rolls) - 1)
print(rolls)

i = 0
sum = 0

while i < len(rolls):
    sum += rolls[i]
    i += 1

print(sum)