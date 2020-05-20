# Objects

Variables in computer programs track data. We saw some of the kinds of data they
can track in chapter 1. In chapter 2, we saw how computers can use variables to
track calculations across a number of functions. Whether this is as internal
variables to remember an intermediate result, in arguments to take or pass data,
or in return statements to hand data back the the caller, variables are integral
to making programs work.

Sometimes, though, we want a bit more structure than what we can get just from
naming them differently. What we want as programs get complex is a way to bundle
several related variables together. In this way, we can treat them as a single
entity in our program. We can create them once, modify each part individually,
and keep the whole thing together when passing it to another function. This also
helps understanding - rather than talking about an area a width and a height
which we keep in our heads as being about one rug, we can instead talk about a
single rug, which has an area, a width, and a height. It may sound pedantic, but
in practice it really makes tracking complex pieces of data much easier!

These bundles of data are called **objects**. Each piece of data bundled into an
object is a **property** on an object. We can think of objects having "shape" or
"structure" based on what properties it has on it, and the types of data that
are stored in those properties. A property in a lot of ways just a variable that
is attached to a single object in our program. The property has an
**identifier** and stores a **value**. It's just that it can't appear alone, and
only is part of the object.

An object is a value, which means you can assign it to a variable. You can pass
it to a function as an argument. You can even assign an object into a property
of another object! Building out complex objects like this is how we'll later
begin building **data structures**. That's a couple chapters away - in the mean
time, just keep in mind objects being a bundle of related data, each piece of
which you can access from its properties. Let's get some practice looking at
dates, objects which store information about a moment in time.

[Python](./01_python.md)