# Create empty dictionary
my_dict = {}

# Add 2 key-pair values
my_dict["London"] = 12
my_dict["Paris"] = 16

# Print a value:
print(my_dict["London"])

# Print all
print(my_dict)

# Dictionaries have a length
print(len(my_dict))

# Print a list of the keys
print(list(my_dict.keys()))

# Print a list of the values
print(list(my_dict.values()))

# Print a list of tuples with the key-value
print(list(my_dict.items()))

# Delete a key-value
del my_dict['London']
print(my_dict)

# Key in dictionary
print("Rome" in my_dict)
print("Paris" in my_dict)

# Get a key if present
# Or return second value
print(my_dict.get("Madrid", 'City not present'))