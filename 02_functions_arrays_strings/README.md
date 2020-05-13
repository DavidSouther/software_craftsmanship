# Functions, Arrays, and Strings

We write programs to manipulate our data. In the last chapter, we treated data
as integers, floats, and strings. We can iterate, or repeat, an operation on
data, and we can branch our programs, doing different things based on the value
of our variables. As programs get bigger, much of programming is managing
complexity, keeping different parts of the program small and logically
connected. This chapter covers three tools - functions, ways to block sections
of code together; arrays, to keep more than one piece of data in a variable, and
more details of strings, as they are useful in many ways in programming.

## Functions

In programming, functions allow us to "wrap up" a section of code and make it
reusable without needing to copy and paste it anywhere we want to use it. Like
mathematical functions, we can take an idea, write it out, give it a name, and
use it over and over any where we need. This allows us to break our program
into composable parts, and put those together like Legos or an erector set.

Functions are made up of four pieces. First, they need a name. Similar to
variables which store data, function names allow us to refer to this block of
code consistently and repeatedly. In fact, in some languages, function names
are variables! Second, a function needs a list of parameters. If you think
about a function we've already used, the square root function, you'll remember
it has a single variable passed to it - or one parameter that's either an int
or a float. Functions can have no parameters, one, two, or as many parameters
as is necessary. Generally, though, a function should be limited to a few
parameters before it just gets unweildy to use and manage.

Third, a function needs a body. This is the computer code that will be
executed when the function is run. It can create its own variables, it can
use the function parameters as variables, and in some languages it can use
data nearby the function. (This is covered in the TypeScript workbook.)
Finally, the function needs to produce a result. This is called returning a
value. Almost all functions will return a value, but there are some cases
where they work only on parameters, or only do something to cause a side
effect (like writing a line of text). We'll cover these as we come to them.

Once you have a function, you need to put them together in interesting ways.
This works exactly the same as with operators in chapter 1. There, we talked
about expressions, like adding 2 and 3 to get 5. While we did that with the
`+` operator, we could also make a function named add, which takes two
parameters, uses the + operator in its body, and then returns the result. You
can also use functions in control flow. Perhaps you want to perform a more
complex calculation when deciding which branch of an if then to take, or you
want to repeat a calculation several times with differing data in a for loop.

That was a lot of theory, so now might be a good time to head to the workbook
and do the first section in this chaper, getting practice with this intro to
functions.

* [Python](./functions/python.md)
* ~[TypeScript](./functions/typescript.md)~
* ~[C](./functions/c.md)~

### Function Libraries (#libraries)

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

#### Dates

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

Let's head over to the workbooks to see all these examples in action!

#### Exercise: Dates

1. Print the current date
  1. Digital Clock Format
  1. At least two lines
  1. Some display styling
  1. Updates every second
1. Print number of days until:
  1. Martin Luther King day
  1. July 4th
  1. Christmas
  1. New Years
  1. Their Birthday

## Arrays

* Arrays group lists of data
* range() actually creates arrays
* for foo in ... works with arrays
* access parts of arrays with slices
* manipulate arrays with list comprehensions

#### Exercise: Statistics

1. Using a given data set
1. Determine if second babies are born sooner
  * See Chapter 1 of Think Stats

## Strings

* Recap strings from ch 1
* String concatenation
* Converting to and from strings
* String interpolation (templates)
* Substrings
* String methods - find, count, upper, lower, (l|r)strip, replace

### Mad Libs
