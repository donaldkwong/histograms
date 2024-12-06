class Histogram:
    def __init__(self, binsize: int):
        self.__minValue = 0
        self.__maxValue = 255
        if (self.__maxValue + 1) % binsize != 0:
            raise 'binsize must be divisible by ' + str(self.__maxValue + 1)
        self.binsize = binsize
        self.values = [0] * ((self.__maxValue + 1) // binsize)

    def add_value(self, value: int):
        self.values[value // self.binsize] += 1

    def get_max_value(self):
        max_count = -1
        for i in range(len(self.values)):
            if self.values[i] > max_count:
                max_count = self.values[i]
        return max_count

    def get_inflection_point(self):
        max_value = self.get_max_value()
        for i in range(1, len(self.values)-1):
            value = self.values[i]
            prev_value = self.values[i-1]
            next_value = self.values[i+1]
            if max_value * .08 <= value <= max_value * .12 and prev_value * 2 * .8 <= value <= prev_value * 2 * 1.2 and next_value * .5 * .8 <= value <= next_value * .5 * 1.2:
                return i
        return 0