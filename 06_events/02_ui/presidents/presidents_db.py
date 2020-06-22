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
