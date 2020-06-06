import os

dir_path = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dir_path, "presidents.csv")
with open(filename) as presidents:
    for president in presidents:
        print(president)
