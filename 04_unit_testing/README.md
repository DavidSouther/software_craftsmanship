# Unit Testing

For most of the programs in the first few chapters, you may have picked up that
every time we did a bit of work, we wrote some code immediately after it to see
what it did and check that it worked. We'd erase it right away as we moved on,
but having those little pieces of checking code served as a useful scaffolding
while we took measured steps along our trail.

In this chapter we will formalize this approach by writing unit tests.
**Unit tests** are small, concise programs which execute and verify isolated
pieces and modules of our larger primary programs. By writing these smaller
verification programs, we gain large amounts of confidence that what we wrote is
in fact doing the correct and reasonable computation.

Unit tests should be small and simple so that they are easily verified. They
should be focused to constrain and contain the areas of interest. Unit tests
help us debug as we're writing, and help us catch any **regressions**, changes
we later make which break the program.

* Unit Testing is validating programs work
* Unit tests are focused
* Unit tests are small
* Unit tests help debug as we're writing, and catch regressions later.

## Anatomy of a unit test

Unit tests are built into a test suite. A **test suite** is a collection of unit
tests around a group of functionality - for insteance, a test suite for a square
rug. Within the test suite, we will have a number of **tests cases** which are
short functions to verify a single behavior or edge case of the square rug.

Unit test methods generally have three parts. They begin by doing **set up** to
get the objects into some state that is interesting. This could be creating a
new instance of a rug, or building a maze with the Player in a certain room. The
test will then **evaluate** some code. This might be calculating the area or
cost of a rug, or insturcting the player to move through a door. Finally, the
test will **assert** that some condition (or conditions) is true. This could be
checking the value of the computation of the rug cost or area, or it could check
that the player did move through the door to a new room (or did not move through
a locked door).

Let's see what this looks like in practice. We'll write some tests for the Rugs
and Maze programs we wrote in Chapter 3: Objects, and then discuss some advanced
techniques in unit testing.

[Rug Tests](./01_rug_tests/)