# Python Classes

In the last chapter, we wrote pairs of functions to calculate costs for rugs,
and to get user input. The function declarations started to get a bit unwieldy
and redundant.

```py
def square_rug_cost(size, fringe):
def compute_square_rug():
def rectangular_rug_cost(width, height, fringe):
def compute_rectangular_rug():
def circular_rug_cost(radius, fringe):
def compute_circular_rug():
```

The idea of classes will separating each of these concepts into distinct pieces.
We can use those pieces in similar and interchangeable ways, and really free
ourselves from needing to track a large number of smallpieces by instead
tracking a small number of big pieces. Those big pieces can just hang out, do
their thing, and let us focus on other areas of our program as it grows.

On the flip side, with object oriented programming and using classes, we do want
to put a bit more effor in up front, thinking through what our design will be,
before we get down to brass tacks. This up-front thinking will let us
potentially shave a lot of time and effort down the road, if it turns out we
later built the wrong thing!

Before we start our class, then, let's remind ourselves of what we're trying to
achieve. Looking back at our last chapter's rug functions, we have this

```python
def square_rug_cost(size, fringe):
    area = size ** 2
    cost = area * 5
    if (fringe):
        perimeter = size * 4
        cost = cost + perimeter * 1.5
    return cost
```

A square rug needs to track two pieces of data - whether it has fringe, and the
size of one edge. It then calculates the area, perimiter, and costs from those
pieces. Rectangular and circular look similar. Looking at this, we probably want
one class, `SquareRug`, which will take two properties, `size` and `has_fringe`.
It will have one method, `cost()`, which uses this same formula but gets the
data from its properties. Let's see what this looks like in Python. Type and run
the following code in a new file.

```py
class SquareRug():
    def __init__(self, size, has_fringe):
        self.size = size
        self.has_fringe = has_fringe
    
    def cost(self):
        area = self.size ** 2
        cost = area * 5
        if (self.has_fringe):
            perimeter = self.size * 4
            cost = cost + perimeter * 1.5
        return cost

square_rug_1 = SquareRug(5, False)
square_rug_2 = SquareRug(2.5, True)
square_rug_1_cost = square_rug_1.cost()
square_rug_2_cost = square_rug_2.cost()
print(f"Rug 1 costs ${square_rug_1_cost:.2f}")
print(f"Rug 2 costs ${square_rug_2_cost:.2f}")
```

Which gives the same output as the similar version of the functions program.

```
Rug 1 costs $125.00
Rug 2 costs $46.25
```

Let's go through this code and look at the new things we haven't used yet. First
we have `class SquareRug():`. Just like a variable or a function, a class has an
**identifier**, this one is `SquareRug`. Like variables and functions, the
identifiers within the scope they are declared in all have to be unique. Python
knows we're making a class, because we say so with `class`. Also like a function
the class has a body, which just like a function is demarked with `:` at the end
of the line and everything below it indented one more level. We'll cover the
pair of parens in the next section.

So we've told Python we want a class named `SquareRug`. We now need to tell it
what a square rug is all about. We do that in the body by defining two
functions. Because these functions are in a class body, we call them
**methods**. The first method is a special method, as you might tell by reading
its name. `__init__` is a special method name that Python will use as the
constructor for the class. A **constructor** is a special method that will be
called every time we build a new instance of a class, and it is responsible for
ensuring all the properties of the class are set up properly.

This `__init__` function is declared using `def`, just like all our other
functions, except at one level of indentation because it's part of a class. The
function then takes three arguments, `self, size, has_fringe`. `size` and
`has_fringe` make sense, because these are what we expect the class needs for
its data, but what is `self`?

In Python, every method has a necessary first argument which will refer to the
instance of the class that the method is invoked on. What that means is that
when you have an object, and you go to call one of its methods, python will
fill in the first argumemt with the value of the object. This must be marked
down explicitly inside the method, and while it's just a variable, by convention
we always name it `self`.

