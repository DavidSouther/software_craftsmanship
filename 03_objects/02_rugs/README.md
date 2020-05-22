# Classes

In our calendar program, we used objects that we got from our language's date
module. This is great for common features when we need them, but we also want to
define our own object types. We do this by creating a class. A **class** is a
description of the type of object that we want, as well as a group of functions
which operate specifically on this data type. These focused functions are called
methods, which allows a class to bundle both data and the operations that
are effective on it.

Once you have a class which describes a bundle of data, we use it to get the
object. A copy of an object created from a class like this is an **instance**,
which has data specific to one copy of the class. Where the class describes the
data in abstract, and you only have one class for any time, you can have any
number of instances of the class. You create a new one any time you want data of
a certain shape that matches the class, fill it in with the specific data, and
can then use it any where that expects a value of this type. Just like some
functions take numbers or strings, they can also take objects to operate on.

All classes start with a **constructor**, a function which specially creates and
initializes an object of that type. The constructor runs any time you want to
get a new instance, and it fills in all the properties on the object.
Constructors, as functions, can take arguments which allow it to specify any
values it needs to correctly initialize the state of the object. Once the
constructor has finished running, our program has a new value of this class'
type, each of its properties filled in by the constructor.

Almost all classes have methods. **Methods** are functions which are attached to
the class and whenever they are called, take an argument either explicitly or
implicitly of the instance to work on. Methods can also take additional
arguments, and they can both change the state (values of internal properties) of
the object as well as returning a value. Usually, a method will either change
internal state, or it will return a value calculated from internal state.

As an example of this, in the workbooks we will create classes for our rugs. We
have been dealing with square, rectangular, and circular rugs, but all of these
are doing basically the same set of operations - calculate area, possibly
calculate perimeter, ask for some inputs, calculate a cost at the end based on
the area and perimeter. In the past chapters, we've had functions which handle
each of these separately. Our programs had to keep track of the inputs, add up
the total cost, print it out, just passing values over and over.

With classes, we can instead define how our general data will behave. It will
handle asking for input in a contained way, using a `get_values` method which
each different rug type will use to get what is important to it. We can have a
`cost` method which delegates to `area` and `perimeter`, which can be written
specifically to each type of rug we have.

One incredibly powerful feature of classes is the idea of **inheritance**.
Inheritance lets us create a class with a reference to some other class, which
it can then add to or partially modify. This is powerful because we can describe
general classes which cover a wide range of cases, and then make later classes
which are more specific to their cases later.

This will let us organize our rugs code even further. We'll have a
**base class** (also known as a **super class**), `Rug`, which knows how to
calculate cost and ask whether it has fringe. We can then make
**derived classes** specific to square rugs and rectungular rugs and circular
rugs to handle each specific case of getting the area and perimeter for each of
those shapes.

The end result of all of this should be code that is much more self contained,
concise, and understandable by ourselves and any future reader.

[Python](./01_python.md)
