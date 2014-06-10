from pyqb import COLORS, CLS, NORMAL, BOLD, at, box
from time import sleep

def addition():
    print CLS
    box(5, 5, 28, 3)
    num1 = input(at(6, 6) + "First number? ")
    print at(6, 6) + " " * 26
    num2 = input(at(6, 6) + "Second number? ")
    print at(6, 6) + " " * 26
    print at(6, 6), num1, '+', num2, '=', num1 + num2
    raw_input()


def menu():
    print CLS
    box(4, 4, 30, 5)
    print at(5, 5), "1. Addition"
    print at(6, 5), "2. Subtraction"
    return input(at(7, 5) + "What is your selection? ")

while True:
    selection = menu()
    if selection == 1:
        addition()
    elif selection == 2:
        subtraction()
