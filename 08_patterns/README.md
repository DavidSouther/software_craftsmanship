# Patterns: Iterators, Composition, Update Loop

## Iterators

* Consistent mechanism to handle groups of similar data
* One operation on multiple pieces of data
* 95% of the time, you'll use a built-in iteratable: Array (or List), Set, Map

### Exercises:
* Loop Back Iterator

## Composition

* Objects referring to objects is more flexible than inheritance
* Game has a list of Invaders
* Invaders can be removed from the list

### Exercises
* 

## Update Loop

* Revisit `while True` from chapter 1
* Rules of Space Invader
  * Invaders move left 20, down, right 20, down, repeat
  * Invaders win if they touch the bottom of the screen
  * Player ship is at the bottom row
  * Player ship can move left and right with arrow keys
  * Player can fire cannon with space
  * One cannon shot per frame (but otherwise can fire as many as they want)
  * When bullet hits invader, it takes one damage
  * Invader can take three damage
  * Player wins when all invaders are dead
* Use iteration and composition to update simulation (game) state
* Use iteration and composition to render a game frame

### Exercises

* Write a Frogger game
