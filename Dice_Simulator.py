# DICE SIMULATOR
# DEVLOPER : CHANCHAL ROY

from random import randint
number = randint(1,6)
magic = randint(1,50)

if magic == 12: print(f"Sorry there are theree Six . You miss the chance!")

else:
    if number == 6:
        number2 = randint(1,6)
        if number2 == 6:
            number3 = randint(1,6)
            if number3 == 6: print(f"Sorry there are theree Six . You miss the chance!")
            else: print(f"You have two Six and and {number3}")

        else: print(f"You have one Six and {number2}")
        
    else: print(f"Your Dice Number is {number}.")