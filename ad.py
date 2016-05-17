import json
from pprint import pprint


with open('Recoreds.json') as data_file:
            text = json.load(data_file)

pprint(text[0])