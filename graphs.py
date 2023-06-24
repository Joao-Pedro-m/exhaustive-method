import matplotlib.pyplot as plt
import matplotlib
import numpy as np


def exhaustive_method(func, prec, x1, x2):
    area = 0
    x_per_step = (x2-x1)/prec
    for x in range(prec):
        tx1 = x1+x_per_step*x
        area += ((func(tx1)*x_per_step)**2)**(1/2)
    return area


def exhaustive_method_rectangle(func, prec, x1, x2):
    rectangles = []
    rectangles2 = []
    x_per_step = (x2 - x1) / (prec+1)
    for i in range(prec):
        tx1 = x1 + x_per_step * i
        rectangles.append(tx1)
        rectangles2.append(func(tx1))
    return [rectangles,x_per_step,rectangles2]

def f(x):
    return x**2


x = np.linspace(-10, 101, 100)


inicio = 2
passos = 10
fim = 5


rects = exhaustive_method_rectangle(f, passos, inicio, fim)
rect1 = rects[0]
width = rects[1]
rect2 = rects[2]

fig = plt.figure()
ax = fig.add_subplot(111)

for y in range(len(rect1)):
    tempvar = matplotlib.patches.Rectangle((rect1[y],0),width,rect2[y],color="blue")
    ax.add_patch(tempvar)



plt.xlim([-5, 15])
plt.ylim([-5, 20])
plt.plot(x, f(x))
plt.axhline(color="black")
plt.show()
