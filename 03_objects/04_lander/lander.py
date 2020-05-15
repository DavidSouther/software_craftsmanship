import colors

def pressEnter():
    return raw_input("Press Enter key to continue...")

def title():
    print colors.CLS
    print colors.at(8, 20) + "Lander!"

def instructions():
    print "This is a simulation of an Apollo Lunar"
    print "landing capsule.\n\n"
    print "The on-board computer has failed, so you"
    print "have to land the capsule manually.\n"
    print "Set the burn rate of the retro rockets"
    print "to any value between 0 (free fall) and 200"
    print "(maximum thrust) pounds per second. Set a new"
    print "burn rate every 10 seconds.\n"
    print "Capsule weight is 32,500 lbs; fuel weight 16,500 lbs"
    print "\n\n\nGood luck!\n\n\n"

fuel = 0


def play():
    print fuel


title()
pressEnter()
print colors.CLS
print colors.at(5, 1)
instructions()
pressEnter()
play()
