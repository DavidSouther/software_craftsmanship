import colors
print colors.CLS
from datetime import date

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
    print colors.at(row, col) + chr(201) + chr(205)*width + chr(187)
    for i in range(row+1, end):
        print colors.at(i, col) + chr(186) + " "*width + chr(186)
    print colors.at(end, col) + chr(200) + chr(205)*width + chr(188)

print colors.BLUE
box(6, 10, 21, 3)
now = date.today()
print colors.PURPLE
print(colors.at(7, 11) + formatDate(now))
raw_input(colors.at(9, 10) + "Press Enter to continue...")
print colors.NORMAL
