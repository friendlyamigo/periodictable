# get index.xml
# index.xml to dict
# for element in index dict
    # get element dict
    # add element dict info to index dict
# convert index dict to json

import xmltodict
from json import dumps


# open index.xml
with open('db/index.xml') as f:
    tabledict = xmltodict.parse(f)


# get each element dict, delete @xmlns:xlink key
elements_key = tabledict['periodictable']
elements = elements_key['element']
del elements_key['@xmlns:xlink']


# try dict: sort out individual element info into index dict
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


# delete a key
def deletekey(a):
    if a in element:
        del element[a]


# test element is diatomic
def diatomic():
    if 'diatomic' in spam.keys():
        element['diatomic'] = True
    else:
        element['diatomic'] = False


# for all elements
for element in elements:
    # get element name
    element_name = element['@name']
    # open individual element xml
    element_dict = open('db/' + element_name + '.xml')
    element_dict = xmltodict.parse(element_dict)
    # turn elelment_dict into a dict
    spam = element_dict['element']

    # sort info
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
    diatomic()
    # delete specific keys
    deletekey('@name')
    deletekey('@symbol')
    deletekey('@xlink:href')

# put element dict into a json
jsonfile = open('dest/elements.json', 'w')
jsonfile.write(dumps(elements_key, sort_keys=True, indent=2))
