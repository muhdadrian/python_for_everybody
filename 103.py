# Matching and Extracting Data

#re.search() returns a True/False depending on whether the string matches the regular expression

#If we actually want the matching strings to be extracted, we use re.findall()

import re

x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print(y)
#[0-9]+ -- one or more digits

y = re.findall('[AEIOU] +', x) #No item of uppercase matching
print(y)