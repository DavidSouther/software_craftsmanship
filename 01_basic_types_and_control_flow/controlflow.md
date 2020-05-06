## Control Flow

In the last section, we talked about primitive data. The basic pieces of
information computers work with, characters or numbers, that can combine in
some interesting ways. It is sometimes described as the "space" dimension of
your programs. In this section, we're going to talk about control flow, which is
the "time" aspect, and how programs gain their power to compute any new piece of
data, given some rules.

In broad strokes, programs will follow one sequence of operations - the sequence
written in the source code. Control flow changes that in one of two ways: either
it jumps forward somewhere else in the program based on some condition on the
data, or it jumps back to repeat a section of code a certain number of times.
These are called branches and loops, respectively.

Each branch or loop is made up of many small pieces, which we want to describe.

### Blocks

A block of code is a logical collection of code, separated from the rest of the
program by some syntactic construct in the programming language. In the
"c-based" languages (languages which got their syntax from C, including C++,
Java, and Javascript), blocks are grouped withing '{' and '}'. In Python,
Coffeescript, Ruby, and some others, blocks are grouped together by indenting
lines of code at the same level. Within a block of code, each piece is executed
in order, until it reaches a branch or a loop, in which case the program moves
to executing that block.

Blocks themselves can be broken down further, with slightly more precise
semantics than speaking of lines of code as a whole.

#### Expression

An expression takes some data and perforom an operation. Adding two numbers is
an expression. Checking if one number is greater than another number is an
expression. Calculating one of the roots of the quadratic equation is an
expression, but storing that result in a variable is not - that is a statement.

Different types of expressions have different precedence - for example, what do
you think would happen with the expression `2 + 3 < 1 * 7`? In the languages in
this book, the will all evaluate to `true`, because the arithmetic `+` and `*`
have priority over the relation `<`. We introduced operators in the first half
of the chapter, and here are a few more of the specific rules.

There are five common arithmetic operations - `+` addition, `-` subtraction,
`*` multiplication, `/` division, and `%` modulus. Addition and subtraction
behave as you would expect for both integers and floating point numbers. When
mixing and integer and a float, the result will be a float. Subtraction with
floats has some finicky details, explored in the basic types exercises.
Multiplication between integers results in an integer, but multiplying very
large numbers may have some side effects, which we explore in the exercises.
Modulus on integers returns the remainder, and between a float and an integer
behaves roughly as expected, but modulus between two floats is (for me) harder
to intuit. There are very, very few places in programming where the modulus of
two non-integers is necessary.

There are six relational operations that compare numbers - `==`, `!=`, `<`,
`<=`, `>`, and `>=`. They should be pretty obvious, but `==` is equality, the
numbers must be exactly the same, `!=` the numbers must not be the same, and the
number must be less than, less than or equal, greater than, or greater than or
equal to. Integers will always behave exactly as expected with the relational
operators, but `==` equality rarely works correctly with floating point numbers.
In calculations involving several steps of arithmetic in floating point numbers,
the least significant part of the numbers will start to drift slightly, thus
making them strictly not equal, while still being incredibly close. In those
situations, it is common to instead of testing equality, testing if the
difference of the numbers is less than some small error margin. More on this is
in the exercises.

When combining several calculations, grouping with `()` guarantees that some
steps will execute first. In the quadratic equation example, the
`(-b + discriminant) / (2 * c)` made it certain that the addition and
multiplication would be performed first. Without those, the implicit order from
the program would have been `- b + ((discriminant / 2) * c)`. It is always good
form to use parenthesis to group operations, even if the language itself would
order your operations correctly.

When working with multiple logical conditions, the three operations `!` not,
`&&` and, and `||` or are useful. The and operation works as expected - provided
the clauses on both sides are true, the entire expression is true. The or
operation does not behave as expected, in English. If I said I was going to make
eggs or bacon, then I brought you eggs and bacon, you would probably be happy
with getting an awesome breakfast, but still say my original statement was
incorrect. In English, or is an exclusive logic operation. Either one OR the
other condition should be true, but not both. In computers, or is an inclusive
operation. At least one of the conditions must be true, but if both are true,
the expression is still correct. The not operation is also a bit different. The
operations covered to this point take two clauses, one to the right and one
to the left. The not operation is 'unary', meaning it takes a single clause, to
the right of the `!` character.

