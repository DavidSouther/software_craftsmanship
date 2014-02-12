# Functions

Let's start with this program, that defines a function, a reusable block of
code, to draw a box on the terminal:

```python
import colors

print colors.CLS

def box(row, col, width, height):
    width = width - 2
    end = row + height-1
    print colors.at(row, col) + u'\u2554' + u'\u2550' * width + u'\u2557'
    for i in range(row+1, end):
        print colors.at(i, col) + u'\u2551' + " " * width + u'\u2551'
    print colors.at(end, col) + u'\u255A' + u'\u2550' * width + u'\u255D'

print colors.BLUE
box(12, 20, 10, 3)
print colors.NORMAL
guess = raw_input(colors.at(13, 21) + "Guess: ")
```

Type this program as `box_functions.py` and run it. If you make a new folder for
this chapter, make sure to save the [`colors.py`][colors.py] file in the same
folder. You should get the blue box from the HiLo program!

But now, what else can we get? Change the last four lines, and try this:

```python
print colors.BLUE
box(11, 19, 12, 5)
box(12, 20, 10, 3)
for i in range(4, 80, 4):
    box(2, i, 2, 2)
print colors.NORMAL
```

Lots of boxes!

The first box command draws a big box, staring at (11, 19), and then a smaller
box directly inside that. It then goes through the `for...range` loop, which
uses a verson of range we haven't seen before. This time, it starts with the
value 4, then increases by 4 until it is greater than or equal to 80. That is,
it takes the values `4`, `8`, `12`, `16`, `20`, `24`, `28`, `32`, `36`, `40`,
`44`, `48`, `52`, `56`, `60`, `64`, `68`, `72`, and `76`. At each of those
columns, it draws a little 2x2 box!

[https://raw2.github.com/DavidSouther/software_craftsmanship/master/01_basic_types_and_control_flow/hilo/colors.py]