## HiLo

HiLo is a simple guessing game. The computer chooses a random number, and the
player is scored on how quickly they guess the number.


```python
import random

print "HiLo"
print
print "This is the game of HiLo."
print
print "You will have 6 tries to guess the amount of money in the"
print "HiLo jackpot, which is between 1 and 100 dollars. If you"
print "guess the amount, you win $10 for every guess you don't take!"
print "Then you get another change to win more money. However,"
print "if you do not guess the amount, the game ends!"
print

winnings = 0
done = False

while not done:
    guesses = 0
    number = random.randint(1, 10)
    lost = False

    while not lost:
        guess = raw_input("Your guess: ")

        if guess == "":
            done = True
            break
        guess = int(guess)

        if guess == number:
            print "Got it! You won " + str(number) + " dollars!"
            winnings = winnings + ((6 - guesses) * 10)
            print "Your total winnings are " + str(winnings) + " dollars!"

            again = raw_input("Play again? (Y/n) ")
            if again != "Y":
                done = True
            break

        else:
            if guess > number:
                print "Your guess was too high!"
            else:
                print "Your guess was too low!"

        guesses = guesses + 1
        if guesses >= 6:
            print "You took too many guesses!"
            lost = done = True

        print

print "Goodbye!"
```

## Exercises

1. Assuming you copied the program exactly as presented, there is one bug that
should be obvious. Fix the program so it uses the correct range of random
numbers.

1. **Terminal Love** You may remember programs in the 80s that used terminal
characters for all their screen printing. Before computers were powerful enough
to regularly display modern images, programmers would use the extra characters
in the ASCII character set to create the precursers to windows, tables, columns,
and other graphical interface elements. There were also utilities available to
draw those characters in a variety (by which I mean all of eight) different
colors. In this series of exercises, we'll make HiLo look like those old games!

  1. **Bold** To start off, we'll include a library (like `random`) for changing
  the typography of pieces of the program. Download [this file](./colors.py)
  and save it next to your hilo program. Add `import colors` to your program.
  Edit the first line of the indroduction paragraph to make HiLo bold -
  `print colors.bold + "HiLo" + colors.normal`. Notice we have to tell the
  program to put the printing back to normal, or else all future priting would
  be in bold.

  1. **Colors** The colors module has a variety of styles, independent of
  eachother. The typography can be `bold`. Printing can be in `white`, `black`,
  `red`, `blue`, `green`, `yellow`, `cyan`, and [TODO LAST COLOR]. The
  background color can be set with `bg_white`, `bg_black`, `bg_red`, and so on.
  Play around with the colors, until you like the look and feel of your HiLo
  game. `normal` puts the terminal back to a normal weight white text on black
  background.

  1. **Print at various points** You can move the cursor (where the print
  happens) using `color.at(r, c)` where r and c are the row and column you want
  to print at. Row and column start at the top-left of the terminal at (1, 1),
  and on "standard" terminals there are 80 columns and 24 rows. Note, if you
  resize the terminal, that will change. When writing this kind of terminal
  program, it's usually best to stick with those dimentions.

1. **Binary Search** You may have found the "optimal" algorithm is to begin by
choosing 50, then either 25 or 75 depending on if your guess is high or low.
This is a strategy called "Binary Search", because there is an either/or
decision to look to one side or the other of the numbers you're searching.
Rewrite the program so that instead of asking the user for a guess, the program
"plays" itself by guessing the number. See how long it takes it to guess any
particular number.
