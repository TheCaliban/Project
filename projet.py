import numpy as np
from math import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate(i) :
    graph_data = open('points.txt', 'r').read()
    lines = graph_data.split('\n')
    xList = []
    yList = []
    coord_x = []
    coord_y = []
    for line in lines :
        if len(line) >= 1 :
            x = float(line)
            xList.append(x)
            yList.append(exp(x))
    points = [(float(xList[i]), float(yList[i])) for i in range(len(xList))]
    P = lagrange(points)
    x = list(np.arange(1, 2, 0.01))
    y = list(map(P, x))
    #~ z = list(map(exp(x), x))
    ax1.clear()
    ax1.plot(x, y)
    
    #~ print(x)
    
    ax1.plot(x, np.exp(x))
    #~ ax1.plot(x, z, color="green")

    for x_p, y_p in points:
        coord_x.append(x_p)
        coord_y.append(y_p)
    ax1.plot(coord_x, coord_y,  'ro')

def lagrange(points):
    def P(x):
        total = 0
        n = len(points)
        for i in range(n):
            xi, yi = points[i]

            def g(i, n):
                tot_mul = 1
                for j in range(n):
                    if i == j:
                        continue
                    xj, yj = points[j]
                    tot_mul *= (x - xj) / float(xi - xj)
                return tot_mul

            total += yi * g(i, n)

        return total
    return P

if __name__ == "__main__":
    fig = plt.figure()
    #fig = plt.axis([0, imgx, 0, imgy])
    ax1 = fig.add_subplot(1,1,1 )

    ani = animation.FuncAnimation(fig, animate, interval=10000)
    plt.show()






