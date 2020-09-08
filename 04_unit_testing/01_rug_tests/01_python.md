# Python unittest

Like `datetime` for working with dates and times, Python includes a standard
library for writing unit tests. It's imaginitively called `unittest`. `unittest`
exports a few utilities, but the main feature is a base class `TestCase`. Each
test case we write will be a class that extends `TestCase`. These test case
classes will use methods for each test case they want to execute. We'll write a
test case class for each rug type, and within them write a test method for each
of the edge cases we want to cover.

We'll write our first test in just a moment, but we do need to do a tiny bit of
clean up and preparation. First, we want to write our test file in the same
folder as the `rugs.py` program from chapter 3. We can either create
`rugs_test.py` in the same folder as `rugs.py` lives now, or we can create a new
folder, copy `rugs.py` there, and then create `rugs_test.py`. Whichever way you
do it, we need to fix `rugs.py` a tiny little bit to make it work as a library.

Right now, `rugs.py` is a *script*, because it executes as a single file and
immediately runs commands to start taking user input. While we want this
behavior when we run the program, the unit test doesn't have user behavior. It
just wants the class definitions from the file. But if we `import` the file
right now, Python will find the class definitions, and then right away start
asking whether the user wants to price a rug.

What we're going to do is put the last two lines (the `while` loop) in a
function, and then add a couple lines of Python which will only execute that
function when we run the file directly, as opposed to when it gets included as a
library in another program.

```py
def price_rugs():
    while not input("Price another rug (Y/n): ").lower().startswith("n"):
        price_rug()

if __name__ == "__main__":
    price_rugs()
```

This last part, `if __name__ == "__main__":` takes advantage of a Python feature
that lets us know if the file we're in is the file that we ran specifically,
rather than a file which was included by another file. `__name__` is a special
variable in Python, and when it has the value `"__main__"`, we know that the
user wanted to run this file, rather than importing it.

Now we can write our first test case! Again, in `rugs_test.py`, add this code
and run it!

```py
import unittest
import rugs


class SquareRugTestCase(unittest.TestCase):
    def test_no_fringe(self):
        rug = rugs.SquareRug(5, False)

        area = rug.area()
        cost = rug.cost()

        self.assertEqual(area, 25)
        self.assertEqual(cost, 125)


if __name__ == "__main__":
    unittest.main()
```

When we run it, `unittest` has some great output for us:

```
.
----------------------------------------------------------------------
Ran 1 test in 1.236s

OK
```

This says that it took about a second to run one test, and all the tests pass!

The code to create the test starts by importing `unittest`, which we'll use to
coordinate and organize the tests, and `rugs`, which is the name of the file
which has our `Rug` classes. The test suite is `SquareRugTestCase`, which
extends the `unittest.TestCase` utilities. These are responsible for triggering
and gathering results, and reporting the final results at the end of the run.
`SquareRugtestCase` has no constructor (`__init__` method) because it doesn't
need to set up any contructors or do any initialization. 

The first test, `test_no_fringe`, makes a square rug. It uses the values `5` and
`False` for size and fringe. With the test set up, it moves on to evaluating the
calculations. It saves `area`, `perimeter`, and `cost` in local variables.
Finally, the assert uses the provided helper classes to check if the values are
what we expect. `self.assertEquals(cost, 125)` compares the two values, and if
they are not exactly equal, print and record the failing test.

To see a failing test, try changing one of the constants, and see what happens!
Here's an example of mine:

```
F
======================================================================
FAIL: test_no_fringe (__main__.SquareRugTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "01_rug_tests\rug_test.py", line 14, in test_no_fringe
    self.assertEqual(perimeter, 25)
AssertionError: 20 != 25

----------------------------------------------------------------------
Ran 1 tests in 0.004s
```

So I changed the perimeter check to be 25, which is not the correct value. I can
read this error message and see specifically the line that was at issue, and the
problems associated. In appendix 3, we look in depth at reading and using
exceptions to debug our programs.

Let's add another two tests!

```py
class SquareRugTestCase(unittest.TestCase):
    def test_square_rug_no_fringe(self):
        # ... the test from before

    def test_square_rug_fringe(self):
        rug = rugs.SquareRug(5, True)

        area = rug.area()
        perimeter = rug.perimeter()
        cost = rug.cost()

        self.assertEqual(area, 25)
        self.assertEqual(cost, 155)
    
    def test_square_rug_no_size(self):
        rug = rugs.SquareRug(0, False)

        area = rug.area()
        perimeter = rug.perimeter()
        cost = rug.cost()

        self.assertEqual(area, 0)
        self.assertEqual(perimeter, 0)
        self.assertEqual(cost, 0)
```

And running this, it says we have three tests, `OK`!

These tests probably don't seem like a lot, but they give us quite a bit of
easily verifiable information. While it looks like a long amount of code (and,
it is...) the code is clear and direct in what it's doing. There's no logic,
only direct calls and direct comparisons. While we've tried to be concise and
tight in our main program, being able to simply read the tests is a great boon.

## Writing your own tests

As you go to write your own unit tests, we need a way to take what we've done
for rugs and apply it generally. The first thing we want to do is create a test
file for every program file we create. In the rugs program, we had `rugs.py` and
put the test in `rugs_test.py`. This convention, of creating a second file and
adding `_test` to it, is a great way to organize your project. It is clear what
your program files are, and what the tests are.

