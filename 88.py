# Tuples and Dictionaries

# The items() method in dictionaries returns a list of (key, value) tuples

d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k, v) in d.items():
    print(k, v)

tups = d.items()
print(tups)
#dict_items([('csev', 2), ('cwen', 4)]) -- list of tuples
