import colors
from datetime import datetime, timedelta
from time import sleep

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

def isWeekend(date):
    # Monday is 0, Sunday is 6
    return date.weekday() > 4

def isHoliday(date):
    return datetime(date.year, date.month, date.day) in HOLIDAYS

def isWorkday(date):
    return not isWeekend(date) and not isHoliday(date)

def countWorkDays(until):
    count = datetime.now()
    days = 0
    work_days = 0
    while count < until:
        days += 1
        if isWorkday(count):
            work_days += 1
        count += one_day
    # A little trick to return two values instead of just one
    return (days, work_days)

def printCalendar():
    now = datetime.now()
    print(colors.CLEAR, colors.at(4, 1))
    print(" Su  M   Tu  W   Th  F   Sa")
    printMonth(now.year, now.month, row=6)

    (days, workdays) = countWorkDays(datetime(2020, 6, 20))
    print()
    print(f"    {colors.RED}{days} {colors.GREEN}days to summer!")
    print(f"    {colors.RED}{workdays} {colors.GREEN}workdays to summer!")
    print(colors.NORMAL, end="")

def printClock():
    now = datetime.now()

    print(colors.at(1, 1))

    hour = now.hour % 12
    minute = now.minute
    ampm = "am" if now.hour < 12 else "pm"
    clock_face = now.strftime(f" It is {hour}:{minute} o'clock in the {ampm} ")
    print(f"{clock_face:^27}")
    month_face = f"{now.day} {month(now)} {now.year}"
    print(f"{month_face:^27}")
    print()

printCalendar()
while True:
    printClock()
    sleep(0.5)

print(colors.NORMAL, colors.CLEAR)