"""
Camel Game
"""

import random

user_input = ""
done = False
miles_traveled = 0
your_thirst = 0
sleepy_camel = 0
native_miles = (-20)
canteen_water = 3
iterations = 0

def a():
    global canteen_water, your_thirst
    if canteen_water == 0:
        print("You have no water")
    elif canteen_water > 0:
        canteen_water -= 1
        your_thirst -= 1
        print("You took a drink.")

def b():
    global your_thirst, miles_traveled, sleepy_camel, native_miles, canteen_water, current_travel, natives_travel
    current_travel = random.randrange(7, 12)
    miles_traveled = miles_traveled + current_travel
    your_thirst += 1
    sleepy_camel += 1
    natives_travel = random.randrange(3, 8)
    native_miles = native_miles + natives_travel
    if random.randrange(20) == 12:
        your_thirst = 0
        canteen_water = 3
        sleepy_camel = 0
        print("You found an oasis!")
        print("Your canteen is filled, and your camel is rested.")
    print("You Traveled", current_travel, "miles.")

def c():
    global native_miles, your_thirst, canteen_water, sleepy_camel, miles_traveled, current_travel
    current_travel = random.randrange(10, 20)
    miles_traveled= miles_traveled + current_travel
    your_thirst += 1
    sleepy_camel += 1
    natives_travel = random.randrange(5, 12)
    native_miles = native_miles + natives_travel
    if random.randrange(20) == 7:
        your_thirst = 0
        canteen_water = 3
        sleepy_camel = 0
        print("You found an oasis!")
        print("Your canteen is filled, and your camel is rested.")
    print("You traveled", current_travel, "miles.")

def d():
    global sleepy_camel, native_miles, natives_travel
    sleepy_camel = 0
    natives_travel = random.randrange(5, 10)
    native_miles = native_miles + natives_travel
    print("Your camel is happy and rested.")

def e():
    print("Miles Traveled:", miles_traveled)
    print("Drinks in Canteen:", canteen_water)
    print("The natives are", native_distance(), "miles behind you.")

def q():
    print("You gave up. The natives caught you.")
    print("The Camel is happy to be home. Only minor therapy needed after being kidnapped.")

def native_distance():
    return (miles_traveled - native_miles)


def main():
    global user_input
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi Desert.")
    print("The natives want their camel back and are chasing you down! Survive your")
    print("desert trek and out run the natives.")

    while user_input !="Q":
        print("A. Drink from your canteen")
        print("B. Ahead moderate speed")
        print("C. Ahead full speed")
        print("D. Stop for the night")
        print("E. Status Check")
        print("Q. Quit")
        user_input = input("What is your choice? ")

        if user_input.upper() =="Q":
            q()
            break

        elif user_input.upper() == "A":
            a()

        elif user_input.upper() == "B":
            b()

        elif user_input.upper() == "C":
            c()

        elif user_input.upper() == "D":
            d()

        elif user_input.upper() == "E":
            e()

        if your_thirst > 6:
            print("You died of thirst")
            break
        elif your_thirst >= 4:
            print("You are thirsty.")

        if sleepy_camel >= 7:
            print("Your Camel is dead")
            break
        elif sleepy_camel >= 5:
            print("Your Camel is getting tired")

        if canteen_water <= 0:
            print("Your canteen is empty")

        if native_miles >= miles_traveled:
            print("The Natives have caught you.")
            print("The Camel is happy to be home! Only minor therapy needed after being kidnapped.")
            break
        elif native_distance() <= 15:
            print("The Natives are getting close, pick up the pace.")

        if miles_traveled >= 200:
            print("You have escaped the desert amd the natives have given up.")
            print("Congratulations, You have won the game!!")
            break

main()