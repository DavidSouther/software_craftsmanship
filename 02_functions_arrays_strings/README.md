# Functions, Arrays, and Strings

We write programs to manipulate our data. In the last chapter, we treated
data as integers, floats, and strings. We can iterate, or repeat, an
operation on data. We can take different branches in our programs, doing
different things based on the value of our variables. As programs get bigger,
much of programming is managing complexity, keeping different parts of the
program small and logically connected. This chapter covers three tools -
functions, ways to block sections of code together; arrays, to keep more than
one piece of data in a variable; and more details of strings, as they are
useful in many ways in programming.

## Functions

In programming, functions allow us to "bundle up" a section of code and make it
reusable without needing to copy and paste it anywhere we want to use it. Like
mathematical functions, we can take an idea, write it out, give it a name, and
use it over and over any where we need. This allows us to break our program
into composable parts, and put those together like Legos or an erector set.

Functions are made up of four pieces - an **identifier**, a list of
**arguments**, the **body** of the function, and some **return** value. Let's
look at each of these!

First, they need a name. Similar to variables which store data, function
names allow us to refer to this block of code consistently and repeatedly. In
fact, in some languages, function names are variables! When defining a function,
choose an identifier which accurately but succintly describes what the function
will do or what it will compute. Where variables capture things we work on,
their identifiers generally use noun phrases. Functions do things, and so their
identifiers will often use verb phrases to convey the actions the function will
perform.

Second, a function needs a list of arguments. If you think about a function
we've already used, the square root function, you'll remember it has a single
variable passed to it - or one argument that's either an int or a float. An
argument is a variable within the function that gets its initial value from
whatever outside code calls (or executes or invokes) the function. Functions
can have no arguments, one, two, or as many parameters as is necessary.
Generally, though, a function should be limited to a few arguments before it
just gets unweildy to use and manage. Having no parameters to a function
often means it will do some action based on outside data. We'll use this in
our next program to get user input for the rugs program.

Third, a function needs a body. This is the computer code that will be
executed when the function is run. It can create its own variables, it can
use the function arguments as variables, and in some languages it can use
data nearby the function. (This is covered in the TypeScript workbook.) Just
like a body of a while loop or if statement, the function body will execute from
top to bottom when the function gets called. Unlike the body of a while loop or
if statement, the variables inside the function are in a new **scope**. A scope
is a way to say that there's a new grouping of variables, independant from other
groups or blocks. This means that two different functions can both have a
variable named `area`, which are completely unrelated to to one another!

Finally, most functions need to produce a result. This is called returning a
value. Almost all functions will return a value, but there are some cases
where they work only on arguments, or only do something to cause a side
effect (like writing a line of text). We'll cover these as we come to them. When
a function returns a result, the function takes whatever value is on the right
side of the return statement and provides it to wherever the function was called
from. The function then immediatly finishes, just like when using break inside a
loop! 

### Calling Functions

Once you have a function, you need to put them together in interesting ways.
This works exactly the same as with operators in chapter 1. There, we talked
about expressions, like adding 2 and 3 to get 5. While we did that with the
`+` operator, we could also make a function named add, which takes two
arguments, uses the + operator in its body, and then returns the result. You
can also use functions in control flow. Perhaps you want to perform a more
complex calculation when deciding which branch of an if then to take, or you
want to repeat a calculation several times with differing data in a for loop.

TODO expand

That was a lot of theory, so now might be a good time to head to the workbook
and do the first section in this chaper, getting practice with this intro to
functions.

* [Python](./01_functions/01_python.md)
* ~[TypeScript](./01_functions/02_typescript.md)~
* ~[C](./01_functions/03_c.md)~

