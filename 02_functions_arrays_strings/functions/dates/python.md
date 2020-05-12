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

Try this function out for several years!

| Year | Leap Year? |
|------|------------|
| 1988 | False |
| 1970 | False |
| 1999 | False |
| 1996 | True  |
| 2000 | True  |
| 1900 | False |
| 2016 | True  |
| 2015 | False |

## Clock

We're going to build a program together that displays a digital clock. We're
going to use dates & times, as well as using the `sleep` function introduced
in the HiLo exercises.

```python
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
```

Type this in to a new file, run it, and you should see a clock ticking in your
terminal! (To stop the program, because otherwise it will run indefinitely, hold
the control key and press "c" on your keyboard. This is commonly abbreviated as
ctrl-c or ^c, and is useful whenever your program gets stuck in a loop.)

OK what all did we just even type!?

The first three lines are importing libraries that we want to use. We're familiar
with `import colors`, but now we have a bit more _color_ to understand it. It must
be a library, because that's the point of imports. It's also a library in a file
in the same directory. This is common in Python, because each file is also a "module"
formally, or a library informally. Whenever you're writing a python file, you can
always use `import some_other_file` to get all the things that other file has defined!
This is a great way to keep your own code clean and organized.

The next two lines use a variant form of the import statement. `datetime` and `time` are
both default modules (libraries) provided by Python itself, so we don't need to copy them
in or anything like that. `datetime` provides a number of utilities to work with dates
and times (it has a very descriptive name), while `time` works more generally with
"machine-time". So datetime gives you and me a clock and a calendar, while `time` helps
the computer keep track of how many ticks it's been awake. `datetime` exports a single
variable, `datetime`, with all its pieces and functions attached to it. We'll cover this
in chapter 3! `time` just exposes its functions directly, so we only grab the one
function we want, `sleep`. It just makes Python wait however many seconds before starting
again.

So with the imports out of the way, our program defines two functions, `tick` and
`print_clock`. `print_clock` takes a datetime (the type that the library gives back, not
the library itself), and writes it to the terminal. The `datetime` value captures a
point in time, and inside the function we call it by the name `when`. One function it
has available is the `strftime` function - and hoo boy, what is that string we pass it!?

That's a "Format String". It is written using its own pseudo-language which Python
reads and interperets to convert the datetime `when` into the much more legible
`Tuesday, May 08 of the year 2020 at 10:37:15 AM`. It does this by putting special
meaning to each of those `%a`, `%B`, etc tokens inside the string. Each of those tokens
says "Take some part of the datetime, convert it to human readable, and store it here."
The first of those, `%a`, is "Weekday as locale’s full name" which means if your computer
is running in English, it prints "Monday" or "Thursday". If your computer were configured
to run in German, it would instead print "Montag" or "Donnerstag". `%B` is the month's
name, similarly translated.

The documentation for all these is [available online](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes).
Take a moment, open that page, and figure out what the rest of those symbols mean!

Now that we understand the strformat command, the rest of the program is straight
forward. The `tick` function uses a while loop which is always True to run forever.
It pauses a moment, then gets the current time with `datetime.now`. That is the datetime
it hands to the `print_clock` function. These two functions work together to make
this program! They get started in the main file itself, by first clearing the screen
and then starting the tick function going.