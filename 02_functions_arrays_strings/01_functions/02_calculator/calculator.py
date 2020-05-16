def get_two_numbers():
    num1 = input("First number? ")
    num2 = input("Second number? ")
    return float(num1), float(num2)

def addition():
    num1, num2 = get_two_numbers()
    result = num1 + num2
    print(str(num1) + " + " + str(num2) + " = " + str(result))

def subtraction():
    num1, num2 = get_two_numbers()
    result = num1 - num2
    print(str(num1) + " - " + str(num2) + " = " + str(result))

def menu():
    print("1. Addition")
    print("2. Subtraction")
    return input("What is your selection? ")

while True:
    selection = menu()
    if selection == "1":
        addition()
    elif selection == "2":
        subtraction()
    else:
        # No entry, done calculating
        break
    input("Press enter to continue...")
exit()
import colors

def get_two_numbers():
    print(colors.CLEAR)
    colors.box(5, 5, 28, 3)
    num1 = input(colors.at(6, 6) + "First number? ")
    print(colors.at(6, 6) + " " * 26)
    num2 = input(colors.at(6, 6) + "Second number? ")
    print(colors.at(6, 6) + " " * 26)
    return float(num1), float(num2)

def addition():
    num1, num2 = get_two_numbers()
    result = num1 + num2
    print(colors.at(6, 6), num1, '+', num2, '=', result)

def subtraction():
    num1, num2 = get_two_numbers()
    result = num1 - num2
    print(colors.at(6, 6), num1, '-', num2, '=', result)

def multiplication():
    num1, num2 = get_two_numbers()
    result = num1 * num2
    print(colors.at(6, 6), num1, '*', num2, '=', result)

def division():
    num1, num2 = get_two_numbers()
    result = num1 / num2
    print(colors.at(6, 6), num1, '/', num2, '=', result)

def menu():
    print(colors.CLEAR)
    colors.box(4, 4, 30, 7)
    print(colors.at(5, 5), "1. Addition")
    print(colors.at(6, 5), "2. Subtraction")
    print(colors.at(7, 5), "3. Multiplication")
    print(colors.at(8, 5), "4. Division")
    return input(colors.at(9, 5) + "What is your selection? ")

def calculator():
    while True:
        selection = menu()
        if selection == "1":
            addition()
        elif selection == "2":
            subtraction()
        elif selection == "3":
            multiplication()
        elif selection == "4":
            division()
        else:
            # No entry, end the program
            break
        input(colors.at(8, 5) + "Press enter to continue...")

calculator()
print(colors.CLEAR)