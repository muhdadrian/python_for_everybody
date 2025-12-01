fname = input('Enter File:')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        # idiom: retrieve/create/update counter all in a line
        di[w] = di.get(w, 0) + 1

print(di)

x = sorted(di.items())
print(x[:5]) # list of key value pair

