# Counting Pattern

counts = dict()
print('Enter a line of text:')
line = input('')

words = line.split()

print('Words:', words)

print('Counting...')
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts', counts)

# the clown ran after the car and the car ran into the tent and the tent fell down on the clown and the car


