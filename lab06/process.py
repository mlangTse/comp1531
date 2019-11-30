import os 
import pickle
import json

data = {}

if os.path.exists('shapecolour.p'):
    data = pickle.load(open('shapecolour.p', 'rb'))

colour = {}
shape = {}

for i in data:
    x = i['colour']
    y = i['shape']
    if x not in colour:
        colour[x] = 0
    else:
        colour[x] += 1

    if y not in shape:
        shape[y] = 0
    else:
        shape[y] += 1

DATA_STRUCTURE = {
    "mostCommon": {
        'colour': max(colour, key=colour.get),
        'shape': max(shape, key=shape.get),
    },
    "rawData": data,
}

with open('processed.json', 'w') as FILE:
    print(json.dumps(DATA_STRUCTURE))
    json.dump(DATA_STRUCTURE, FILE)
