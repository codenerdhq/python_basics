try:
    result = 10 / 0
except ZeroDivisionError:
    print("Can't divide by 0!")

try:
    num = int("abc")
except ValueError:
    print("Not an integer")