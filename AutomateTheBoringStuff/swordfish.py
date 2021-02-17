while True:
    print('Who are you?')
    name = input()
    if name != 'Jon':
        continue
    print('What\'s the password? (It is a fish)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')
