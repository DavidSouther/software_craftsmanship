class Room():
    def __init__(self, description, key = None):
        self.description = description
        self.key = key
        self.doors = []
    
    def on_enter(self, player):
        if self.key != None:
            player.keyring.add_key(self.key)

class Door():
    def __init__(self, side_a, side_b, description = "", lock = None):
        self.side_a = side_a
        self.side_b = side_b

        if description == "":
            description = f"Door between {side_a.description} and {side_b.description}"
        self.description = description

        self.lock = lock

        side_a.doors.append(self)
        side_b.doors.append(self)
    
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

class Player():
    def __init__(self, start_room):
        self.keyring = Keyring()
        self.current_room = start_room

    def move_through(self, door):
        if door != None and self.keyring.can_unlock(door):
            self.current_room = door.other_side(self.current_room)
            self.current_room.on_enter(self)
        else:
            print(f"Cannot move through {door.description}")

class Game():
    def __init__(self, start_room, end_room):
        self.start_room = start_room
        self.end_room = end_room
        self.player = Player()
        self.player.current_room = self.start_room

    def print_room(self):
        room = self.player.current_room
        print(f"You are in {room.description}.")
        doors = len(room.doors)
        if doors == 1:
            print("There is 1 door")
        else:
            print(f"There are {doors} doors")
        i = 0
        for door in room.doors:
            print(f"{i + 1}) {door.description}")
            i += 1
    
    def move_player(self, direction):
        if direction < len(self.player.current_room.doors):
            door = self.player.current_room.doors[direction]
            self.player.move_through(door)
        else:
            print("No room in that direction.")
    
    def play(self):
        while True:
            print() # A blank line
            self.print_room()

            direction = input("Which door do you go through? (q to quit) ")[0]
            if direction.lower() == "q":
                break
    
            self.move_player(int(direction) - 1)

            if self.player.current_room == self.end_room:
                print("You won the treasure!")
                break 

blue_key = "blue"
blue_lock = Lock()
blue_lock.add_fitting_key(blue_key)
room_a = Room("the entry room")
room_b = Room("the library", blue_key)
room_c = Room("the dining room")
room_d = Room("the kitchen")

Door(room_a, room_b)
Door(room_a, room_c)
Door(room_c, room_d, lock=blue_lock)

game = Game(room_a, room_d)
game.play()
