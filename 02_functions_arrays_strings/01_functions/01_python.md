# Functions

Let's start with this program, that defines a function, a reusable block of
code, to calculate the price of our square rug from chapter 1:

```python
def square_rug_cost(size, fringe):
    area = size ** 2
    cost = area * 5
    if (fringe):
        perimeter = size * 4
        cost = cost + perimiter * 1.5
    return cost

print(square_rug_cost(5, False))
print(square_rug_cost(5, True))
```

Type this program as `box_functions.py` and run it. You should see it print out
the two rug costs - 125 and 155, respectively.

Let's take a closer look at the anatomy of this function. Recall from the
textbook portion that a function needs three things: A name, its parameters
(also called arguments), and a body. In this square_rug_cost function, those
look like this:

![diagram of a python function](./digraph_of_a_python_function.png)

In python, a function starts with the key word `def`. That's followed by its
name, in this case `box`. It then has twu parameters, all inside the
parenthises - `(size, fringe)`. Finally, in python, the function declaration
(the name and argument list) ends with the `:` (colon). We've seen this in
the chapter on control flow as well, and it indicates that we're about to
group a bunch of code at the next indentation level.

To get an indentation level, we add a new line (press enter on our keyboard)
and indent one level. There are several ways to indent. One is to hit the tab
key on your keyboard. Another is to add some number of spaces - at least two,
but four and eight are also common. A third way is to let VSCode do it for
you! You've probably seen this already when working through the first
chapter, that VSCode would automatically add the indendation for you when you
started a new line after a `:` colon.

So, why does Python have so many ways to do indentation? Mostly it's
historical reasons. For our purposes, we're going to start with using 4
spaces for indentation, because that's VSCode's default, and usually it'll
handle it for us. The only rule is to be consistent with the amount of
indentation you use in your program.

## One function, many calculations

Now that we have a function that prints a box, what else can we get? Delete the
last two lines of file you started, and try this instead:

```python
size = input("Rug size (empty to quit): ")
while size != "":
    size = float(size)
    fringe = input("Does the rug have fringe (y/n)? ")
    fringe = fringe == "y"
    cost = square_rug_cost(size, fringe)
    print(cost)

    # Get the size for the next rug
    size = input("Rug size (empty to quit): ")
print("Goodbye")
```

We can price (square) rugs over and over!

So now our function just loops as long as the user gives us a size, asks if
they want fringe with that, and prints the rug price. That's good, but it
actually took more lines of code than if we'd just written it all inline...
We'll come back to that. For now, bear with me two more steps. First, we
will turn that input into its own function. Then, we're going to do make
two similar functions for a rectangular rug. While that will look like
more code than we needed, it will pay off when we add circles and start
talking about abstraction.

But wait a minute, why do we have `cost` in two different places? Those are
actually two completely separate variables, in what we call different scopes.
Every function starts a new **scope**, which is a way to set a new group of
variables it knows about. A function knows about all the variables in any scope
outside of it, as well as all the variables it declares. However, the variables
that get declared _inside_ the function aren't visible further out. This neatly
allows each function to do its own work without stepping on the toes of other
functions! Also, the base level of every file is its own scope.

Aside from files, only functions with `def` define new scopes. The body of a
`while` loop or `if` block does not create a new scope!

Let's take that while loop, and break it into a function and a loop. Delete
everything you typed in the last section, and type this instead.

```python
def compute_square_rug():
    size = float(input("Rug Size: "))
    fringe = input("Does the rug have fringe (y/n)? ")
    fringe = fringe == "y"
    cost = square_rug_cost(size, fringe)
    print(cost)

while input("Price a rug (y/n)? ") == "y":
    compute_square_rug()
```

But why are we adding more code when it just does the same thing!? ARGH!
I asked you to stay with me one more step, before we see the pay off.
First, delete the last two lines (the while loop that asks whether to
price another rug), and then add this:

```python
def rectangular_rug_cost(width, height, fringe):
    area = width * height
    cost = area * 5
    if fringe:
        perimeter = width * 2 + height * 2
        cost += perimeter * 1.5
    return cost

def compute_rectangular_rug():
    width = float(input("Rug width: "))
    height = float(input("Rug height: "))
    fringe = input("Fringe (y/n)?: ") == "y"
    print(rectangular_rug_cost(width, height, fringe))

while input("Price another rug (y/n)? ") == "y":
    rug_type = input("(1) square or (2) rectangular? ")
    if rug_type == "1":
        compute_square_rug()
    elif rug_type == "2":
        compute_rectangular_rug()
```

At this point, we've written four functions. For each rug type, we have two
functions - one to perform the calculation, and one to perform the user
input. So why would we write all four of these, instead of just one loop?
The first answer is to make it easier to read and understand. One big
function or loop body would be shorter to write, yes, but in sofware
engineering there's a somewhat paradoxical fact that code is read by humans
much more often than it's written. You've likely seen this yourself while
trying to get your prior programs to work - you would run it, it wouldn't
work right or you'd get an error, and then you had to go back through many
times reading it to figure out what it was doing.

