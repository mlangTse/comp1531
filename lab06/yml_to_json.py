import yaml
import json

with open('data_2.yml', 'r') as yaml_in, open('data_2.json', 'w') as out:
    in_object = yaml.safe_load(yaml_in)
    json.dump(in_object, out)