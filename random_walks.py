import random as rand
import numpy as np
import matplotlib.pyplot as plt

def random_walk(n):

    x0 = 0
    y0 = 0
    plt.plot(x0,y0,marker='o',ms=10,c='black')
    for i in range(0,n):
        r = rand.randrange(1,5)
        match r:
            case 1:
                x1 = x0 + 1
                y1 = y0
            case 2:
                x1 = x0
                y1 = y0 + 1
            case 3:
                x1 = x0 - 1
                y1 = y0
            case 4:
                x1 = x0
                y1 = y0 - 1
        X = np.linspace(x0,x1,20)
        Y = np.linspace(y0,y1,20)
        plt.plot(X,Y,marker = ',')
        x0 = x1
        y0 = y1
    plt.plot(x1,y1,marker = 'o',ms=10,c='orange')
    plt.show()
