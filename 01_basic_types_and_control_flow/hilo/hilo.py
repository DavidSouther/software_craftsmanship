import random

print "HiLo"
print
print "This is the game of HiLo."
print
print "You will have 6 tries to guess the amount of money in the"
print "HiLo jackpot, which is between 1 and 100 dollars. If you"
print "guess the amount, you win all the money in the jackpot!"
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
            winnings = winnings + number
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
