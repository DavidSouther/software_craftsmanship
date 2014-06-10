# Dates

In computer programming, handling dates can get complicated. Unlike numbers,
dates have dozens of rules controlling how a date is handled. From different
numbers of days in months, to leap years, to "11th" compared to "21st", dates
require much special handling from computer programmers.

In this section, we will create and use a variety of functions to ease working
with dates.

In Python, the basic date handling is in a module called datetime, but we only
need the 'date' portion.

```python
from datetime import date
```

This allows us to use `date` later in the program. It's similar to `math` from
chapter 1. For us, we want the utility `date.today()`, which gives us a "date"
thing, seperate from an integer, float, or string, that allows us to check the
month, day, and year.

Let's take a look at a function that returns the string for which month of the
year a date is. The `def` keyword starts starts *def*ining a section of code.
The parenthesese tell python it is a function, while `month` gives it a name.
Finally, `date` names a parameter for the function. Take careful notice that
this date inside the function is different than the date from the `import`
statement at the top of the program!

```python
def month(date):
    if date.month == 1:
        return "January"
    elif date.month == 2:
        return "February"
    # 10 more cases
```

The `month` function is pretty straight forward. For each of the 12 possible
months, it returns a string. The function doesn't validate anything about the
date, and just trust that the date passed is good and valid.

The next function, `mark`, returns the string part of an ordinal number, like
"1st", "2nd", "28th", based on the day of the function.

```python
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
```

The `mark` function, like `month`, takes one parameter `date`, and returns "th",
"st", or "rd".

We can finally use all these pieces to make a function to format a date.

```python
def formatDate(date):
    return month(date) + ' ' + str(date.day) + mark(date) + ', ' + str(date.year)
```

With these pieces in place, we can add a final bit of program that makes a new
date, and prints out something like "January 14th, 2014".

```python
now = date.today()
print(formatDate(now))
```

Besides date formatting, determining the number of days in a month is also a
non-intuitive problem. Take leap years alone. When the Earth orbits the Sun, it
completes one year in about 364.25 days. The extra quarter day adds up, and if
left unchecked, in a century we'd be celebrating Christmas in the middle of a
summer heat wave!

Write a function that returns True when a date is a leap year, or False
otherwise.

```python
def leapYear(date):
    if date.year % 4 == 0:
        if date.year % 100 == 0:
            if date.year % 400 = 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return True
```
