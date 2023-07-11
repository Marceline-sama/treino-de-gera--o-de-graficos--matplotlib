import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
line, = ax.plot([])


def update(frame):
    line.set_data(range(frame), np.random.rand(frame))
    ax.relim()
    ax.autoscale_view()
    return line,


ani = FuncAnimation(fig, update, frames=range(1, 101), blit=True)
plt.show()