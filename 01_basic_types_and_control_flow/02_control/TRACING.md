# Tracing Program Execution

At this point, we've run a few programs. We've gotten a bit of practice with
programs that can take user input, perform calculations on those inputs, and
then give the user some output based on the calculation. Whether this was rug
prices, checking account balances for a transaction, or converting to roman
numerals, the idea is the same for each.

As we learn to program, we find ourselves in this position of having a very
powerful piece of machinery that has very limited capabilities for anything
outside how it was built. It has no self-reflection, and no capability to reason
or intuit its own behavior. All of that is left to us, which means we need to
have a very good understanding of what specifically the computer will do with
all these instructions we give it.

The technique we use to determine these behaviors is called tracing. When we
**trace** a computer program, we take a piece of paper $ a pencil and, step by
step, record exactly what the computer would do if it were running the program.
To make a trace, we want to capture three columns of information. The first two
columns are side by side - "identifier" and "value". That should be familiar, as
those are the two parts of a variable! We are going to go through the program
line by line and track each identifier as we come across it, and the value it
has at any given time. There will be a third column, separate from the first
two, called "Input/Output". Whenever the program creates output or asks for
input, we'll record that in this column before copying it to the apropriate row
in the variables section.

## Tracing types

Let's see how this looks! Take this snippet from the python workbook:

```
i = 2
j = 3
k = 5

print(i, j, k)

m = i * j
n = j + k

print(m, n)
```

As we build a trace for this, we start with our paper looking like this:

```text
Id | Value       _Output_
---|------
   |
```

We then look at the first line of our program.

```
i = 2
```

We see an identifier, `i`. We look at our trace, and beccause we don't have an
ID yet for `i`, we add it:

```text
Id | Value       _Output_
---|------
 i |
```

We look on the right side of the `=` sign to find the value to assign to the 
variable, and see that it's `2`, so we add that to the value column:

```text
Id | Value       _Output_
---|------
 i |  2
```

That's the entirety of that line! We can now go to the next line:

```text
j = 3
```

We don't have an id `j` yet, so we add it and its value `3` to our trace:

```text
Id | Value       _Output_
---|------
 i |  2
 j |  3
```

That's the whole line, and we can do it one more time with `k = 5`:

```text
Id | Value       _Output_
---|------
 i |  2
 j |  3
 k |  5
```

The next line is a bit diferent, it's got the `print(i, j, k)` statement. For
this, we take what the computer will output and put it under the `Output`
column. What will it output? Well, it will print the variables `i`, `j`, and `k`
which we can look up in the table of IDs to values! We look at the table, and
read `2` for `i`, `3` for `j`, and `5` for `k`. Print will put those all on one
line of output:

```text
Id | Value       _Output_
---|------         2 3 5
 i |  2
 j |  3
 k |  5
```

Moving on to the next block, we have 

```py
m = i * j
n = j + k

print(m, n)
```

The first line is `m = i * j`. `m` is a new identifier, so we can add that to
our table:

```text
Id | Value       _Output_
---|------         2 3 5
 i |  2
 j |  3
 k |  5
 m | 
```

What value does it have? `i * j` is an operation that creates a value, not a
value itself. So to get the value, we need to perform the operation! To do
that, first we look at the identifiers `i` and `j`, and get their values from
the table: `2 * 3`. Multiplying `2` by `3` is `6`, and that's the value we
can put in `m`!

```text
Id | Value       _Output_
---|------         2 3 5
 i |  2
 j |  3
 k |  5
 m |  6
```

We can do the same process for the next line - note that we have a new variable
`n`, get the values `j` and `k` for the operation, add those values together,
and put the result in `n`:

```text
Id | Value       _Output_
---|------         2 3 5
 i |  2
 j |  3
 k |  5
 m |  6
 n |  8
```

And then we have a print statement again. Looking up the values, we have `6` and
`8`, which we can add to our next line of output in our trace:

```text
Id | Value       _Output_
---|------        2 3 5
 i |  2           6 8
 j |  3
 k |  5
 m |  6
 n |  8
```

While this might feel slow and tedious, that's a good thing at this point -
doing these traces will help you slow down and think through what the computer
is actually doing, which is rarely 100% in line with what you want it to do!

**Exercise**: finish tracing your `types` program in the language you're
using.

## Changing variables and control flow

We've seen how to track new variables in our program, and use identifiers to
find the value of a variable created elsewhere to use in an operation. We will
use this same approach to track changing values in a variable, looking at our
control flow program.

```python
sum = 0
for i in range(1, 6):
	print(i)
	sum = sum + i
print(sum)
```

We'll make a new trace for this program

```text
Id | Value       _Output_
---|------
   |
```

Starting at the first line, we see a new identifier, `sum`, which gets set to
`0` right away. (We call this immediate setting a variable to a value
**initialization**, so that when we access it later we know what value it
started with).

```text
 Id | Value       _Output_
----|------
sum |  0
```

