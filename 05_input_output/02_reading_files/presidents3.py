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
        return f"{self.name} served {self.duration.days} days"

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

dir_path = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dir_path, "presidents.csv")
with open(filename) as presidents_file:
    presidents_reader = csv.reader(presidents_file)
    for row in presidents_reader:
        president = make_president_from(row)
        print(president)
