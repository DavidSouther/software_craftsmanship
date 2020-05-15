import colors

print(colors.CLEAR)

def box(row, col, width, height):
    width = width - 2
    end = row + height - 1
    print(colors.at(row, col) + "\u2554" + "\u2550" * width + "\u2557")
    for i in range(row+1, end):
        print(colors.at(i, col) + "\u2551" + " " * width + "\u2551")
    print(colors.at(end, col) + "\u255A" + "\u2550" * width + "\u255D")

print(colors.BLUE)
box(12, 20, 10, 3)
print(colors.NORMAL)
guess = input(colors.at(13, 21) + "Guess: ")
```

Type this program as `box.py` and run it. If you make a new folder for
this chapter, make sure to save the [`colors.py`][colors.py] file in the same
folder. You should get a blue box!

There are a couple things to point out here. The first I want to call out is that
multiplying a string by a number will repeat the string that number of times. To
take advantage of this, we subtract 2 from our width (because we have one column
on either side for the vertical lines), and then print that many top box characters.

For the vertical repeats, we use a different loop than before: `for ... in ...`.
While the `while` loop repeated every time a condition was true, `for ... in ...`
is going to take a list of data and repeat the block once for every item in that
list. To be useful, it also saves that item in a variable for us! But the variable
does change every time through the loop. Here, we use the variable `i`, which is
a common variable to use for small loops over a range of numbers.

To get the list of numbers, we use `range(row + 1, row + height - 1)`. We want to
start with the next row after our first, and we want to continue until the last
row. Why is that `row + height - 1`, insted of `row + height - 2`? Because range
is "open" - that is, it returns the first item _up to but not including_ the last
item.

## Emoji  and special characters.

What's up with those `"\u2554"` bits? In chapter 1, we discussed the ASCII
character set, and briefly mentioned there were more than those 128 characters
in the Unicode character set. You're almost certainly familiar with a number of
unicode characters already - emoji! 😂, 🖤, and 😍 are all emoji, and are also
single unicode characters! If you have an emoji input on your keyboard (like the
touchbar on the Mac Pro), you could type them directly. If you don't have those
buttons, you can use the longer explicit number forms. In this case, we could
write those as `"\u1F602"`, `"\u2764"`, and `"\u1F60A"`. 

For the boxes, we're going to use a different set of unicode characters, the
"box drawings" characters. You can either type them using the `\uNNNN` unicode
notation, or copy and paste them from below. You can find many more box drawing
characters at https://www.compart.com/en/unicode/block/U+2500.

*   ═ \u2550
*   ║ \u2551
*   ╔ \u2554
*   ╗ \u2557
*   ╚ \u255A
*   ╝ \u255D
*   ╠ \u2560
*   ╣ \u2563
*   ╦ \u2566
*   ╩ \u2569

## Diagram of a function
Let's start with this program, that defines a function, a reusable block of
code, to draw a box in the terminal:

```python
import colors

print(colors.CLS)

def box(row, col, width, height):
    width = width - 2
    end = row + height - 1
    print(colors.at(row, col) + "\u2554" + "\u2550" * width + "\u2557")
    for i in range(row+1, end):
        print(colors.at(i, col) + "\u2551" + " " * width + "\u2551")
    print(colors.at(end, col) + "\u255A" + "\u2550" * width + "\u255D")

