from pandas import DataFrame
from math import log10


class GroupedFrequencyTable:
    """
    This class create Grouped Frequency Tables

    Attributes:
        raw_data = [list of numbers]
    """

    def __init__(self, raw_data):
        self.raw_data = raw_data
        self.raw_data.sort()

    def get_raw_data(self):
        return self.raw_data

    def class_interval_width(self):
        """ Calculate the width of the interval class, the range and
        the number of interval classes
        """
        range_data = max(self.raw_data) - min(self.raw_data)
        numbers_interval_classes = 1 + 3.322 * log10(range_data)
        numbers_interval_classes = int(numbers_interval_classes)
        if numbers_interval_classes % 2 == 0:
            numbers_interval_classes += 1
        else:
            pass
        interval_width = range_data // numbers_interval_classes
        return f"{interval_width} is the interval width \n{range_data} is the range " \
               f"\n{numbers_interval_classes} is the number of intervals"


pedro = GroupedFrequencyTable([80, 4, 9, 85, 72, 95, 80, 24, 4, 85, 90, 67, 68, 43, 97,
                               76, 76, 58, 44, 56, 46, 54, 51, 13, 32, 12, 23, 100])

print(pedro.class_interval_width())
