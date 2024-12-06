from DigitizedImage import DigitizedImage, Rect

window = Rect(140, 300, 400, 140)
di = DigitizedImage('/Users/dwong/src/wyzant/DonaldW/NYState--3206---000215--medium--jpg--gs.jpg')
h = di.create_histogram(8, window)
print(h.values)
print(h.get_max_value())

extracted = di.extract(window)
extracted.save('/Users/dwong/Downloads/extracted.png')

binarized = di.binarize(window, h)
binarized.save('/Users/dwong/Downloads/binarized.png')
