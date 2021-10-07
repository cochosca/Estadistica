# Hecho por jose Scappini
# Este modulo realizar poliformismo a el modulo de Grouped_Frequency_Table
from Estadistica.Ungrouped_Frequency_Table import CentralTrendMeasures
from Grouped_Frequency_Table import *


class TableToGroupedFrequencies(DeviationMeasuresGrouped):
    """Converts a table with data into lists to calculate the grouped frequencies"""

    def __init__(self, intervals, fi, raw_data):
        super().__init__(raw_data)
        self.intervals_raw = intervals
        self.fi_raw = fi

    def class_interval_width(self):
        self.interval_width = self.intervals_raw[1] - self.intervals_raw[2]
        self.number_interval_classes = len(self.fi_raw)

    def get_intervals(self):
        TableToGroupedFrequencies.class_interval_width(self)
        intervals_for_frequency = []
        amount_intervals = len(self.intervals_raw)
        for n in range(amount_intervals - 1):
            intervals_for_frequency.append([self.intervals_raw[n], self.intervals_raw[n + 1]])
        intervals_for_frequency[-1][-1] += 1
        self.intervals_raw[-1] += 1

        self.intervals_for_plot = self.intervals_raw
        self.intervals_for_frequency = intervals_for_frequency
        return self.intervals_for_frequency

    def fi(self):
        self.freq_absolute = self.fi_raw

    def calculate_all(self):
        TableToGroupedFrequencies.class_interval_width(self)
        TableToGroupedFrequencies.get_intervals(self)
        TableToGroupedFrequencies.get_class_mark(self)
        TableToGroupedFrequencies.fi(self)
        TableToGroupedFrequencies.fac(self)
        TableToGroupedFrequencies.fr(self)
        TableToGroupedFrequencies.fr_ac(self)
        TableToGroupedFrequencies.percentage(self)
        TableToGroupedFrequencies.nest_frequency(self)
        TableToGroupedFrequencies.make_data_frame(self)
        return self.df

    def calculate_central_measures(self):
        print(TableToGroupedFrequencies.calculate_all(self))
        print(TableToGroupedFrequencies.arithmetic_mean_grouped(self))
        print(TableToGroupedFrequencies.median_grouped(self))
        print(TableToGroupedFrequencies.trend_grouped(self))

    def calculate_deviation(self):
        TableToGroupedFrequencies.calculate_all(self)
        TableToGroupedFrequencies.deviation_media(self)


class First(CentralTrendMeasures):
    def __init__(self, x, fi, raw_data):
        super().__init__(raw_data)
        self.x = x
        self.fi = fi

    def get_variable(self):
        self.variables = self.x

    def fi(self):
        return f"{self.x}"

    def arithmetic_mean(self):
        for i in range(2):
            pass

    def calculate_all(self):
        First.get_variable(self)
        First.fi(self)
        First.fac(self)
        First.fr(self)
        First.fr_ac(self)
        First.percentage(self)
        First.nest_frequency(self)
        First.make_data_frame(self)
        return self.df
