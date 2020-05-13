# Drawing

* Canvases allow 2d drawing
* Lines, circles, arcs
* Setting colors, thickness, other styles

## Fractals

* Self-similar shapes
* Defined by simple relations
* Koch snowflake: take a line. Subdivide it into three equal sections. Take the middle section and
  replace with a pair of lines of equal length. Repeat as long as desired.
* Mandelbrot set: for every point in a 2-d plane, treat the point as a complex number. Iterate the
  recurrance relation f(c, z) = z^2 + c replacing z with the last iteration value (starting at 0).
  Count the number of iterations for z to become > 2, and map that to a color. If after some number
  of iterations z is still < 2, consider the value bounded (and use black).

### Exercises
* Make a Mandelbrot Fractal Explorer

## Turtle

* Turtle is a friendly drawing buddy.
* Turtle has a pen. It can change the color of the tip. It can lift the tip or set the tip down, but
  is always holding the pen. Turtle can move forward, or can turn left or right some amount.
* Write a simple Turtle library with:
  * penUp()
  * penDown()
  * move(n)
  * turnLeft(d)
  * turnRight(d)
* Use this library to draw your initials

### Exercises
* Add penColor(c) to your turtle
* Make a UI with buttons that map to each of Turtle's actions.
