"""
@The get method for dictionaries

-The pattern of checking to see if a key is already in a dictionary and
assuming a default value if the key is not there is so common that there is a method
called get() that does this for us
"""

# Simplified counting with get()
# We can use get() and provide a 'default value of zero' when the key is not yet in the dictionary - and then just add one

counts = dict()
# print(counts)
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1
    # print(counts[name])
print(counts)

# To better understand the default value of zero:

"""
if name in counts:
    x = counts[name]
else:
    x = 0

@ The four lines of code above is equal to a line of code at below
    
x = counts.get(name, 0)
"""