#! /usr/bin/env python

print "HiLo"
print
print "This is the game of HiLo."
print
print "You will have 6 tries to guess the amount of money in the"
print "HiLo jackpot, which is between 1 and 100 dollars. If you"
print "guess the amount, you win all the money in the jackpot!"
print "Then you get another change to win more money. However,"
print "if you do not guess the amount, the game ends!"

R = 0
B = 0
Y = random.randint(1, 100)

print Y
