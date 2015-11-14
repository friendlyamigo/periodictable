# get index.xml
# index.xml to dict
# for element in index dict
    # get element dict
    # add element dict info to index dict
# convert index dict to json

import xmltodict
from json import dumps

charges_dict = {
    'hydrogen': 1,
    'helium': 0,
    'lithium': 1,
    'beryllium': 2,
    'boron': [3, -3],
    'carbon': 4,
    'nitrogen': -3,
    'oxygen': -2,
    'flourine': -1,
    'neon': 0,
    'sodium': 1,
    'magnesium': 2,
    'aluminium': 3,
    'silicon': [4, -4],
    'phosphorus': [5, 3, -3],
    'sulfur': [6, 4, 2, -2],
    'chlorine': -1,
    'argon': 0,
    'potassium': 1,
    'calcium': 2,
    'scandium': 3,
    'titanium': [4, 3],
    'vanadium': [5, 4, 3, 2],
    'chromium': [6, 3, 2],
    'manganese': [7, 4, 2],
    'iron': [3, 2],
    'cobalt': [3, 2],
    'nickel': 2,
    'copper': [2, 1],
    'zinc': 2,
    'gallium': 3,
    'germanium': [4, 2, -4],
    'arsenic': [5, 3, -3],
    'selenium': [6, 4, -2],
    'bromine': [5, 1, -1],
    'krypton': 0,
    'rubidium': 1,
    'strontium': 2,
    'yttrium':  3,
    'zirconium': 4,
    'niobium': [5, 3],
    'molybdenum': [6, 3],
    'technetium': 6,
    'ruthenium': [8, 4, 3],
    'rhodium': 4,
    'palladium': [4, 2],
    'silver': 1,
    'cadmium': 2,
    'indium': 3,
    'tin': [4, 2],
    'antimony': [5, 3, -3],
    'tellurium': [6, 4, -2],
    'iodine': -1,
    'xenon':  0,
    'cesium': 1,
    'praseodymium': 3,
    'neodymium': [4, 3],
    'promethium': 3,
    'samarium': 3,
    'europium': 3,
    'gadolinium': 3,
    'terbium': [4, 3],
    'dysprosium': 3,
    'holmium': 3,
    'erbium': 3,
    'thulium': 3,
    'ytterbium': 3,
    'lutetium': 3,
    'hafnium': 4,
    'tantalum': 5,
    'tungsten': 6,
    'rhenium': [7, 6, 4, 2],
    'osmium': [8, 6, 4, 3],
    'iridium': [6, 4, 3],
    'platinum': [6, 4, 2],
    'gold': [3, 2, 1],
    'mercury': [2, 1],
    'thallium': [3, 1],
    'lead': [4, 2],
    'bismuth': 3,
    'polonium': [4, 2],
    'astatine': -1,
    'radon': 0,
    'francium': 1,
    'radium': 2,
    'actinium': 3,
    'thorium': 4,
    'protactinium': 5,
    'uranium': [6, 4, 2],
    'neptunium': 7,
    'plutonium': [7, 4],
    'americium': 3,
    'curium': 3,
    'berkelium': 3,
    'californium': 3,
    'einsteinium': 3,
    'fermium': 3,
    'mendelevium': 3,
    'nobelium': 2,
    'lawrencium': 3,
    'rutherfordium': 4,
    'dubnium': None,
    'seaborgium': None,
    'bohrium': None,
    'hassium': None,
    'mietnerium': None,
    'darmstadtium': None,
    'roentgenium': None,
    'copernicium': None,
    'ununtrium': None,
    'flerovium': None,
    'ununpentium': None,
    'livermorium': None,
    'ununseptium': None,
    'ununoctium': None
}

# open index.xml
with open('resources/db/index.xml') as f:
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


def charges(element_name, charges_dict):
    for key, value in charges_dict.iteritems():
        if element_name.lower() == key:
            element['charge'] = value


# for all elements
for element in elements:
    # get element name
    element_name = element['@name']
    # open individual element xml
    element_dict = open('resources/db/' + element_name + '.xml')
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
    # charges
    charges(element_name, charges_dict)
    # diatomic
    diatomic()
    # delete specific keys
    deletekey('@name')
    deletekey('@symbol')
    deletekey('@xlink:href')


# put element dict into a json
jsonfile = open('dest/elements.json', 'w')
jsonfile.write(dumps(elements_key, sort_keys=True, indent=2))
