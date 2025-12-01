# Finding the smallest value

smallest = None
print('Before')
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('After', smallest)

# data types: int, floating point, string, bool and None type
# None data type is a special marker -- it's like a flag
# None has only a value
# None is a constant value
# Bool has two values -- true and false
# int and float point has infinite number values
# None is the smallest value on the code above.
# None can be assigned to any variable
