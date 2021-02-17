#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

#n = 600851475143

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

print('Enter number:')
n = int(input())
div = []
x = []

for i in range(2, int(math.sqrt(n))):
    if n % i == 0:
        div.append(i)

for i in div:
    if findPrime(i):
        x.append(i)

print(div)
print(x)
