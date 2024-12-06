from PIL import Image
from typing import NamedTuple

from Histogram import Histogram

class Rect(NamedTuple):
    left: int
    top: int
    width: int
    height: int

class EdgeInsets(NamedTuple):
    left: int
    top: int
    right: int
    bottom: int

class DigitizedImage:
    def __init__(self, path: str):
        self.img = Image.open(path)
        if self.img.mode != 'L':
            self.img = self.img.convert('L')
        self.__data = list(self.img.getdata())
        self.__detect_edges()
        self.__real_width = self.img.width
        self.__real_height = self.img.height
        self.width = self.img.width - (self.edgeInsets.left + self.edgeInsets.right)
        self.height = self.img.height - (self.edgeInsets.top + self.edgeInsets.bottom)

    def __detect_edges(self):
        # TODO: Add edge detection code
        self.edgeInsets = EdgeInsets(0, 0, 0, 0)

    def __validate_window(self, window: Rect):
        if window.left < 0 or window.top < 0 or window.width < 0 or window.height < 0:
            raise 'Invalid window'
        if window.left + window.width > self.width or window.top + window.height > self.height:
            raise 'Window outside of bounds'

    def create_histogram(self, binsize: int, window: Rect):
        self.__validate_window(window)
        histogram = Histogram(binsize)
        for row in range(window.height):
            for col in range(window.width):
                index = (row + window.top + self.edgeInsets.top) * self.__real_width + col + window.left + self.edgeInsets.left
                histogram.add_value(self.__data[index])
        return histogram

    def extract(self, window: Rect):
        self.__validate_window(window)
        values = []
        for row in range(window.height):
            for col in range(window.width):
                index = (row + window.top + self.edgeInsets.top) * self.__real_width + col + window.left + self.edgeInsets.left
                values.append(self.__data[index])
        image = Image.new('L', [window.width, window.height])
        image.putdata(values)
        return image

    def binarize(self, window: Rect, histogram: Histogram):
        self.__validate_window(window)
        max_value = histogram.get_max_value()
        values = []
        for row in range(window.height):
            for col in range(window.width):
                index = (row + window.top + self.edgeInsets.top) * self.__real_width + col + window.left + self.edgeInsets.left
                if self.__data[index] >= max_value:
                    values.append(255)
                else:
                    values.append(0)
        image = Image.new('L', [window.width, window.height])
        image.putdata(values)
        return image