The second thing to do is to make sure our program has no behavior when it's
first called. That is, Python can run the file and find all the functions and
classes and variables, but it won't execute any code right away. It needs to
wait until it's told explicitly to run in a test or another file. But many of
our programs do need to do something if we run them specifically! To achieve
this, at the end of our python files we check if we're running the "main" file
that was specified on the command line.

```
if __name__ == "__main__":
    # Run the program if it was called directly
```

Because we should be testing all our programs, any python file we write that does
more than declare classes and functions should end with this block of code.

Third, we can import the pieces of our program into our test. Because the test
file lives in the same folder as the program, we can just use the file name
(without the .py extension) in the `from` part of our import. There are two ways
we can import our implementation. Using the rugs example, we could use either
of these forms:

```
import rugs

squareRug = rugs.SquareRug()
rectRug = rugs.RectangularRug()
```

This form imports the file as an object, where the properties are all the
functions and classes at the top level of the `rugs.py` file. Alternatively,
you can import each item in isolation. This is useful if you only need one or
two items from the file.

```
from rugs import SquareRug
from rugs import RectangularRug

squareRug = SquareRug()
rectRug = RectangularRug()
```

We have used this form before when we only wanted one or two things out of a
much larger module, like when we did `from math import sqrt`. While we're doing
imports, we also want to import TestCase from the unittest module which Python
provides.

After importing the parts of our program we intend to test, we can fourthly start
creating TestCases. A TestCase does two things - it groups together tests for
related pieces of functionality, and it extends from the Python TestCase
base class to get a bunch of "magic" that will actually execute the tests when
you run the test file.

To get that magic, we need to create a class structured in a very specific
way. First, it must extend from unittest.TestCase. Second, it must have methods
whose name begins with `test`. Python looks at classes which extend TestCase
for any method that starts with `test`, and treats those as the specific tests
to run and, whether they pass or fail, will report them with that name.

We can look at the Rugs tests for an example:

```python
import unittest
import rugs

class RectangularRugsTest(TestCase):
    def test_rectangle_fringe(self):
        # The body of the test
```

When you create tests for your own projects, it's usually a good idea to have
one test file per program file, and one test case in the test file per class
or function in the program file. Each TestCase then has multiple tests methods
to verify each part of functionality that it has. A simple function might have
just a single test method, while a complex class could have dozens or hundreds!

Our fifth step in creating a test for our programs is writing out the details
of each possible way to run the function or class. You want to be writing a
test method for the common ways to use it, and you realy want to write a test
method for each of the uncommon ways! For instance, in the rugs, we tested both
with and without fringe. These are common cases. We also tested what happens
if a size is 0! This and other uncommon cases are **edge cases**, and because
they're dealing with things a bit wonky or out of the ordinary, we really want
to focus on them in our tests to make sure it behaves just as we thing it should.

Within our test methods, there's a common approach: set up, execute, assert.
It's easiest to look at these in backwards order. Assert is how we will verify
our program is behaving correctly. We know that if it does perform as specified,
our program will be in some certain state. As a very simple example, let's say
our program is adding two numbers: `a = b + c`. After the program has completed
this step, we expect the variable `a` to have a certain value. And to demonstrate
that, we will `assert` that it does. We do this with the `assert...` methods.
In rugs, this was `self.assertEqual(rug.cost, 50)`. For this example, it would be
`self.assertEqual(a, # The value of b + c #)`. 

> NOTE: We use the expected value of b + c, instead of calculating it inline!
By manually performing the expected calculation, you save yourself from
accidentally using a value that came from a bug in your code! And yes, most of
the time the computation is much more complex than addition!

`assertEqual` is the most common assertion you'll do, but others are available
if you check the Python documentation.

To assert something about a program state, we must have executed it before.
In the rugs test, that was calling the cost method and storing the result. In our
simple example here, it would just be the one line of code `a = b + c`. For
this to work, we need some values for `b` and `c`, and that's the set up part.
All in all, this test would look like so:

```
# Create a test case
class ArithmeticTests(unittest.TestCase):
  # Declare a test method
  def test_simple_addition(self):
    # Set up
    b = 5
    c = 3
    
    # Execute
    a = add(b, c)

    # Assert
    self.assertEqual(a, 8)
```
    
There you go! These are all the pieces of defining, creating, and implementing
a unit test for your program. The last piece is to run it. To do that, we're
going to tell unittest to run when the test class is executed directly:

```
if __name__ == "__main__":
  unittest.main()
```

Putting that at the end of your `_test.py` file will let you run it with python
on the command line, and it will either tell you all the unit tests passed, or
it will show you an error for exactly which one failed!

The whole example again:


```python
import unittest # Get the testing library

from my_arithmetic import add # Get the thing we wrote and will test

# Create a test case
class ArithmeticTests(unittest.TestCase):
  # Declare a test method
  def test_simple_addition(self):
    # Set up
    b = 5
    c = 3
    
    # Execute
    a = add(b, c)

    # Assert
    self.assertEqual(a, 8)
   
# Run the tests when we execute this file
if __name__ == "__main__":
  unittest.main()
```

## Exercises

*   Write tests for the other rugs types you have.
*   Write tests for recipe ingredient scaling.
