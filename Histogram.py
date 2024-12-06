class Histogram:
    def __init__(self, binsize: int):
        self.__minValue = 0
        self.__maxValue = 255
        if (self.__maxValue + 1) % binsize != 0:
            raise 'binSize must be divisible by ' + str(self.__maxValue + 1)
        self.binSize = binsize
        self.values = [0] * ((self.__maxValue + 1) // binsize)

    def add_value(self, value: int):
        self.values[value // self.binSize] += 1

    def get_max_value(self):
        max_index = 0
        max_count = -1
        for i in range(len(self.values)):
            if self.values[i] > max_count:
                max_count = self.values[i]
                max_index = i
        return max_index * self.binSize
