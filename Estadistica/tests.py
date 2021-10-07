import random
from Estadistica.Grouped_Frequency_Table import GroupedFrequencyTable, CentralTrendMeasuresGrouped
from Estadistica.Ungrouped_Frequency_Table import *
from Exam import *

sample = [8, 8, 12, 18, 18, 18, 20, 20, 20, 20, 36, 36, 36, 36, 36, 40, 40, 50, 50, 50, 60, 60, 60, 60, 60, 90, 90, 90,
          100, 120, 120, 120, 140, 140, 140, 150, 150, 150, 160, 16]
test1 = GroupedFrequencyTable(sample)
print(test1.calculate_all())
# n = []
# for i in range(60):
#     n.append(random.randint(1, 200))
# # print(n)