So in the constructor, named `__init__`, we have take three arguments. `self`
refers to the object we are setting up. `size` and `has_fringe` come from
whatever code asked for a new `SquareRug`. The body of the `__init__`
constructor takes the arguments, and just stores them as properties on `self`.

Just like we can read properties in the calendar program of datetime, so too can
we write to properties. We just use the variable name of the object, put a `.`,
put the identifier of the property, and use = to assign it like any other
variable we've used thus far.

The second method we have, `cost`, should look pretty familiar. The only change
is that instead of taking `size` and `fringe` directly, it instead takes `self`
and looks up `size` and `has_fringe` as properties on the instance.

Outside the class we have our little bit of test code. We create two square rugs
by using the class name as if it were a function, and passing all the arguments
*except* `self`, the first. Python handles filling in the first `self` argument
on the calling side; it only needs to be explicit inside the method. We create
two rugs passing `5, False` and `2.5, True` for the parameters. We call the
`cost` methods on each instance, and print out the final value.

We can do this again for the rectangle rug.

```py
class RectangularRug():
    def __init__(self, width, length, has_fringe):
        self.width = width 
        self.length = length 
        self.has_fringe = has_fringe
    
    def cost(self):
        area = self.width * self.length
        cost = area * 5
        if (self.has_fringe):
            perimeter = self.width * 2 + self.length * 2
            cost = cost + perimeter * 1.5
        return cost

rectangle_rug_1 = RectangularRug(4, 6, False)
rectangle_rug_2 = RectangularRug(2.5, 5, True)
rectangle_rug_1_cost = rectangle_rug_1.cost()
rectangle_rug_2_cost = rectangle_rug_2.cost()
print(f"Rug 1 costs ${rectangle_rug_1_cost:.2f}")
print(f"Rug 2 costs ${rectangle_rug_2_cost:.2f}")
```

With these test cases, we get

```
Rug 1 costs $120.00
Rug 2 costs $85.00
```

This should look and feel pretty similar. We define the new class, 
`RectangularRug`. Its constructor takes four arguments, instead of three. The
cost calculation is a little different. But otherwise, it's all still there!

Take a few minute to write the last rug class, `CircularRug`. Using `5, False`
and `2.5, True` you should again get

```
Rug 1 costs $392.70
Rug 2 costs $121.74
```

Let's remove all the testing code and take a look at how we might ask for user
input for each of these rugs. Naively, it'll be just like what we had in the
functions exercises - ask the user for which type of rug, then ask them all the
numbers for that type, and then finally create that rug and print its cost.

```python
def price_rug():
    print("1) Square Rug")
    print("2) Rectangular Rug")
    print("3) Circular Rug")
    rug_type = input("Which type of rug? ")
    if rug_type == "1":
        size = float(input("Size of rug: "))
        wants_fringe = input("Has fringe (y/n): "))
        rug = SquareRug(size, wants_fringe == 'y')
    # ... three other types
    
    rug_cost = rug.cost()
    print(f"The rug costs ${rug_cost:.2f}")

while input("Price another rug? (y/n) ").lower() == 'y':
    price_rug()
```

Right away we see that maybe this isn't the best approach. The whole point of
classes was to contain the information necessary to build a rug, but we have
this whole function which just asks all the information over again anyway! Let's
fix this by moving the code to get the various rug information to inside the
classes themselves. We'll still be able to creat a rug of a certain shape and
size, but now we'll have a second option to tell the rug to ask for input on
its own, simplifying the main loop of our program.

In the SquareRug class, we need to change the constructor to have default values
for its arguments, and we need to add a get_values method which asks for input
and stores it in the class' properties.

```py
class SquareRug():
    def __init__(self, size = 0, has_fringe = False):
        self.size = size
        self.has_fringe = has_fringe

    # The old cost function, it doesn't change

    def get_values(self):
        wants_fringe = input("Should this rug have fringe (y/N)? ")
        if wants_fringe.lower().startswith('y'):
            self.has_fringe = True
        self.size = float(input("Side length of this square rug? "))
```

