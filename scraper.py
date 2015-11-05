# get index.xml
# index.xml to dict
# for element in index dict
    # get element dict
    # add element dict info to index dict
# convert index dict to json

import xmltodict
from json import dumps


with open('db/index.xml') as f:
    tabledict = xmltodict.parse(f)


elements_key = tabledict['periodictable']
elements = elements_key['element']
del elements_key['@xmlns:xlink']


def trydict(a, link=False):

    if link:
        try:
            element['link'] = 'https://en.wikipedia.org/wiki/' + spam[a]
        except:
            pass

    else:
        try:
            element[a] = spam[a]
        except:
            pass

def deletekey(a):
    if a in element:
        del element[a]


for element in elements:

    element_name = element['@name']

    element_dict = open('db/' + element_name + '.xml')
    element_dict = xmltodict.parse(element_dict)

    spam = element_dict['element']

    trydict('name')
    trydict('symbol')
    trydict('atomic_number')
    trydict('mass_number')
    trydict('electronegativity')
    trydict('melting_point')
    trydict('boiling_point')
    trydict('density')
    trydict('thermal_conductivity')
    trydict('covalent_radius')
    trydict('atomic_radius')
    trydict('specific_heat')
    trydict('electrical_conductivity')
    trydict('name', link=True)

    deletekey('@name')
    deletekey('@symbol')
    deletekey('@xlink:href')

jsonfile = open('dest/elements.json', 'w')
jsonfile.write(dumps(elements_key, sort_keys=True, indent=2))
