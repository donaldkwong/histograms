from DigitizedImage import DigitizedImage, Rect

di = DigitizedImage('/Users/dwong/src/wyzant/DonaldW/NYState--3206---000215--medium--jpg--gs.jpg')
h = di.create_histogram(8, Rect(0, 0, 100, 50))
print(h.values)
