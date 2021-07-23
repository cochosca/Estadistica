from pandas import DataFrame
from math import sqrt


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

    def nest_frequency(self):
        """Nest the frequencies in one variable for make a pandas DataFrame"""
        # UngroupedFrequencyTable.calculate_all(self)
        table_frequency = []
        for a, b, c, d, e, f in zip(self.variables, self.freq_absolute, self.freq_cumulative, self.freq_relative,
                                    self.freq_relative_cumulative, self.percentage_var):
            table_frequency.append([a, b, c, d, e, f])
        self.table_frequency = table_frequency
        # return table_frequency

    def make_data_frame(self):
        """Make a data frame from table_frequency"""
        # UngroupedFrequencyTable.nest_frequency(self)
        df = DataFrame(self.table_frequency, columns=["Variable", "Absolute Frequency",
                                                      "Absolute Cumulative Frequency", "Relative Frequency",
                                                      "Relative Cumulative Frequency", "Percentage"])
        self.df = df
        # self.df.to_csv("")
        self.df.to_csv(r'/home/cocho/Documents/Proyectos python/Estadistica/csv/Test.csv', index=False)
        return self.df

    def calculate_all(self):
        """Calculates all frequencies"""
        UngroupedFrequencyTable.get_variable(self)
        UngroupedFrequencyTable.fi(self)
        UngroupedFrequencyTable.fac(self)
        UngroupedFrequencyTable.fr(self)
        UngroupedFrequencyTable.fr_ac(self)
        UngroupedFrequencyTable.percentage(self)
        UngroupedFrequencyTable.nest_frequency(self)
        print(UngroupedFrequencyTable.make_data_frame(self))


class CentralTrendMeasures(UngroupedFrequencyTable):
    """This class calculate the central trend measures for ungrouped frequencies"""

    def __init__(self, raw_data):
        super().__init__(raw_data)
        self.mean = None
        self.median = None

    def arithmetic_mean(self):
        """Calculates the arithmetic mean of the raw data"""
        summation = sum(self.raw_data)
        mean = round(summation / self.n, 2)
        print(f"The mean is: {mean}")
        self.mean = mean

    def median(self):
        """Calculates the median of the raw data"""
        amount_data = len(self.raw_data)  # Number of date in the list
        if amount_data % 2 == 0:
            first_position = (amount_data // 2) - 1
            second_position = (amount_data // 2)
            median = (self.raw_data[first_position] + self.raw_data[second_position]) // 2
            print(f"The median is: {median}")

        else:
            median = self.raw_data[((amount_data + 1) // 2) - 1]
            print(f"The median is: {median}")
        self.median = median

    def trend(self):
        """Calculates the trends"""
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
        CentralTrendMeasures.calculate_all(self)
        CentralTrendMeasures.arithmetic_mean(self)
        CentralTrendMeasures.median(self)
        CentralTrendMeasures.trend(self)


class DeviationMeasures(CentralTrendMeasures):
    """Calculates all deviation measures"""

    def __init__(self, raw_data):
        super().__init__(raw_data)
        self.variance_s = None
        self.variance_p = None
        self.standard_for_sample = None
        self.standard_for_population = None

    def deviation_media(self):
        """Calculates the deviation media of the data"""
        deviation_list = []
        for value in range(len(self.variables)):
            deviation_list.append(abs((self.mean - self.variables[value]) * self.freq_absolute[value]))

        deviation_media = round(sum(deviation_list) / self.n, 2)
        return deviation_media

    def sample_variance(self):
        """Calculates the variance of a sample"""
        sample_variance_list = []
        for variable in range(len(self.variables)):
            sample_variance_list.append(((self.mean - self.variables[variable]) ** 2) * self.freq_absolute[variable])
        self.variance_s = round(sum(sample_variance_list) / (self.n - 1), 2)
        return f"- The sample variance is: {self.variance_s}"

    def population_variance(self):
        """Calculates the variance of a population"""
        population_variance_list = []
        for variable in range(len(self.variables)):
            population_variance_list.append(
                ((self.mean - self.variables[variable]) ** 2) * self.freq_absolute[variable])
        self.variance_p = round(sum(population_variance_list) / self.n, 2)
        return f"- The population variance is: {self.variance_p}"

    def standard_deviation(self):
        self.standard_for_sample = round(sqrt(self.variance_s), 1)
        self.standard_for_population = round(sqrt(self.variance_p), 1)
        return f"-- The standard deviation for sample is: {self.standard_for_sample} \n" \
               f"-- The standard deviation for population is: {self.standard_for_population}"

    def coefficient_variance(self):
        cv_s = round(self.standard_for_sample / self.mean, 1)
        cv_p = round(self.standard_for_population / self.mean, 1)
        return f"--> The coefficient of variance for sample is: {cv_s} \n"\
               f"--> The coefficient of variance for population is: {cv_p}"

    def make_all(self):
        DeviationMeasures.get_all(self)
        DeviationMeasures.deviation_media(self)
        print(DeviationMeasures.sample_variance(self))
        print(DeviationMeasures.population_variance(self))
        print(DeviationMeasures.standard_deviation(self))
        print(DeviationMeasures.coefficient_variance(self))
