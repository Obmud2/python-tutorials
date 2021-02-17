def sumProperDivisors(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s


A = []

for i in range(1, 10000):
    a = sumProperDivisors(i)
    if (sumProperDivisors(a) == i) and (i not in A) and a!=i:
        A.append(a)
        A.append(i)

print(sum(A))
