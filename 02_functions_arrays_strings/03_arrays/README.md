# Arrays

The programs we've written so far work on one piece of data at a time. Each
variable holds a single value, and while we've looped work based on what the
user wants to do, we haven't done anything that uses multiple pieces of similar
data. Pricing one rug is helpful, but what if I have a whole warehouse to price?

We handle this by using arrays. Arrays are themselves a data type, but unlike
the data types we've encountered so far, they are comprised of multiple pieces
of some other data type. Actually, there is one type we've seen like this, the
string! We can think of a string as an array of characters, and in a lot of ways
that will help us ground our understanding.

So an array is a list or collection of lots of data of the same type. Instead of
using a different variable to access each piece of data, we use a single
variable that references the array as a whole, and then we use an **index** to
access individual elements of the array. We discussed indexes when we talked
about substrings, but they're really important so we're going to repeat them
again here!

An index is an **offset** into an array. That means that rather than saying the
index is the "1st" or "2nd" or "4th" element, the index is the number of
elements to skip to get to the element we want. This means that (in any language
we will use) the first element of an array is actually at index 0! And if you
have an array with 20 items, if you access the element at index 20, you'll
actually be off the end of the list entirely! This is generally considred a Bad
Thing, and you are discouraged from doing so.

The most common thing we'll do with an array of data is iterate or loop over it,
doing some operation for each item in the array. This is in contrast to the
looping we've done so far, which each looks for a condition to be met with a
`while` loop. In the `for` loop, we give it an array and access every item
sequentially, stopping when we've run out of items to check!

Later in the book, we'll look at arrays with all sorts of data types in them,
and get a lot of interesting behavior. For this section, though, we're going to
stick with good old fashioned numbers, and write some functions that calculate
statistics about these numbers.

## Changing arrays

Arrays are not static. Just like how we can assign different values to
variables, so to can we change an array. We can do this by assigning to a single
index. We can also change the number of items in an array, adding items by
**appending** them to the end (and making the array larger) or **removing** them
(and making the array smaller). Like strings, we can join two or more arrays
together using concatenation. Some languages like Python and TypeScript even let
us slice and dice chunks from the middle of an array! 

[Python](./01_python.md)
