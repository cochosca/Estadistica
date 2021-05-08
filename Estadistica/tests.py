import random
from Estadistica.Grouped_Frequency_Table import GroupedFrequencyTable

n = []
for i in range(50):
    n.append(random.randint(1, 100))
print(n)

test1 = GroupedFrequencyTable(n)
