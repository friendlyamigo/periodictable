import xmltodict
from json import dumps

with open('db/index.xml', 'r') as file:
    tabledict = xmltodict.parse(file)

with open('dest/elements.json', 'w') as file:
    file.write(dumps(tabledict))
