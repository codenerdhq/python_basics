# A string stored in a variable
my_string = "Hey!"

# Strings are sequence of chars!
print(my_string[2])

print(my_string[3:4])

# Strings have a length
print(len(my_string))

for x in my_string:
    print(x)

# String concatenation
my_string = "Hey " + "you!"
print(my_string)

# String multiplication
print(5 * "#")

# New line
print("Hello\nWorld")

# Tab
print("Hello\tWorld")

# Printing also a new line
print("Hello\n")

# End="" will drop \n
print("Hello\n", end="")

# Changing the ending char
print("Hello", end=" - ")
print("World")

# Joining a list in a string
print(" ".join(["Hello", "World"]))

# Splitting a string
print("Hello World".split())

# Split with another sequence
print("Hello-World-Hello".split("-"))

# Convert to float
x = "123.45"
print(float(x))

# This returns ValueError!
# print(int(x))

# Cnvert int
y = "10"
print(int(y))

# ValueError!
# print(int("Hello!"))

# Replacement chars
x = "wall"
x = x.replace("w", "b")
print(x)

# Case
print("hello".upper())

print("hello".capitalize())

print("HELLO".lower())