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
def title():
    # Perform HiLo animation

def instructions():
    # Print the HiLo instructions

def guess():
    guess = raw_input("Your guess: ")

def tooHi():
    print("Too Hi!")

def tooLo():
    print("Too Lo!")

def justRight():
    print("You win!")

def checkGuess():
    if guess > number:
        tooHi()
    elif guess < number:
        tooLo()
    else:
        justRight()

def play():
    while playing:
        getGuess()
        checkGuess()

title()
instructions()
play()
```

You can see how each section gets broken out into its own small piece, which can
be written and tested in isolation, rather than having to work on the entire
program at once.

