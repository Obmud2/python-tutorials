a = 1
for i in range(1, 101):
    a *= i
a = str(a)
b = 0
for i in range(len(a)):
    b += int(a[i])

print(b)
