# Sample 1
i = 1
while i <= 3: 
    print(i)
    i += 1

# Sample 2
j = 1
while j <= 10:
    if j == 2:
        break
    print(j)
    j += 1

# Sample 3
k = 1
while k <= 2: 
    print(k)
    k += 1
else:
    print("The End")

# If there is no 'break', this prints the same
k = 1
while k <= 2: 
    print(k)
    k += 1
print("The End")

# Sample 4
z = 1
while z <= 10:
    if z == 2:
        break
    print(z)
    z += 1
else:
    print("The End")

# Sample 5
z = 1
while z <= 5:
    if z % 2 == 0:
        print(z)
        z += 1
        continue
    z += 1
else:
    print("The End")