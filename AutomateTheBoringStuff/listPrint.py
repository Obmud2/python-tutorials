
spam = ['apples', 'cats']

x = spam[0] + ', '

for i in range (1, len(spam) - 1):
    x += spam[i] + ', '

x += 'and ' + spam[-1]

print(x)
