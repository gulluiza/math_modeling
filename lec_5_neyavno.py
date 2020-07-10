import matplotlib.pyplot as plt 
import numpy as np
def circlea_plotter(R=1, title='Circle plotter'):
    x = np.arange(-2.0, 2.0, 0.1)
    y = np.arange(-2.0, 2.0, 0.1)
    X, Y = np.meshgrid(x, y) #указание на неявное задание координат
    fxy = X**2 + Y**2 #уравнение окружности
    plt.contour(X, Y, fxy, levels=[R**2]) #команда рисования неявнозаданных кривых
    plt.savefig('dfghjk.png')
circlea_plotter(3)