# if/elif/else
def show_points(points):
    if points < 6:
        return "Well, not many points. "
    elif points == 6:
        return f"That's exactly {points} points!"
    else:
        return "That's a lot of points!"
    
# Sample 1
print(show_points(10))

# Sample 2
print(show_points(2))

# Sample 3
print(show_points(6))

# Other if/elif/else
number = -5
if number < 0:
    print(f"{number} is negative.") 
elif number > 0:
    print(f"{number} is positive") 
else:
    print(f"{number} is zero.")

# if statement that gets ignored
temperature = 10
if temperature > 20:
    print("That's warm!")