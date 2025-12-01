data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos) #index

sppos = data.find(' ', atpos)
print(sppos) #index

host = data[atpos+1 : sppos]
print(host)