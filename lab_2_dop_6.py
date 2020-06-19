x = int(input('введите число x до которого будут искаться совершенные числа: '))

y = 1 #число
z = 1 #делитель
a = 0 #сумма детителей
c = ''
b = ' '

while x > y:
    while y > z :
        if y % z == 0:
            a = a + z
            z = z + 1
        else: 
            z = z + 1
    if y == a:
        v = c + b + str(y)
        y = y + 1
    else:
        y = y + 1

print('совершенные числа до х:', c)


