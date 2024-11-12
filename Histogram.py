class Histogram:
    def __init__(self, binSize):
        self.__minValue = 0
        self.__maxValue = 255
        if (self.__maxValue + 1) % binSize != 0:
            raise 'binSize must be divisible by ' + str(self.__maxValue + 1)
        self.binSize = binSize
        self.values = [0] * ((self.__maxValue + 1) // binSize)

    def add_value(self, value):
        self.values[value // self.binSize] += 1
