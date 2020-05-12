# Control

These exercises put the control flow concepts to use. They use the techniques
from part 1, types, extensively. Many control flow constructs derive their
operation from the types and operations within them, so having condidence from
the first half of the chapter is critical to success, really in the rest of your
programming career.

As in the first two groups of examples, start by opening a new file in gedit.
Type in these two lines.

```python
for i in range(0, 10):
    print(i)
```

Save the new file, as `control.py`

Run the file - `python3 control.py`

```
0
1
2
3
4
5
6
7
8
9
```

What happens here? This is a "for" loop, which runs the statement `print(i)` 10
times, each time with the variable `i` taking a different value. `print(i)`
itself is an expression, that becomes a statement when the start of the new line
tells python to end the expression. The `for i ... :` tells python what variable
to change within the block. The `range(0, 10)` tells python to use that range
for the values of `i`, starting at 0 and going up to, but not inclding, 10.
The block is everything after that line, _that is at the next indentation level_.
An indentation level is anything with the same number of spaces at the start of
the line. `for i in range(0, 10):` has no spaces. `    print(i)` has four spaces.
Indentatation level is very important in Python, and we will revist it several times.

## Summations

With that in mind, rewrite the file so it contains this.

```python
sum = 0
for i in range(1, 11):
	print(i)
	sum = sum + i
print(sum)
```

Save it, run it, and the results:

```
1
2
3
4
5
6
7
8
9
10
55
```

Take a moment, and think about what happened.

The program started with an additional declaration, setting `sum` to 0. There
is an additional line in the for statement, `sum = sum + i`. It is at the same
indentation level as `print(i)`, and so runs in the same segment of the program.
Finally, `print(sum)` is back at no indentation, so runs after the for statement
finishes.

Change this program again:

```python
sum = 0
N = input("Summing 1 to N: ")
for i in range(1, (N + 1)):
    sum = sum + i
print(sum)
```

Now when it runs, it will stop and ask you to input a number for N. Choosing 10
will print 55. What does choosing 100 print?

```
Summing 1 to N: 100
5050
```

The `input("Summing 1 to N: ")` is a python way to ask the user to enter a
number. Whatever the user types, up to the enter, is the result of the
expression. While what the user types is a string, python immediately makes
it an integer.

Now that we have a program that sums a few numbers, change it to ask the user to
choose between summing or making a product.

```python
add = raw_input("Sum or Product? (S/P): ")
if add == "S" or add == "s":
	sum = 0
	N = input("Summing 1 to N: ")
	for i in range(2, (N + 1)):
		sum = sum + i
	print(sum)
elif add == "P" or add == "p":
	prod = 1
	N = input("Product 1 to N: ")
	for i in range(1, (N + 1)):
		prod = prod * i
	print(prod)
else:
	print("Unsupported Operation")
```

As we go along, the programs get bigger! The sum program is still there, lines 3
through 7. They're repeated again, lines 9 through 13. The two parts of the
program are separated by an if clause, with three branches. The first `if` is
the same as from the text. The second, the `elif`, is a way to do a second check
in the program. The `else` handles any time the input isn't `s`, `S`, `p`, `P`.
Notice in the `if` conditions, the `or` checks for the two different possible
characters. Remember that upper case and lower case characters are different, so
checking for both is the polite thing for users.

There is one very important thing to note about the `if` statements - the use of
`==` or double equals. To this point, we've been using `=` to be assignment,
making a variable have some value. This `==` is a different operation entirely,
and is actually comparing two values. Be careful not to confuse them!

Use this program to compute the sum of 1 to 57, and the product of 1 to 100.
Python internally handles integers to arbitrary length, making it ideal for many
numerical programs. When the number is smaller than some internal integer size
(at minimum 32 bits, possibly 64 bits on modern computers), Python will use that
for speed. When a calculation needs more precision, it moves to a "long integer"
format that allows integers of any size. That said, it is still constrained by
things like its memory and processing power - you can't reasonably iterate over
more than about 2^16. (TODO check the exact numberings on this.)

## Roman Numerals

We're going to write a completely new program, so start a new file. Name it
`roman.py`, in the same folder as `control.py`. We are going to build this new
program up bit by bit, discussing each piece we add.

Start with these lines:

```python
print("Decimal to Roman Numeral")
print()
number = input("Decimal integer: ")
print()
print("Converting " + str(number) + " to Roman.")
```

This form will become fairly common - print some header content, ask the user
for input, tell the user about the input. There is the slight technicality of
going between string and number - the `int()` and `str()` parts of line 3 and
5. They will make more sense next chapter, but for now remember that the
number `15` and the word with the letters "15" are different in Python's mind.

Running it does what you'd expect:

```
Decimal to Roman Numeral

Decimal integer: 18

Converting 18 to Roman.
```

With the basics out of the way, let's start work on Roman numerals. The rules
for Roman Numerals involve making groups of five, starting with "I" characters.
A group of five "I"s is replaced with a "V". Two "V"s become an "X". Characters
are added from left to right. With this simplified Roman Numeral ruleset, add
this to the program:

```python
numeral = ""
while (number > 0):
	if (number >= 10):
		numeral = numeral + "X"
		number = number - 10
	elif (number >= 5):
		numeral = numeral + "V"
		number = number - 5
	else:
		numeral = numeral + "I"
		number = number - 1

print(numeral)
```

Running the program, again converting 18 should print out:

```
Decimal to Roman Numeral

Decimal integer: 18

Converting 18 to Roman.
XVIII
```

Huzzah! Of course, our program doesn't handle numbers larger than 49, and it
doesn't follow the rule that 4 should be "IV", instead of "IIII". Let's fix
the second one together. Edit the body of the algorithm (the while loop) to
have a new case for when number is 4:

```python
	elif (number == 4):
		numeral = numeral + "IV"
		number = 0
```

and run it, using 14:

```
Decimal to Roman Numeral

Decimal integer: 14

Converting 14 to Roman.
XIV
```

It's also a good idea, whenever changing a program, to run it using the old
values, to make sure it's still correct.

## Exercises

1.  **Roman Numerals** Finish the Roman Numeral program.
    1.  The full order of Roman numerals was:
        *   I - One
        *   V - Five
        *   X - Ten
        *   L - Fifty
        *   C - Hundred
        *   D - Five hundred
        *   M - One Thousand
    1. The used subractions were
        *   IV - Four
        *   IX - Nine
        *   XL - Forty
        *   XC - Ninety
        *   CD - Four Hundred
        *   CM - Nine Hundred
    1. Sample numbers
        1.  551 - DLI
        1.  707 - DCCVII
        1.  90 - DCCCXC
        1.  1800 - MDCCC

These control statements - `while`, `for`, and `if`, are the bread and butter of
making programs do interesting things. Many times, we want to do the same
calculations on slightly different numbers - `for` and `while`. Other times, we
need to do different things based on some condition. In programming, these are
called iteration and banching, respectively.

Let's use these to write our first big program - a video game called HiLo!

# [HiLo](../hilo/README.md)
