from pandas import DataFrame


class UngroupedFrequencyTable:
    """ 
    This class create objets like tables of frequency
    Attributes:
        raw_data = [list of the numbers]
    """

    def __init__(self, raw_data):
        self.raw_data = raw_data
        self.variables = None
        self.freq_absolute = None
        self.freq_cumulative = None
        self.freq_relative = None
        self.freq_relative_cumulative = None
        self.percentage_var = None
        self.table_frequency = None

    def get_variable(self):
        """ Extract raw data and create a set,
            for delete duplicate and get only the
            variables
            """
        variables = {data for data in self.raw_data}
        variables = list(variables)
        self.variables = variables
        return self.variables

    # Absolute Frequency
    def fi(self):
        """Calculate the frequency absolute of
        each variable"""
        freq_absolute = [self.raw_data.count(i) for i in self.variables]
        self.freq_absolute = freq_absolute
        return self.freq_absolute

    # Absolute cumulative Frequency
    def fac(self):
        """Calculate the frequency accumulated of each variable"""
        freq_cumulative = []
        accumulated = int()
        for i in self.freq_absolute:
            accumulated += i
            freq_cumulative.append(accumulated)
        self.freq_cumulative = freq_cumulative
        return self.freq_cumulative

    # Relative Frequency
    def fr(self):
        """Calculate the relative frequency of each variable"""
        n = self.freq_cumulative[-1]  # n = total quantity of variables
        freq_relative = [round(i / n, 2) for i in self.freq_absolute]
        self.freq_relative = freq_relative
        return self.freq_relative

    # Relative cumulative frequency
    def fr_ac(self):
        """Calculate the frequency relative accumulated of each variable"""
        freq_relative_cumulative = []
        accumulated_relative = float()
        for n in self.freq_relative:
            accumulated_relative += n
            freq_relative_cumulative.append(round(accumulated_relative, 1))
        self.freq_relative_cumulative = freq_relative_cumulative
        return self.freq_relative_cumulative

    # Percentage
    def percentage(self):
        """Decide the percentage of each variable"""
        percentage_var = ['{:1.1%}'.format(i * 1) for i in self.freq_relative]
        self.percentage_var = percentage_var
        return self.percentage_var

    def calculate_all(self):
        """Calculate all frequencies"""
        UngroupedFrequencyTable.get_variable(self)
        UngroupedFrequencyTable.fi(self)
        UngroupedFrequencyTable.fac(self)
        UngroupedFrequencyTable.fr(self)
        UngroupedFrequencyTable.fr_ac(self)
        UngroupedFrequencyTable.percentage(self)
        # return f"{test.variable()} \n{test.fi()} \n{test.fac()} \n{test.fr()} " \
        #       f"\n{test.fr_ac()} \n{test.percentage()} "

    def nest_frequency(self):
        """Nest the frequencies in one variable for make a pandas DataFrame"""
        UngroupedFrequencyTable.calculate_all(self)
        table_frequency = []
        for a, b, c, d, e, f in zip(self.variables, self.freq_absolute, self.freq_cumulative, self.freq_relative,
                                    self.freq_relative_cumulative, self.percentage_var):
            table_frequency.append([a, b, c, d, e, f])
        self.table_frequency = table_frequency
        return table_frequency

    def make_data_frame(self):
        UngroupedFrequencyTable.nest_frequency(self)
        df = DataFrame(self.table_frequency, columns=["Variable", "Absolute Frequency",
                                                      "Absolute Cumulative Frequency", "Relative Frequency",
                                                      "Relative Cumulative Frequency", "Percentage"])
        return df


test = UngroupedFrequencyTable([4, 9, 85, 72, 95, 80, 24, 4, 85, 90])
print(test.make_data_frame())
