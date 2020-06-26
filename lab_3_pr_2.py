from math import cos, tan, sqrt, pi
from astro_constant import g

h = 100
a = pi/3
b = pi/6

v = sqrt((g * h * (tan(b))**2) / (2 * (cos(a))**2 * (1 - tan(b) * tan(a))))

print(v)




from astro_constant import boltzmann_constant as bc
from astro_constant import e
from astro_constant import planck_constant as pc

T = 200
E = 300

N = (2 * pc * e**(-E/(bc * T)) * E**(T/2)) / (pi**0,5 * (bc * T)**(1,5))

print(N)