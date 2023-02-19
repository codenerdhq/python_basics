def fun():
    global a
    a = 1
    b = 2

a = "One"
b = "Two"
fun()
print(a)
print(b)