On the next line, we see a `for ... in ...` loop. As discussed earlier, this
does create a new variable, in this case `i`, and will assign a new value to it
every time we come back through the loop. We cover `range(1, 6)` in depth in
the next chapter; for now, just know that it will give `1` and then `2` each
time we come to it again, up to `5` when it will be done.

```text
 Id | Value       _Output_
----|------
sum |  0
 i  |  1
```

Now, we go inside the loop. The first line inside the loop is `print(i)`. We
look for an identifier `i`, and read its value, `1`. We print this value, so put
it in the `Output` column.

```text
 Id | Value       _Output_
----|------          1
sum |  0
 i  |  1
```

The second line in the loop body is `sum = sum + i`. We see that we already have
an identifier for `sum`, so we don't need to make a new one. On the right side,
we see that we have a `+` for `sum` and `i`. This happens *before* the `=`, so
we look at the values in the identifiers `sum` and `i` _as they are right now_.
`sum` is `0` and `i` is `1`, so we add those together, getting `1`, and put that
in the `sum` value. But wait, sum already has a value? That's right. We're going
to change the value, and we do that in the trace by crossing out the old value
and putting the new value adjacent to it.

```text
 Id | Value       _Output_
----|------          1
sum | ~0~ 1
 i  |  1
```

If we read this now, we see that `sum` started at `0`, and then later became
`1`.

So we've finished both lines of the loop body, which means we go back to the
top, `for i in range(1, 6):`. We already have an `i`, so we don't need to make
a new one. We remember that last time `range` gave us `1`, so this time it will
give us `2`. We assign that to the variable `i` just like we did with `sum`, and
we end up with this trace:

```text
 id | value       _output_
----|------          1
sum | ~0~ 1
 i  | ~1~ 2
```

