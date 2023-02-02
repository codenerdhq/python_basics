# 3 elements tuple
x = (1, 2, 3)

# Print an element
print(x[1])

# This sums 2 and 5
x = (2 + 5)
print(x)

# This sums 2 and 5 and puts the sum in a tuple
x = (2 + 5,)
print(x)

# Unpack
(one, two, three) = (1, 2, 3)
print(two)

# Same as
one, two, three = 1, 2, 3
print(two)

# Easily swap vars
a, b = "A", "B"
a, b = b, a
print(b)

# Convert from tuple to list
list(("a", "b", "c"))

# Convert from list to tuple
tuple(("a", "b", "c"))

# Does this work? Example that returns error
# y = (1, 2, 3)
# y.append(3)