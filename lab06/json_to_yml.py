import json
import yaml

with open('data_1.json', 'r') as josn_in, open('data_1.yml', 'w') as out:
    in_object = json.load(josn_in)
    yaml.safe_dump(in_object, out)