from DigitizedImage import DigitizedImage, Rect

window = Rect(140, 300, 1000, 300)
di = DigitizedImage('/Users/dwong/src/wyzant/DonaldW/NYState--3206---000215--medium--jpg--gs.jpg')
h = di.create_histogram(8, window)
print(h.values)
print(h.get_max_value())
print(h.get_inflection_point())

extracted = di.extract(window)
extracted.save('/Users/dwong/Downloads/extracted.png')

ip = h.get_inflection_point()
binarized1 = di.binarize(window, ip * h.binsize)
binarized1.save('/Users/dwong/Downloads/binarized1.png')
binarized2 = di.binarize(window, (ip - 3) * h.binsize)
binarized2.save('/Users/dwong/Downloads/binarized2.png')
binarized3 = di.binarize(window, (ip - 4) * h.binsize)
binarized3.save('/Users/dwong/Downloads/binarized3.png')
