data = range(2, 20, 3)
for i in data:
    print(i)

def sum(my_array):
    total = 0
    for val in my_array:
        total += val
    return total

data_sum = sum(data)
print(f"Data sums to {data_sum:.2f}")

def avg(my_array):
    total = sum(my_array)
    length = len(my_array)
    return total / length

data_avg = avg(data)
print(f"Data average is {data_avg:.2f}")

import math
def std_dev(my_array):
    length = len(my_array)
    my_array_average = avg(my_array)
    std_dev_sum = 0
    for val in my_array:
        diff = val - my_array_average
        std_dev_sum += (diff ** 2)
    return math.sqrt(std_dev_sum / length)

data_std_dev = std_dev(data)
print(f"Data std dev is {data_std_dev:.2f}")

from data import PREGNANCIES

# Set up the lists to calculate sums on
preg_length_by_baby = [[], []]

for pregnacy in PREGNANCIES:
    order = pregnacy[0]
    weeks = pregnacy[1]
    if order > 2:
        # Only interested in second babies compared to first
        continue
    preg_length_by_baby[order - 1].append(weeks)

avg_first_babies = avg(preg_length_by_baby[0])
avg_second_babies = avg(preg_length_by_baby[1])
std_dev_first_babies = std_dev(preg_length_by_baby[0])
std_dev_second_babies = std_dev(preg_length_by_baby[1])

print(f"First babies are born at an average of {avg_first_babies:.2f} weeks.")
print(f"First babies have a standard deviation of {std_dev_first_babies:.2f} weeks")
print(f"Second babies are born at an average of {avg_second_babies:.2f} weeks.")
print(f"Second babies have a standard deviation of {std_dev_second_babies:.2f} weeks")
