# Sorting Lists of Tuples

"""
- We can take advantage of the ability to sort a list of tuples to get
a sorted version of a dictionary

- First we sort the dictionary by the key using the items() method and
sorted() function
"""

d = {'a': 10, 'b': 1, 'c': 22}
print(d.items())
print(sorted(d.items()))