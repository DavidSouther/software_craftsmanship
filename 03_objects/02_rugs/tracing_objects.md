# Tracing Objects

Now that we're starting to develop our feel for using objects as a way to bundle
data, let's take a closer look at how the computer handles the data in an object
under the hood. We'll do that by extending the notation we use when tracing a
program.

In our traces for chapters 1 and 2, we kept a two-column table of identifiers
and values, which represented variables in our program. We separated the rows by
functions, and used arrows to track where return values came from and went to.

For objects, we could write out the entire set of properties and their values in
the value column, but that seems difficult as objects get larger than maybe two
or three properties. It also doesn't give us a reasonable picture of what is
actually happening in memory. Instead, whever we create an object, we're going
to draw a T in the right half of the trace. Above the T, we're going to write
what type the object. And then we're going to use the left and rigt parts as
identifier and value - of the properties of the object! So just like each
function has its own scope in the main table, over on the side here each object
will also have its own little area to track its data.

So what do we put in the value for the variable in the function? We're going to
draw an arrow from the value box and point at the object we just wrote out! This
lets us clearly see where each variable is pointing, when it has an object value
instead of a simple value.


> TODO: Replace with a proper digram. Until then, instead of arrows, the text
diagrams will use "tags" - `0x10` is the first object, `0x20` the second, etc.
Then down below, in addition to the type, we'll track the tag of the object as
well. When I get around to making a real graphic all the `0x..` tags will be
replaced with arrows.

```

```

