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

entry_room = Room("Entrance")
exit_room = Room("Exit")
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
program, we'll give the player a keyring and let 

```py
class Lock():
    def __init__(self):
        self.fitting_keys = []

    def accepts(self, key):
        return key in self.fitting_keys
    
    def add_fitting_key(self, key):
        if not key in self.fitting_keys:
            self.fitting_keys.append(key)

class Keyring():
    def __init__(self):
        self.keys = []

    def add_key(self, key):
        if not key in self.keys:
            print(f"Picked up {key}")
            self.keys.append(key)
    
    def can_unlock_door(self, door):
        if door.lock == None:
            return True
        for key in self.keys:
            if door.lock.accepts(key):
                return True
        return False
```

## Game and Player

```py
class Player():
    def __init__(self):
        self.keyring = Keyring()
        self.current_room = None

    def move_through(self, door):
        if door != None and self.keyring.can_unlock_door(door):
            self.current_room = door.other_side(self.current_room)
            self.current_room.on_enter(self)

class Game():
    def __init__(self, start_room, end_room):
        self.start_room = start_room
        self.end_room = end_room
        self.player = Player()
        self.player.current_room = self.start_room

    def print_room(self):
        room = self.player.current_room
        print("You are in a room.")
        print(room.description)
        if room.north_door != None:
            print("There is a door to the (n)orth.")
        if room.east_door != None:
            print("There is a door to the (e)ast.")
        if room.south_door != None:
            print("There is a door to the (s)outh.")
        if room.west_door != None:
            print("There is a door to the (w)est.")
    
    def move_player(self, direction):
        room = self.player.current_room
        if direction == "n" and room.north_door != None:
            self.player.move_through(room.north_door)
        elif direction == "e" and room.east_door != None:
            self.player.move_through(room.east_door)
        elif direction == "w" and room.west_door != None:
            self.player.move_through(room.west_door)
        elif direction == "s" and room.south_door != None:
            self.player.move_through(room.south_door)
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

blue_key = ("blue"
blue_lock = Lock()
blue_lock.add_fitting_key(blue_key)
room_a = Room("The entry room")
room_b = Room("The Library", blue_key)
room_c = Room("The dining room")
room_d = Room("The kitchen")

room_a.add_east_door(room_b)
room_a.add_north_door(room_c)
room_c.add_north_door(room_d, blue_lock)

game = Game(room_a, room_d)
game.play()
```
