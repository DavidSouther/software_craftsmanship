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
 
print(month(date.today))
```

Ok we can look up details on a 

## Time differences

Once you have a first date, it's probably useful to compare it with the first
date to find out how far apart they are. How many days until Christmas, or your
birthday? How many days has it been since Elon Musk first launched a car into
space? In Python, we answer these questions with a `timedelta`. We can make a
timedelta directly, with code like `five_days = timedelta(days=5)`, or we could
create one from two dates we have, like `delta = now - then`. Once we have a
timedelta, we can add it to other dates to find out which date is that far from
the first.

```python
from datetime import datetime

now = datetime.now()
christmas = datetime(now.year, 12, 25)
days_until_christmas = (christmas - now)
print(days_until_christmas)
```

When I ran it on May 13th, I got

```
224 days, 22:05:49.793276
```

224 days and some hours! Almost there!

We can also create a time delta specifically, which is what we're going to use
to make a calendar in our terminal.



## Exercise: Days Until... Clock

TODO keyboard polling to switch between clock modes.