print(colors.BLUE)
box(12, 20, 10, 3)
print(colors.NORMAL)
guess = input(colors.at(13, 21) + "Guess: ")
```

Type this program as `box_functions.py` and run it. If you make a new folder for
this chapter, make sure to save the [`colors.py`][colors.py] file in the same
folder. You should get the blue box from the HiLo program!

There are a couple things to point out here, but the important one to remember is
that multiplying a string by a number will repeat the string that number of times.
To take advantage of this, we subtract 2 from our width (because we have one column
on either side for the vertical lines), and then print that many top box characters.

For the vertical repeats, we use a different loop than before: `for ... in ...`.
While the `while` loop repeated every time a condition was true, `for ... in ...`
is going to take a list of data and repeat the block once for every item in that
list. To be useful, it also saves that item in a variable for us! But the variable
does change every time through the loop. Here, we use the variable `i`, which is
a common variable to use for small loops over a range of numbers.

To get the list of numbers, we use `range(row + 1, row + height - 1)`. We want to
start with the next row after our first, and we want to continue until the last
row. Why is that `row + height - 1`, insted of `row + height - 2`? Because range
is "open" - that is, it returns the first item _up to but not including_ the last
item.

## Emoji  and special characters.

What's up with those `"\u2554"` bits? In chapter 1, we discussed the ASCII
character set, and briefly mentioned there were more than those 128 characters
in the Unicode character set. You're almost certainly familiar with a number of
unicode characters already - emoji! 😂, 🖤, and 😍 are all emoji, and are also
single unicode characters! If you have an emoji input on your keyboard (like the
touchbar on the Mac Pro), you could type them directly. If you don't have those
buttons, you can use the longer explicit number forms. In this case, we could
write those as `"\u1F602"`, `"\u2764"`, and `"\u1F60A"`. 

For the boxes, we're going to use a different set of unicode characters, the
"box drawings" characters. You can either type them using the `\uNNNN` unicode
notation, or copy and paste them from below. You can find many more box drawing
characters at https://www.compart.com/en/unicode/block/U+2500.

*   ═ \u2550
*   ║ \u2551
*   ╔ \u2554
*   ╗ \u2557
*   ╚ \u255A
*   ╝ \u255D
*   ╠ \u2560
*   ╣ \u2563
*   ╦ \u2566
*   ╩ \u2569

## Diagram of a function

Let's take a closer look at the anatomy of this function. Recall from the
textbook portion that a function needs three things: A name, its parameters (also
called arguments), and a body. In the box function, those look like this:

![diagram of a python function](./digraph_of_a_python_funciton.png)

In python, a function starts with the key word `def`. That's followed by its name,
in this case `box`. It then has four parameters, all inside the parenthises -
`(row, col, width, height)`. Finally, in python, the function declaration (the name
and argument list) ends with the `:` (colon). We've seen this in the chapter on control
flow as well, and it indicates that we're about to group a bunch of code at the
next indentation level.

To get an indentation level, we add a new line (press enter on our keyboard) and
indent one level. There are several ways to indent. One is to hit the tab key on
your keyboard. Another is to add some number of spaces - at least two, but four
and eight are also common. A third way is to let VSCode do it for you! You've
probably seen this already when working through the first chapter, that VSCode
would automatically add the indendation for you when you started a new line after
a `:` colon.

So, why does Python have so many ways to do indentation? Mostly it's historical
reasons. For our purposes, we're going to start with using 4 spaces for indentation,
because that's VSCode's default, and usually it'll handle it for us. The only rule
is to be consistent with the amount of indentation you use in your program.

## One function, many boxes

Now that we have a function that prints a box, what else can we get? Delete the
last four lines of file you started, and try this instead:

```python
print(colors.BLUE)
box(11, 19, 12, 5)
box(12, 20, 10, 3)
for i in range(4, 80, 4):
    box(2, i, 2, 2)
print(colors.NORMAL)
```

Lots of boxes!

The first box command draws a big box, staring at (11, 19), and then a smaller
box directly inside that. It then goes through the `for...range` loop, which
uses a verson of range we haven't seen before. This time, it starts with the
value 4, then increases by 4 until it is greater than or equal to 80. That is,
it takes the values `4`, `8`, `12`, `16`, `20`, `24`, `28`, `32`, `36`, `40`,
`44`, `48`, `52`, `56`, `60`, `64`, `68`, `72`, and `76`. At each of those
columns, it draws a little 2x2 box!

Functions are great for grouping chunks of code together that you'd have to
run many times, either by typing over and over or copy/pasting. Let's look at
the box function a bit closer.

It starts with the Python keyword `def` - short for "Define", and used here to
"define" a function. The next word, `box`, tells Python what to call your
function, and is the word you'll use to refer to the function in the future,
like variables elsewhere. The parenthesis mark the *arguments* to the function.
Arguments are variables, but variables that are only valid inside the function.
The function declaration ends with the `:`.

The definition of the function is everything happening below that line at the
next indentation level. Remember that in Python, whitespace is important. An
**indentation level** is all code which has the same amount of leading spaces -
in our case, four.