The first line of the loop is the print. We see that the current value (the one
furtherst to the right, that isn't striked out) is 2. Let's output that:

```text
 id | value       _output_
----|------          1
sum | ~0~ 1          2
 i  | ~1~ 2
```

We then have the `sum = sum + i` line again. We just saw that `i` is currently
`2`, and when we look at `sum` we see that it's `1`. Adding them together, we
store `3` back in `sum`.

```text
 id | value       _output_
----|------          1
sum | ~0 1~ 3        2
 i  | ~1~ 2
```

We go back to the top of the loop. This time, `range` will give us `3`.

```text
 id | value       _output_
----|------          1
sum | ~0 1~ 3        2
 i  | ~1 2~ 3
```

And when we've finished the loop body, we have this trace:

```text
 id | value       _output_
----|------          1
sum | ~0 1 3~ 6      2
 i  | ~1 2~ 3        3
```

Take a moment to check what the rest of the program will look like. Remember
that `range` will give numbers up to 5, and then will exit the loop the next
time it gets called.

When you've written this out, we should see this trace:

```text
 id | value           _output_
----|------              1
sum | ~0 1 3 6 10~ 15    2
 i  | ~1 2 3 4~ 5        3
                         4
                         5
```

And we're at the end of the loop. We come back to the top, `range` already gave
us 5, which is the last thing we used in the loop. `range` has nothing left, so
we exit the loop body. There's one more line - `print(sum)`, and looking at the
final value for `sum` we get 15!


```text
 id | value           _output_
----|------              1
sum | ~0 1 3 6 10~ 15    2
 i  | ~1 2 3 4~ 5        3
                         4
                         5
                         15
```

So we looped 5 times, with an increasing value of `i` for each. We printed out
that `i` each time to see where we were at in the loop, and kept adding it to
sum. After the loop was finished, we look back at `sum` one last time, and
output its value, `15`. Then, the program is done and ends!

## Tracing input

In the Roman Numerals program, we also have input. We can handle this one of
two ways, whichever is more comfortable for you, but either way basically has us
write another column for input. You can either write this separate from `output`
and have

```text
 input  | output
--------|---------
input 1 | output 1
input 2 | output 2
        | output 3
```

and they have their own columns, or you combine them and wrte them on opposite
sides of one column in order:

```text
  in / out  
------------
    output 1
input 1
    output 2
input 2
    output 3
```

It's up to you which way you want to do it.

So let's look at how to do this with the roman numerals program. We're using the
first version we typed, not the later version that you filled in with all the
remaining types

```python
print("Decimal to Roman Numeral")
number = int(input("Decimal integer: "))

numeral = ""
while number > 0:
    if number >= 10:
        numeral = numeral + "X"
        number = number - 10
    elif number >= 5:
        numeral = numeral + "V"
        number = number - 5
    elif number == 4:
        numeral = numeral + "IV"
        number = 0
    else:
        numeral = numeral + "I"
        number = number - 1

print(numeral)
```

The first thing it does is print out `"Decimal to Roman Numeral"`, so put that
in the `_output` column of the trace.

```text
 ID    | Value         input | output
-------|------        -------|---------
                             | Decimal to Roman Numeral
```

To keep this from getting too long, we're going to skip the empty print which
just gives us an extra newline for prettier output. So the next line is
`number = int(input("Decimal integer: "))`. This is a new variable, so we need
to record that first:

```text
 ID    | Value         input | output
-------|------        -------|---------
number |                     | Decimal to Roman Numeral
```

Then we have the `input("Decimal integer: ")` part. This will do two things -
first, it will print output, and then, it will take whatever input we provide so
that we can use that as the value for `number`. To do this, first we'll record
the output

```text
 ID    | Value         input | output
-------|------        -------|---------
number |                     | Decimal to Roman Numeral
                             | Decimal integer:
```

And then, we'll decide what input we will give it, and record that in the
`input` column.  This value comes from the user, and isn't part of the program.
Therefore, we will choose `18` arbitrarily as what our users has put in.

```text
 ID    | Value         input | output
-------|------        -------|---------
number |                18   | Decimal to Roman Numeral
                             | Decimal integer:
```

Now we can finish the line of code - `number = int(input...)` means we can take
the value in the input column, and put it into the value for the `number`
identifier.

```text
 ID    | Value         input | output
-------|------        -------|---------
number |  18            18   | Decimal to Roman Numeral
                             | Decimal integer:
```

From here, we can continue tracing the code exactly like we did in the last
section. The next line starts `numeral = ""`, making a new identifier and
setting it to the empty string.

```text
 ID    | Value         input | output
-------|------        -------|---------
number |  18            18   | Decimal to Roman Numeral
numeral|  ""                 | Decimal integer:
```

In the `while number > 0:` decision, we look up `number`, see that it is
`18`, and do the loop body. In the loop body, the first statement is the
first if condition, `if number >= 10:`. In this `if` condition, we look up
`number` (again), see that it is (still) `18`, and then do the first body
ignoring the other `if` branches. The body sets `numeral` (`""`) to `numeral
+ "X"` (which with string concatenation becomes just `"X"`), and sets
`number` (`18`) to `number - 10` (`8`). When the body is done, we have this
trace:

```text
 ID    | Value         input | output
-------|------        -------|---------
number |  ~18~ 8        18   | Decimal to Roman Numeral
numeral|  ~""~ "X"           | Decimal integer:
```

The `while number > 0:` sees `number` is `8`, which is larger than zero, and
does the loop body. `if number >= 10:` is not true, though - `8` is less than
`10`, so this `if` condition does not apply and we do not execute its body!
Instead, it goes to the next `elif` and checks that condition, `number >= 5`.
It is, so at this point the `elif` block gets started. Notice, though, that
the computer did execute each `if` check individually. It did *not* just jump
straight to the block we wanted to.

So it has found the `elif` condition true, executes that block, and goes back
to the top.

```text
 ID    | Value             input | output
-------|------            -------|---------
number |  ~18 8~ 3          18   | Decimal to Roman Numeral
numeral|  ~"" "X"~ "XV"          | Decimal integer:
```

From the top again, `while number > 0:` finds `number` to be `3`. The first
if finds `3` to be less than `10`, so it doesn't do that body. The first elif
then gets a shot, and finds that `3` is less than `5` so again doesn't
execute it. The second `elif` is up, but `3` doesn't equal `4` so no dice.
The only thing left is the `else`, which means that the `else` body has to
execute. But it did still first try all of the other conditions! The
computer executes in order, it does not pick the _best_ option. It's up to
you to put the more specific cases first, and the more general cases later.

At the end of this round we have this trace:

```text
 ID    | Value                   input | output
-------|------                  -------|---------
number |  ~18 8 3~ 2              18   | Decimal to Roman Numeral
numeral|  ~"" "X" "XV"~ "XVI"          | Decimal integer:
```

It should be pretty easy for you to finish the rest of the trace. Take a minute
to do so.

```text
 ID    | Value                                  input | output
-------|------                                 -------|---------
number |  ~18 8 3 2 1~ 0                         18   | Decimal to Roman Numeral
numeral|  ~"" "X" "XV" "XVI" "XVII"~ "XVIII"          | Decimal integer:
                                                      | XVIII
```

With the `print` at the end of our program, this is our finished trace!

### Traces in the book

Through the rest of the book, we will use traces whenever we come across new and
interesting control flow & concepts. To keep the traces consistent and contained
we'll be formatting them like such:

```text
 ID    | Value                                 
-------|------                                 
number |  ~18 8 3 2 1~ 0                         
numeral|  ~"" "X" "XV" "XVI" "XVII"~ "XVIII"          
                                                      

  output / input
------------------
Decimal to Roman Numeral
Decimal integer:
                       18
XVIII
```

That is, the variables will be up at the top, and we will use one column of
combined output and input below. Output will be left justified, and input will
be right justified. When you make traces on your own, it doesn't matter where
these pieces go. Find a layout for your page that works for you!

## Exercises

You guessed it - trace your roman numerals project with several other inputs.

## Wrap Up

This is a pedagogical tool

## Project

Let's use these to write our first big program - a video game called
[HiLo](../03_hilo/README.md)