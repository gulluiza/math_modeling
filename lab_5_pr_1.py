import matplotlib.pyplot as plt 
import numpy as np


plt.plot([1, 1,],[1, 5,])
plt.plot([1, 5], [5, 5])
plt.plot([5, 5], [5, 1])
plt.plot([5, 1], [1, 1])

plt.axis('equal')
plt.savefig('dfgh.png')
