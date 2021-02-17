D = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']
Md = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
M = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#1st Jan
#No of dis

dates = []

for i in range(1900, 2001):
    for j in range(12):
        if j == 1:
            M[j] = 28
            if i % 4 == 0:
                if (i % 100 == 0) and (i % 400 != 0):
                    M[j] = 28
                else:
                    M[j] = 29
        for k in range(M[j]):
            dates.append(D[len(dates) % 7] + ' ' + str(k + 1) + ' ' + Md[j] + ' ' + str(i))
count = 0
for i in range(len(dates)):
    if (i % 7 == 6) and (' 1 ' in dates[i]):
        count += 1
print(count)
