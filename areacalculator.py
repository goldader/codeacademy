"""CodeAcademy project to return the area of a shape based on the user's selected shape and input dimensions"""

from math import pi
from time import sleep
from datetime import datetime

now = datetime.now()
hint = "Don't forget to include the correct units! \nExiting..."
shape_list = ("C", "T")

# startup the calculator
print("The calculator is starting up!")
print("\nThe current date and time is %s/%s/%s %s:%s") % (now.month, now.day, now.year, now.hour, now.minute)

option = input("Enter C for Circle or T for Triangle: ")

if option.upper() in shape_list:
    if option.upper() == "C":
        print("\nYou chose a circle")
    else:
        print("\nYou chose a triangle.")
else:
    print("\nYou've not chosen a shape we can calculate")

if option.upper() == "C":
    radius = float(input("\nWhat is the radius of your circle: "))
    area = pi * (radius ** 2)
    print("The pie is baking ...")
    # sleep the programme for 1 second to simulate thinking
    sleep(1)
    print("\nThe area of your circle is " + str(round(area, 2)) + ".\n" + hint)
elif option.upper() == "T":
    print("\nWe need to know the base and height of your trianle.")
    base = float(input("\nWhat is the base of your triangle: "))
    height = float(input("\nWhat is its height: "))
    area = 0.5 * base * height
    print("Uni Bi Tri ...")
    # sleep the programme for 1 second to simulate thinking
    sleep(1)
    print("\nThe area of your triangle is " + str(round(area, 2)) + ".\n" + hint)
else:
    print("\nGoodbye")
