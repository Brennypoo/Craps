import random

i=0
seven_count = 0
field_count = 0
top_count =0
numRolls=100000
while i <numRolls:
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2

    if dice_sum == 7:
        seven_count +=1
    if dice_sum == 2 or dice_sum == 3 or dice_sum == 4 or dice_sum == 9 or dice_sum == 10 or dice_sum == 11 or dice_sum == 12:
        field_count += 1
    if dice_sum == 4 or dice_sum == 5 or dice_sum == 6 or dice_sum == 9 or dice_sum == 10 or dice_sum == 8:
        top_count += 1
    i += 1

seven_percent = seven_count/numRolls
field_percent = field_count/numRolls
place_percent = top_count/ numRolls

print(f"{seven_percent * 100}% chance of hitting a seven")
print(f"{field_percent * 100}% chance of hitting the field")
print(f"{place_percent * 100}% chance of hitting a place bet")