By separating out each task into functions like this, you are using
_abstraction_. Each function lets us move from handling the details of getting
input or calculating a rug size, to instead working with the *idea* of getting
input or calculating the rug's size. Why is this useful? Mainly, it means
that now whenever I think about calculating a rug, I don't need to remember
the formulas for its area and perimeter, I only need to know which parameters
are necessary.

It also gives us a good separation of concerns. That's a fancy way of saying
the opposite of what was in the last paragraph - from the ouside, I only
need to know what parameers to pass the function and it does the work. From
the inside, I only need to take those parameters and do the calculation. I don't
care how I got those parameters! The could come from a command line interface,
like here, or in chapter 5, they could come from a web server which provides
this functionality to customers online. That separation is a great boon that
abstraction using functions gives us.

## Anatomy of a function

Let's cover the critical pieces of a function again.

It starts with the Python keyword `def` - short for "Define", and used here to
"define" a function. The next word, `square_rug_cost` or `calculate_rectangular_rug`,
tells Python what to call your function. It is the word you'll use to refer to
the function in the future, like variables elsewhere. The parentheses mark the
*arguments* to the function. Arguments are variables, but variables that are only
visible and valid inside the function. The function declaration ends with the `:`.

The definition of the function is everything happening below that line at the
next indentation level. Remember that in Python, whitespace is important. An
**indentation level** is all code which has the same amount of leading spaces -
in our case, four. Just like in `if` and `for` and `while` loops, this code at
the same level of indendation is the **function body** is what gets executed
each time you call your function.

Ok, let's write one more function, this time to combine the two rugs we had
before. Again, delete the "Price another rug" while loop, and add this.

```python
def choose_rug():
    type = input("Would you like to price a (S)quare rug or a (R)ectangular rug? ")
    if type == "S" or type == "s":
        compute_square_rug()
    elif type == "R" or type == "r":
        compute_rectangular_rug()
        
while input("Price another rug (y/N)? ") == "Y":
    choose_rug()
```

I don't know about you, but I really like how easy it is to read and understand
what this block of code is doing compared to the big long chunks we had in
chaper 1!

On your own, try to add the circle calculations using the same set up we have here.

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
    print("Then you get another chance to win more money. However,")
    print("if you do not guess the amount, the game ends!")
    print()

def get_guess():
    guess = input("Your guess: ")
    return int(guess)

def check_guess(guess, number):
    if guess > number:
        print("Too Hi!")
        return False
    elif guess < number:
        print("Too Lo!")
        return False
    else:
        print("You win!")
        return True

def calc_winnings(guesses):
    winnings = (6 - guesses) * 10
    print("You won " + str(winnings) + " dollars!")
    return winnings

def play_round():
    guesses = 0
    number = random.randint(1, 100)

    while guesses < 6:
        guess = get_guess()
        if check_guess(guess, number):
            return calc_winnings(guesses)
        guesses += 1

    print("You took too many guesses!")
    return -1 # They lost!

def play_again():
    again = input("Play again? (y/n) ")
    return again == "y"

def finished(winnings):
    print("Thank you for playing! Your total winnings were " + str(winnings) + " dollars!")

def game():
    title()
    instructions()
    winnings = play_round()
    if winnings == -1:
        break
    while play_again():
        new_winnings = play_round()
        if lost:
            break # Exit the round playing loop
        else:
            winnings += new_winnings
    finished(winnings)

game()
```

You can see how each section gets broken out into its own small piece, which
can be written and understood in isolation, rather than having to work on the
entire program at once. All the text to print out the title and instructions
banner have been isolated into their own sections. After that, the program
defines several functions for each isolated part of the game. The `get_guess`
function asks for a player's gues, and then returns it as an integer. Check
guess takes a target number and a guessed number, compares them, prints the
apropriate message, and returns `True` if the user guessed correctly, and
`False` if they did not. That value is used in `play_round`, which generates
a random number, and asks the user for a guess until they run out of guesses.
If it has returned true, the game will use `calc_winnings` to figure out how
much that game was worth. `game` coordinates all the pieces. First it prints
the banner lines. Then, it plays the first round. The game continues to play
rounds until the user, during `play_again`, asks not to. The game adds up all
the winnings after each round, and at the very end, prints the total the user
has won.

Pehw!
Take some time to practice with functions. Take your HiLo program with the
additional features you added, and try breaking it up into functions similar
to how we have here!

## Exercises

Revisit the [exercises in chapter
1](../../01_basic_types_and_control_flow/types/python.md). Instead of writing
them out by hand, write a function (or functions) for each one, and use them
to calculate the answers to the following problems. To get you started,
here's a function to calculate the cost of a square rug:

```python
def square_rug(width, fringe):
    area = width * width
    perimeter = fringe * 4
    cost = area * 5 + fringe * 1.5
    return cost
```

(TODO add a bunch more example values for the exercises from ch 1 types)

When you're feeling more comfortable writing and calling functions, head on to
[date and time functions](./01_dates/README.md)
