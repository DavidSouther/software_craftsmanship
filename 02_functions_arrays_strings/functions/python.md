# Functions

Let's start with this program, that defines a function, a reusable block of
code, to draw a box on the terminal:

```python
import colors

print(colors.CLS)

def box(row, col, width, height):
    width = width - 2
    end = row + height-1
    print(colors.at(row, col) + u'\u2554' + u'\u2550' * width + u'\u2557')
    for i in range(row+1, end):
        print(colors.at(i, col) + u'\u2551' + " " * width + u'\u2551')
    print(colors.at(end, col) + u'\u255A' + u'\u2550' * width + u'\u255D')

print(colors.BLUE)
box(12, 20, 10, 3)
print(colors.NORMAL)
guess = input(colors.at(13, 21) + "Guess: ")
```

Type this program as `box_functions.py` and run it. If you make a new folder for
this chapter, make sure to save the [`colors.py`][colors.py] file in the same
folder. You should get the blue box from the HiLo program!

But now, what else can we get? Delete the last four lines, and try this:

```python
print(colors.BLUE)
box(11, 19, 12, 5)
box(12, 20, 10, 3)
for i in range(4, 80, 4):
    box(2, i, 2, 2)
print(colors.NORMAL)
```

Lots of boxes!

The first box command draws a big box, staring at (11, 19), and then a smaller
box directly inside that. It then goes through the `for...range` loop, which
uses a verson of range we haven't seen before. This time, it starts with the
value 4, then increases by 4 until it is greater than or equal to 80. That is,
it takes the values `4`, `8`, `12`, `16`, `20`, `24`, `28`, `32`, `36`, `40`,
`44`, `48`, `52`, `56`, `60`, `64`, `68`, `72`, and `76`. At each of those
columns, it draws a little 2x2 box!

Functions are great for grouping chunks of code together that you'd have to
run many times, either by typing over and over or copy/pasting. Let's look at
the box function a bit closer.

It starts with the Python keyword `def` - short for "Define", and used here to
"define" a function. The next word, `box`, tells Python what to call your
function, and is the word you'll use to refer to the function in the future,
like variables elsewhere. The parenthesis mark the *arguments* to the function.
Arguments are variables, but variables that are only valid inside the function.
The function declaration ends with the `:`.

The definition of the function is everything happening below that line at the
next indentation level. Remember that in Python, whitespace is important. An
**indentation level** is all code which has the same amount of leading spaces -
in our case, four.

## HiLo Revisited

# Functions

One of the most critical and fundamental concepts in computer programming is
Abstraction. You may have noticed your code getting a bit difficult to manage
towards the end of the HiLo program, especially if you added a lot of
functionality. Any large system becomes complex (almost by definition), and
managing that complexity is a huge factor in what computer programmers do on a
daily basis. One of the most useful ways to manage that complexity is the
concept of a function.

In its simplest form, a function is a way to group a related block of code
together, so that it only needs to be written once and can then be used many
times over. In the HiLo program, it would make sense to break each of the
messages into their own functions. In Python, this would look something like:

```python
import random

def title():
    print("HiLo")
    print()

def instructions():
    print("This is the game of HiLo.")
    print()
    print("You will have 6 tries to guess the amount of money in the")
    print("HiLo jackpot, which is between 1 and 100 dollars. If you")
    print("guess the amount, you win $10 for every guess you don't take!")
    print("Then you get another changc to win more money. However,")
    print("if you do not guess the amount, the game ends!")
    print()

def get_guess():
    guess = input("Your guess: ")
    return int(guess)

def check_guess(guess, number):
    if guess > number:
        print("Too Hi!")
        return false
    elif guess < number:
        print("Too Lo!")
        return false
    else:
        print("You win!")
        return true

def calc_winnings(number, guesses):
    print("You won " + str(number) + " dollars!")
    winnings = (6 - guesses) * 10
    print("Your latest winnings are " + str(winnings) + " dollars!")
    return winnings

def play_round():
    guesses = 0
    number = random.randint(1, 10)

    while guesses < 6:
        guesses += 1
        guess = get_guess()
        if checkGuess(guess, number):
            return calc_winnings(number, guesses)

    print("You took too many guesses!")
    return 0

def play_again():
    again = input("Play again? (Y/n) ")
    reaturn again != "n"

def finished(winnigs):
    print("Thank you for playing! Your total winnings were " + str(winnings) + " dollars!")

def game():
    title()
    instructions()
    winnings = play_round()
    while play_again():
        winnings += play_round()
    finished(winnings)

game()
```

You can see how each section gets broken out into its own small piece, which can
be written and understood in isolation, rather than having to work on the entire
program at once. All the text to print out the title and instructions banner have
been isolated into their own sections. After that, the program defines several
functions for each isolated part of the game. The `get_guess` function asks for a
player's gues, and then returns it as an integer. Check guess takes a target number
and a guessed number, compares them, prints the apropriate message, and returns
`True` if the user guessed correctly, and `False` if they did not. That value is
used in `play_round`, which generates a random number, and asks the user for a guess
until they run out of guesses. If it has returned true, the game will use
`calc_winnings` to figure out how much that game was worth. `game` coordinates all
the pieces. First it prints the banner lines. Then, it plays the first round. The
game continues to play rounds until the user, during `play_again`, asks not to. The
game adds up all the winnings after each round, and at the very end, prints the
total the user has won.

Pew!

Take some time to practice with functions. Take your HiLo program, wiht the
additional features you added, and try breaking it up into functions similar to how
we have here!
