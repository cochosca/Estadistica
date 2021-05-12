import random
from Estadistica.Grouped_Frequency_Table import GroupedFrequencyTable
from math import log10

n = []
for i in range(60):
    n.append(random.randint(1, 200))
# print(n)

m = [1, 2, 3, 4, 5, 5, 6, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10]

test1 = GroupedFrequencyTable(m)
print(test1.make_data_frame())

