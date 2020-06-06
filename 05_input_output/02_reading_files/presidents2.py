import csv
import os


dir_path = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dir_path, "presidents.csv")
with open(filename) as presidents_file:
    presidents_reader = csv.reader(presidents_file)
    for row in presidents_reader:
        print(row)
