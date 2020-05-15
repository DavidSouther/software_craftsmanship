from data import PREGNANCIES

# Set up the lists to calculate sums on
preg_length_by_baby = [[], []]

for [order, length, outcome] in PREGNANCIES:
    if order > 2:
        # Only interested in second babies compared to first
        continue
    preg_length_by_baby[order - 1].append(length)

def avg(list):
    sum = 0
    for val in list:
        sum += val
    return sum / len(list)

print("Average first baby weeks: " + str(avg(preg_length_by_baby[0])))
print("Average second baby weeks: " + str(avg(preg_length_by_baby[1])))
