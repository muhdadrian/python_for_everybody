# A tale of two sequences

l = list()
print(dir(l))

t = tuple()
print(dir(t)) #tuple only has 'count' and 'index'

"""
- Since Python does not have to build tuple structures to be modifiable,
they are simpler and more efficient in terms of memory use and performance 
than lists

- So in our program when we are making "temporary variables" we prefer tuples over lists 
"""