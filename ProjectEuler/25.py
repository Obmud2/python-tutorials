F = [1, 1, 0]
count = 0

while(True):
    F = [F[1], F[2], F[1] + F[2]]
    count += 1
    if len(str(F[2])) == 2:
        print(count)
        break
