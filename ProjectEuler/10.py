import math

def findPrime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if (num % i == 0):
            return False
    return True

primeSum = 0
for i in range(1,2000000):
    if findPrime(i) == True:
        primeSum += i

print(primeSum)
