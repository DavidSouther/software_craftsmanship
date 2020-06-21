import csv
import json
import rugs

from os import path
from absl import app
from absl import flags


flags.DEFINE_string("db_path", "./rugs.csv", "Path to .csv file to store rugs.")
FLAGS = flags.FLAGS

class RugDatabase():
    def __init__(self, db_path):
        self.db_path = path.abspath(db_path)
        self.rugs = []

    def load_rugs(self):
        if not path.isfile(self.db_path):
            return
        with open(self.db_path) as db_file:
            rug_reader = csv.reader(db_file)
            for rug_data in rug_reader:
                self._load_rug(rug_data)

    def _load_rug(self, rug_data):
        if len(rug_data) == 0:
            return
        shape = rug_data[0]
        has_fringe = bool(rug_data[1])
        if shape == "square":
            rug = rugs.SquareRug(float(rug_data[2]), has_fringe)
        elif shape == "rectangle":
            rug = rugs.RectangularRug(float(rug_data[2]), float(rug_data[3]), has_fringe) 
        elif shape == "circle":
            rug = rugs.CircularRug(float(rug_data[2]), has_fringe)
        
        self.rugs.append(rug)

    def write_rugs(self):
        with open(self.db_path, 'w') as db_file:
            writer = csv.writer(db_file)
            for rug in self.rugs:
                rug_data = rug.row()
                writer.writerow(rug_data)

    def add_rug(self, rug):
        self.rugs.append(rug)
    
    def remove(self, idx):
        self.rugs.pop(idx)

def print_rugs(rugs_db):
    print (f"There are {len(rugs_db.rugs)} rugs.")
    i = 1
    for rug in rugs_db.rugs:
        print(f"{i}: {rug}")
        i += 1

def delete_rug(rugs_db):
    try:
        idx = int(input("Rug number to delete? "))
        rugs_db.remove(idx - 1)
    except:
        pass

def main_menu(rugs_db: RugDatabase):
    while True:
        print("Main menu")
        print("1) View rugs")
        print("2) Add rug")
        print("3) Remove rug")
        print("q) quit")

        choice = input("Selection? ")
        print()
        if choice == "q":
            break
        elif choice == "1":
            print_rugs(rugs_db)
        elif choice == "2":
            rug = rugs.price_rug()
            rugs_db.add_rug(rug)
        elif choice == "3":
            delete_rug(rugs_db)
        print()

def main(argv):
    rugs_db = RugDatabase(FLAGS.db_path)
    rugs_db.load_rugs()
    main_menu(rugs_db)
    rugs_db.write_rugs()

if __name__ == "__main__":
    app.run(main)
    exit(0)
