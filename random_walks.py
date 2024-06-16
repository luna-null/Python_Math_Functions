import random as rand
import numpy as np
import matplotlib.pyplot as plt

def random_walk(n):

    x0 = 0
    y0 = 0

    for i in range(0,n):
         x1 = x0 + rand.randint(-5,5)
         y1 = y0 + rand.randint(-5,5)
         X = np.linspace(x0,x1,50)
         Y = np.linspace(y0,y1,50)
         plt.plot(X,Y,color="blue")
         x0 = x1
         y0 = y1
    plt.show()

