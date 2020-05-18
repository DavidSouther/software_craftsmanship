# Arrays in Python

In this section, we're going to do some math on sets of numbers. We're going
to write a couple functions to determine some statistics about these sets of
numbers. Just like chapter 1, the math is NOT the interesting bit here! Focus on
the code and the programming, and if you're interested, you can follow up on the
math on Wikipedia.

Let's start a new program, `arrays.py`

```python
data = range(2, 20, 3)
for i in data:
    print(i)
```

When we run this, we get 6 lines:

```
2
5
8
11
14
17
```
 
 `range` is a built in function that gives us an array of integers. The first
 integer in the array is `2`, the first number in the arguments. The array will
 grow up to (but not including) `20`, the second number. The last argument, `3`,
 tells the range how many to increment by each time. This argument is optional,
 and defaults to `1`. So if you just want a normal list of 20 numbers, you can
 do `range(0, 20)` to get the numbers 0 through 19, or `range(1, 21)` to get
 1 through 20. Because we set it to 3, we jump several at a time.

 This is the data we'll use to test the functions, and then we'll get a bigger
 data set to answer a real science question!

Add this code at the end of the file:

 ```python
 def sum(my_array):
    total = 0
    for val in my_array:
        total += val
    return total

data_sum = sum(data)
print(f"Data sums to {data_sum:.2f}")
```
 
 When we run it, we should see the output from above, and this line as well:

 ```
Data sums to 57.00
 ```

Here, we define a new function, `sum`. It takes one argument, `my_array`,
which will be the array of data to operate on. Sum, or summation, is just a
really fancy way of saying "Add up all the numbers". We do that by starting
the variable `total` with the value 0, and then we use a `for ... in ...`
loop to get every item. With a for loop, we name the variable in the first
area, and then provide the value to loop over as the second (before the `:`).
So this `for ... in ...` the array to loop over is `my_array` and the
variable for each time is `val`.

The body of the loop is one line - `total += val`. We saw `+=` in the rugs and
it's just a short way to say `total = total + val`.

The body of the loop will execute one time for every value in `my_array`. Each
time before the body executes, python will assign the next value in `my_array`
to the variable `val`.

After the loop body (because it's back to the first level of indendation), we
return the total. And that's it for the function!

Back at the file level, we run the function using the data we got above, and
the print it using a format string. This string uses `{data_sum:.2f}`, which
takes `data_sum`, treats it as a `f`loat, and provides 2 digits of precision.

Let's keep going with a function to calculate the average. The average, or mean,
of a set of numbers is found by adding all of them up and dividing by the total
number of items in the set. 

```py
def avg(my_array):
    total = sum(my_array)
    length = len(my_array)
    return total / length

data_avg = avg(data)
print(f"Data average is {data_avg:.2f}")
```

The new line of output should be

```
Data average is 9.50
```

This function starts the same way as sum, by giving it the name `avg` and taking
one parameter, my_array. But then, instead of adding up all the numbers itself,
it just uses the function we wrote in the last exercise. Then it uses the built
in function `len` to get the length of the array. Keep `len` in mind, as it's
the canonical way in python to get the size of any complex object - arrays or
otherwise! At the end, we print out the same way.

We have one last function, which is a lot more complex. The standard
deviation of a set of numbers describes their statistical distribution. If
the standard deviation is a larger number, it means there is more variability
in the sample. The numbers are more different to each other than similar. If
the standard deviation is smaller, the numbers are more clustered together.

> The formal definition of the standard deviation involves taking all the
numbers in the array, squaring the difference in the average of all values from
the single value, summing all those squares, dividing that sum by the number of
values in the data set, and finally taking a square root of the whole thing. Ask
your nearest stats professor for details, and trust the math part of the code
below :)


```py
import math
def std_dev(my_array):
    my_array_average = avg(my_array)

    diffs_squared = []
    for val in my_array:
        diff = val - my_array_average
        diff_squared = diff ** 2
        diffs_squared.append(diff_squared)

    sum_of_squares = sum(diffs_squared)
    length = len(my_array)
    return math.sqrt(sum_of_squares / length)

data_std_dev = std_dev(data)
print(f"Data std dev is {data_std_dev:.2f}")
```

When we run this, we find quite a wide standard deviation:

```
Data std dev is 5.12
```

