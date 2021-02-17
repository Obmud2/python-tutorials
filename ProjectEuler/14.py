def collatzLen(number):
    count = 0
    n = number
    while n > 1:
        count += 1
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
    return count


longest = [0, 0]

for i in range(1000000):
    print(i)
    if collatzLen(i) > longest[0]:
        longest[0] = collatzLen(i)
        longest[1] = i

print(longest)
