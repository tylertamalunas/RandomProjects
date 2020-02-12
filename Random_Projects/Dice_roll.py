"""
User inputs which dice they are rolling and how many, and then this calls the correct function to roll
the dice and show the player their roll.
D20, D12, D10, D8, D6, D4
"""
import random

number_of_dice = int(input("Number of dice: "))
dice_sides = int(input("Amount of sides: "))


class Dice:
    def d4(self):
        roll_number = 1
        rolls = []
        while roll_number <= number_of_dice:
            roll_number += 1
            rolls.append(random.randint(1, dice_sides))
        return rolls

    def d6(self):
        roll_number = 1
        rolls = []
        while roll_number <= number_of_dice:
            roll_number += 1
            rolls.append(random.randint(1, dice_sides))
        return rolls

    def d8(self):
        roll_number = 1
        rolls = []
        while roll_number <= number_of_dice:
            roll_number += 1
            rolls.append(random.randint(1, dice_sides))
        return rolls

    def d10(self):
        roll_number = 1
        rolls = []
        while roll_number <= number_of_dice:
            roll_number += 1
            rolls.append(random.randint(1, dice_sides))
        return rolls

    def d12(self):
        roll_number = 1
        rolls = []
        while roll_number <= number_of_dice:
            roll_number += 1
            rolls.append(random.randint(1, dice_sides))
        return rolls

    def d20(self):  # Should this just be for one dice or also include 2+?
        roll_number = 1
        rolls = []
        while roll_number <= number_of_dice:
            roll_number += 1
            rolls.append(random.randint(1, dice_sides))
        return rolls


dice = Dice()
if dice_sides == 4:
    print(dice.d4())
elif dice_sides == 6:
    print(dice.d6())
elif dice_sides == 8:
    print(dice.d8())
elif dice_sides == 10:
    print(dice.d10())
elif dice_sides == 12:
    print(dice.d12())
elif dice_sides == 20:
    print(dice.d20())
