# Types

This exercise will give you practice typing programs that use many different...
types! (Get it... typing... types?) In the example, there are many instances of
using variables that have integers, floating point numbers (floats), characters,
and strings. There are also some basic control flow statements at the end. If
you haven't read the second half of the chapter, type them in exactly as they're
written and think about what you expect the result of running them will be. If
you have read the second half of the chapter, well, do the same, but you'll have
a hint on what they are expected to do!

Looking back on the steps from the introduction "Hello, World!", start by
opening your text editor (probably gedit), and write these two lines of code:

```
print "Hello, world"
print 'Hello, again'
```

Save the file (in a new folder for this chapter) as "types.py". Open a command
prompt, cd to the new folder you created, and type `python types.py`. You should
see:

```
Hello, world
Hello, again
```

If you have trouble with these steps, go back to
[the first exercise](../../00_introduction/python) and follow the instructions
there, but for this program. When you have it running, do these next few lines:

```
print 2, 3, 5, 7, 11

print 0.5, 1.27, 3.146

print 'h', 'e', 'l', 'l', 'o'
```

Type them at the end of `types.py`, save the file, and run it in your terminal
again (leaving the terminal open so you don't have to navigate to the directory
every time would be a good idea ;).

You should see

```
Hello, world
Hello, again
2 3 5 7 11
0.5 1.27 3.146
h e l l o
```

Great! Are you having fun yet?

The next block is a bit bigger. I would recommend only doing a section at a time
before running the program - the sooner you catch a mistake, the easier it will
be to correct!

```
i = 2
j = 3
k = 5

print i, j, k

m = 2 * 3
n = 3 + 5

print m, n

x = 0.5
y = 1.27
pi = 3.146

print x, y, pi
```

When it's running, you should see

```
Hello, world
Hello, again
2 3 5 7 11
0.5 1.27 3.146
h e l l o
2 3 5
6 8
0.5 1.27 3.146
```

Moving a bit faster, for the biggest section yet:

```
circumference_1 = pi * y
circumference_2 = pi * n

print circumference_1, circumference_2

average = (i + j + k) / 3
average_2 = (i + j + k) / 3.0

print average, average_2

a = 3
b = 8.6
c = 2.12

import math
discriminant = math.sqrt(b * b - 4 * a * c)
denominator = 2 * a
x1 = (-b + discriminant) / denominator
x2 = (-b - discriminant) / denominator

print x1, x2
```

Remember, we're just adding these blocks to the end of the types.py file. When
it's correct, the output will be

```
Hello, world
Hello, again
2 3 5 7 11
0.5 1.27 3.146
h e l l o
2 3 5
6 8
0.5 1.27 3.146
3.99542 25.168
3 3.33333333333
-0.272395015515 -2.59427165115
```

Let's skip ahead of math for awhile, and look at those strings again. We're
going to cover what, exactly, this notation means in the next chapter, but for
now practice the typing and think about what the output means the code is doing.

```
a = "Hello, world"
b = 'Hello, world'
c = "This is" + " more text"

print a, b, c

print len(a), len(b), len(c)

print a[4:]
print b[-4:]
print c[2:9]
```

The output of the program at this point is

```
Hello, world
Hello, again
2 3 5 7 11
0.5 1.27 3.146
h e l l o
2 3 5
6 8
0.5 1.27 3.146
3.99542 25.168
3 3.33333333333
-0.272395015515 -2.59427165115
Hello, world Hello, world This is more text
12 12 17
o, world
orld
is is m
```

One last Monkey-see-monkey-do exercise, practicing typing full statements rather
than simple expressions:

```
MIN_BALANCE = 25
current_balance = 30
transaction_amount = 10

if( (current_balance - transaction_amount) < MIN_BALANCE):
	print "This transaction is too large."
else:
	current_balance -= transaction_amount

print "Your current balance is: $" + str(current_balance)

for i in range(0, 10):
	print i;
```

And the complete output from the first big program file is

```
Hello, world
Hello, again
2 3 5 7 11
0.5 1.27 3.146
h e l l o
2 3 5
6 8
0.5 1.27 3.146
3.99542 25.168
3 3.33333333333
-0.272395015515 -2.59427165115
Hello, world Hello, world This is more text
12 12 17
o, world
orld
is is m
This transaction is too large.
Your current balance is: $30
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

## Exercises

You should do each of these exercises in their own files.

1. **Pricing rugs** A company has hired you to develop their website, where they
	sell rugs. They have square rugs, rectangular rugs, and circular rugs. Rugs
	are $5 per square foot of finished rug. Write a program that prints the cost
	of rugs for these sizes:
	1. Square, 1 foot on a side. ($5)
	1. Square, 2.5 feet on a side. ($31.25)
	1. Rectangular, 3 feet by 5 feet. ($125)
	1. Circular, 1.5 foot radius (3 feet across).  ($35.34)

1. **Harder Math**  You might recognize the math section in the middle of the
	program (where we use the 'discriminant' variable) as the quadratic equation
	- a formula mathemeticians use to determine where a parabola has the value
	zero, and that physicists use to calculate where a baskbetball will land
	when thrown with a certain force.

	Solve the quadratic equation for:
	1. A = -2, B = 5, C = 3. [x1 = -0.5, x2 = 3](http://www.wolframalpha.com/input/?i=-2+*+x+%5E+2+%2B+5+*+x+%2B+3)
	1. A = 1.5, B = -6, C = 4.25. [x1 = 0.919877, x2 = 3.08012](http://www.wolframalpha.com/input/?i=1.5+*+x+%5E+2+-6+*+x+%2B+4.25)
	1. A = 1, B = 200, C = -0.000015. [x1 = 7.50000026528e-08, x2 = -200.000000075](http://www.wolframalpha.com/input/?i=x+%5E+2+%2B+200+x+-+0.000015) (x1 = 7.5*10^-8, x2 = -200)

	Notice in the last the result from Wolfram Alpha is different than the
	result we got in Python. Formally, the variation of the quadratic formula we
	use here is "numerically unstable" - when used on certain values, the
	solution we chose is not capable of giving the right answer. While this
	might not look like more than a peculiarity today, it is a serious issue in
	many branches of software engineering.

	Rerun the last calculation using the following formula:

	[TODO Numerically stable quadratic]

	In this exercise, the details of the math aren't particularly important. The
	important piece is recognizing there are situations where the first, obvious
	solution to a programming problem might have subtle errors. It's critical to
	always check your assumptions and work against some external source. For an
	interface, grab a friend to test it out. For an algorithm, verify the result
	against some other program that performs correctly (even if that means by
	hand). We will come back to this concept of using an external source to test
	your programs many times throughout the text.

	This exercise will also provide the basis for first example in the appendix
	on computer hardware - we will see exactly what happens to cause the
	computer to calculate the incorrect result from a technically "correct"
	formula.

1. **Your Own Maths** I promise, the only reason we're doing this much math is
	because we don't know how do to anything more interesting until the next
	chapter! We will start branching out! For now, though, the practice of
	typing various maths is excellent coding practice.

	In this exercise, choose one or more of these formulas and implement it,
	using several sets of numbers. For more practice, do more of these!

	1. [Board-foot](https://en.wikipedia.org/wiki/Board_foot)
	1. [Standard Deviation](https://en.wikipedia.org/wiki/Standard_deviation#Basic_examples)
	1. [Projectile Distance](https://en.wikipedia.org/wiki/Range_of_a_projectile)
	1. [Simplified Division Algorithm](https://en.wikipedia.org/wiki/Board_foot)