#2520 is the smallest number that can be divided by each of
#the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible
#by all of the numbers from 1 to 20?

def gcd(x, y):
   while(y):
       x, y = y, x % y
   return x
def lcm(x, y):
   lcm = (x*y)//gcd(x,y)
   return lcm

result = 1
for i in range(2, 21):
    result = lcm(i, result)
print(result)



#for i in range(1, 9999999):
#    for j in range(1, 18):
#        if i % j != 0:
#            break
#        if j == 17
#            print(i)
