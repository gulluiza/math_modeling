import matplotlib.pyplot as plt 
import numpy as np

q = int(input('введите коэффицент а: '))
w = int(input('введите коэффицент b: '))
t = int(input('введите предел изменения Ха: '))
u = int(input('введите предел изменения Хb: '))
n = int(input('введите количество точек N: '))

f = (u - t) / (n - 1)

def ellipse_plotter(a = q, b = w, title='ellipse plotter'):
    x = np.arange(t, u, f)
    y = np.arange(t, u, f)
    
    X, Y = np.meshgrid(x, y)
    fxy = (X**2) / (a**2) + (Y**2) / (b**2)
    plt.contour(X, Y, fxy, levels=[q, 4*q])
    
    
    plt.axis('equal')
    plt.savefig('qwertyu.png')
    
ellipse_plotter()