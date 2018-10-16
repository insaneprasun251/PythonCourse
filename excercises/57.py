import json
from pprint import pprint

with open("C:\\Users\\mkucman\\Downloads\\company1.json") as file:
    d = json.loads(file.read())

pprint(d)
