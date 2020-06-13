x = int(input('введите количество чисел '))
y = 1
a = y
while x != 0:
    x = x - 1
    print(y)
    a = y - a 
    y = y + a
