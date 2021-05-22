from pandas import DataFrame


class UngroupedFrequencyTable:
    """ 
    This class create Ungrouped frequency tables
    Attributes:
        raw_data = [list of the numbers]
    """

    def __init__(self, raw_data):
        self.raw_data = raw_data
        self.raw_data.sort()
        self.variables = None
        self.freq_absolute = None
        self.freq_cumulative = None
        self.n = None
        self.freq_relative = None
        self.freq_relative_cumulative = None
        self.percentage_var = None
        self.table_frequency = None
        self.df = None

    def get_variable(self):
        """ Extract raw data and create a set,
            for delete duplicate and get only the
            variables
            """
        variables = {data for data in self.raw_data}
        variables = list(variables)
        self.variables = variables
        self.variables.sort()
        # return self.variables

    # Absolute Frequency
    def fi(self):
        """Calculate the frequency absolute of
        each variable"""
        freq_absolute = [self.raw_data.count(i) for i in self.variables]
        self.freq_absolute = freq_absolute
        # return self.freq_absolute

    # Absolute cumulative Frequency
    def fac(self):
        """Calculate the frequency accumulated of each variable"""
        freq_cumulative = []
        accumulated = int()
        for i in self.freq_absolute:
            accumulated += i
            freq_cumulative.append(accumulated)
        self.freq_cumulative = freq_cumulative
        # return self.freq_cumulative

    # Relative Frequency
    def fr(self):
        """Calculate the relative frequency of each variable"""
        n = self.freq_cumulative[-1]  # n = total quantity of variables
        freq_relative = [round(i / n, 2) for i in self.freq_absolute]
        self.freq_relative = freq_relative
        self.n = n
        # return self.freq_relative

    # Relative cumulative frequency
    def fr_ac(self):
        """Calculate the frequency relative accumulated of each variable"""
        freq_relative_cumulative = []
        accumulated_relative = float()
        for n in self.freq_relative:
            accumulated_relative += n
            freq_relative_cumulative.append(round(accumulated_relative, 1))
        self.freq_relative_cumulative = freq_relative_cumulative
        # return self.freq_relative_cumulative

    # Percentage
    def percentage(self):
        """Decide the percentage of each variable"""
        percentage_var = ['{:1.1%}'.format(i * 1) for i in self.freq_relative]
        self.percentage_var = percentage_var
        # return self.percentage_var

    def calculate_all(self):
        """Calculate all frequencies"""
        UngroupedFrequencyTable.get_variable(self)
        UngroupedFrequencyTable.fi(self)
        UngroupedFrequencyTable.fac(self)
        UngroupedFrequencyTable.fr(self)
        UngroupedFrequencyTable.fr_ac(self)
        UngroupedFrequencyTable.percentage(self)

    def nest_frequency(self):
        """Nest the frequencies in one variable for make a pandas DataFrame"""
        UngroupedFrequencyTable.calculate_all(self)
        table_frequency = []
        for a, b, c, d, e, f in zip(self.variables, self.freq_absolute, self.freq_cumulative, self.freq_relative,
                                    self.freq_relative_cumulative, self.percentage_var):
            table_frequency.append([a, b, c, d, e, f])
        self.table_frequency = table_frequency
        # return table_frequency

    def make_data_frame(self):
        """Make a data frame from table_frequency"""
        UngroupedFrequencyTable.nest_frequency(self)
        df = DataFrame(self.table_frequency, columns=["Variable", "Absolute Frequency",
                                                      "Absolute Cumulative Frequency", "Relative Frequency",
                                                      "Relative Cumulative Frequency", "Percentage"])
        self.df = df
        # self.df.to_csv("")
        return self.df


class CentralTrendMeasures(UngroupedFrequencyTable):
    """This class calculate the central trend measures for ungrouped frequencies"""
    def __init__(self, raw_data):
        super().__init__(raw_data)
        # Create de data frame and initialize the calculation of variables
        CentralTrendMeasures.make_data_frame(self)

    def arithmetic_mean(self):
        """Calculate the arithmetic mean of the raw data"""
        summation = sum(self.raw_data)
        mean = round(summation / self.n, 2)
        print(f"The mean is {mean}")

    def median(self):
        """Calculate the median of the raw data"""
        amount_data = len(self.raw_data)  # Number of date in the list
        if amount_data % 2 == 0:
            first_position = (amount_data // 2) - 1
            second_position = (amount_data // 2)
            median_pair = (self.raw_data[first_position] + self.raw_data[second_position]) // 2
            print(f"The median is: {median_pair}")

        else:
            median_odd = self.raw_data[((amount_data + 1) // 2) - 1]
            print(f"The median is: {median_odd}")

    def trend(self):
        """Calculate the trends"""
        max_freq = max(self.freq_absolute)
        amount_trend = self.freq_absolute.count(max_freq)
        if 1 < amount_trend:
            if amount_trend > 2:
                multimodal_info = self.df["Absolute Frequency"] == max_freq
                multimodal_table = self.df[multimodal_info]
                multimodal_list = list(multimodal_table["Variable"])
                print(f"The trend is {multimodal_list} and is a multimodal")
            else:
                bimodal_info = self.df["Absolute Frequency"] == max_freq
                bimodal_table = self.df[bimodal_info]
                bimodal_list = list(bimodal_table["Variable"])
                print(f"The trend is {bimodal_list} and is a bimodal")
        else:
            unimodal_info = self.df["Absolute Frequency"] == max_freq
            unimodal_table = self.df[unimodal_info]
            unimodal_list = list(unimodal_table["Variable"])
            print(f"The trend is {unimodal_list} and is a unimodal")

    def get_all(self):
        CentralTrendMeasures.arithmetic_mean(self)
        CentralTrendMeasures.median(self)
        CentralTrendMeasures.trend(self)
