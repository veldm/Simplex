import numpy as np
from matplotlib import cm
import matplotlib.pyplot

def Show():
    fig, ax = matplotlib.pyplot.subplots()
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Геометрическое решение');
    x = np.linspace(-10, 20, 11)
    ax.plot(x, -3 * x, label="y = -3x")
    ax.plot(x, 5 - 2 * x, label="y = 5 - 2x")
    ax.plot(y, 7, label="x = 7")
    ax.plot(x, 3, label="y = 3")
    #ax.arrow(0, 0, 4, 3, head_width=0.5, head_length=0.7, fc='lightblue', ec='black')
    ax.scatter(4.5, 1.0)
    ax.legend()
    matplotlib.pyplot.show()

