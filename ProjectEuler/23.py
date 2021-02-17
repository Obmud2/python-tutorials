def sumProperDivisors(n):
    s = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            s += i + n / i
        if (n ** 0.5) == int(n ** 0.5):
            s -= 1#n ** 0.5
    return s

limit = 28123
abundant = [i for i in range(1, limit) if sumProperDivisors(i) > i]

lists = [i for i in range(limit)]

for a in range(len(abundant)):
    for b in range(a, limit):
        if abundant[a] + abundant[b] < limit:
            lists[abundant[a] + abundant[b]] = 0
        else:
            break
    print(a)


print(sum(lists))
