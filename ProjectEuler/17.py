S = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
D = [0, 3, 6, 6, 5, 5, 5, 7, 6, 6]
H = 7
T = 8

total = 0

for i in range(1,1000):
    c = i % 10 #singles
    b = int(((i % 100) - c) / 10) #tens
    a = int(((i % 1000) - (b * 10) - c) / 100) #hundreds


    if a != 0:
        total += S[a] + H
        if b != 0 or c != 0:
            total += 3
    if b == 0 or b == 1:
        total += S[b * 10 + c]
    else:
        total += D[b] + S[c]

print(total + 11)
