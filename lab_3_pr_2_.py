from math import cos, sin, pi
from astro_constant import g

v = float(input('введите начальную скорость в м/с: '))
n = float(input('введите угол в формате pi*n, n = '))
a = pi * n
t = float(input('введите момент времени в секундах: '))



r = ((((v * cos(a))**2) + (v * sin(a) - g * t)**2)**(1.5)) / (v * g * cos(a))
print('радиус кривизны в момент времени t:', r, 'метров')