And do the same thing for the other two classes. Now we can rewrite the control
loop, delegating to this new get_values function!

```python
def get_rug():
    print("1) Square Rug")
    print("2) Rectangular Rug")
    print("3) Circular Rug")
    rug_type = input("Which type of rug? ")
    if rug_type == "1":
        rug = SquareRug()
    elif rug_type == "2":
        rug = RectangularRug()
    elif rug_type == "3":
        rug = CircularRug()

    return rug

def print_rug(rug)
    price = rug.cost()
    if rug.has_fringe:
        with_fringe = "with"
    else:
        with_fringe = "without"
    print(f"This rug costs ${price:.2f} {with_fringe} fringe.")
    
while input("Price another rug? (y/n) ").lowercase() == 'y':
    rug = get_rug()
    # Ask for inputs
    rug.get_values()

    print_rug(rug)
```

Now the `get_rug` function only needs to know about the types of rugs we have in
the program, and chooses one of them. It has the rug itself ask the user for
the values, and then returns the created & filled in rug. The control loop sends
that rug to this new `print_rug` function, to get nice formatting. Now, we have
a clean, clear, logical separation of concerns for our rug types!

## Inheritance

You may have noticed some duplication starting to crop up across these classes.
Each class has almost the same implementation of the `cost` method, and each
one has to duplicate `get_values` asking for whether the rug has fringe.

As you might have guessed, we have tools to handle this type of complexity! When
several classes need to share the same functionality, we can introduce a
**base class** to handle the shared pieces, and then each of the classes we
have becomes a **derived class** which fills in just the pieces it cares about.

This sounds a little more complicated than it is, so let's walk through what we
will do to get this separation before we look at it in practice. What we're
going to do is create a new class, `Rug`. `Rug` will do all the things our other
rugs can do, but it's not going to have any logic that's specific to a rug
shape. It will have a constructor, which will only take whether it has a frince
(which applies to all rugs). It will have a method that calculates cost, and one
that asks for `get_values` that asks whether the user wants fringe. But instead
of doing the calculation for an area and a perimeter, it will instead have a new
pair of methods `area` and `perimeter` to extract those calculations out. All
together, our base `Rug` class looks like this:

```py
class Rug():
    def __init__(self, has_fringe = False):
        self.has_fringe = has_fringe 
    
    def get_values(self):
        wants_fringe = input("Should this rug have fringe (y/N)? ")
        if wants_fringe.lower().startswith('y'):
            self.has_fringe = True

    def area(self):
        return 0
    
    def perimeter(self):
        return 0

    def cost(self):
        area_cost = self.area() * 5
        if self.has_fringe:
            perimeter_cost = self.perimeter() * 1.5
        else:
            perimeter_cost = 0
        total_cost = area_cost + perimeter_cost
        return total_cost
```

We can't really run this yet, because any time we create a `Rug` its cost will
always come out as `0`. Instead, we need to tell Python that `SquareRug` and the
rest want to **derive** or **inherit** from this class' definition. What that
means is that any class we have derived will have access to these functions and
behaviors, but more importantly, it is able to replace the definitions as
needed! It also can use all the properties the parent class (the one it derives
from) has, as well as being able to declare new properties specific to it.

In practice, this means that our `SquareRug` class will need to add properties
for its size, and provide new definitions for the `area` and `perimeter`
methods. I'll give the example of `SquareRug`, and you can do the same for
`RectangularRug` and `CircularRug`.

```py
class SquareRug(Rug):
    def __init__(self, size = 0, has_fringe = False):
        self.has_fringe = has_fringe
        self.size = size 
    
    def get_values(self):
        self.side_length = float(input("Side length of this square rug? "))

    def area(self):
        return self.side_length ** 2

    def perimeter(self):
        return self.side_length * 4
```

Here, we still have our class identifier, but we added the `Rug` parent class to
the inside of the first parenthesis. This is what tells python this is a derived
class. The `get_values` method asks for the side of the rug, and the `area` and
`perimeter` methods do just the specific calculations for the square.

