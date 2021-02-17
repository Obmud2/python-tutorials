def perm(num,index):
    global count
    if index == len(num)-1:
        count += 1
        if count == 1000000 - 1:
            print(num)
        return

    for i in range(index, len(num)):
        newList = num[:]
        temp = newList.pop(i)
        newList.insert(index, temp)
        perm(newList, index+1)

n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

count = 0
perm(n, 0)
print(count)
