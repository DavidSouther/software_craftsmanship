# Function Libraries

As you build up several functions which work on related things or otherwise
complement one another, it's common to bundle them together to provide more
widely than a single file or program. Functions bundled together in this way
are called a library. As you work through this chapter's workbook, and
through later chapters, you will build your own libraries of code to keep
solutions to earlier problems around. This means you won't need to write
the same code over and over, but will have your own grab bag of common tools.
At times, you'll also use libraries other developers have created.

All major programming languages have a set of functions provided "out of the
box" for common programming tasks. These provided functions are usually
called the "standard library" for a language. As you might guess from the
name, these are libraries of functions whose behavior and tasks are so
fundamental that it wouldn't make sense to have a language without them.
These usually include math calculations, string processing, date & time
utilities, and a variety of tools closely related to the running of programas.
We'll look at a few of these in later chapters, but right now let's take a
look at common date utilities, and how we might create functions for ourselves.

## Dates

Time is integral to our lives, and calendars are how we divvy time into
useful discrete chunks. In programming, we call a single moment in time a
Date. A Date includes its actual calendar day, like December 10th, 2020, as
well as a specific time, usually to one one-thousanth second accuracy (a
millisecond). We can also do things with dates, like find out what the next
date is (the date after 2019/02/18 is 2019/3/1, but the date after 2020/02/18
is 2019/02/19), or find out how many days apart two events are.

The Date Library in each of our programming languages handles these
calculations and logic for us, and exposes this with several functions. The
first function is to get a date. It can either be the date at this moment,
or it could be a date started at some specific time either specified with
several numbers for year, month, day, etc, or by giving it a string like
you'd use on an envelope. Once we have that date, we can use other functions
to get the specific year or hour it represents, or we can use functions to
tell us the number of days between two dates. We could even use a function
which takes one date, changed just the month, and returns that to us!

While dates tell us the time in human-readable format, there's also the concept
of "system time". This is the time the computer uses to verify its internal
clock. In many cases, this is as simple as a counter it keeps internally.
If your computer has a 1 gigahertz processor, that means its internal chip
performs 1 billion calculations per second. If it keeps a counter that goes
up by one every 1,000 calculations, then for every million times the counter
goes up, one second has passed.

This timing information can be used in a huge number of ways, but we used it
during animations in hilo to make the computer sleep for some period of time
before moving on to the next operation. This let us control the speed of
the program tied to what works for humans, rather than letting the program
run as fast as it can. Usually we want to just let the program run, but for
anything involving animation, we want to tie it to speeds for our user.

Let's head over to the workbooks to see all these examples in action!

[Python](./dates/python.md)

## Exercise: Dates

1.  Print the current date
    1.  Digital Clock Format
    1.  At least two lines
    1.  Some display styling
    1.  Updates every second
1.  Print number of days until:
    1.  Martin Luther King day
    1.  July 4th
    1.  Christmas
    1.  New Years
    1.  Your Birthday
