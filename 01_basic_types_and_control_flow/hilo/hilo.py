'''
HiLo

A BASIC-esque game

For Software Craftsmanship, by David Souther

This is the instructor's file. Use it for reference if you get stuck, but try
to do all the exercises on your own. Also, you can run this program to see a
completed example. For the exercises, see `python.md` in this directory.

To play this game, you'll want to set your terminal to a black background, and
use an ANSI character set (EG NOT UTF-8). On OSX Terminal, I use the Pro
profile and change the character encoding to Latin-US (DOS), in the Character
Encoding dropdown under the Advanced settings in Terminal Preferences.
'''

# A few imports. Math for pow, random for randint,
# colors for ANSII Terminal things, time to sleep.
import math
import random
import colors
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

# Reset the colors
print colors.NORMAL

# Print the instructions, one line at a time, after the last line of
# the intro scroll, aligned right.
print colors.BOLD
print "This is the game of HiLo"
print colors.NORMAL
print "You will have 6 tries to guess the amount of money in the"
print "HiLo jackpot. If you guess the right amount, you win all"
print "the money in jackpot. However, if you lose, you lose all"
print "your money!"

# Pause half a moment...
time.sleep(1.5)

# Will learn how to do full blown "any" key later.
n = raw_input("Press enter key to continue...")

# This constant sets the left edge of the program's text
LEFT = 20

# Clear the portion of the screen we care about - the lines below
# the HiLo title, 70 characters wide.
for i in range(11, LEFT):
    print colors.at(i, 1) + " " * 70 # Note * for 70 spaces

# Print the difficulty menu
print colors.at(11, LEFT) + "1. Between 1 and 10"
print colors.at(12, LEFT) + "2. Between 1 and 100"
print colors.at(13, LEFT) + "3. Between 1 and 1000"
difficulty = raw_input(colors.at(14, LEFT) + "Difficulty? ")
# Easter Egg: Insane Mode!
difficulty = int(math.pow(10, int(difficulty)))

# Erase the Difficulty menu
for i in range(11, 15):
    print colors.at(i, LEFT) + " " * 40

# Print the "Guess" box
print colors.BLUE
print colors.at(12, LEFT) + chr(201) + chr(205)*10 + chr(187)
print colors.at(13, LEFT) + chr(186) + " " * 10 + chr(186)
print colors.at(14, LEFT) + chr(200) + chr(205)*10 + chr(188)
print colors.WHITE

# The game itself. The shell of the code is from the lecture.
winnings = 0
done = False

while not done:
    guesses = 0
    number = random.randint(1, difficulty) # Using the selected difficulty
    lost = False

    while not lost:
        print colors.at(13, LEFT + 8) + "   " # Clear the last guess
        guess = raw_input(colors.WHITE + colors.at(13, LEFT + 1) + "Guess: ")

        # Shortcut to leave early, with the empty guess
        if guess == "":
            done = True
            break

        guess = int(guess)

        if guess == number:
            # The winning combination!
            winnings = winnings + number # Could redo for different scoring
            
            # Fill in the status lines, and now that they've won they'll see their winnings
            print colors.BOLD + colors.GREEN + colors.at(15, LEFT + 1) + "You won!" + " "*LEFT
            time.sleep(1)
            print colors.NORMAL + colors.WHITE + colors.at(16, LEFT + 1) + "Winnings: " + " "*LEFT
            print colors.GREEN + colors.at(16, 32) + "$" + str(winnings)

            
            again = raw_input(colors.NORMAL + colors.at(17, LEFT + 1) + "Play again? (Y/n) ")
            print colors.at(17, LEFT + 1) + " " * LEFT # Only resetting line 17, the input line. 16 stays.
            if again != "Y":
                done = True
            break

        else:
            # Fill in line 15 with the game feedback.
            if guess > number:
                print colors.PURPLE + colors.at(15, LEFT + 1) + "Your guess was too high!" + " "*LEFT
            else:
                print colors.PURPLE + colors.at(15, LEFT + 1) + "Your guess was too low!" + " "*LEFT

        guesses = guesses + 1
        if guesses >= 6:
            # OH NO! They lost!
            print colors.RED + colors.at(15, LEFT + 1) + "You took too many guesses!" + " "*LEFT
            lost = done = True


n = raw_input(colors.at(18, 1) + "Goodbye!")

print colors.NORMAL
