import random
from Estadistica.Grouped_Frequency_Table import GroupedFrequencyTable, CentralTrendMeasuresGrouped
from Exam import *

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

fio = [2, 8, 14, 21, 32, 15, 8]
intervals = [150, 155, 160, 165, 170, 175, 180]
# test2 = TableToGroupedFrequencies(intervals, fio, [0])
# print(test2.calculate_central_measures())
n_test = [2, 21, 24, 33, 37, 39, 39, 43, 43, 45, 50, 68, 74, 74, 75, 82, 85, 86, 86, 86, 87, 94, 96, 97, 101, 103,
          105, 105, 112, 113, 120, 127, 129, 129, 131, 134, 136, 138, 138, 150, 152, 156, 157, 157, 162, 166, 177,
          179, 181, 183, 183, 186, 187, 188, 188, 189, 189, 193, 199, 200]


test4 = CentralTrendMeasuresGrouped(n)
print(test4.calculate_central_measures())
# test1 = CentralTrendMeasuresGrouped(n)
# # print(test1.())
# # print(test1.arithmetic_mean_grouped())
# print(test1.median_grouped())
# print(test1.trend_grouped())
