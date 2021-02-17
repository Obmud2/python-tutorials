

def collatz(number):
    if number % 2 == 0:
        x = number // 2
    else:
        x = 3 * number + 1
    print(x)
    return(x)

print('Enter number:')
try:
    number = int(input())
    while number != 1:
        number = collatz(number)
except ValueError:
    print('You must enter an integer.')
