# Another way to avoid 'traceback' in 63.py

han = open('mbox.txt')

for line in han:
    line = line.rstrip()
    print('Line:', line)
    if line == '':
        # print('Skip Blank')
        continue
    wds = line.split()
    print('Words:', wds)
    if wds[0] != 'From':
        # print('Ignore')
        continue
    print(wds[2])

