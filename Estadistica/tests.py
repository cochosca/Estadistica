import random
from Estadistica.Grouped_Frequency_Table import GroupedFrequencyTable, CentralTrendMeasuresGrouped
from math import log10

n = []
for i in range(60):
    n.append(random.randint(1, 200))
# print(n)

m = [1, 2, 3, 4, 5, 5, 6, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10]

# x = max(m)
# p = m.index(x)
#
#
# print(p)

test1 = CentralTrendMeasuresGrouped(m)
print(test1.arithmetic_mean_grouped())
print(test1.median_grouped())
print(test1.trend_grouped())

