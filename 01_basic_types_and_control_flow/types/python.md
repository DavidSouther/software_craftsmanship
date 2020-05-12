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

```python
print("Hello, world")
print('Hello, again')
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

```python
print(2, 3, 5, 7, 11)

print(0.5, 1.27, 3.141)

print('h', 'e', 'l', 'l', 'o')
```

Type them at the end of `types.py`, save the file, and run it in your terminal
again (leaving the terminal open so you don't have to navigate to the directory
every time would be a good idea ;).

You should see

```
Hello, world
Hello, again
2 3 5 7 11
0.5 1.27 3.141
h e l l o
```

Great! Are you having fun yet?

Let's go back and look very closely at what each of these is. On every line
you've typed to this point, you started with the command `print`. This is a
built in piece of Python that takes whatever comes after it and outputs that
value. The first two lines you typed, `print("Hello, world")` and `print('Hello,
world')`, are very similar. The only difference is that one uses the single
quotation mark, and the other uses the double quotation mark. Both the single
and double quotation marks wrap some text that you want to declare as a String.
Recall from the main text that a string is some arbitrary list of characters.
At this point, the single and double quotes are almost interchangeable. You
would use one when you want to include the other symbol in your string itself.
That said, you should choose a primary one to stick with - I encourage double
quotes for Python.

The second three lines each show off a different data type. `print(2 3 5 7 11)`
outputs several integers. Integers in Python store whole numbers only. The
folowing line, `print(0.5, 1.27, 3.141)`, outputs floating point numbers, or
numbers that can be fractional. Doing arithmetic with integers can only make
integers, which we'll see in a later block of code. The last line here creates
several one-character strings, or just characters. Python treats the two as the
same. Strings, Integers, and Floating Point Numbers make up the entirety of data
you will ever work with in a computer. From here, it's all about learning new
ways to combine them!

The next code block is a bit bigger. I would recommend only doing a section at a
time before running the program - the sooner you catch a mistake, the easier it
will be to correct!

```python
i = 2
j = 3
k = 5

print(i, j, k)

m = 2 * 3
n = 3 + 5

print(m, n)

x = 0.5
y = 1.27
pi = 3.141

print(x, y, pi)
```

When it's running, you should see

```
Hello, world
Hello, again
2 3 5 7 11
0.5 1.27 3.141
h e l l o
2 3 5
6 8
0.5 1.27 3.141
```

Working with numbers as they're typed in isn't very useful. In this block of
code, we create several variables. Variables are words in your program that
refer to a piece of data. That piece of data we call its value. The value a
variable has can change over the course of a program. We change the value of a
variable with the `=` sign. It's important to remember that when we use a single
equal sign in a program, it acts as a verb, "to make equal" - it makes the
variable on the left have the value of whatever is on the right for the rest of
the program. When a variable is anywhere else in the program, like in these
print lines, the program simply uses the value currently assigned to the
variable.

> A note on naming: variables can be as long as you want, but there are a few
rules. First, they can't have any spaces in them. Second, they can't start with
a digit (0-9). But they can have a digit in them, and you can also use `_`, an
underscore, to separate "words" in a long variable. In fact, Pythonistas are
encouraged to!

Moving a bit faster, for the biggest section yet:

```python
circumference_1 = pi * y
circumference_2 = pi * n

print(circumference_1, circumference_2)

average = (i + j + k) / 3
average_2 = (i + j + k) / 3.0

print(average, average_2)

a = 3
b = 8.6
c = 2.12

import math
discriminant = math.sqrt((b * b) - (4 * a * c))
denominator = 2 * a
x1 = (-b + discriminant) / denominator
x2 = (-b - discriminant) / denominator

print(x1, x2)
```

Remember, we're just adding these blocks to the end of the types.py file. When
it's correct, the output will be

```
Hello, world
Hello, again
2 3 5 7 11
0.5 1.27 3.141
h e l l o
2 3 5
6 8
0.5 1.27 3.141
3.98907 25.128
3 3.33333333333
-0.272395015515 -2.59427165115
```

Oh boy! That's a lot of math! Ok, let's break it down. First, there's not much
in these few lines except arithmetic - addition, subtraction, multiplication,
and division. The first four lines calculate two diffrent circumferences, using
the variables and values we typed above for `y`, `n`, and `pi`. The `=` sign
says "assign the value from the right to the variable on the left". The value
on the right, or "right hand side", is `pi * y` and `pi * n`. `pi` was assigned
`3.141` above, and `y` was assigned `1.27`, so this right hand side is `3.141 *
1.27`, which is equal to `3.98907`. That value, `3.98907`, is assigned to
`circumference_1`. The same thing happens for `circumference_2`, but with `n`.
`n` was assigned the value `3 + 5`, or `8`, which when multiplied by `3.141` is
`25.128`, the value stored in `circumference_2`.

Let's take a look at those two average lines. In both, we add `i`, `j`, and `k`.
From above, `i = 2`, `j = 3`, and `k = 5`. When those are all added together,
they equal `10`. The parenthesese are there to tell Python to do the addition
first, before the division. Here is where the two lines diverge. So far, `i`,
`j`, and `k` are all integers. `3` itself is also an integer. When we do
arithmetic with integers, we can only ever get an integer. So when we divide the
integer 10 by the integer 3, we get the closes integer - 3! In the second line,
we divide the integer 10 by the float 3.0. As soon as floats are involved, the
value of the arithmetic is ALWAYS a float! So we get the much more accurate
`3.33333333333`, which is not exactly correct but as precise as the computer can
calculate. (See the appendix on computer arithmetic if you want the gory, mathy
details!)

We've covered addition, multiplication, and division. Subtraction should be easy
to figure out. The next section does some math with a square root. Specifically,
the next few lines calculate the `x` values that the equation
`3x^2 + 8.6x + 2.12 = 0` is equal to `0`. This equation describes a parabola,
which is the mathematical name for the shape a projectile travels in - a thrown
basketball, or a cannon ball fired from artillery. (Some of the earliest
computers were created and used by the US Navy to calculate firing angles and
distances for battleships during World War II.) 

There are two values of `x` that the equation equals zero, and using the
[quadratic formula][quad_formula], we can find the two values. However, the
quadratic formula requires we take a square root of a number. There's no key for
square root, so instead Python provides a variety of utilities in the `math`
package. Similar to `print`, but we need to tell Python explicitly that we want
them. To do that, we type the line `import math`. The quadratic formula has two
intermediate calculations, which we perform with
`discriminant = math.sqrt((b * b) - (4 * a * c))` and `denominator = 2 * a`.
Multiplication has a higher priority than subraction, so in the discriminant it
will happen first, but we add parens to make it clear what the order is.

Finally, we use those two intermediate variable values to calculate the two `x`
values where `3x^2 + 8.6x + 2.12 = 0` holds true.

Whew! That's a lot of math! But the computer does it all, correctly, every time.
That alone should save your skin in a math class or two!

Let's skip ahead of math for awhile, and look at those strings again. We're
going to cover what, exactly, this notation means in the next chapter, but for
now practice the typing and think about what the output means the code is doing.

```python
a = "Hello, world"
b = 'Hello, world'
c = "This is" + " more text"

print(a, b, c)

print(len(a), len(b), len(c))
```

The output of the program at this point is

```
Hello, world
Hello, again
2 3 5 7 11
0.5 1.27 3.141
h e l l o
2 3 5
6 8
0.5 1.27 3.141
3.99542 25.168
3 3.33333333333
-0.272395015515 -2.59427165115
Hello, world Hello, world This is more text
12 12 17
```

The first two lines should make sense - a variable can have a value that is a
string, as well as an integer or float. The third line shows something new. We
can add strings together? Yes! Technically, the operation is called
"concatenation", but it uses the `+` character, and simply joins the two strings
into one single string, side by side. It doesn't add a space or anything, you
have to do that on your own. You can get the integer length, or number of
characters in a string, using the `len(string_variable)` command.

One last Monkey-see-monkey-do exercise, practicing typing full statements rather
than simple expressions:

```python
MIN_BALANCE = 25
current_balance = 30
transaction_amount = 10

if (current_balance - transaction_amount) < MIN_BALANCE:
	print("This transaction is too large.")
else:
	current_balance = current_balance - transaction_amount

print("Your current balance is: $" + str(current_balance))

for i in range(0, 10):
	print(i)
```

And the complete output from the first big program file is

```
Hello, world
Hello, again
2 3 5 7 11
0.5 1.27 3.141
h e l l o
2 3 5
6 8
0.5 1.27 3.141
3.99542 25.168
3 3.33333333333
-0.272395015515 -2.59427165115
Hello, world Hello, world This is more text
12 12 17
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

The last two lines give a way to do the same code many times with a single value
changing - in this case, printing the variable with the value 0, then 1, then 2,
and so forth.

Before that, we have a possible bank application. This bank requires that a
savings account must always have at least $25. When someone tries to do a
transaction, the program first checks if the account has enough money. If not,
it prints a warning to the user. Otherwise, it deducts the transaction amount
from the account. Either way, it always tells the user how much money is
remaining in the account. We'll cover these more in the next section.

## Exercises

You should do each of these exercises in their own files. They include a lot of
math. Don't let the math scare you! We're just using python as a calculator at
this point. Do each computation, store it in a variable, and then print that
variable out. The goal here is to practice typing python code and running python
problems. It is *not* a math course! Formulas for all the exercises are included.

Do as many or as few of the exercises as is interesting to you. This is a chance
to play around with a new hobby, and you might find some of these types of
calculations are interesting. But it's really not critical to understand all the
details - just do what's fun, and then go on to the control flow section!

1. **Pricing rugs** A company makes rugs, and has asked you to calculate the
    price for their rugs. They have square rugs (area = length ^ 2), rectangular
	rugs (area = length * width), and circular rugs (area = pi * radius ^ 2). Rugs
	are $5 per square foot of finished rug. Write a program that prints the cost of
	rugs for these sizes:
	1. Square, 1 foot on a side. ($5)
	1. Square, 2.5 feet on a side. ($31.25)
	1. Rectangular, 3 feet by 5 feet. ($75)
	1. Circular, 1.5 foot radius (3 feet across).  ($35.33645, using pi = 3.141)

1. **Advanced rugs** The rug company loves your code! They want you to add another
	feature! They now offer edges on their rugs. Edging costs $1/foot of
	edge. (The perimeter of a square is length * 4. A rectangle is length * 2 + width * 2. A circle's perimeter is Pi * radius * 2.) The same rugs, with edging, should be
	1. $9
	2. $41.25
	3. $91
	4. $44.77

1. **Harder Math**  You might recognize the math section in the middle of the
	program (where we use the 'discriminant' variable) as the quadratic equation - 
	a formula mathemeticians use to determine where a parabola has the value
	zero - and that physicists use to calculate where a basketball will land
	when thrown with a certain force.

	The full quadratic equation is

	```
	x1 = (-b + discriminant) / (2 * a)
	x2 = (-b - discriminant) / (2 * a)
	```

	the different being a + in the first and a - in the second.

	Solve the quadratic equation for:

	1. A = -2, B = 5, C = 3. [x1 = -0.5, x2 = 3](http://www.wolframalpha.com/input/?i=-2+*+x+%5E+2+%2B+5+*+x+%2B+3)
	1. A = 1.5, B = -6, C = 4.25. [x1 = 0.919877, x2 = 3.08012](http://www.wolframalpha.com/input/?i=1.5+*+x+%5E+2+-6+*+x+%2B+4.25)
	1. A = 1, B = 200, C = -0.000015. [x1 = 7.50000026528e-08, x2 = -200.000000075](http://www.wolframalpha.com/input/?i=x+%5E+2+%2B+200+x+-+0.000015) (x1 = 7.5*10^-8, x2 = -200)

	(Click the answer links to see the problem breakdown in Wolfram Alpha.)

	Notice in the last the result from Wolfram Alpha is different than the
	result we got in Python. Formally, the variation of the quadratic formula we
	use here is "numerically unstable" - when used on certain values, the
	solution we chose is not capable of giving the right answer. While this
	might not look like more than a peculiarity today, it is a serious issue in
	many branches of software engineering.

	Rerun the last calculation using the [following formula (7)](http://people.csail.mit.edu/bkph/articles/Quadratics.pdf):

	```
	basis = -b - discriminant
	x1 = basis / (2 * a)
	x2 = (2 * c) / basis
	```
	
	Notice how it is closer to the exact values provided by Wolfram Alpha, but
	still slightly incorrect.

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

	1. [Board-foot](https://en.wikipedia.org/wiki/Board_foot) Calculate the
		board-footage for several types of boards, including 
		
		* 350 feet of 2x4 (233.33333333333334)
		* 100 feet of 2x6 (100)
		* 20 sheets of 8 foot by 4 foot half-inch plywood (320)

	1. [Simplified Division Algorithm](https://en.wikipedia.org/wiki/Division_algorithm)
		When you divide two numbers, there are many ways to express the
		result. So far, we've been using the floating point format, with
		some number of decimals after the number. That leads to some odd
		answers, like with the board-foot calculation being 233.33333333333334.
		In ancient Greece, Euclid showed how to determine the "remainder"
		of a division - in this case, remainder 1 when dividing by 3.
		In Python, there is an operator called "modulus" which returns
		the remainder of dividing two numbers. It's typed as `%`, as in
		`3 % 2`, which would be `1`. Try putting `print(5 % 3)` in your
		python program, and see that it prints 2.

		Use the modulus operator to improve your board-foot calculations.
		Come up with new board-foot calculations that need remainders
		to be sensible.

	1. [Standard Deviation](https://en.wikipedia.org/wiki/Standard_deviation#Basic_examples)
		* Calculate the standard deviation for the sample data - `2, 4, 4, 4, 5, 7, 9 = 5`
		* Given the height of an adult male in inches, calculate which
			deviation he is in (mean = 70, deviation = 3). Try using
			the modulus operator.
			
			* `71 = 1/3`
			* `68 = - 2/3`
			* `78 = 2 2/3`

	1. [Projectile Distance](https://en.wikipedia.org/wiki/Range_of_a_projectile)
		One of the first applied uses of computing machines was in naval
		[artillery situations](https://en.wikipedia.org/wiki/Ship_gun_fire-control_system#Analogue_computed_fire_control).
		Write some code to calculate the range of a projectile fired at
		various velocities and angles (in [radians](https://en.wikipedia.org/wiki/Radian))
		from ground level. To calculate sine, use `math.sin(x)`. Assume
		velocity is in meters per second, so `g = 9.81` in the simplified
		formula on the wikipedia page.

		* `v = 100, theta = 0.1745; D = 348.581308308` (theta is ~10 degrees)
		* `v = 1000, theta = 0.1745; D = 34858.1308308`
		* `v = 250, theta = 0.6981; D = 6274.18922949` (theta is ~40 degrees)

Congratulations! You have a lot of experience typing Python programs! Getting
used to typing and running programs is a skill in itself, independant of the
actual programming you will do. This typeing programs is usually called coding,
seperate from actually figuring out what a program should do, which is the
programming.

Now that you can add and subtract, it's time to tackle [control flow](../controlflow.md)

[quad_formula]: http://en.wikipedia.org/wiki/Quadratic_formula
