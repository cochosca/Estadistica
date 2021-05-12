from math import log10
from Estadistica.Ungrouped_Frequency_Table import UngroupedFrequencyTable
import matplotlib.pyplot as plt
from pandas import DataFrame


class GroupedFrequencyTable(UngroupedFrequencyTable):
    """
    This class create Grouped Frequency Tables

    Attributes:
        raw_data = [list of numbers]
    """

    def __init__(self, raw_data):
        super().__init__(raw_data)
        self.raw_data.sort()
        self.number_interval_classes = None
        self.interval_width = None
        self.intervals_for_plot = None
        self.intervals_for_frequency = None
        self.class_mark = None
        self.freq_absolute = None
        self.grouped_frequency_table = None
        self.df = None

    def get_raw_data(self):
        return max(self.raw_data)

    def class_interval_width(self):
        """ Calculate the width of the interval class, the range and
        the number of interval classes
        """
        range_data = max(self.raw_data) - min(self.raw_data)
        numbers_interval_classes = int(1 + 3.322 * log10(range_data))
        if numbers_interval_classes % 2 == 0:
            numbers_interval_classes += 1
        else:
            pass
        interval_width = round(range_data / numbers_interval_classes, 1)

        # making the reference
        self.interval_width = interval_width
        self.number_interval_classes = numbers_interval_classes
        return f"--> The interval width =  {interval_width} " \
               f"\n--> The range = {range_data}" \
               f"\n--> The number of intervals = {numbers_interval_classes}"

    def get_intervals(self):
        """Calculate the intervals for the plots and for the frequencies"""
        print(GroupedFrequencyTable.class_interval_width(self))

        # get the interval for plots of matplotlib
        accumulated = int(min(self.raw_data))
        intervals_for_plot = []
        for i in range(self.number_interval_classes + 1):
            intervals_for_plot.append(round(accumulated))
            accumulated += self.interval_width

        # get the intervals for calculate the frequencies later
        intervals_for_frequency = []
        amount_intervals = len(intervals_for_plot)
        for n in range(amount_intervals - 1):
            intervals_for_frequency.append([intervals_for_plot[n], intervals_for_plot[n+1]])
        intervals_for_frequency[-1][-1] += 1
        intervals_for_plot[-1] += 1

        # make the references for each type of interval
        self.intervals_for_plot = intervals_for_plot
        self.intervals_for_frequency = intervals_for_frequency
        return f"\n=> The intervals for plot: {intervals_for_plot} " \
               f"\n=> The interval for frequency: {intervals_for_frequency}"

    def get_class_mark(self):
        """Calculate the class marks"""
        print(GroupedFrequencyTable.get_intervals(self))

        # mean of each interval
        class_mark = []
        for i in range(len(self.intervals_for_frequency)):
            class_mark.append((self.intervals_for_frequency[i][0] + self.intervals_for_frequency[i][1])/2)
        self.class_mark = class_mark
        return f"=> The class marks: {class_mark}"

    # Absolute Frequency for grouped Frequencies
    def fi_gf(self):
        """Create a list of frequencies of each interval"""
        print(GroupedFrequencyTable.get_class_mark(self))
        self.freq_absolute = [0 for i in range(len(self.intervals_for_frequency))]
        # calculate the frequencies
        for data in self.raw_data:
            for position in range(len(self.intervals_for_frequency)):
                if self.intervals_for_frequency[position][0] <= data < self.intervals_for_frequency[position][1]:
                    self.freq_absolute[position] += 1
                    break
        return f"\n-->> The absolute frequency is: {self.freq_absolute}"

    def calculate_all(self):
        """Calculate all frequencies"""
        GroupedFrequencyTable.fi_gf(self)
        GroupedFrequencyTable.fac(self)
        GroupedFrequencyTable.fr(self)
        GroupedFrequencyTable.fr_ac(self)
        GroupedFrequencyTable.percentage(self)

    def nest_frequency(self):
        """Nest the frequencies for the pandas DataFrame"""
        GroupedFrequencyTable.calculate_all(self)
        grouped_frequency_table = []
        for a, b, c, d, f, g, h in zip(self.intervals_for_frequency, self.class_mark,
                                       self.freq_absolute, self.freq_cumulative,
                                       self.freq_relative, self.freq_relative_cumulative,
                                       self.percentage_var):
            grouped_frequency_table.append([a, b, c, d, f, g, h])
        self.grouped_frequency_table = grouped_frequency_table

    def make_data_frame(self):
        """Make the data frame of pandas"""
        GroupedFrequencyTable.nest_frequency(self)
        df = DataFrame(self.grouped_frequency_table,
                       columns=["Class Interval", "Class Mark", "Absolute Frequency",
                                "Absolute Cumulative Frequency", "Relative Frequency",
                                "Relative Cumulative Frequency", "Percentage"])
        self.df = df
        return self.df


class MakeHistogram(GroupedFrequencyTable):
    """Create the histogram"""
    def __init__(self, raw_data):
        super().__init__(raw_data)
        MakeHistogram.fi(self)

    def make_hist(self):
        fig, ax = plt.subplots()
        ax.hist(x=self.raw_data, bins=self.intervals_for_plot,
                color="#A12E02", rwidth=0.9)
        ax.plot(self.class_mark, self.freq_absolute)
        ax.title('Histogram')
        ax.xlabel('Raw_data')
        ax.ylabel('Absolute frequency')
        ax.xticks(self.intervals_for_plot)
        ax.show()
