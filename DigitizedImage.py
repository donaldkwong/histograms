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
    def __init__(self, path):
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
        self.edgeInsets = EdgeInsets(10, 10, 10, 10)

    def create_histogram(self, binSize, window):
        if window.left < 0 or window.top < 0 or window.width < 0 or window.height < 0:
            raise 'Invalid window'
        if window.left + window.width > self.width or window.top + window.height > self.height:
            raise 'Window outside of bounds'
        histogram = Histogram(binSize)
        for row in range(window.height):
            for col in range(window.width):
                index = (row + window.top + self.edgeInsets.top) * self.__real_width + col + window.left + self.edgeInsets.left
                histogram.add_value(self.__data[index])
        return histogram