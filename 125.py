import json
data = '''{
"name" : "Chuck",
"phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
 },
 "email" : {
    "hide" : "yes"
 }
 }
'''

info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"] ["hide"])

#JSON -- JavaScript Object Notation
#You will encounter more JSON than XML.
#XML is good for rich and hierarchal documents.
#JSON is best for pulling data out of system and moving between two systems.
#JSON represents data as nested "lists" and "dictionaries"