Which makes sense. We don't have a lot of numbers, and they have a bit of space
between them. Let's get a real data set, and try to answer an
[old wive's tale](https://www.bbc.com/future/article/20171127-the-truth-about-three-childbirth-myths):
"First babies arrive late". We'll be using a dataset taken from the Unite States
Center for Disease Control's 2002 National Family Growth Survey (or US CDC 2002
NFGS) for short. This survey captures a myriad of details about tens of
thousands of pregnancies in the United States in the one year alone. From that
data set, I've create a small file you can download and save next to your
`arrays.py` program:
[`data.py`](https://raw.githubusercontent.com/DavidSouther/software_craftsmanship/master/02_functions_arrays_strings/03_arrays/data.py)

Once this file is saved, go back to `arrays.py` and add

```py
from data import PREGNANCIES

# Set up the lists to calculate sums on
preg_weeks_first_babies = []
preg_weeks_second_babies = []

for [order, weeks] in PREGNANCIES:
    if order > 2:
        # Only interested in second babies compared to first
        continue
    elif order == 2:
        preg_weeks_second_babies.append(length)
    elif order == 1:
        preg_weeks_first_babies.append(length)

avg_first_babies = avg(preg_weeks_first_babies)
avg_second_babies = avg(preg_weeks_second_babies)
std_dev_first_babies = std_dev(preg_weeks_first_babies)
std_dev_second_babies = std_dev(preg_weeks_second_babies)

print(f"First babies are born at an average of {avg_first_babies:.2f} weeks.")
print(f"First babies have a standard deviation of {std_dev_first_babies:.2f} weeks")
print(f"Second babies are born at an average of {avg_second_babies:.2f} weeks.")
print(f"Second babies have a standard deviation of {std_dev_second_babies:.2f} weeks")
```

Let's find out if the old wive's tale holds up to statistical scrutiny

```
First babies are born at an average of 38.58 weeks.
First babies have a standard deviation of 2.68 weeks
Second babies are born at an average of 38.64 weeks.
Second babies have a standard deviation of 2.72 weeks
```

The verdict is in - first and second babies have some difference on the order
of hours, certainly not the weeks claimed in the anecdote we're questioning.

Let's take a closer look at this code we have above. First, we get the data that
we are interested in by using `from data import PREGNANCIES`. We've see simple
import statements before, like `import math`. This let us use `math.sqrt`, but
also gave us access to `math.sin` and `math.atan2`. If we don't ever use the
trigonometry functions, why would we want to import all of them? The same thing
with this file- rather than importing the whole thing and asking for
`data.PREGNANCIES`, it's way easier to just import the single thing we want. So
we use this `from ... import ...` form and fill it in with the file or library,
and the individual value that we want from that file.

Now that we have our pregnancies, we're going to keep track of two arrays, one
for first babies and another for second babies. We saw with `range()` that we
could create an array with integers already filled in, but now we're going to
start with an empty array (just like we started with empty string). The empty
array is `[]`, which says "This is a big long list that we can add things to
later". Later we will add to it not by using `+` like with trings, but instead
by calling `append` which is a function the array has to add data to it.

With our data keeping set up, we start our for loop over the pregnancies array.
If you looked at the data file, you may have seen that it's actually a bunch of
arrays inside a big one. In python, we call a small fixed-length array (like
these ones, with two elements) a tuple. This is useful for exactly this case -
we want to keep pairs of data about each pregnancy in our list. The pieces of
data here are first, the order of the pregnancy (so whether this is the woman's
first or second or fifth pregnancy), and second, the number of weeks into the
pregnancy she gave birth.

When we loop over an array that has these small tuple arrays inside of them, we
can use a shorthand syntax to make two variables, instead of a single variable.
`for [order, length] in PREGNANCIES:` will go through each tuple in
`PREGNANCIES`, take the first number in that tuple, assign it to the variable
`order`, take the second value, assign it to the variable `length`, and then
with those variables perform the body of the loop.

The loop body is an `if ... elif ... elif` block. It looks at the order, and
decides which of the lists we're tracking it should append with the length of
the next pregnancy. If the order is great than 2, we will ignore it because we
are only interested in either a woman's first or second pregnancy. Then if the
order is two, we append the length to the array of numbers of weeks in a second
pregnancy. If the order is one, we put it in the other array.

After we've split the `PREGNANCIES` data set up this way, we exit the `for` loop
and pass our two arrays into our functions we had defined for `avg` and
`std_dev`. With these results back, we print them out for the user!

## Exercises

*   Using the `sum` function above, trace the execution of these programs:
    *   `print(sum([15, 15, 15, 14, 16]))`
    *   `print(sum([2, 7, 14, 22, 30]))`
*   Using the `avg` function above, trace the execution of these programs:
    *   `print(avg([15, 15, 15, 14, 16]))`
    *   `print(avg([2, 7, 14, 22, 30]))`
*   Using the `std_dev` function above, trace the execution of these programs:
    *   `print(([15, 15, 15, 14, 16]))`
    *   `print(std_dev([2, 7, 14, 22, 30]))`
*   In statistics, population *variance* is a part of the standard deviation.
    Specifically, it's the part of calculating a standard deviation that sums
    the squares of differences and divides by N, before taking the square root.
    In other words, the standard deviation is the square root of the variance of
    the array of data. Rewrite your `std_dev` function to perform the first
    part of the calculation, the `variance`, in its own function, and then use
    that function to calculate the standard deviation.

When you've completed the exercises, we can
[wrap up this chapter](../wrap_up.md).