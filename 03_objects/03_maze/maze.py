class Room():
    """
    A Room is in a maze.

    It has a brief description. It might have a maze. It has walls in the
    cardinal directions, and each wall may or may not have a door.

    A room has methods for adding doors in each of the cardinal directions.
    These methods take the other room to connect this room to, creat a door
    between them, and sets the door appropriately for both sides. If the other
    room already had a door there... well, that door is broken and only goes one
    way now, I guess?
    """
    def __init__(self, description, key = None):
        self.description = description
        self.key = key
        self.doors = []
    
    def on_enter(self, player):
        if self.key != None:
            player.keyring.add_key(self.key)

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

class Lock():
    def __init__(self):
        self.fitting_keys = []

    def accepts(self, key):
        return key in self.fitting_keys
    
    def add_fitting_key(self, key):
        if not key in self.fitting_keys:
            self.fitting_keys.append(key)

class Key():
    def __init__(self, color):
        self.color = color
    
    def __str__(self):
        return f"{self.color} key"

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

blue_key = Key("blue")
blue_lock = Lock()
blue_lock.add_fitting_key(blue_key)
room_a = Room("The entry room")
room_b = Room("The Library", blue_key)
room_c = Room("The dining room")
room_d = Room("The kitchen")

Door(room_a, room_b)
Door(room_a, room_c)
Door(room_c, room_d, blue_lock)

game = Game(room_a, room_d)
game.play()