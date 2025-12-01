han = open('mbox.txt')

for line in han:
    line = line.rstrip()
    wds = line.split()
    #Guardian a bit stronger
    if len(wds) < 3:
        continue
    if wds[0] != 'From':
        continue
    print(wds[2])