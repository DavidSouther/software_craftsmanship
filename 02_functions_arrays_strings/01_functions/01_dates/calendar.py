import colors
from datetime import datetime, timedelta

def isWeekend(date):
    # Monday is 0, Sunday is 6
    return date.weekday() > 4

HOLIDAYS = [
    datetime(2020, 1, 1), # New Year's Day
    datetime(2020, 1, 20), # MLK Jr
    datetime(2020, 2, 17), # George Washington's Birthday
    datetime(2020, 5, 25), # Memorial Day
    datetime(2020, 6, 3), # 4th of July Holiday
    datetime(2020, 9, 7), # Labor Day
    datetime(2020, 10, 12), # Columbus Day
    datetime(2020, 11, 11), # Veteran's Day
    datetime(2020, 11, 26), # Thanksgiving Day
    datetime(2020, 12, 25), # Christmas Day
]

def isHoliday(date):
    return datetime(date.year, date.month, date.day) in HOLIDAYS

def isWorkday(date):
    return not isWeekend(date) and not isHoliday(date)

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

now = datetime.now()
def printDay(date, row):
    print(colors.at(row, 2 + (4 * date.weekday())), end="")
    if date.day == now.day:
        print(colors.YELLOW, end="")
    elif isHoliday(date):
        print(colors.PURPLE, end="")
    elif isWeekend(date):
        print(colors.RED, end="")
    else:
        print(colors.WHITE, end="")
    print(date.day)

one_day = timedelta(1)
def printMonth(year, month, row):
    monthly = datetime(year, month, 1)
    while monthly.month == month:
        printDay(monthly, row)
        if monthly.weekday() == 6:
            row += 1
        monthly += one_day

def countWorkDays(until):
    count = datetime.now()
    days = 0
    work_days = 0
    while count < until:
        days += 1
        if isWorkday(count):
            work_days += 1
        count += one_day
    return (days, work_days)

def printCalendar():
    now = datetime.now()

    print(colors.CLEAR)
    print(colors.at(1, 5), now.month, ' ', now.year)
    print(colors.at(1, 1), 'Su  M   Tu  W   Th  F   Sa')
    printMonth(now.year, now.month, 3)

    (days, workdays) = countWorkDays(datetime(2020, 6, 20))
    print()
    print(" " * 4, colors.RED, days, colors.GREEN, ' days to summer.')
    print(" " * 4, colors.RED, workdays, colors.GREEN, ' work days to summer!')

    print(colors.NORMAL)

printCalendar()