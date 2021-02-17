sumsq = 0
sqsum = 0

for i in range(1, 101):
    sumsq = i * i + sumsq
    sqsum = i + sqsum

print(sumsq - sqsum * sqsum)
