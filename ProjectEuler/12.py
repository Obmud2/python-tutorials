import math

divisors = []

for i in range(2, 10000000):
    n = 0
    divisors = []
    for j in range(1, i):
        n = n + j
    for k in range(1, int(math.sqrt(n)) + 1):
        if n % k == 0:
            divisors.append(k)
    print(i)
    if len(divisors) >= 250:
        break

print(n)
