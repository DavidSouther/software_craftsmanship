import math
import random
import colors
import time

print colors.CLS, colors.NORMAL, colors.BOLD

for i in range(1, 9):
    print colors.CLS
    print colors.at(i, 38), colors.GREEN, "Hi"
    print colors.at(i+1, 40), colors.RED, "Lo"

    time.sleep(0.5)

print colors.NORMAL

print colors.BOLD
print "This is the game of HiLo"
print colors.NORMAL
print "You will have 6 tries to guess the amount of money in the"
print "HiLo jackpot. If you guess the right amount, you win all"
print "the money in jackpot. However, if you lose, you lose all"
print "your money!"

print

time.sleep(1.5)

n = raw_input("Press any key to continue...")

for i in range(11, 20):
    print colors.at(i, 1) + " " * 70

print colors.at(11, 20) + "1. Between 1 and 10"
print colors.at(12, 20) + "2. Between 1 and 100"
print colors.at(13, 20) + "3. Between 1 and 1000"
difficulty = raw_input(colors.at(14, 20) + "Difficulty? ")
difficulty = int(math.pow(10, int(difficulty)))

for i in range(11, 15):
    print colors.at(i, 20) + " " * 40

print colors.BLUE
print colors.at(12, 20) + chr(201) + chr(205)*10 + chr(187)
print colors.at(13, 20) + chr(186) + " " * 10 + chr(186)
print colors.at(14, 20) + chr(200) + chr(205)*10 + chr(188)
print colors.WHITE


winnings = 0
done = False

while not done:
    guesses = 0
    number = random.randint(1, difficulty)
    lost = False

    while not lost:
        print colors.at(13, 28) + "   "
        guess = raw_input(colors.WHITE + colors.at(13, 21) + "Guess: ")

        if guess == "":
            done = True
            break

        guess = int(guess)

        if guess == number:
            winnings = winnings + number
            print colors.BOLD + colors.GREEN + colors.at(15, 21) + "You won!" + " "*20
            time.sleep(1)
            print colors.NORMAL + colors.WHITE + colors.at(16, 21) + "Winnings: " + " "*20
            print colors.GREEN + colors.at(16, 32) + "$" + str(winnings)

            again = raw_input(colors.NORMAL + colors.at(17, 21) + "Play again? (Y/n) ")
            print colors.at(17, 21) + " " * 20
            if again != "Y":
                done = True
            break

        else:
            if guess > number:
                print colors.PURPLE + colors.at(15, 21) + "Your guess was too high!" + " "*20
            else:
                print colors.PURPLE + colors.at(15, 21) + "Your guess was too low!" + " "*20

        guesses = guesses + 1
        if guesses >= 6:
            print colors.RED + colors.at(15, 21) + "You took too many guesses!" + " "*20
            lost = done = True


n = raw_input(colors.at(18, 1) + "Goodbye!")

print colors.NORMAL
