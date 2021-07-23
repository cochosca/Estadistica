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
            intervals_for_frequency.append([intervals_for_plot[n], intervals_for_plot[n + 1]])
        intervals_for_frequency[-1][-1] += 1
        intervals_for_plot[-1] += 1

        # make the references for each type of interval
        self.intervals_for_plot = intervals_for_plot
        self.intervals_for_frequency = intervals_for_frequency
        return f"\n=> The intervals for plot: {intervals_for_plot} " \
               f"\n=> The interval for frequency: {intervals_for_frequency}"

    def get_class_mark(self):
        """Calculate the class marks"""

        # mean of each interval
        class_mark = []
        for i in range(len(self.intervals_for_frequency)):
            class_mark.append((self.intervals_for_frequency[i][0] + self.intervals_for_frequency[i][1]) / 2)
        self.class_mark = class_mark
        return f"=> The class marks: {class_mark}"

    # Absolute Frequency for grouped Frequencies - Polymorphism
    def fi(self):
        """Create a list of frequencies of each interval"""

        self.freq_absolute = [0 for i in range(len(self.intervals_for_frequency))]
        # calculate the frequencies
        for data in self.raw_data:
            for position in range(len(self.intervals_for_frequency)):
                if self.intervals_for_frequency[position][0] <= data < self.intervals_for_frequency[position][1]:
                    self.freq_absolute[position] += 1
                    break
        return f"\n-->> The absolute frequency is: {self.freq_absolute}"

    def nest_frequency(self):
        """Nest the frequencies for the pandas DataFrame"""
        # GroupedFrequencyTable.calculate_all(self)

        grouped_frequency_table = []
        for a, b, c, d, f, g, h in zip(self.intervals_for_frequency, self.class_mark,
                                       self.freq_absolute, self.freq_cumulative,
                                       self.freq_relative, self.freq_relative_cumulative,
                                       self.percentage_var):
            grouped_frequency_table.append([a, b, c, d, f, g, h])
        self.grouped_frequency_table = grouped_frequency_table

    def make_data_frame(self):
        """Make the data frame of pandas"""
        # GroupedFrequencyTable.nest_frequency(self)

        df = DataFrame(self.grouped_frequency_table,
                       columns=["Class Interval", "Class Mark", "Absolute Frequency",
                                "Absolute Cumulative Frequency", "Relative Frequency",
                                "Relative Cumulative Frequency", "Percentage"])
        # Path: /home/cocho/Documents/Proyectos python/Estadistica/csv
        self.df = df
        # self.df.to_csv(r'/home/cocho/Documents/Proyectos python/Estadistica/csv/Test.csv', index=False)
        return self.df

    def calculate_all(self):
        """Calculate all frequencies"""
        GroupedFrequencyTable.class_interval_width(self)
        GroupedFrequencyTable.get_intervals(self)
        GroupedFrequencyTable.get_class_mark(self)
        GroupedFrequencyTable.fi(self)
        GroupedFrequencyTable.fac(self)
        GroupedFrequencyTable.fr(self)
        GroupedFrequencyTable.fr_ac(self)
        GroupedFrequencyTable.percentage(self)
        GroupedFrequencyTable.nest_frequency(self)
        print(GroupedFrequencyTable.make_data_frame(self))


class CentralTrendMeasuresGrouped(GroupedFrequencyTable):
    """This class calculate the central trend measures for ungrouped frequencies"""

    def __init__(self, raw_data):
        super().__init__(raw_data)
        # CentralTrendMeasuresGrouped.calculate_all(self)
        self.median_interval = None
        self.median_index = None
        self.mean_grouped = None

    def arithmetic_mean_grouped(self):
        """Calculate the arithmetic mean of grouped frequencies"""
        # summation = sum(self.class_mark)
        # mean_grouped = round(summation / self.n, 2)
        summation = []
        for p in range(len(self.class_mark)):
            summation.append(self.class_mark[p] * self.freq_absolute[p])
        mean_grouped = round(sum(summation) / self.n, 2)
        self.mean_grouped = mean_grouped
        return f"--> The mean is: {mean_grouped}"

    def median_grouped(self):
        """Calculate the median for grouped frequencies"""
        # Calculate the median position in relation to the total of data
        if self.n % 2 == 0:
            first_position = (self.n // 2)
            second_position = (self.n // 2) + 1
            median_value = (first_position + second_position) // 2
        else:
            median_value = (self.n + 1) // 2

        # Determinate which interval is median
        self.median_index = 0
        for i in range(len(self.freq_cumulative)):
            if self.freq_cumulative[i] > median_value:
                self.median_index += i
                break

        # Calculate the median
        self.median_interval = self.intervals_for_frequency[self.median_index][0]
        if self.median_index == 0:
            division_up = ((self.n / 2) - 0)
        else:
            division_up = ((self.n / 2) - self.freq_cumulative[self.median_index - 1])
        median_grouped = round(self.median_interval + (division_up / self.freq_absolute[self.median_index]) *
                               self.interval_width, 2)
        return f"--> The median is: {median_grouped}"
        # return median_interval

    def trend_grouped(self):
        max_freq = max(self.freq_absolute)
        trend_position = self.freq_absolute.index(max_freq)
        trend_interval = self.intervals_for_frequency[trend_position]

        # d1 = Difference between the absolute frequency of  trend and the previous absolute frequency
        d1 = self.freq_absolute[trend_position] - self.freq_absolute[trend_position - 1]

        # d2 = Difference between the absolute frequency of  trend and the next absolute frequency
        if self.freq_absolute[trend_position] == self.freq_absolute[-1]:
            # When the absolute frequency is equal to the last frequency
            d2 = self.freq_absolute[trend_position]
        else:
            d2 = self.freq_absolute[trend_position] - self.freq_absolute[trend_position + 1]
        trend = round(trend_interval[0] + (d1 / (d1 + d2)) * self.interval_width, 2)
        return f"--> The trend is: {trend}"

    def calculate_central_measures(self):
        CentralTrendMeasuresGrouped.calculate_all(self)
        print(CentralTrendMeasuresGrouped.arithmetic_mean_grouped(self))
        print(CentralTrendMeasuresGrouped.median_grouped(self))
        print(CentralTrendMeasuresGrouped.trend_grouped(self))


class MakeHistogram(CentralTrendMeasuresGrouped):
    """Create the histogram"""

    def __init__(self, raw_data):
        super().__init__(raw_data)
        MakeHistogram.calculate_central_measures(self)

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


class DeviationMeasuresGrouped(CentralTrendMeasuresGrouped):
    """Calculates all deviation measures"""
    def __init__(self, raw_data):
        super().__init__(raw_data)

    def deviation_media(self):
        deviation_list = []
        for value in range(len(self.class_mark)):
            deviation_list.append(abs((self.mean_grouped - self.class_mark[value]) * self.freq_absolute[value]))

        deviation_media = round(sum(deviation_list) / self.n, 2)
        return deviation_media
