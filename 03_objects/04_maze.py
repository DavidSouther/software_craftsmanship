#/usr/bin/env python3

class Room():
    def __init__(self, description, key = None):
        self.description = description
        self.key = key
        self.north_door = None
        self.south_door = None
        self.west_door = None
        self.east_door = None
    
    def add_north_door(self, north_room, lock = None):
        self.north_door = Door(self, north_room, lock)
        north_room.south_door = self.north_door 

    def add_south_door(self, south_room, lock = None):
        self.south_door = Door(self, south_room, lock)
        south_room.north_door = self.south_door

    def add_east_door(self, east_room, lock = None):
        self.east_door = Door(self, east_room, lock)
        east_room.west_door = self.east_door
    
    def add_west_door(self, west_room, lock = None):
        self.west_door  = Door(self, west_room, lock)
        west_room.east_door = self.west_door

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

    def rekey_lock(self, lock):
        lock.add_fitting_key(self)

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
            self.keyring.add_key(self.current_room.key)

class Game():
    def __init__(self, start_room, end_room):
        self.start_room = start_room
        self.end_room = end_room
        self.player = Player()
        self.player.current_room = self.start_room
    
    def play(self):
        while True:
            print("You are in a room.")
            room = self.player.current_room
            print(room.description)
            if room.north_door != None:
                print("There is a door to the (n)orth.")
            if room.east_door != None:
                print("There is a door to the (e)ast.")
            if room.south_door != None:
                print("There is a door to the (s)outh.")
            if room.west_door != None:
                print("There is a door to the (w)est.")
            print("(q) to quit.")
            direction = input("Which direction do you go? ")
            if direction == 'q':
                break
            if direction == 'n' and room.north_door != None:
                self.player.move_through(room.north_door)
            elif direction == 'e' and room.east_door != None:
                self.player.move_through(room.east_door)
            elif direction == 'w' and room.west_door != None:
                self.player.move_through(room.west_door)
            elif direction == 's' and room.south_door != None:
                self.player.move_through(room.south_door)
            else:
                print("No room in that direction.")
                continue

            if self.player.current_room == self.end_room:
                print("You won the treasure!")
                return

blue_key = Key("blue")
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