# Shorter version of 93.py started from 'lst = list()'

c = {'a': 10, 'b': 1, 'c':22}

print(sorted([(v, k) for k, v in c.items()]))

#In this case, we make a list of reversed tuples and then sort it.
