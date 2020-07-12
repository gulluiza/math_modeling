import matplotlib.pyplot as plt 
import numpy as np

z = str(input('введите название графика: '))
q = int(input('введите коэффицент при хˆ2: '))
w = int(input('введите коэффицент при хˆ1: '))
e = int(input('введите коэффицент при хˆ0: '))
t = int(input('введите предел изменения Ха: '))
u = int(input('введите предел изменения Хb: '))
n = int(input('введите количество точек N: '))
             
f = (u - t) / (n - 1)

def parabola_plotter(a=q, b=w, c=e, title='parabola plotter'):
    x = np.arange(t,u,f)
    y = a*x**2 + b*x + c
    plt.plot(x,y,label='my parabola')
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    plt.title(z)
    plt.legend()
    plt.savefig('parabola.png')
parabola_plotter()