# Less verbose compared to 79.py

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

# print(di)

# now we want to find the most common word
largest = -1 #-1 is bad assumption
theword = None
for k,v in di.items():
    # print(k, v)
    if v > largest:
        largest = v
        theword = k  #capture/remember the word that was largest

print('Done', theword, largest)