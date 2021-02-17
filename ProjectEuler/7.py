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

primeList = []
while len(primeList) < 10001:
    for i in range(1,1000000):
        if findPrime(i) == True:
            primeList.append(i)
        if len(primeList) == 10001:
            break

print(primeList[-1])
print(primeList[0])
print(len(primeList))
