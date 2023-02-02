# Creating a set
x = set([1, 3, 3, 1, 3, 2])
print(x)

# Check presence
print(2 in x)

# Add element
x.add(4)
print(x)

# Remove element
x.remove(2)
print(x)

# Frozenset
y = frozenset([1, 2, 3, 1, 3, 5])
print(y)

# Does this work? Example with error
# y.add(4)