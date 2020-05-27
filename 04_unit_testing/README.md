# Unit Testing

For most of the programs in the first few chapters, you may have picked up that
every time we did a bit of work, we wrote some code immediately after it to see
what it did and check that it worked. We'd erase it right away as we moved on,
but having those little pieces of checking code served as a useful scaffolding
while we took measured steps along our trail.



* Unit Testing is validating programs work
* Unit tests are focused
* Unit tests are small
* Unit tests help debug as we're writing, and catch regressions later.

## Anatomy of a untit test

* Test Suite
* Test Methods
  * Set up
  * Evaluate
  * Assert

### Exercises:

* Rugs Tests
* Maze Tests

## Advanced Topics

* Before Each: Block of setup
* Mocks: Replacing complex with simple behavior
  * Test rugs input/output
* Spies: Checking if related code has been called with the expected values
  * Spy on datetime to test clock
* Test Driven Development
  * Red/Green/Refactor
