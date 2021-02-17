#a^2 + b^2  = (1000 - (a + b))(1000 - (a + b))
#       0    = 1000000 - 2000a + 2b(a - 1000)
# b = 1000a - 500000 / (a - 1000)


for a in range(1, 1000):
    b1 = 1000 * a - 500000
    b2 = a - 1000
    if b1 % b2 == 0:
        b = b1 / b2
        c = 1000 - a - b
        break

print("a: " + str(a) + " b: " + str(int(b)) + " c: " + str(int(c)))
print(int(a * b * c))
