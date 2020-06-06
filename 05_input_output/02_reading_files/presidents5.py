import csv
import os

from datetime import datetime

class President():
    def __init__(self, number, name, start_date, end_date, party, vice_pres):
        self.number = number
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.party = party
        self.vice_president = vice_pres
        self.duration = end_date - start_date
    
    def __str__(self):
        return self.name

class PresidentsDatabase():
    def __init__(self):
        self.presidents = []
        self.parties = []
    
    def __del__(self):
        self.close()

    def open(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        filename = os.path.join(dir_path, "presidents.csv")
        self.openfile = open(filename)
        self.filereader = csv.reader(self.openfile)

    def close(self):
        if self.openfile != None:
            self.openfile.close()
            self.openfile = None

    def load_presidents(self):
        if len(self.presidents) > 0:
            return
        for row in self.filereader:
            president = make_president_from(row)
            if not president.party in self.parties:
                self.parties.append(president.party)
            self.presidents.append(president)

    def presidents_of(self, party):
        return [
            president
            for president in self.presidents
            if president.party == party
        ]

def parse_presidents_cvs_date(datestring):
    if datestring == "Incumbent":
        return datetime.now()
    return datetime.strptime(datestring, "%B %d, %Y")

def make_president_from(row):
    return President(
        row[0],
        row[3],
        parse_presidents_cvs_date(row[1]),
        parse_presidents_cvs_date(row[2]),
        row[4],
        row[5]
    )

def choose_from_list(list, page_size=8):
    """
    Print a list in pages. Prints 8 items in the list, allowing the user to
    choose from 1) of those, n) next page, or q) quit. Returns the index of the
    selected item in the list, or -1 if no item was chosen.
    """
    page = 0
    looping = True
    while page < len(list) and looping:
        print_list_page(list, page)
        selection = input("Choose an item by number, n) for next page, q) to quit. ")
        if selection.lower().startswith("n"):
            page += page_size
        elif selection.lower().startswith("q"):
            looping = False
        else:
            return int(selection) - 1 + page
    return -1

def print_list_page(list, index=0, count=8):
    i = 1
    for item in list[index : index + count]:
        print(f"{i}) {item}")
        i += 1

class PresidentsUI():
    def __init__(self):
        self.database = PresidentsDatabase()
    
    def __del__(self):
        self.database.close()

    def main(self):
        self.database.open()
        self.database.load_presidents()
        running = True
        while running:
            menu_choice = self.main_menu()
            print()
            if menu_choice.lower().startswith("q"):
                running = False
            else:
                self.run_menu(menu_choice)
                input("Press enter to continue...")
                print()

    def main_menu(self):
        print("Presidents's Database Main Menu")
        print("1) List presidents in order")
        print("2) List presidents by party")
        print("q) Exit the database")
        print()
        menu_choice = input("Menu option? ")
        return menu_choice

    def run_menu(self, menu_choice):
        if menu_choice == "1":
            self.list_presidents()
        if menu_choice == "2":
            self.party_presidents()

    def list_presidents(self):
        pres = choose_from_list(self.database.presidents)
        print()
        if pres > -1:
            self.show_president(self.database.presidents[pres])

    def choose_party(self):
        party_index = choose_from_list(self.database.parties)
        return self.database.parties[party_index]

    def party_presidents(self):
        party = self.choose_party()
        presidents = self.database.presidents_of(party)
        pres = choose_from_list(presidents)
        print()
        if pres > -1:
            self.show_president(presidents[pres])

    def show_president(self, president):
        print(f"{president.name} was the {president.number} president of the United States. They were a memeber of the {president.party} party, and served for {president.duration.days} days, with {president.vice_president} as their vice president.")

if __name__ == "__main__":
    PresidentsUI().main()