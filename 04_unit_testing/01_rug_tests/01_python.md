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

## Exercises

*   Write tests for the other rugs types you have.
*   Write tests for recipe ingredient scaling.
