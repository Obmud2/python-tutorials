def route(size):
    L = [[1] * size for _ in range(size)]
    for i in range(size):
        for j in range(i+1):
            print(str(i) + ', ' + str(j))
            if j > i:
                continue
            elif j == 0:
                L[i][j] = 1
            elif j < i:
                L[i][j] = L[i][j-1] + L[i-1][j]
                L[j][i] = L[i][j]
            elif j == i:
                L[i][j] = 2 * L[i][j-1]
    return L

a = route(21)
for i in range(len(a)):
    print(a[i])
