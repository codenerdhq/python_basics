my_dict = {"somekey": "somevalue"}
try:
    print(my_dict["otherkey"])
except KeyError:
    print("Key not present")

if "otherkey" in my_dict:
    print(my_dict["otherkey"])
else:
    print("Key not present")