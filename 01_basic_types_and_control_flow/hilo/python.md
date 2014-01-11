## HiLo

HiLo is a simple guessing game. The computer chooses a random number, and the
player is scored on how quickly they guess the number. In a new file, type this
program, then run it in your terminal!


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
  `print colors.BOLD + "HiLo" + colors.NORMAL`. Notice we have to tell the
  program to put the printing back to normal, or else all future priting would
  be in bold.

  1. **Colors** The colors module has a variety of styles, independent of
  eachother. The typography can be `BOLD`. Printing can be in `WHITE`, `BLACK`,
  `RED`, `BLUE`, `GREEN`, `YELLO`, `CYAN`, and `PURPLE`. The
  background color can be set with `BG_WHITE`, `BG_BLACK`, `BG_RED`, and so on.
  Play around with the colors, until you like the look and feel of your HiLo
  game. `NORMAL` puts the terminal back to a normal weight white text on black
  background.

  1. **Start Over** If you've gotten your terminal into a jumbled mess, print
  `colors.CLS` to clear the screen, and move the cursor to the top-left corner.

  1. **Print at various points** You can move the cursor (where the print
  happens) using `print color.at(r, c)` where r and c are the row and column you
  want to print at. Row and column start at the top-left of the terminal at `(1,
  1)`, and on "standard" terminals there are 80 columns and 24 rows. Note, if
  you resize the terminal, that will change. When writing this kind of terminal
  program, it's usually best to stick with those dimentions.

    * **Drawing Boxes** One use for this is to draw a box around some portion of
    the screen. This takes a bit of computing known as the "Extended ASCII
    Character Set". In the discussion of characters, we menionted that the first
    128 characters are mapped to various numbers in the ASCII character table.
    There are many other ways to map characters, and many other characters to
    map. One version from the 1980s was called "[Code Page 437][page437]", and
    was used by the original IBM PC computers and MS DOS.

    * In code page 437, the numbers from 128 through 255 were used for printing
    characters to make user interfaces, especially boxes, as an early form of
    windowing concepts. Today, with our preponderance of Graphical and web-based
    interfaces, these characters have largely fallen out of use, but you can
    still get access to them. In OSX, you will need to change your terminal to
    use the US-Latin (DOS) character set. Once you do, you could run a program
    like this in python:

```python
import colors

LEFT = 20

# Print the "Guess" box
print colors.BLUE
print colors.at(12, LEFT) + chr(201) + chr(205)*10 + chr(187)
print colors.at(13, LEFT) + chr(186) + " " * 10 + chr(186)
print colors.at(14, LEFT) + chr(200) + chr(205)*10 + chr(188)
print colors.WHITE

guess = 0
while guess >= 0:
  print colors.at(13, LEFT + 8) + "   " # Clear the last guess  
  guess = raw_input(colors.WHITE + colors.at(13, LEFT + 1) + "Guess: ")
```

* We use `colors.at` to control where the box will show up. We use `chr()`
to convert a number to a character at that code point. If you look at the
linked wikipedia page, you see that 186, 187, 188, 200, 201, and 201 are
double-wide block border characters. You can also see that instead of
printing 10 chr(205) characters to make the top and bottom portions, we
use the `*` operation, which for a character or string repeats the
character several times.

* Try using this in your program to make your interface more exciting!


1. ** Pauses / Animation ** The original Hi Lo program, at the top of the page,
doesn't stop between showing the instructions and asking for the first guess.
We could stop that with a simple way to ask the user for some input. Try putting
`n = raw_input("Press enter key to continue...")` in your program, and you'll
see that now the program waits for the user before continuing. In other places,
you might not want to wait for the user, but you do want a pause. Using the time
module, you can have your program wait a moment.

```python
import time

print("Hello, world!")
time.sleep(1.5)
print("A second and a half later...")
```

While a pregnant pause in the interface might be interesting, this becomes very
useful when putting animation in a program. Try the following HiLo intro scroll:

```python
import time

# An 8 frame animation
for i in range(1, 9):
    # Clear the screen
    print colors.CLS
    # Hi
    #   Lo
    # scrolls down the marquee
    print colors.at(i, 38), colors.GREEN, "Hi"
    print colors.at(i+1, 40), colors.RED, "Lo"
    # Half-second delay in each frame
    time.sleep(0.5)
```

1. **Difficulty** Give your program several difficulty levels. You could use
easy = 1 to 10, medium = 1 to 100, and hard = 1 to 1000. You could do a custom
difficulty. You may want to improve the scoring, so you don't get fewer points
when the random number happens to be smaller.

1. **Binary Search** You may have found the "optimal" algorithm is to begin by
choosing 50, then either 25 or 75 depending on if your guess is high or low.
This is a strategy called "Binary Search", because there is an either/or
decision to look to one side or the other of the numbers you're searching.
Rewrite the program so that instead of asking the user for a guess, the program
"plays" itself by guessing the number. See how long it takes it to guess any
particular number.

[page437]: http://en.wikipedia.org/wiki/Code_page_437#Interpretation_of_code_points_1.E2.80.9331_and_127
