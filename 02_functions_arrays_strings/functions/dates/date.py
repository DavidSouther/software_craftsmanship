import colors
print colors.CLS
from datetime import datetime
import time

def month(date):
    if date.month == 1:
        return "January"
    elif date.month == 2:
        return "February"
    elif date.month == 3:
        return "March"
    elif date.month == 4:
        return "April"
    elif date.month == 5:
        return "May"
    elif date.month == 6:
        return "June"
    elif date.month == 7:
        return "July"
    elif date.month == 8:
        return "August"
    elif date.month == 9:
        return "September"
    elif date.month == 10:
        return "October"
    elif date.month == 11:
        return "November"
    elif date.month == 12:
        return "December"

def mark(date):
    if date.day % 10 == 1:
        if date.day == 11:
            return "th"
        else:
            return "st"
    if date.day % 10 == 2:
        return "nd"
    if date.day % 10 == 3:
        return "rd"
    return "th"

def formatDate(date):
    return month(date) + ' ' + str(date.day) + mark(date) + ', ' + str(date.year)

def box(row, col, width, height):
    width = width - 2 # Subtract 2 for the left and right sides
    end = row + height-1
    print colors.at(row, col) + u'\u2554' + u'\u2550'*width + u'\u2557'
    for i in range(row+1, end):
        print colors.at(i, col) + u'\u2551' + " "*width + u'\u2551'
    print colors.at(end, col) + u'\u255A' + u'\u2550'*width + u'\u255D'

def showDay(now):
    print colors.GREEN
    box(6, 10, 21, 3)
    print colors.BLUE
    print(colors.at(7, 11) + formatDate(now))

def showTime(now):
    print colors.GREEN
    box(9, 10, 4, 3)
    print colors.RED
    print(colors.at(10, 11) + str(now.hour % 12))

    print colors.GREEN
    box(9, 13, 4, 3)
    print colors.RED
    print(colors.at(10, 14) + str(now.minute))

    print colors.GREEN
    box(9, 16, 4, 3)
    print colors.RED
    print(colors.at(10, 17) + str(now.second))

    print colors.GREEN
    box(9, 19, 4, 3)
    print colors.RED

    meridian = "AM"
    if now.hour > 12:
        meridian = "PM"
    print(colors.at(10, 20) + meridian)

while True:
    now = datetime.now()
    showDay(now)
    showTime(now)
    print colors.NORMAL
    time.sleep(0.5)
