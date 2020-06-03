# Maze Design with Classes

As we discussed in the textbook, we're going to build a program that lets us
control a character moving through a maze. We will represent this using a
variety of classes which interact. The roooms themselves will be instances of a
`Room` class, which will have doors to the north, south, west, and east. (In a
later exercise, we'll change the room to have an unlimited number of doors.) A
door, similarly, will be an instance of a `Door` class. Unlike the room, it will
have an ever fixed number of sides. A door can only connect two specific rooms,
never more, never less.

So for properties, a room will need a door in each cardinal direction. However,
not every cardinal direction will have a door. We represent this case with the
special value `None`. `None` in Python is used as a value wherever you need to
indicate a missing object. So it's for a variable or property that we would
expect to have a value that's an object type, but instead it isn't present. We
then can look for when a value is `None`, and behave accordingly - in this case,
by saying there's not a door in the north or west walls.

Let's start writing out this code. I'm going to do this for the base features as
well as the north door. You will need to fill in the east, south, and west doors
in your own `maze.py` file.

```py
class Room():
    def __init__(self, description, key = None):
        self.description = description
        self.key = key
        self.north_door = None
    
    def add_north_door(self, north_room, lock = None):
        self.north_door = Door(self, north_room, lock)
        north_room.south_door = self.north_door 

class Door():
    def __init__(self, side_a, side_b, lock = None):
        self.side_a = side_a
        self.side_b = side_b
        self.lock = lock
    
    def other_side(self, side):
        if side == self.side_a:
            return self.side_b
        else:
            return self.side_a

entry_room = Room("the entrance")
exit_room = Room("the exit")
entry_room.add_north_door(exit_room)

print(exit_room.south_door.other_side(exit_room).description)
```

When you run this code, it should print out `Entrance`, which is the room on the
other side of the south door from the exit room. The last line of code looks a
bit onerous right now, but we'll be replacing it with something more sensible in
a moment.

Disecting the code we just wrote, we have two classes, one each for `Room` and
`Door`. Neither extends another class, so we have nothing in the parens. Both
classes have a **constructor** , which in Python is a method `__init__`. The
room takes a `description`, a string that describes the room, and `key`, which
is the key (if any) the room has. We use the default value `None` because we
expect it's more common for a room not to have a key. The room needs the two
sides, and also a lock. It has `None` as a default value for the same reason as
the `key` in the `Room`.

Both classes take their constructor arguments and put those values into
properties on the objects that the class constructor created.

`Room` has a method to add a door connecting a room to the north. Rather than
requiring the program to create the door and then attach it themselves, which
would be three steps for the programmer, we'll instead have a single method for
each door direction will will handle creating the door, and attaching it to both
rooms. This type of **object creation** is common because it reduces the number
of things necessary to remember to do to create a correct object. 

## Locks and Keys and Keyrings

In the next section of the code, we need to look at how the locks and keys fit
together. We're actually going to make two classes here - one to represent the
locks themselves, and the second to represent a keyring as a whole. Later in the
program, we'll give the player a keyring and use that to check whether some
doors can or cannot be traveresed.

```py
class Lock():
    def __init__(self, fitting_key = None):
        self.fitting_key = fitting_key

    def accepts(self, key):
        return key == self.fitting_key 
 
class Keyring():
    def __init__(self):
        self.keys = []

    def add_key(self, key):
        if not key in self.keys:
            print(f"Picked up {key} key")
            self.keys.append(key)
    
    def can_unlock(self, door):
        if door.lock == None:
            return True
        for key in self.keys:
            if door.lock.accepts(key):
                return True
        return False

entry_room = Room("entrance")
exit_room = Room("exit")
blue_lock = Lock("blue")
entry_room.add_north_door(exit_room, blue_lock)
keyring = Keyring()

print(keyring.can_unlock(entry_room.north_door))
keyring.add_key("blue")
print(keyring.can_unlock(entry_room.north_door))
```

A lock keeps track of which key fits it, and provides a simple method to check
whether it accepts a certain key. Having this as a separate method allows more
flexibility down the line - while today we have locks which take a single key,
we could think of ways to extend the `Lock` class to require one of several keys
(like a specific key and a master key), or make it need multiple keys to unlock.

The keyring tracks which keys have been found, and for any given door, it asks
the lock on the door if any of its keys fit. If they do, the `can_unlock`
method returns `True` and we know this `Keyring` lets us through that door.

## Game and Player

The last two pieces before our game works are a `Player` and a `Game`. `Player`
tracks where the player currently is in the maze, keeps a `Keyring` to unlock
doors, and a method `move_through` to check if the door is open and then update
which room the player is in.

```py
class Player():
    def __init__(self, start_room):
        self.keyring = Keyring()
        self.current_room = start_room 

    def move_through(self, door):
        if door != None and self.keyring.can_unlock(door):
            self.current_room = door.other_side(self.current_room)
            self.current_room.on_enter(self)
        else:
            print("Cannot move through that door.")
```

The player starts itself in some given room, and makes itself an empty keyring.
The `move_through` method takes a door that the player should attempt to go
through. If the door doesn't exist (is `None`, or a missing object), or if the
keyring dosn't unlock the door, nothing happens. If the door is present and can
be unlocked by the keyring, the player does move through the door. It updates
the current room to be whichever room is on the other side of the door from
where they started. The last line is a call to a method we haven't seen yet -
`on_enter`.

The idea here is that, when a player enters a room, the room has an opportunity
to tell the player object anything that it needs to know. In this case, we're
going to let the room tell the player about the key it has. Let's add this
method to the room class.

```py
class Room():
    # ...

    def on_enter(self, player):
        if self.key != None:
            player.keyring.add_key(self.key)
```

This type of programming is called **inversion of control** which is just a
fancy way to say one object passing itself to another object to let the other
object decide what to call and which properties to change on the first.

Our final class will be the `Game`, which wraps all the rooms and players up and
handles user input and output. Let's type it in, and then we'll review it. Just
like the first `Room` class, this code includes the north door. You will need to
do the other four directions.

```py
class Game():
    def __init__(self, start_room, end_room):
        self.player = Player(start_room)
        self.end_room = end_room

    def print_room(self):
        room = self.player.current_room
        print(f"You are in {room.description}.")
        if room.north_door != None:
            print("There is a door to the (n)orth.")

    def move_player(self, direction):
        room = self.player.current_room
        if direction == "n" and room.north_door != None:
            self.player.move_through(room.north_door)
        else:
            print("No room in that direction.")
    
    def play(self):
        while True:
            self.print_room()

            direction = input("Which direction do you go? (q to quit) ")[0].lower()
            if direction == "q":
                break
    
            self.move_player(direction)

            if self.player.current_room == self.end_room:
                print("You won the treasure!")
                break 
```

A `Game` needs the starting and ending room of the maze. Instead of storing the
`start_room`, it instead creates a new `Player` which starts in the
`start_room`. The `Game` does store the `end_room`, to check during the `play`
method when the player has won.

The bulk of `Game` is in `play`. Like the HiLo game or the rug calculator, a
`while True:` loop keeps repeating the game steps over and over. The steps are
intended to be concise, using the helper methods for the working aspects. The
`Game` prints out the room the player is currently in. It asks which way the
user wants to go. If the user decides to quit, the loop exists. Otherwise, have
the player move in the input direction. After they have moved, check if they
won - and if so, congratulate them and exit! If they're not at the exit yet,
loop back and play some more!

Let's try it out on a bigger maze:

```py
blue_lock = Lock("blue")
room_a = Room("the entry room")
room_b = Room("the library", "blue")
room_c = Room("the dining room")
room_d = Room("the kitchen")

room_a.add_east_door(room_b)
room_a.add_north_door(room_c)
room_c.add_north_door(room_d, blue_lock)

game = Game(room_a, room_d)
game.play()
```

This last block builds out a full game! We have four rooms, a locked door, and
start the player in the entry. Give it a shot!

# Exercises

* Make a bigger maze!
* Add more items or types of keys?
* Provide descriptions of doors.
* Make rooms support as many doors as you want to give them.
