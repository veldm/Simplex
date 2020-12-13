import numpy as np
from matplotlib import cm
import matplotlib.pyplot

def Show():
    fig, ax = matplotlib.pyplot.subplots()
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Геометрическое решение');
    x = np.linspace(-10, 20, 11)
    ax.plot(x, 2*x - 8, label="y1 = 2x - 8")
    ax.plot(x, -3 - x, label="y2 = -3 - x")
    ax.plot(x, 1 -x + x, label="y3 = 1")
    ax.arrow(0, 0, 4, 3, head_width=0.5, head_length=0.7, fc='lightblue', ec='black')
    ax.scatter(4.5, 1.0)
    ax.legend()
    matplotlib.pyplot.show()

