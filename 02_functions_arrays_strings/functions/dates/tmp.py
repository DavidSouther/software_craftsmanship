import colors
from datetime import datetime
from time import sleep

def print_clock(when):
    clock_face = when.strftime("%a, %B %d of the year %Y at %I:%M:%S%p")
    print(colors.at(5, 5) + clock_face)

def tick():
    while True:
        sleep(0.2)
        when = datetime.now()
        print_clock(when)

print(colors.CLS)
tick()