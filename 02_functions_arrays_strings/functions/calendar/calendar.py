from pyqb import COLORS, CLS, BOLD, NORMAL, at
from datetime import datetime, timedelta
from schooldays import month, isSchoolDay, isWeekend

print CLS

def printDay(date, week):
    print at(week, 1 + (4 * date.weekday())),
    if date.day == now.day:
        print COLORS.YELLOW,
    elif isWeekend(date):
        print COLORS.RED,
    elif not isSchoolDay(date):
        print COLORS.PURPLE,
    else:
        print COLORS.WHITE,
    print date.day

day = timedelta(1)
def printMonth(year, month, week):
    monthly = datetime(year, month, 1)
    while monthly.month == month:
        printDay(monthly, week)
        if monthly.weekday() == 6:
            week += 1
        monthly += day

def countSchoolDays(count):
    lastDay = datetime(2014, 6, 13)
    days = 0
    schooldays = 0
    while count < lastDay:
        days += 1
        if isSchoolDay(count):
            schooldays += 1
        count += day
    return (days, schooldays)

now = datetime.now()

print at(1, 5), month(now), ' ', now.year
print at(2, 1), ' Su  M   Tu  W   Th  F   Sa'
printMonth(now.year, now.month, 3)
(days, schooldays) = countSchoolDays(now)

print
print " " * 4, COLORS.RED, days, COLORS.GREEN, ' days to summer.'
print " " * 4, COLORS.RED, schooldays, COLORS.GREEN, ' school days to summer!'

print NORMAL
