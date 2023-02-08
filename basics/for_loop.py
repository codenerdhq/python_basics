# Author: CodeNerdHQ

# List Declaration in Python
numbers = [10, 5, 12]

# If we just need the element
for i in numbers:
  print(i)

# In case we need the index of the element
for i in range(len(numbers)):
    print(numbers[i])


# Let's use range to get an iterable
for x in range(3, 7):
    print(x, end=" ")
  
print()
# This will not count backwards
for x in range(5, 3):
   print(x)

print()
# To go back
for i in range(5, 0, -1):
   print(i, end=" ")

print()
# Count by an amount different than 1
for i in range(0, 10, 2):
   print(i, end=" ")

print()
# Use enumerate to get index and value
x = [-7, 3, 9, -5, 4]
for index, element in enumerate(x):                                
    if element < 0:                                            
        print("Negative number at index", index)