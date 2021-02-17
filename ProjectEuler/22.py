def importNames():
    files = open('p022_names.txt')
    names = files.read()
    files.close()
    a = names.split(',')
    for i in range(len(a)):
        a[i] = a[i].strip('"')
    a.sort()
    return a

alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

names = importNames()
scores = []
for i in range(len(names)):
    scores.append(0)
    for j in range(len(names[i])):
        scores[i] += alpha.index(names[i][j]) + 1
    scores[i] *= i + 1
print(sum(scores))
