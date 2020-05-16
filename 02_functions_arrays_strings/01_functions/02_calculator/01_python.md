# Calculator

To get a better feel for how functions work, we're going to write a program
that's similar to rugs. It will ask the user what type of calculation they would
like to perform. Then it will ask them for their input. It will get the input
from a separate function than the ones that do the calculation. Once the
operation is done, it'll print the results, before going back to do it all again
(until the user stops asking it to, anyway).

```
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
    print()
```

Type this in and play with it. A typical session might look like this:

```
1. Addition
2. Subtraction
What is your selection? 1
First number? 4
Second number? 3
4.0 + 3.0 = 7.0
Press enter to continue...

1. Addition
2. Subtraction
What is your selection? 2
First number? 4
Second number? 6
4.0 - 6.0 = -2.0
Press enter to continue...

1. Addition
2. Subtraction
What is your selection? 1
First number? 2
Second number? 2991.23923
2.0 + 2991.23923 = 2993.23923
Press enter to continue...

1. Addition
2. Subtraction
What is your selection?
```

This program should look very familiar to the rugs! There are a few things to
call out. None of the functions have any parameters. We might call these
"Procedures", because instead of taking some value as input and returning the
result of a calculation, they simply go off on their own, do their work, and
then come back with no additional guidance needed. The function that does return
something back is `get_two_results`, and here we see it using python's ability
to return several things from functions (if necessary), but using `return num1, 
num2`. When assigning to variables in the calling (the original) function, it
does the same thing and just says `num1, num2 = get_two_inputs()`. 

## Exercises

*   Add multiplication and division functions.
*   Add a division remainder function. 
*   Using the tracing techniques from the textbook, trace through how the
    program executes using a few inputs.
