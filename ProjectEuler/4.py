#A palindromic number reads the same both ways.
#The largest palindrome made from the product of two 2-digit
#numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.
import math
prod1, prod2 = 0, 0

for i in range(999, 100, -1):
    num = str(i)
    num = int(num + num[2] + num[1] + num[0])
    for j in range(int(math.sqrt(num)), 999):
        if num % j == 0:
            prod1 = j
            prod2 = int(num / prod1)
            break
    else:
        continue
    break

print(num)
print(str(prod1) + ' * ' + str(prod2))