But wait, this is missing something - how will it get whether the user wants
fringe? Because we replaced the `get_values` method, this new version will get
called which will only ask for the side length of the rug! What we want in this
case is to call a **super** method. That's a fancy way of saying we want to get
the original version of the `get_values` method, before we changed it, and use
that instead.

```py
class SquareRug(Rug):
    def __init__(self, size = 0, has_fringe = False):
        super().__init__(has_fringe)
        self.size = 0
    
    def get_values(self):
        super().get_values()
        self.size = float(input("Side length of this square rug? "))
```

These two methods first get access to the parent class with the `super()`
function call. While `self` gives us the current instance as type `SquareRug`,
`super()` gives us the current instance as type `Rug`. We then call `get_values`
on that instance to have it ask for and set the has_fringe property, beore doing
the square's user input for side length. For completeness and consistency, we do
the same thing in the `__init__` constructor - instead of setting `has_fringe`
at this point, we let the super class constructor handle it. While it's a bit
silly for this simple case, it's a good habit to get into for when the base
class has more complex initialization behavior.

Let's look at this for `RectangleRug`, and then you can do it yourself for
`CircleRug`!


```py
class RectangularRug(Rug):
    def __init__(self, length = 0, width = 0, has_fringe = False):
        super().__init__(has_fringe)
        self.length = length
        self.width = width
    
    def get_values(self):
        super().get_values()
        self.length = float(input("Length of this rectangular rug? "))
        self.width = float(input("Width of this rectangular rug? "))

    def area(self):
        return self.width * 2 + self.length * 2

    def perimeter(self):
        return (self.width + self.length) * 2
```

Now this is looking like it's saving us some code! Our control loop and
functions for choosing and printing a rug are still working, because we didn't
change how any of the types of properties or methods on the object! We only
changed the implementations of the methods themselves. This process, taking an
existing program and rewriting parts of it to be more legible or efficient, is
called **refactoring**. We will do it many more times!

There's one more refactoring I'd like to do in this program before we move on
to the next section. There's no reason the rugs can't print out themselves. They
already ask for input, and if we have them print their own output, we can easily
say what type the rug is!

We'll do this in two parts. First, we'll add a method `print` with no arguments
to the base `Rug` class. Then we'll add a property `description` to each rug
class.

```py
class Rug():
    # ... The other lines
    def print(self)
        price = self.cost()
        if self.has_fringe:
            with_fringe = "with"
        else:
            with_fringe = "without"
        description = self.description
        print(f"This {description} rug costs ${price:.2f} {with_fringe} fringe.")

class SquareRug(Rug):
    def __init__(self, size, has_fringe):
        super().__init__(has_fringe)
        self.size = size 
        self.description = 'square'
    
    # Other methods
```

I think you get the point, and can handle `RectangularRug` and `CircularRug` on
your own!

Here's a sample session:

```
Price another rug (Y/n): 
1) Square Rug
2) Rectangular Rug
3) Circular Rug
Which type of rug? 1
Should this rug have fringe (y/N)? 
Side length of this square rug? 5
This square rug costs $125.00 without fringe.
Price another rug (Y/n): 
1) Square Rug
2) Rectangular Rug
3) Circular Rug
Which type of rug? 3
Should this rug have fringe (y/N)? y
Radius of this circular rug? 5
This circular rug costs $439.82 with fringe.
Price another rug (Y/n): n
Goodbye!
```

## Examples

*   Change the price per square foot and the price per perimeter.
*   Allow the programmer to set the prices per area and perimeter on a
    rug-by-rug basis

In this section, we've looked at how we define and create our own classes.
Classes describe objects, bundles of data with certain properties and methods
that work hand-in-hand. We rewrote our Rugs programs, and saw how using classes
and objects let us finally have much less duplication and much clearer flow of
operations & data. Taken together, objects allow us to abstract data in the same
way functions allow us to abstract operations and code execution.

Now that we know the basics of programming with objects, we can look at
[tracing objects in memory](./tracing_objets.md).