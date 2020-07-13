import matplotlib.pyplot as plt 
import numpy as np

z = str(input('введите название графика: '))
t = int(input('введите предел изменения Ха: '))
u = int(input('введите предел изменения Хb: '))
n = int(input('введите количество точек N: '))
r = int(input('введите радиус: '))

f = (u - t) / (n - 1)

def circlea_plotter(R=1, title='Circle plotter'):
    
    x = np.arange(t, u, f)
    y = np.arange(t, u, f)
    
    X, Y = np.meshgrid(x, y) #указание на неявное задание координат
    fxy = X**2 + Y**2 #уравнение окружности
    plt.contour(X, Y, fxy, levels=[R**2]) #команда рисования неявнозаданных кривых
    
    plt.axis('equal')
    plt.savefig('dfghjk.png')
    
circlea_plotter(r)