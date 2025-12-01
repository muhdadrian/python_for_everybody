#Tuples are comparable

"""
The comparison operators work with tuples and other sequences. If the first
item is equal, Python goes on to the next element, and so on until it finds elements that differ.
"""

(0, 1, 2) < (5, 1, 2)

(0, 1, 2000000) < (0, 3, 4)

('Jones', 'Sally') < ('Jones', 'Sam') #m > l

('Jones', 'Sally') > ('Adams', 'Sam') #J > A