import random

choice = "y"
while choice.lower() == "y":
    rolled_num = random.randint(1,6)
    print("You rolled : " + str(rolled_num))
    choice = input("Do you want to roll again? ")
    print()