The final operation, and one used in every program, is assignment `=`.
Assignment takes the computation on the right side and stores the value in the
variable on the left. This leads to calling the pieces the "lvalue" and the
"rvalue" - the rvalue can be nearly any expression, but the lvalue must be
something that can be assigned to. In C, that means a single variable. In Python
and Coffeescript, there are ways to assign to several variables at a single
time.

#### Statement

A statement is the smallest executable chunk of code. In C, making a statement
is as easy as adding a `;` to the end of an expression, delineating where one
expression ends and the next begins. Usually, statements group blocks of code.
An expression will run to check a condition of the program, and some number of
blocks of code are executed in some way. The complete collection of the
expression and the blocks are the statement. Of course, the blocks in the
statement are statements themselves. Branching and looping, discussed next, are
the best ways to see how statements combine to form a program.

### Branching

With the concept of a block of code being a logical chunk of code, combining
them in interesting ways gives programs their power. The most common piece of
control flow is the logical branch. A logical branch examines some condition of
the program's data, and runs one or another block of code depending on whether
that condition is true.

#### If-Then-Else

This basic branch is called "If/Else", and often the "If" is set off in programs
from the truthy block by the word "Then". Even if the "Then" is not in the
programming language, it's still discussed as such.

There was an example of an "If/Else" statement in the examples for the first
part of this chapter. In common English, the statement reads:

```
Check the expected result of the Transaction.
IF the result of the transaction is greater than the account balance
THEN warn the teller the transaction is too large
ELSE execute the banking transaction.
```

If/Else statements are very regularly used when interacting with users. The
program will ask the user for some input - "Would you like to run again? (Y/n)"
IF the user types "Y", THEN the program runs again, ELSE the program says "Bye!"
and exists.

Many business requirements can be expressed with If/Else logic - the transaction
example is common, but think about a security card scanner.

```
IF the scanned card has an employee ID
THEN
	IF the employee id is allowed in this building,
	THEN
		the door is unlocked for 10 seconds
	ELSE
		flash "Unauthorized Access" on the keypad
ELSE
	Do nothing (so the thief doesn't even know they can't get in)
```

Notice how the first IF clause has a second IF inside it. By nesting these
statements as deep as needed, any business rule that can be expressed in terms
of true/false is valid to write a program to manage. 

### Looping

Where branching runs a block of code based on some condition of the state of the
program, looping runs the same block of code multiple times. Looping comes,
broadly, in two flavors. When the number of iterations is known, the loop is a
*for* loop. When the number of iterations is based on some changing condition
of the program, the loop is a *while* loop. 

#### For Range

The most common looping construct repeats a block of code some discrete number
of times, usually changing the value of one or two variables each time the loop
repeats. Take the example of summing several numbers:

```
Let the variable "sum" be set to 0
FOR i taking values between 1 and 3, inclusive
	Set sum to be the current value of sum plus the value of i
Print sum
```

Implementing this program would print `6`. Going through it line by line, the
program would:

1. Set `sum` to 0
1. Set `i` to 1
1. Add the value of `i` (1) to `sum`, and store it - `sum` equals 1.
1. Set `i` to 2 (jumping back to the next iteration).
1. Add the value of `i` (2) to `sum`, and store it - `sum` equals 3.
1. Set `i` to 3 (the start of the next iteration).
1. Add `i` (3) to `sum` (3) - `sum` equals 6.
1. There are no more numbers to iterate over
1. Print `sum` (6)

This wouldn't be too hard to write the three additions by hand. When the
operation is taking the product of the numbers, or grows to summing hundreds of
numbers, loops become very attractive.

Finally, when we move to handling lists and groups of data in the next chapter,
the number of iterations is unknown when writing the program but is defined
when running the program. Loops are the only way to work on all those pieces of
data.

#### While

There are other times when a program needs to perform an operation many times,
but must make a decision every time it repeats. In the HiLo game example, the
loop repeats as often as the user continues entering "yes" when asked if they
want to play again.

## Comments

There is one last piece of a program we need to mention. Comments are text in
our programs that are not used by the computer, but purely for a programmer to
explain a particular piece of code. Comments have a checkered position in the
software development community. Because comments aren't part of the execution of
a program, they have a tendency to drift from the original implementation, after
programs have been in development for some time. Comments can also be useless -
in C, `x = x + 1; // Add one to x`. Even with their faults, a well-written and
well placed comment can be invaluable in aiding other programmers understanding
some code.

## Practice

Work with the `control flow` program in the language of your choice.

* [Python](control/python.md)
* ~~[CoffeeScript](control/coffee.md)~~
* ~~[C](control/c.md)~~
