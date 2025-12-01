fruit = 'banana'

pos = fruit.find('na')
print(pos)
#2
aa = fruit.find('z')
print(aa)
#-1

# We use the find() function to search for a substring within another function.
# find() finds the first occurence of the substring
# if the substring is not found, find() returns -1
# remember that string position starts at zero