# Software Design and Architecture

On our journey into the world of Software Craftsmanship, we've completed our
first steps. We have an understanding of the way computers run and store values.
We've used functions to abstract reusable blocks of executable code, and we've
used objects to abstract bundles of data. These core pieces are all we need to
write software. Everything else is just using them - either built in to our
language, from a library we include, or that we've written ourselves. Of course,
you probably aren't comfortable with that level of power yet!

The rest of this book explores how to take these tools and use them in effective
ways. How to take the objects we're creating, and develop & iterate on their
designs so that they effectively solve our problems. How to verify the
correctness of our objects and functions, both so they meet our original
requirements as well as so they don't break when someone edits them later. How
to evaluate, learn, and utilize libraries from other developers to short cut
lots of effort using pre-built and off-the-shelf tools. How to work in a team
and collaborative environment to build tools that work for more people in a
wider range of settings.

That's a lot left to cover, but in this section we're going to start small.
We're going to look at a problem statement, discuss several approaches to
designing code which will handle that problem, and then implementing one version
based on our analysis.

## Maze

We're writing a video game called "Maze". In this game, the player starts in
some room of a maze. Their goal is to find the exit of the maze. They can wander
the maze going through doorways which connect rooms. Some of these doors are
locked, and the keys to any locked doors are place in rooms throughout the maze.
Let's look at an almost trivial sample maze:


```
  012345678
6 ┌───┐
5 │ X │
4 ├│B│┤
3 │   ├───┐
2 ├─╫─┤ B │
1 │ E ╪   │
0 └───┴───┘
```

In this maze, the player starts in the room on the bottom left marked `E`. This
room has two doors, one to the north and one to the west. The room to the west
is a bit larger, and has a key marked `(B)lue`. North of the entrance room,
there's an empty room with another door again to the north. This door is locked
and needs the blue key to unlock it. Once through that door, the player is at
the exit and has beaten the level! To solve the maze, the player clearly needs
to visit the room with the blue key in order to make it out.

While we don't have much programming under our belts, we can at least start to
think of a couple ways to represent this. One possibility, looking at the one
drawing we have, would be to represent the maze as an array of arrays. What this
means is that each row in the maze is an array of characters or strings, and
each character in that array we compare against a number or the ASCII values of
the drawing we have. We would then need some notion of a player, which would
need to figure out how to "walk around" in this two dimensional array. Let's
see what this might look like for a single function, `move_left`, in Python:

```python
def move_up(maze, player):
    if len(maze) <= player.row + 1:
        # Can't move this direction
        return
    cell = maze[player.row + 1][player.column]
    if cell == 'X':
        print("Found the exit!")
    if maze[player.row + 1][player.column - 1] == '|'
            and maze[player.row + 1][player.column + 1] == '|':
        if not player.keyring.includes(cell):
            # The door is locked
            return
    if cell == ' ' or cell == '╫':
        player.rows += 1
```

If we call this function using the above maze and a player at row 1 column 2, we
can see what happens. First, we check if the cell up one row is outside the
bounds of the maze. In this case, it is not. So we look into the maze, first at
row 2 and then inside row 2 at column 3. That cell has a ╫. It's not an X, so we
skip the first condition. Then we need to look to see if the cell above us is
in a door - we do that by checking it it's the | characters. They are not, so we
continue to the last condition. If it's an empty cell or the vertical open door
we change the player so that they're in the next row up.

This... is convoluted, to say the least. One of the most important design
criteria in software engineering is the "single responsibility principle". It's
like the Occham's Razor of programming. Any function, class, or other
abstraction we create should choose one thing to do, and do that one thing well.
Complexity should come from the domain the program is being written for, and not
from the program itself.

Looking at this sample code from the single responsibility principle, we can
see several competing concerns. Each `if` block really tries to do its own thing
with some checking for the exit, some checking for open doors, others checking
for locked doors. On second review, we actually see that this code doesn't do
anything in the case of moving onto a square with a key - try tracing the
function starting at row 1 column 6.

## Rooms and Doors

Let's try a different design. The last design tried to create a model of the
maze with the ASCII diagram being the "source of truth". With our notion of
classes and objects, we can take a more abstract view of the maze, which will
lend itself to clearer, more sraightforward code to traverse the maze.

Instead of looking at the maze as a grid of cells, we can create a class which
represents each room. The room, then, knows which room it connects to, and which
keys it has. In the future, it would provide a convenient point to logically add
more generic items. So if we think of rooms,  instead of blindly looking around,
we can have a player object that can just look at the room object it's in for
what doors are around.

As we think through this, one issue pops up quickly - how do we keep track which
doors are locked? With classes and objects, this is easy! We just introduce the
idea of a door. A door is an object which has two sides, each being rooms, and
a property for whether it's locked (and which key unlocks is). Now, how does
the `move_up` code look in python?

```python
def move_up(player):
    room = player.current_room
    door = room.north_door
    if door == None:
        return
    if door.is_unlocked_by(player.keyring):
        return
    player.current_room = door.other_side(room)
    player.current_room.on_enter(player)
```

Comparing the two functions, it's hopefully apparent this is a much clearer as
to what's happening. We know that the function is working with the north door
(there's a clear connection between "move up" and "north door"). The bounds
checking is very clear - when the door to the north is not present, the function
does nothing. The door can check itself if the player's keyring has a key that
fits it. And then, with the clear setup of what's happening, the player steps
through the door - and lets the room on the other side tell the player what they
just found!

Beyond teaching programming, a goal of this book is to teach programming in a
way that shows how to make these types of decision, or at least where these
decisions will arise in a setting of a larger development process. It is not an
overstatement to say that code like the first example has grown to cause
projects to run over time, over budget, and even to fail, while clear
architecture and design during the software engieering process has directly led
to projects coming in on time, in budget, and serving a long and useful life.

Let's take a look at the full example and explore this maze in depth in our
language of choice.

[Python](./01_python.md)