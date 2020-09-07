class Room:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
    
    def add_neighbor(self, neighbor):
        if not neighbor in self.neighbors:
            self.neighbors.append(neighbor)
            neighbor.add_neighbor(self)
    
    def print_room(self):
        print(f"This is the {self.name}.")
        doors = len(self.neighbors)
        if doors == 1:
            print("There is 1 door")
        else:
            print(f"There are {doors} doors")

        for i, room in enumerate(self.neighbors, start=1):
            print(f"{i}) {room.description}")
    
    def on_enter(self, player):
        print(f"You entered the {self.name}")

class TreasureRoom(Room):
    def __init__(self, name, value):
        Room.__init__(self, name)
        self.value = value
        self.visited = False
    
    def on_enter(self, player):
        Room.on_enter(self, player)
        if not self.visited:
            self.visited = True
            print(f"It has {self.value} gold!")
            player.treasure += self.value

class MonsterRoom(Room):
    def __init__(self, name, strength):
        Room.__init__(self, name)
        self.strength = strength
    
    def on_enter(self, player):
        Room.on_enter(self, player)
        if not self.visited:
            self.visited = True
            print(f"It has a monster, which deals ${strength} damage!")
            player.health -= self.strength

class Player:
    def __init__(self, starting_room, health = 20):
        self.health = health
        self.current_room = starting_room
        self.treasure = 0

    def move(self, direction):
        if direction < len(self.current_room.neighbors):
            room = self.current_room.neighbors[direction]
            self.current_room = room
            room.on_enter(self)
        else:
            print("No room in that direction.")    
    
class Game:
    def __init__(self, start_room, end_room):
        self.player = Player(start_room)
        self.end_room = end_room

    def play(self):
        while True:
            print()
            player.current_room.print_room()

            direction = input("Which door would you like to go through? ([q]uit) ")[0]
            if direction.lower() == "q":
                break

            # Subtract 1 because the room descriptions start at 1 but the array starts at 0
            player.move(int(direction) - 1)

            if self.player.health <= 0:
                print("You have died!")
                break

    
    print("Goodbye!")

entrance = Room('Entryway')
hallway = Room('Hallway')
dining_room = MonsterRoom('Dining Room', 2)
billiards_room = TreasureRoom('Billiards Room', 100)
ballroom = TreasureRoom('Ballroom', 300)
library = MonsterRoom('Library', 4)
lounge = MonsterRoom('Lounge', 4)
study = MonsterRoom('Study', 3)
kitchen = TreasureRoom('Kitchen', 100)
conservatory = TreasureRoom('Conservatory', 200)

entrance.add_neighbor(hallway)
hallway.add_neighbor(dining_room)
hallway.add_neighbor(billiards_room)
hallway.add_neighbor(ballroom)
hallway.add_neighbor(library)
hallway.add_neighbor(study)
hallway.add_neighbor(lounge)
kitchen.add_neighbor(conservatory)

kitchen.add_neighbor(study)
conservatory.add_neighbor(lounge)

Game(entrance)