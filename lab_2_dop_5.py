x = int(input('введите число '))

y = 2
a = ' '
b = '*'

while x != 1:
    if x % y != 0:
        y = y + 1
    elif x % y == 0:
        a = a + b + str(y)
        x = x // y
    else:
        print('-')
        
print('простые множители вашего числа:', a)
