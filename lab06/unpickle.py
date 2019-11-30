import os 
import pickle

data = {}

if os.path.exists('shapecolour.p'):
    data = pickle.load(open('shapecolour.p', 'rb'))

def find_most_common():
    pair = None
    count = 0

    for i in data:
        count_most = data.count(i)
        if count_most > count:
            count = count_most
            pair = i
    return pair

pair = find_most_common()
print(f"Colour: {pair['colour']}")
print(f"Shape: {pair['shape']}", end = '')