def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    elif age > 120:
        raise ValueError("Over 120 years, woah!")

try:
    age = -1
    validate_age(age)
except ValueError as e:
    print(f"Error: {str(e)}")

try:
    age = 121
    validate_age(age)
except ValueError as e:
    print(f"Error: {str(e)}")
