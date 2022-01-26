"""example while loop"""

counter: int = 0
maximum: int = int(input("Count up to but not including what? "))

while counter < maximum:
    counter_squared = counter ** 2
    print("The square of " + str(counter) + " is " + str(counter_squared))
    counter += 1 
print("Done")